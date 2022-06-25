import pandas as pd
df = pd.read_csv('TheGioi.csv')

for i in range(len(df)):
    print(df.iloc[i]['image'])