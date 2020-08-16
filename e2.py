import json
import csv
import pandas as pd


# read json
with open('data.json', 'r') as j:
     content = json.loads(j.read())


# write json
header = ['fullname', 'age', 'address', 'occupation']

with open('data.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile, delimiter=',')
    writer.writerow(header)
    
    for i in content:
        try:
            writer.writerow([i, content[i]['age'], content[i]['address'], content[i]['occupation']])
        except:
            print('unable to write data for ' + i)


# make a df from the csv
csv = pd.read_csv('data.csv')
csv


# create lastname column
csv['lastname'] = csv['fullname'].apply(lambda x: x.split()[-1])


output = dict()


# count
def count(df):
    n_of_people = df['lastname'].value_counts()
    
    for i in n_of_people.index:
        output[i] = {'count': int(n_of_people.loc[i])}
    
    for i in ['age', 'address', 'occupation']:
        df_pivot = pd.pivot_table(csv, index='lastname', columns=[i], aggfunc='count')
        for n in df_pivot.index:
            output[n][i] = df_pivot.loc[n].dropna().reset_index(level=0, drop=True).astype('int32').to_dict()


count(csv)

print(json.dumps(output, indent=2))

