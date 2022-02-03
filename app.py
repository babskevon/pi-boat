#!/usr/bin/env python
from importlib import import_module
import os
from flask import Flask, render_template, Response,request
from move import Drive

# import camera driver
if os.environ.get('CAMERA'):
    Camera = import_module('camera_' + os.environ['CAMERA']).Camera
else:
    from camera import Camera

# Raspberry Pi camera module (requires picamera package)
from camera_pi import Camera



app = Flask(__name__)


@app.route('/')
def index():
    """Video streaming home page."""
    print("function workin so well")
    return render_template('index.html')

def gen(camera):
    """Video streaming generator function."""
    yield b'--frame\r\n'
    while True:
        frame = camera.get_frame()
        yield b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n--frame\r\n'


@app.route('/video_feed')
def video_feed():
    """Video streaming route. Put this in the src attribute of an img tag."""
    return Response(gen(Camera()),
                    mimetype='multipart/x-mixed-replace; boundary=frame')



@app.route("/move",methods=['GET', 'POST'])
def command():
    if request.method == 'POST':
        request_data = request.form.get('cmd')
        speed = request.form.get('speed')
        #kkk = request_data['cmd']
        Drive(request_data,int(speed))
        #print("{} its working so well".format(kkk))
        return speed
    return "testing"


if __name__ == '__main__':
    app.run(host='0.0.0.0',port=80, threaded=True)
