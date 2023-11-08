#!/usr/bin/python3
"""This module defines top_ten function"""


def top_ten(subreddit):
    """
    Queries the reddit API
    Prints the titles of the first 10 hot posts listed for a given subreddit
    """
    import requests
    headers = {
        'user-agent': 'Mozilla/5.0 Chrome/118.0.0.0',
    }
    url = 'https://www.reddit.com/r/'+str(subreddit)+'/hot.json'
    try:
        response = requests.get(url=url, headers=headers)
        for post in (response.json())['data']['children'][:10]:
            print(post['data']['title'])
    except Exception as e:
        print("None")
