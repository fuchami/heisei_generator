# coding:utf-8

from flask import Flask, render_template, request, logging, Response, redirect, flash
import tw_generate

# Flaskの起動 -インスタンス作成-
app = Flask(__name__)

@app.route('/', methods=["GET", "POST"])
def index():
    if request.method == 'POST':
        word = tw_generate.gen_tweet()
        tweet = "平成最後の" + word 

        return render_template('index.html', gen_tweet=tweet)
    else:
        return render_template('index.html')

if __name__ == "__main__":
    # app.run(host="localhot")
    app.run(host="0.0.0.0")