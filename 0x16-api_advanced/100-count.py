#!/usr/bin/python3
"""This module defines top_ten function"""


import functools
import re
import requests


def compare(item1, item2):
    if item1[1] < item2[1]:
        return 1
    elif item1[1] > item2[1]:
        return -1
    elif item1[0] < item2[0]:
        return -1
    elif item1[0] > item2[0]:
        return 1
    return 0


def count_words(subreddit, word_list, after=None, counts=None):
    """
    Queries the reddit API
    Returns the counts of words in word list
    """
    if counts is None:
        word_list = [word.lower() for word in word_list]
        counts = {word: 0 for word in word_list}
    headers = {
        'user-agent': 'AppleWebKit/537.36 (KHTML, like Gecko) Safari/537.36',
        # 'user-agent': 'Chrome/118.0.0.0',
    }
    params = dict()
    if after:
        params = {'after': str(after)}
    url = 'https://www.reddit.com/r/'+str(subreddit)+'/hot.json'
    try:
        response = requests.get(url=url, headers=headers, params=params)
        json_resp = response.json()
        for post in json_resp['data']['children']:
            for word in counts:
                text = post['data']['selftext']
                matches = re.findall(r"\b" + word + r"\b", text.lower())
                counts[word] += len(matches)
        if json_resp['data'].get('after', None):
            return count_words(subreddit,
                               word_list,
                               after=json_resp['data']['after'],
                               counts=counts)
        results = [[word, count] for word, count in counts.items()]
        for result in sorted(results, key=functools.cmp_to_key(compare)):
            count = word_list.count(result[0])
            print("{}: {}".format(result[0], result[1] * count))
        return
    except Exception as e:
        return
