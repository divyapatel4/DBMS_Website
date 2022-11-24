import random
import string
import pandas as pd


def getname(N):
    res = ''.join(random.choices(string.ascii_uppercase, k=N))
    return res


def getnum(l, r):
    return random.randrange(l, r)

def getreal(l,r):
    return random.uniform(l,r)

weather = ['sunny', 'cloudy', 'rainy', 'snowy', 'windy', 'foggy']

wind_direction = ['North', 'South', 'East', 'West',
    'North-East', 'North-West', 'South-East', 'South-West']

Type_of_animal_sanctuary = ['National Park', 'Wildlife Sanctuary',
    'Marine Reserve', 'Bird Sanctuary', 'Bio-Reserve']

# make csv file of 3 columns weather, wind direction and type of animal sanctuary and generate random 100 rows out of these values


df = pd.DataFrame(columns=['name','sanctuary_id','state', 'district','budget','type','weather', 'temperature', 'humidity', 'precipitation', 'wind_direction'])
for i in range(100):
    df.loc[i] = [getname(getnum(5, 10)),
                 i,
                 getname(getnum(5, 10)),
                 getname(getnum(5, 10)),
                 getnum(100000, 100000000),
                 random.choice(Type_of_animal_sanctuary),
                 random.choice(weather),
                 getreal(-10, 50),
                 getreal(0, 100),
                 getreal(0,100),
                 random.choice(wind_direction)]
                 
                 
                 

# save thlis csv file in 'D:' drive
df.to_csv('./temp.csv', index=False)
