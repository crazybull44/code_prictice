# pandas转为list
import pandas as pd
df = pd.DataFrame({'a':[1,3,5,7,4,5,6,4,7,8,9],'b':[3,5,6,2,4,6,7,8,7,8,9]})
df['a'].values.tolist()
# or you can just use
df['a'].tolist()
# To drop duplicates you can do one of the following:
df['a'].drop_duplicates().values.tolist()
list(set(df['a']))