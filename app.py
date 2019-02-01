# coding:utf-8

from flask import Flask, render_template, request, logging, Response, redirect, flash

# Flaskの起動 -インスタンス作成-
app = Flask(__name__)

@app.route('/', methods=["GET", "POST"])
def index():
    tw = 'これはテストツイートです。'

    if request.method == 'POST':
        return render_template('index.html', gen_tweet=tw)
    else:
        return render_template('index.html')

if __name__ == "__main__":
    app.run(host="localhost")