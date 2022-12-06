# Wrangling Report
___
## *Section #1 - Gathering Data*
I began by manually downloading `'twitter-archive-enhanced.csv'` from Udacity's given URL.
Then, I created the module `gather.py` ***(detailed docstrings within the module)***, 
which consists of the functions I needed in order to gather the required data. 
The first method - `gather.download_file_from_url` was used to download and save
the `image_predictions.tsv` file programmatically. Then, I went on to create the functions necessary for
getting WeRateDogs' retweet and favorites counts:
1. `gather.get_auth`, which returns an auth object required for getting tweet's data from the tweeter API.
2. `gather.dump_tweets_data`, which dumps json-formatted counts data into `tweets_data.json`.

*SIDENOTE: It was crucial to take account of the API's rate limit, 
otherwise a lot of valid data would be ignored by the function.*

Finally, I loaded the collected data into three DataFrames:
1. `archive_original` for `'twitter-archive-enhanced.csv'`.
2. `tweet_cnts` for `tweets_data.json`.
3. `img_preds` for `image_predictions.tsv`.

At a quick glance, I noticed that in all of the above frames the id column is cast by default as int, So as a quick quality fix
I've cast them to `str`, as the latter would be the appropriate data type for id.
## Section #2 - Assessing Data

## Section #3 - Cleaning Data