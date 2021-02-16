import pandas as pd
from sklearn import preprocessing
from matplotlib import pyplot as plt

# base_friend_df = base_friend_df.loc[:, ~base_friend_df.columns.str.contains('Unnamed: 0']
base_friend_df = pd.read_csv("/Users/aylingulum/Desktop/Twitter_API/venv/files/friends.csv", delimiter=",")
base_friend_df.dropna(how='all', axis=0,  inplace=True)
base_friend_df.dropna(how='all', axis=1,  inplace=True)

headers = base_friend_df.iloc[0]
new_df = pd.DataFrame(base_friend_df.values[1:], columns=headers)
new_df = new_df[["id", "Number of followers", "Number of user followed",
            "Number of favorited tweets", "Number of statuses"]].astype("int32")

info = new_df.describe()

dict = info.to_dict()
_min = dict['Number of followers']['min']
_first_quarter = dict['Number of followers']['25%']
_second_quarter = dict['Number of followers']['50%']
_third_quarter = dict['Number of followers']['75%']
_max = dict['Number of followers']['max']

c = pd.cut(
    new_df["Number of followers"],
    [_min, _first_quarter, _second_quarter, _third_quarter, _max],
    labels=['low', 'med', 'high', 'pheno']
)


x = new_df['Number of followers'].to_frame()
min_max_scaler = preprocessing.MinMaxScaler()
x_scaled = min_max_scaler.fit_transform(x)
normalized_df = x_scaled.to_frame()
normalized_df = normalized_df.sort_values(by="0")
fig, ax = plt.subplots()
ax.plot(x)
fig, ax = plt.subplots()
