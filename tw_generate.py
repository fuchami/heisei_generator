# coding:utf-8
"""
wikipediaからのウェブスクレイピング
"""

import urllib.request, urllib.error
from bs4 import BeautifulSoup

url="https://ja.wikipedia.org/wiki/Special:Random"

def gen_tweet():
    # URLにアクセス
    html=urllib.request.urlopen(url)

    soup=BeautifulSoup(html, "html.parser")
    title_tag = soup.title
    title = title_tag.string
    word = title.split(" ")
    return word[0]

if __name__ == "__main__":
    gen_tweet()