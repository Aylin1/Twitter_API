"""

Dataframe
Build a csv file of the last 200 favorited tweets by user_name with the columns of creation date,
id of the tweet, full text of the tweet, owner of the tweet, number of user who favorited the tweet, number of
 user retweeted the tweet and the language of the tweet. Then update it day by day in case of newly favorited
  tweets come up, add them to the csv file. Make a graph of favorited tweet frequency day by day.

   Effect size 1 = #of followers * #of tweets favorited by other users * #of tweets retweeted by other users
        Low potential
        Moderate potential
        High potential

    Effect size 2 = #of followers * #of tweets favorited by the owner user * #of tweets retweeted by owner user
        Ghost
        Moderate
        Active

    Text analysis of the favorited tweets by the user

"""

# import libraries
import datetime as dt
import pandas as pd
import twitter
from pandas import DataFrame

# set variables for keys and tokens to access the Twitter API

TWITTER_CONS_KEY = 'vtgJBw59RMg8zlzvPtFEne2Hj'
TWITTER_CONS_SEC = 'lLgh4S3T4rcZuj4yHDoJ2YK8ktyzOIBYQmEuu8g58pUfKDmwFb'
TWITTER_ACCESS_TOKEN = '285572179-85c2D2cszC1KcrNsimRoUWnXac7e1hO7NTLcy96A'
TWITTER_ACCESS_SEC = 'UI7KBpJncUNOPXeWbZQzs7FAn3b9NhmF0VlbLZZOfxbEp'

# create an object for querying the API using the python-twitter library
t = twitter.Api(
    consumer_key=TWITTER_CONS_KEY,
    consumer_secret=TWITTER_CONS_SEC,
    access_token_key=TWITTER_ACCESS_TOKEN,
    access_token_secret=TWITTER_ACCESS_SEC,
    tweet_mode='extended',
    sleep_on_rate_limit=True)

# name of the account you want to analyze
screen_name = input('Enter the screen name:')


def fetch_favorited_tweets(name):
    f_tweets = t.GetFavorites(screen_name=name, count=200, return_json=True)

    # call the Twitter API, get n tweets favorited by the user
    dates = [i["created_at"] for i in f_tweets]
    texts = [i["full_text"] for i in f_tweets]
    user_favorited = [i["user"] for i in f_tweets]
    favorited_users_list = [i["name"] for i in user_favorited]
    screen_name_favorited = [i["screen_name"] for i in user_favorited]
    description_favorited = [i["description"] for i in user_favorited]

    # favorited_users.to_csv("favorite_users.csv")
    df_favorited = pd.DataFrame(list(zip(dates, texts, favorited_users_list, screen_name_favorited,
                                         description_favorited)), columns=['dates', 'texts', 'favorited_users_list',
                                                                           'screen_name_favorited',
                                                                           'description_favorited'])

    return df_favorited


favorited_df = fetch_favorited_tweets(screen_name)


def dater(df):
    dates = df['dates']
    element_list = []
    datetimes = []
    for i in dates:
        i.replace("+0000", "")
        elements = i.split(" ")
        elements.pop(4)
        element_list.append(elements)
        joined_elements = "-".join([str(elem) for elem in elements])
        datetimes.append(joined_elements)
    return datetimes


date_list = dater(favorited_df)


def date_formatter(listed):
    date_time = []
    for i in listed:
        datetime_object = dt.datetime.strptime(str(i), '%a-%b-%d-%H:%M:%S-%Y')
        date_time.append(datetime_object)
    df = DataFrame(date_time, columns=['dates'])
    df['minute'] = df['dates'].dt.minute.astype(str)
    df['hour'] = df['dates'].dt.hour.astype(str)
    df['day'] = df['dates'].dt.day.astype(str)
    df['month'] = df['dates'].dt.month.astype(str)
    df['year'] = df['dates'].dt.year.astype(str)

    df['period'] = df[['year', 'month', 'day']].agg(''.join, axis=1)
    df_period = df[['period']].copy()
    df_period["period"] = pd.to_datetime(df_period['period'], format='%Y%m%d')
    return df_period

periods_add = date_formatter(date_list)
favorited_df["D/M/Y"] = periods_add["period"]


def time_se(time):
    time['day_of_week'] = time["period"].dt.day_name()
    time.sort_values(by=["period"], inplace=True, ascending=False)
    time.reset_index(drop=True)
    short_time_series = time.head(n=15)
    return short_time_series

long_short = time_se(periods_add)


''' def highest_rate_graph(time_series):
    time_series.sort_values(by=["period"], inplace=True)
    graph = time_series.plot.bar(y=['period'], figsize=(16,8), grid=True, log=True)
    return graph

highest_rate_graph(time_series)

#mask = (favorited_df['created_at_2'] == "2020-10-11")
#df = favorited_df.loc[mask] '''
