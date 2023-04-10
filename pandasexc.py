import pandas as pd


# Raed a CSV file into a Pandas DataFrame:


df = pd.read_csv('data.csv')

# print(df)
# print(type(df))
# print(help(df))
print(df.columns)
print(len(df))
print(df)
print(df.to_string())