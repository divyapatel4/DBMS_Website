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

Price = pd.read_csv('./item.csv')
item = Price.loc[:, "Item"].values
rate = Price.loc[:, "Rate"].values

df = pd.DataFrame(columns=['Item', 'Invoice_ID',
                  'Quantity', 'Price', 'Sanctuary_ID', 'Emp_ID'])
for i in range(100):
    ind = getnum(0, 100)
    q = getnum(1, 10)
    df.loc[i] = [
        item[ind],
        getname(getnum(5, 10))+str(i),
        q,
        q*rate[ind],
        getnum(0,99+1),
        random.choice(emp_id)[0]
    ]


# save thlis csv file in 'D:' drive
df.to_csv('./expenditure.csv', index=False)
