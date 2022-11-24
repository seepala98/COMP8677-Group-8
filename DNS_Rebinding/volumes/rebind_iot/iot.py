from flask import (
    Blueprint, Flask, redirect, render_template, request, url_for, current_app as app, json
)
import flask


bp = Blueprint('iot', __name__)

@bp.route('/password', methods=('GET',))
def password():
    data = {
        'password': app.password
    }
    return app.response_class(
        response=json.dumps(data),
        mimetype='application/json; charset=utf-8'
    )


@bp.route('/', methods=('GET',))
def index():
    return render_template('index.html')

@bp.route('/change', methods=('GET',))
def change():
    return render_template('change.html')

@bp.route('/brightness', methods=('GET',))
def get_brightness():
    data = {
        'brightness': app.brightness
    }

    return app.response_class(
        response=json.dumps(data),
        mimetype='application/json; charset=utf-8'
    )

@bp.route('/brightness', methods=('POST',))
def set_brightness():
    l_password = request.args.get('password', None)
    if l_password != app.password:
        return app.response_class(
            response='wrong password',
            status=401
        )
    brightness = request.args.get('value', None)
    if not brightness:
        return app.response_class(
            response='not value',
            status=400,
            mimetype='text/plain'
        )
    brightness = int(brightness)
    if app.config['LOWEST'] <= brightness <= app.config['HIGHEST']:
        app.brightness = brightness
        data = {'brightness': brightness}
        return app.response_class(
            response=json.dumps(data),
            mimetype='application/json; charset=utf-8'
        )
    else:
        return app.response_class(
            response='brightness out of bound',
            status=400,
            mimetype='text/plain'
        )
