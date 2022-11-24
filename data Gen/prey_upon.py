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



species_data = pd.read_csv('./species_data.csv')
species_data = species_data.loc[:, "name"].values
#print(species_data)


df = pd.DataFrame(columns=['Pred_Species', 'Prey_Species'])

for i in range(100):
    df.loc[i] = [
        species_data[i],
        species_data[(i+1)%100]
    ]


# save thlis csv file in 'D:' drive
df.to_csv('./preys_upon.csv', index=False)
