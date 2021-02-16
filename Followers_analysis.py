# import libraries
import datetime as dt
import pandas as pd
import twitter

# set variables for keys and tokens to access the Twitter API
TWITTER_CONS_KEY = 'vtgJBw59RMg8zlzvPtFEne2Hj'
TWITTER_CONS_SEC = 'lLgh4S3T4rcZuj4yHDoJ2YK8ktyzOIBYQmEuu8g58pUfKDmwFb'
TWITTER_ACCESS_TOKEN = '285572179-85c2D2cszC1KcrNsimRoUWnXac7e1hO7NTLcy96A'
TWITTER_ACCESS_SEC = 'UI7KBpJncUNOPXeWbZQzs7FAn3b9NhmF0VlbLZZOfxbEp'

# create an object for querying the API using the python-twitter library
t = twitter.Api(consumer_key=TWITTER_CONS_KEY,
                consumer_secret=TWITTER_CONS_SEC,
                access_token_key=TWITTER_ACCESS_TOKEN,
                access_token_secret=TWITTER_ACCESS_SEC,
                tweet_mode='extended',
                sleep_on_rate_limit=True)

GetFollowers(user_id=None, screen_name=None, cursor=None, count=None, total_count=None, skip_status=False, include_user_entities=True)

GetFollowerIDs(user_id=None, screen_name=None, cursor=None, stringify_ids=False, count=None, total_count=None)

GetRetweeters(status_id, cursor=None, count=100, stringify_ids=False)

GetRetweets(statusid, count=None, trim_user=False)

GetSearch(term=None, raw_query=None, geocode=None, since_id=None, max_id=None, until=None, since=None, count=15, lang=None, locale=None, result_type='mixed', include_entities=None, return_json=False)[source]
>>> api.GetSearch(geocode="37.781157,-122.398720,1mi").

GetStatus(status_id, trim_user=False, include_my_retweet=True, include_entities=True, include_ext_alt_text=True)[source]

InitializeRateLimit()[source]

