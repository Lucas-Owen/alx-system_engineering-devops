#!/usr/bin/python3
"""This module defines recurse function"""


import requests


def recurse(subreddit, hot_list=None, after=None):
    """
    Queries the reddit API
    Returns the titles of the first hot posts for a given subreddit
    """
    if hot_list is None:
        hot_list = []
    headers = {
        'user-agent': 'Chrome/118.0.0.0',
    }
    params = dict()
    if after:
        params = {'after': str(after)}
    url = 'https://www.reddit.com/r/'+str(subreddit)+'/hot.json'
    try:
        response = requests.get(url=url, headers=headers, params=params)
        json_resp = response.json()
        for post in json_resp['data']['children']:
            hot_list.append(post['data']['title'])
        if json_resp['data'].get('after', None):
            return recurse(subreddit,
                           hot_list=hot_list,
                           after=json_resp['data']['after'])
        return hot_list
    except Exception as e:
        return None
