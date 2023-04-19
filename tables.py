import pandas as pd

users_df = pd.read_csv('tables/users.csv')

items_df = pd.read_csv('tables/items.csv')

print(pd.merge(users_df, items_df, on="buyer_pk"))