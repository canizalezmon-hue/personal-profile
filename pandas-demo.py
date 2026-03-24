import pandas as pd

df = pd.read_csv('GoogleApps.csv')


data = df[(df['Rating'] > 4.9) & (df['Type' == 'Free'])]['Installs'].mean()
print(data)