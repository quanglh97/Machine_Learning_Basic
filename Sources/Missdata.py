import numpy as np
import pandas as pd
from sklearn.impute import SimpleImputer

data = pd.read_csv('../Data//dt.csv', header=None)
print(data)
x = data.values
imp = SimpleImputer(missing_values=np.nan, strategy='mean')
imp.fit(x)
result = imp.transform(x)
print('ket qua la:')
print(result)


