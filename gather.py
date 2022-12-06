"""Gathering functions."""

import json

import requests
import tweepy


def download_file_from_url(url_path, destination):
    """Save File From a given url.

    :param url_path: (str) a path a file containing the url.
    :param destination: (str) a path to save the response at.
    """
    with open(url_path) as file:
        url = file.read()
    response = requests.get(url)
    print(response.status_code)
    with open(destination, mode='wb') as file:
        file.write(response.content)


def get_auth(auth_file):
    """Return authentication from params in auth file.

    See README.md for how to format auth file.
    :param auth_file: (str) path to auth file
    :return: (tweepy.auth.OAuth1UserHandler) an auth object.
    """
    with open(auth_file) as file:
        args = [line.split('=')[1].rstrip('\n') for line in file]
    return tweepy.OAuth1UserHandler(*args)


def dump_tweets_data(id_lst, auth):
    """Dump tweets' id, retweet count and favorite count into json file.

    :param id_lst: (list[str]) a list containing tweet id's.
    :param auth: (tweepy.auth.OAuth1UserHandler) an auth object.
    """
    api = tweepy.API(auth, wait_on_rate_limit=True)

    def get_tweet_counts(tweet_id):
        """Return counts of favorites and retweets."""
        try:
            tweet = api.get_status(tweet_id)
        except tweepy.TweepyException:
            print(f'{tweet_id[:5]}... failed')
            favorite_count = float('nan')
            retweet_count = float('nan')
        else:
            print(f'{tweet_id[:5]}... successful')
            if hasattr(tweet, 'retweeted_status'):
                favorite_count = tweet.retweeted_status.favorite_count
                retweet_count = tweet.retweeted_status.retweet_count
            else:
                favorite_count = tweet.favorite_count
                retweet_count = tweet.retweet_count
        return {'id': tweet_id, 'favorite_count': favorite_count,
                'retweet_count': retweet_count}

    data = [get_tweet_counts(item) for item in id_lst]
    with open('tweets_data.json', mode='w') as file:
        json.dump(data, fp=file)


if __name__ == '__main__':
    pass
