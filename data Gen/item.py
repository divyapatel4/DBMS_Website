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
    return datetime.time(getnum(0, 23), getnum(0, 60), getnum(0, 60))


def random_date(begin_year, end_year):
    start = datetime.date(begin_year, 1, 1)
    years = end_year - begin_year + 1
    end = start + datetime.timedelta(days=365 * years)
    return start + (end - start) * random.random()



df = pd.DataFrame(columns=['Item',  'Rate'])


for i in range(100):
    df.loc[i] = [
        getname(getnum(10, 20)),
        getreal(5, 100000)
    ]


# save thlis csv file in 'D:' drive
df.to_csv('./item.csv', index=False)
