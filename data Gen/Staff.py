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
#convert name to array
name = name.values

country = pd.read_csv('./country.csv')
country = country.values
city = pd.read_csv('./City.csv')
city = city.values
state = pd.read_csv('./state.csv')
state = state.values
street = pd.read_csv('./street.csv')
street = street.values

department_id = ['vjdakvb',
                 'vkdajbv',
                 'xksabfp',
                 'nvioewhvg3209',
                 'cnewoif02fbeq',
                 'veniowH320',
                 'VNIOW0232',
                 'CVNDown382',
                 'em204b',
                 'vcn302',
                 'vcn032hf',
                 'vn03284']

df = pd.DataFrame(columns=['name', 'Emp_ID', 'Sanctuary_ID', 'Nation', 'State',  'district', 'city', 'street', 'block', 'department_ID'])
for i in range(100):
    df.loc[i] = [
        random.choice(name)[0],
        getname(getnum(5, 10))+str(i),
        getnum(0,99),
        random.choice(country)[0],
        random.choice(state)[0],
        getname(getnum(5, 10)),
        random.choice(city)[0],
        random.choice(street)[0],
        getnum(5, 150),
        getnum(0,12)
    ]


# save thlis csv file in 'D:' drive
df.to_csv('./staff.csv', index=False)
