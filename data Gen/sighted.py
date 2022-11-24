import random
import string
import pandas as pd
import datetime


def getname(N):
    res = ''.join(random.choices(string.ascii_letters, k=N))
    return res


def getnum(l, r):
    return random.randrange(l, r)


def getreal(l, r):
    return random.uniform(l, r)

def randomTime():
    return datetime.time(getnum(0,23),getnum(0,60),getnum(0,60))

def random_date(begin_year, end_year):
    start = datetime.date(begin_year, 1, 1)
    years = end_year - begin_year + 1
    end = start + datetime.timedelta(days=365 * years)
    return start + (end - start) * random.random()


visitor = pd.read_csv('./visitor.csv')
name = visitor.loc[:, "Citizen_ID"].values
nation = visitor.loc[:, "Nation"].values


animal = pd.read_csv('./animal.csv')
animal = animal.loc[:, "Animal_Name"].values

df = pd.DataFrame(columns=['Date','Time', 'Nation',
                  'Citizen_ID', 'Animal_Name'])


for i in range(25):
    df.loc[i] = [
        random_date(2010, 2020),
        randomTime(),
        nation[i],
        name[i],
        animal[i+25]
    ]


# save thlis csv file in 'D:' drive
df.to_csv('./sighted.csv', index=False)
