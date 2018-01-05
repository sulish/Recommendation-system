import numpy as np
import pandas as pd

df=pd.read_csv('train1.csv')
# np.where(pd.isnull(df))
a= df.isnull().sum().sum()
print a