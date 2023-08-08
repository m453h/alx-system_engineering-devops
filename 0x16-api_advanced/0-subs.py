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
    if subreddit is None or not isinstance(subreddit, str):
        return 0

    url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)

    try:
        response = requests.get(url)
        results = response.json()
        return results.get('data').get('subscribers')
    except Exception:
        return 0
