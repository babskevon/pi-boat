#!/usr/bin/env python
from importlib import import_module
import os
from flask import Flask, render_template, Response,request
from move import Drive



app = Flask(__name__)


@app.route('/')
def index():
    """Video streaming home page."""
    print("function workin so well")
    return render_template('index.html')



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
    app.run(host='0.0.0.0', threaded=True)
