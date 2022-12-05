import json

import requests
import pandas as pd
import tweepy


def download_file_from_url(url_path, destination):
    with open(url_path) as file:
        url = file.read()
    response = requests.get(url)
    print(response.status_code)
    with open(destination, mode='wb') as file:
        file.write(response.content)


def get_tweeter_api():
    with open('auth.txt') as file:
        args = [line.split('=')[1].rstrip('\n') for line in file]
    auth = tweepy.OAuth1UserHandler(*args)
    return tweepy.API(auth)


def dump_tweets_data(id_lst, api):
    """Dump tweets information into json file."""

    def get_tweet_counts(tweet_id):
        """Return counts of favorites and retweets."""
        try:
            tweet = api.get_status(tweet_id)
            if hasattr(tweet, 'retweeted_status'):
                favorite_count = tweet.retweeted_status.favorite_count
                retweet_count = tweet.retweeted_status.retweet_count
            else:
                favorite_count = tweet.favorite_count
                retweet_count = tweet.retweet_count
            print(f'succeeded to get data of id {tweet_id}')
        except tweepy.TweepyException:
            print(f'failed to get data of id {tweet_id}')
            favorite_count = float('nan')
            retweet_count = float('nan')
        return {'id': tweet_id, 'favorite_count': favorite_count,
                'retweet_count': retweet_count}

    data = [get_tweet_counts(item) for item in id_lst]
    with open('tweets_data.json', mode='w') as file:
        json.dump(data, fp=file)


if __name__ == '__main__':
    # download_file_from_url(url_path='link.txt', destination='image_predictions.tsv')
    df = pd.read_csv('twitter-archive-enhanced.csv')
    dump_tweets_data(id_lst=df['tweet_id'].astype(str),
                     api=get_tweeter_api())
