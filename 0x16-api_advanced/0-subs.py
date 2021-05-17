#!/usr/bin/python3
""" module to get info of a subreddit """

import requests
import sys


def number_of_subscribers(subreddit):
    """ function to get the subscribers of a subreddit """
    user = {
        "User-Agent": "user/0.0.2"
    }
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    data = requests.get(url, headers=user)
    if data.status_code == 200:
        dct = data.json()
        return(dct["data"]["subscribers"])
    return(0)
