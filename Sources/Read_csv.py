import numpy as np
import pandas as pd
from os.path import abspath

df = pd.read_csv('../Data//dt.csv', header = None)
print(df)
x = df.values
print('test x:')
print(x)
for i in range(len(x)):
    x[i, 2] =1

print(x)
