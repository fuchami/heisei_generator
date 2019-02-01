# coding:utf-8

import os
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello world!'

@app.route('/ja')
def hello_world_ja():
    return 'こんにちは 世界'

if __name__ == "__main__":
    app.run()