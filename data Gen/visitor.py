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


name = pd.read_csv('./Human_name.csv')
name = name.loc[:, "Name"].values
#print(species_data)

nation = pd.read_csv('./country.csv')
nation = nation.loc[:, "country"].values
#print(species_data)


state = pd.read_csv('./state.csv')
state = state.loc[:, "State"].values
#print(species_data)



df = pd.DataFrame(columns=['Name', 'Nation',
                  'Citizen_ID', 'Gender', 'State', 'District'])

for i in range(200):
    df.loc[i] = [
        random.choice(name),
        random.choice(nation),
        i+765678,
        random.choice(['Male','Female']),
        random.choice(state),
        getname(getnum(5, 20))
    ]


# save thlis csv file in 'D:' drive
df.to_csv('./visitor.csv', index=False)
