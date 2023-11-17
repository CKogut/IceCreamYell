import pandas as pd
from tabulate import tabulate

ic = pd.read_csv('ice_cream.csv')

# print(ic.head(10))

ic.columns = ['id', 'gender', 'ice_cream_flavor', 'video_game_score', 'puzzle_game_score']
ic['gender'] = ic['gender'].replace({0: 'male', 1: 'female'})
ic['ice_cream_flavor'] = ic['ice_cream_flavor'].replace({1: 'Vanilla', 2: 'Chocolate', 3: 'Strawberry'})

print(tabulate(ic.head(), headers='keys', tablefmt='git') + '\n')

avg_gender_video = ic.groupby('gender').video_game_score.mean().reset_index()
print(tabulate(avg_gender_video, headers='keys', tablefmt='git') + '\n')



