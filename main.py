import pandas as pd

df = pd.read_csv('GooglePlayStore_wild.csv')

df.info()

print(df.isnull().head())




















#¡Crea tu proyecto individual aquí!

import pandas as pd
df = pd.read_csv('train.csv')

columns_to_drop = ['id', 'bdate', 'sex', 'followers_count', 'graduation', 'relation', 'langs', 'city', 'last_seen', 'occupation_name']

df.drop(columns= columns_to_drop, inplace=True)

df.info()

df.dropna(inplace= True)


print(df.isnull().sum())

#def ser_gender(gender):
#    if gender == 'male':
 #       return 1
 #   return 0

 #cambiar el survive por result

 

