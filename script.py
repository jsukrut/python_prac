import pandas as pd


def read_csv(path):
  if path:
      df = pd.read_csv(path)
      return  df

countries_df =read_csv(country.csv)
state_df =read_csv(country.csv)
