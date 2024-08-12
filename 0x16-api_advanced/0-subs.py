#!/usr/bin/python3
import requests

def number_of_subscribers(subreddit):
    # Set a custom User-Agent to avoid "Too Many Requests" error
    headers = {"User-Agent": "SubredditSubscriberCount/1.0"}

    # Construct the URL for the subreddit's JSON data
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    
    try:
        # Make the request to the Reddit API without following redirects
        response = requests.get(url, headers=headers, allow_redirects=False)

        # Check if the request was successful
        if response.status_code == 200:
            data = response.json()
            return data['data']['subscribers']
        else:
            return 0
    except requests.RequestException:
        return 0

# Example usage:
# subscribers = number_of_subscribers("python")
# print(f"Subscribers: {subscribers}")

