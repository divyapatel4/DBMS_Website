import random
import string
import pandas as pd


def getname(N):
    res = ''.join(random.choices(string.ascii_letters, k=N))
    return res


def getnum(l, r):
    return random.randrange(l, r)


def getreal(l, r):
    return random.uniform(l, r)


name = pd.read_csv('./species.csv')
name = name.values

species_data = pd.read_csv('./species_data.csv')
species_data = species_data.loc[:,"name"].values
#print(species_data)



df = pd.DataFrame(columns=['Animal_Name', 'Species_Name', 'Sanctuary_ID', 'Health',
                  'Age',  'Gender'])
for i in range(100):
    df.loc[i] = [
        getname(getnum(5, 20)),
        random.choice(species_data),
        getnum(0,100),
        random.choice(['good','bad']),
        getnum(1, 100),
        random.choice(['Female', 'Male']),
    ]


# save thlis csv file in 'D:' drive
df.to_csv('./animal.csv', index=False)
