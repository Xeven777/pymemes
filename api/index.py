from flask import Flask, render_template
import requests
import json

app = Flask(__name__)


def get_meme():
    url = "https://meme-api.com/gimme"
    response = json.loads(requests.request("GET", url).text)
    meme = response["preview"][-1]
    memeSmall = response["preview"][1]
    subreddit = response["subreddit"]
    postLink = response["postLink"]
    title = response["title"]
    return meme, memeSmall, subreddit, postLink, title


@app.route("/refresh")
def refresh():
    meme, memeSm, subreddit, postLink, title = get_meme()
    return render_template("index.html", meme=meme, memeSm=memeSm, subreddit=subreddit, url=postLink, title=title)


@app.route("/")
def index():
    meme, memeSm, subreddit, postLink, title = get_meme()
    return render_template("index.html", meme=meme, memeSm=memeSm, subreddit=subreddit, url=postLink, title=title)


# app.run(host="0.0.0.0", port=80, debug=True)
