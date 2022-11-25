let url_prefix = 'http://www.iot.com'

function updateBrightness(brightness) {
    $.get(url_prefix + '/password', function(data) {
        $.post(url_prefix + '/brightness?value=' + brightness + '&password=' + data.password, function(data) {
            console.debug('response from the server: '+ data);
        });
    });
}

button_on = document.getElementById("on");
button_off = document.getElementById("off");

button_on.onclick = function() {
  updateBrightness(99);
}
button_off.onclick = function() {
  updateBrightness(0);
}
