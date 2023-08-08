#!/usr/bin/python3
"""
This function queries the Reddit API and returns a list
of the titles of all the hot posts for a given subreddit.
"""
import requests


def recurse(subreddit, hot_list=[], after=""):
    """
    Returns the title(s) of all hot posts
    retrieved from the Reddit API

    Args:
        subreddit (string): The name of the subreddit
        after (string): The id of the parameter in url used
                        to query for next page items
    Return:
           hot_list (list): List of all posts of a subredit
    """
    if subreddit is None:
        return None

    url = 'https://www.reddit.com/r/{}/hot/.json'.format(subreddit)
    user_agent = {'User-agent': 'Mozilla/5.0 (Windows; U; Windows NT 6.0)\
     AppleWebKit/538.0.0 (KHTML, like Gecko) \
     Chrome/17.0.821.0 Safari/538.0.0'}

    try:
        response = requests.get(url, headers=user_agent,
                                params={'limit': 100,
                                        'after': after})

        if response.status_code == 404:
            return None
        results = response.json()
        top_posts = results.get('data').get('children')

        for post in top_posts:
            hot_list.append(post.get('data').get('title'))

        after = results.get('data').get('after')

        if results.get('data').get('after') is not None:
            return recurse(subreddit, hot_list, after)
        else:
            return hot_list
    except Exception:
        return None
