#!/usr/bin/python3
""" module to get info of a subreddit """

import requests


def top_ten(subreddit):
    """ function to get the subscribers of a subreddit """
    user = {
        "User-Agent": "user/0.0.2"
    }
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    data = requests.get(url, headers=user, allow_redirects=False)
    if data.status_code == 200:
        dct = data.json()
        posts = dct.get("data", {}).get("children", [])
        if not posts:
            print(None)
        for post in posts[:10]:
            toprint = post.get("data").get("title")
        print(toprint)
    else:
        print(None)
