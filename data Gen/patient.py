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


Emp_ID = pd.read_csv('./staff.csv')
Emp_ID = Emp_ID.loc[:, "Emp_ID"].values
#print(species_data)


disease = pd.read_csv('./disease.csv')
disease = disease.loc[:, "Disease"].values
#print(species_data)


species_data = pd.read_csv('./animal.csv')
animal = species_data.loc[:, "Animal_Name"].values
species = species_data.loc[:, "Species_Name"].values


df = pd.DataFrame(columns=['Species', 'Animal_Name', 'Disease', 'History_of_illness', 'Emp_ID'])

for i in range(25):
    df.loc[i] = [
        animal[i],
        species[i],
        random.choice(Emp_ID),
        random.choice(disease),
        getname(getnum(5, 20))
    ]


# save thlis csv file in 'D:' drive
df.to_csv('./patient.csv', index=False)
