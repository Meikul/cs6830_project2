import pandas as pd

df = pd.read_csv('data/crime-housing-austin-2015.csv')
sample = df.sample(n=200)

sample.to_csv('sample.csv')