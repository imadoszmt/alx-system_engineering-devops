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
        'User-Agent': '0-subs.py/1.0 (by /u/Legitimate-Tone4703)'
    }

    # Make the request to the Reddit API
    response = requests.get(url, headers=headers, allow_redirects=False)

    # Check if the response is valid
    if response.status_code == 200:
        # Parse the JSON response
        data = response.json()
        # Return the number of subscribers
        return data['data']['subscribers']
    elif response.status_code == 404:
        # If the subreddit is invalid, return 0
        return 0
    else:
        # Handle other status codes if necessary
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
