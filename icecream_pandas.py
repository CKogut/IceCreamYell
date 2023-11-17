import pandas as pd
from tabulate import tabulate

ic = pd.read_csv('ice_cream.csv')

# print(ic.head(10))

# make df more readable and descriptive
ic.columns = ['id', 'gender', 'ice_cream_flavor', 'video_game_score', 'puzzle_game_score']
ic['gender'] = ic['gender'].replace({0: 'male', 1: 'female'})
ic['ice_cream_flavor'] = ic['ice_cream_flavor'].replace({1: 'Vanilla', 2: 'Chocolate', 3: 'Strawberry'})

# print(tabulate(ic.head(), headers='keys', tablefmt='git') + '\n')

# How many males and females
print(ic['gender'].value_counts())  # 91 female, 109 male
print(ic['ice_cream_flavor'].value_counts())  # 95 vanilla, 58 strawberry, 47 chocolate

# Favorite flavor by gender
fav_per_gender = ic.groupby('gender').ice_cream_flavor.value_counts().reset_index()
print(tabulate(fav_per_gender, headers='keys', tablefmt='git') + '\n')  # Vanilla is the favorite of both


# average video game score grouped by gender
avg_gender_video = ic.groupby('gender').video_game_score.mean().reset_index()
print(tabulate(avg_gender_video, headers='keys', tablefmt='git') + '\n')  # Males did slightly better

# average video game score grouped by gender
avg_gender_puzzle = ic.groupby('gender').puzzle_game_score.mean().reset_index()
print(tabulate(avg_gender_puzzle, headers='keys', tablefmt='git') + '\n')  # Females did slightly better

# average video game score grouped by flavor
avg_flavor_video = ic.groupby('ice_cream_flavor').video_game_score.mean().reset_index()
print(tabulate(avg_flavor_video, headers='keys', tablefmt='git') + '\n')  # Strawberry has the highest average score

# average video game score grouped by flavor
avg_flavor_puzzle = ic.groupby('ice_cream_flavor').puzzle_game_score.mean().reset_index()
print(tabulate(avg_flavor_puzzle, headers='keys', tablefmt='git') + '\n')  # Strawberry has the highest average score





