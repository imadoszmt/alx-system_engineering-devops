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
    # Define the URL for the subreddit's about page
    url = f'https://www.reddit.com/r/{subreddit}/about.json'

    # Set the User-Agent header
    headers = {
        'User-Agent': 'Chrome/91.0.4472.124 Safari/537.36'
    }

    # Make the request to the Reddit API
    response = requests.get(url, headers=headers, allow_redirects=False)

    # Check if the response is valid
    if response.status_code == 200:
        data = response.json()
        # Parse the JSON response
        subscribers = data.get("data", {}).get("subscribers", 0)
        # Return the number of subscribers
        return subscribers
    else:
        # Handle other status codes if necessary
        return 0

"""
if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Please pass an argument for the subreddit to search.")
    else:
        print("{:d}".format(number_of_subscribers(sys.argv[1])))
"""
