import pandas as pd
import numpy as np

series = pd.Series(np.random.rand(15))

print('Series: ', series)
print('type of series: ', type(series))
print('Index: ', series.index)
print('Data type: ', series.dtype)
print('First Seven elements: ', series.head(7))
print('Last Seven elements: ', series.tail(7))

df = pd.DataFrame(np.random.rand(16, 4), index = np.arange(16))
df.to_csv('code.csv')

print('df: ', df)
print('data type: ', type(df))
print('columns index: ', df.columns)
print('convert to numpy array: ', df.to_numpy())

newDf = pd.read_csv('code.csv')
print('Read csv file: ', newDf)
