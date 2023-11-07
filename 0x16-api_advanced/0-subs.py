#!/usr/bin/python3
"""This module defines number_of_subscribers function"""


def number_of_subscribers(subreddit):
    """
    Queries the reddit API
    Returns the number of subscribers for the given subreddit
    """
    import requests
    headers = {
        'user-agent': 'Chrome/118.0.0.0',
    }
    url = 'https://www.reddit.com/r/'+str(subreddit)+'/about.json'
    try:
        response = requests.get(url=url, headers=headers)
        return (response.json())['data']['subscribers']
    except Exception as e:
        return 0
