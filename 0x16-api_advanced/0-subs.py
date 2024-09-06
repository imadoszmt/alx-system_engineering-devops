#!/usr/bin/python3
"""
This module queries the Reddit API to get the number of subscribers for
a given subreddit.
"""
import requests
import sys


def number_of_subscribers(subreddit):
    """
    Queries the Reddit API to get the number of subscribers for a
    given subreddit.

    Args:
        subreddit (str): The name of the subreddit.

    Returns:
        int: The number of subscribers for the specified subreddit.
        Returns 0 if the subreddit is invalid.
    """
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {
        "User-Agent": "Custom Reddit API Client"
    }

    # Fetch the subreddit data.
    response = requests.get(url, headers=headers, allow_redirects=False)

    # Check if the request was successful.
    if response.status_code == 200:
        data = response.json()
        subscribers = data["data"]["subscribers"]
        return subscribers
    else:
        return 0


"""
if __name__ == "__main__":

    #Get subreddit name from the command line argument and call the function
    #to print the number of subscribers.

    if len(sys.argv) != 2:
        sys.exit(1)
    else:
        subreddit = sys.argv[1]
        print("{:d}".format(number_of_subscribers(subreddit)))
"""
