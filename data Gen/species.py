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



df = pd.DataFrame(columns=['name', 'Population', 'Trend', 'Male_female_ratio',
                  'Birth_rate',  'Life_expectancy', 'Remarks'])
for i in range(100):
    df.loc[i] = [
        name[i][0],
        getnum(100, 1000000),
        getreal(-100,100),
        getreal(0,1000),
        getnum(0,1000),
        getnum(0,100),
        getname(getnum(5, 20))
    ]


# save thlis csv file in 'D:' drive
df.to_csv('./species_data.csv', index=False)
