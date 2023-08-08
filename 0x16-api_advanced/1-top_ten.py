#!/usr/bin/python3
"""
This function queries the Reddit API and prints
the titles of the first 10 hot posts
listed for a given subreddit.
"""
import requests


def top_ten(subreddit):
    """
    Displays the title of the first 10 hot posts
    retrieved from the Reddit API

    Args:
        subreddit (string): The name of the subreddit

    Return:
           (nothing)
    """
    if subreddit is None:
        print("None")
    else:
        url = 'https://www.reddit.com/r/{}/hot/.json'.format(subreddit)
        user_agent = {'User-agent': 'Mozilla/5.0 (Windows; U; Windows NT 6.0)\
         AppleWebKit/538.0.0 (KHTML, like Gecko) \
         Chrome/17.0.821.0 Safari/538.0.0'}

        try:
            response = requests.get(url, headers=user_agent,
                                    allow_redirects=False,
                                    params={'limit': 10})
            results = response.json()
            top_posts = results.get('data').get('children')

            for post in top_posts:
                print(post.get('data').get('title'))
        except Exception:
            print("None")
