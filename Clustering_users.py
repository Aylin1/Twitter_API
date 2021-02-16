import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns

base_friends_df = pd.read_csv("/Users/aylingulum/Desktop/Twitter_API/friends.csv", delimiter=",")
base_friends_df = base_friends_df.loc[:, ~base_friends_df.columns.str.contains('Unnamed')]

user_cluster_df = base_friends_df[['Number of followers', 'Number of user followed',
                                   'Number of favorited tweets']].astype('int32')

f, (ax_box, ax_hist) = plt.subplots(2, gridspec_kw={"height_ratios": (0.2, 1)})
mean = base_friends_df['Number of followers'].mean()
median = base_friends_df['Number of followers'].median()
mode = base_friends_df['Number of followers'].mode()


sns.histplot(base_friends_df["Number of followers"], ax=ax_hist)
ax_hist.axvline(mean, color='r', linestyle='--')
ax_hist.axvline(median, color='g', linestyle='-')
ax_hist.axvline(mode, color='b', linestyle='-')

plt.legend({'Mean': mean, 'Median': median, 'Mode': mode})

ax_box.set(xlabel='')
plt.show()
