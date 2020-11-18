import pandas as pd

df1 = pd.read_csv('drive1.csv')
df2 = pd.read_csv('kunal1.csv')

out = df1.append(df2)

out.to_csv("update.csv")