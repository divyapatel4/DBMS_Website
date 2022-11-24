import random
import string
import pandas as pd


def getname(N):
    res = ''.join(random.choices(string.digits, k=N))
    return res


def getnum(l, r):
    return random.randrange(l, r)


def getreal(l, r):
    return random.uniform(l, r)


emp_id = pd.read_csv('./emp_id.csv')
emp_id = emp_id.values


df = pd.DataFrame(columns=['Mobile_number', 'Emp_ID'])
for i in range(100):
    df.loc[i] = [
        getname(10),
        random.choice(emp_id)[0]
    ]


# save thlis csv file in 'D:' drive
df.to_csv('./mobile_no.csv', index=False)
