#!/usr/bin/python3
"""
This function queries the Reddit API and
returns the number of subscribers
(not active users, total subscribers)
for a given subreddit
"""
import requests


def number_of_subscribers(subreddit):
    """
    Queries the number of subscribers in a subreddit

    Args:
        subreddit (string): The name of the subreddit

    Return:
            number_of_subscribers (int)
    """
    if subreddit is None:
        return 0

    url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    user_agent = {'User-agent': 'Mozilla/5.0 (Windows; U; Windows NT 6.0)\
     AppleWebKit/538.0.0 (KHTML, like Gecko) \
     Chrome/17.0.821.0 Safari/538.0.0'}

    try:
        response = requests.get(url, headers=user_agent)
        results = response.json()
        return results.get('data').get('subscribers')
    except Exception:
        return 0
