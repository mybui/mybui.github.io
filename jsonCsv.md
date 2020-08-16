## 1. Create a CSV file, with a header, that contains the fullname, age, address and occupation.
- Note: fullname is in "Firstname Lastname: format)

## 2. Generate statistics (in JSON format) using the following criteria and answers the following questions:
- Use the lastname as the key.
- How many people have the same last name?
- How many different ages are there?
- How many different occupations?
- The output should look like:
		{
			'lastname1': {
				'count': number_of_people,
				'age': {
					'age1': occurence,
					'age2': occurence
				},
				'address': {
					'address1': occurence,
					'address2': occurence
				},
				'occupation': {
					'job1': occurence
				}
			}
		}


```python
import json
import csv
import pandas as pd
```


```python
json_file_path = "data.json"

with open(json_file_path, 'r') as j:
     content = json.loads(j.read())
```


```python
content
```




    {'John Peterson': {'age': 20, 'address': 'Turku', 'occupation': 'Doctor'},
     'John Munoz': {'age': 26, 'address': 'Oulu', 'occupation': 'Nurse'},
     'Samantha Kennedy': {'age': 27,
      'address': 'Turku',
      'occupation': 'Researcher'},
     'Tiffany Munoz': {'age': 21,
      'address': 'Tampere',
      'occupation': 'Programmer'},
     'Thea Peterson': {'age': 55,
      'address': 'Helsinki',
      'occupation': 'Programmer'},
     'Evie Kennedy': {'age': 32, 'address': 'Lapland', 'occupation': 'Programmer'},
     'Beth Wagner': {'age': 37, 'address': 'Tampere', 'occupation': 'Programmer'},
     'Marie Reid': {'age': 42, 'address': 'Helsinki', 'occupation': 'Programmer'},
     'John Reid': {'age': 46, 'address': 'Oulu', 'occupation': 'Doctor'},
     'Adele Wagner': {'age': 37, 'address': 'Oulu', 'occupation': 'Doctor'},
     'Lola Reid': {'age': 32, 'address': 'Oulu', 'occupation': 'Analyst'},
     'Charlie Peterson': {'age': 41, 'address': 'Tampere', 'occupation': 'Doctor'},
     'Tiffany Kennedy': {'age': 37, 'address': 'Tampere', 'occupation': 'Doctor'},
     'Evie Wagner': {'age': 51, 'address': 'Lapland', 'occupation': 'Analyst'},
     'Annie Reid': {'age': 21, 'address': 'Tampere', 'occupation': 'Doctor'},
     'Aeysha Kennedy': {'age': 35, 'address': 'Turku', 'occupation': 'Analyst'},
     'Jacqueline Peterson': {'age': 26,
      'address': 'Helsinki',
      'occupation': 'Researcher'},
     'Amirah Wagner': {'age': 46, 'address': 'Oulu', 'occupation': 'Programmer'},
     'Beth Peterson': {'age': 34, 'address': 'Oulu', 'occupation': 'Analyst'},
     'Gabrielle Munoz': {'age': 47, 'address': 'Helsinki', 'occupation': 'Doctor'},
     'Gabrielle Wagner': {'age': 29, 'address': 'Lapland', 'occupation': 'Doctor'},
     'Marie Munoz': {'age': 24, 'address': 'Oulu', 'occupation': 'Nurse'},
     'Beth Kennedy': {'age': 44, 'address': 'Turku', 'occupation': 'Doctor'},
     'Gabrielle Reid': {'age': 20, 'address': 'Turku', 'occupation': 'Nurse'},
     'Aimee Reid': {'age': 47, 'address': 'Turku', 'occupation': 'Programmer'},
     'Thea Wagner': {'age': 55, 'address': 'Tampere', 'occupation': 'Programmer'},
     'Aeysha Reid': {'age': 50, 'address': 'Oulu', 'occupation': 'Analyst'},
     'Adele Peterson': {'age': 42,
      'address': 'Tampere',
      'occupation': 'Programmer'},
     'Gabrielle Peterson': {'age': 32,
      'address': 'Helsinki',
      'occupation': 'Doctor'},
     'Amirah Reid': {'age': 36, 'address': 'Helsinki', 'occupation': 'Nurse'},
     'Aeysha Munoz': {'age': 42, 'address': 'Oulu', 'occupation': 'Doctor'},
     'Annie Wagner': {'age': 50, 'address': 'Oulu', 'occupation': 'Doctor'},
     'Samantha Peterson': {'age': 48,
      'address': 'Tampere',
      'occupation': 'Doctor'},
     'Thea Kennedy': {'age': 43, 'address': 'Tampere', 'occupation': 'Researcher'},
     'Lola Munoz': {'age': 28, 'address': 'Tampere', 'occupation': 'Researcher'},
     'Kimberly Reid': {'age': 44, 'address': 'Lapland', 'occupation': 'Doctor'},
     'Adele Kennedy': {'age': 32, 'address': 'Oulu', 'occupation': 'Analyst'},
     'Kimberly Kennedy': {'age': 41,
      'address': 'Lapland',
      'occupation': 'Programmer'},
     'Amirah Munoz': {'age': 45, 'address': 'Lapland', 'occupation': 'Doctor'},
     'Aimee Munoz': {'age': 24, 'address': 'Turku', 'occupation': 'Programmer'},
     'Samantha Reid': {'age': 21, 'address': 'Oulu', 'occupation': 'Researcher'},
     'Taylor Munoz': {'age': 53, 'address': 'Oulu', 'occupation': 'Researcher'},
     'John Wagner': {'age': 51, 'address': 'Turku', 'occupation': 'Nurse'},
     'Aimee Peterson': {'age': 55, 'address': 'Tampere', 'occupation': 'Doctor'},
     'Evie Peterson': {'age': 46, 'address': 'Oulu', 'occupation': 'Doctor'},
     'Aimee Kennedy': {'age': 29,
      'address': 'Lapland',
      'occupation': 'Researcher'},
     'Adele Reid': {'age': 46, 'address': 'Lapland', 'occupation': 'Researcher'},
     'Taylor Peterson': {'age': 55, 'address': 'Helsinki', 'occupation': 'Nurse'},
     'Gabrielle Kennedy': {'age': 30,
      'address': 'Lapland',
      'occupation': 'Analyst'},
     'Lola Peterson': {'age': 31, 'address': 'Helsinki', 'occupation': 'Doctor'},
     'Thea Reid': {'age': 33, 'address': 'Oulu', 'occupation': 'Nurse'},
     'Amirah Kennedy': {'age': 42, 'address': 'Oulu', 'occupation': 'Nurse'},
     'Taylor Wagner': {'age': 53, 'address': 'Turku', 'occupation': 'Doctor'},
     'Lola Wagner': {'age': 49, 'address': 'Oulu', 'occupation': 'Analyst'},
     'Jacqueline Munoz': {'age': 42,
      'address': 'Helsinki',
      'occupation': 'Programmer'},
     'Amirah Peterson': {'age': 22, 'address': 'Lapland', 'occupation': 'Nurse'},
     'Kimberly Peterson': {'age': 28, 'address': 'Tampere', 'occupation': 'Nurse'},
     'Charlie Reid': {'age': 45,
      'address': 'Helsinki',
      'occupation': 'Researcher'},
     'Beth Munoz': {'age': 21, 'address': 'Lapland', 'occupation': 'Programmer'},
     'Mariam Kennedy': {'age': 45, 'address': 'Tampere', 'occupation': 'Analyst'},
     'Marie Peterson': {'age': 26, 'address': 'Tampere', 'occupation': 'Analyst'},
     'Tiffany Reid': {'age': 25, 'address': 'Oulu', 'occupation': 'Analyst'},
     'Kimberly Wagner': {'age': 20,
      'address': 'Tampere',
      'occupation': 'Programmer'},
     'Evie Reid': {'age': 47, 'address': 'Lapland', 'occupation': 'Nurse'},
     'Adele Munoz': {'age': 34, 'address': 'Helsinki', 'occupation': 'Researcher'},
     'Evie Munoz': {'age': 52, 'address': 'Oulu', 'occupation': 'Researcher'},
     'Annie Peterson': {'age': 22, 'address': 'Oulu', 'occupation': 'Programmer'},
     'Annie Kennedy': {'age': 47, 'address': 'Lapland', 'occupation': 'Doctor'},
     'Thea Munoz': {'age': 42, 'address': 'Helsinki', 'occupation': 'Analyst'},
     'Jacqueline Reid': {'age': 45, 'address': 'Oulu', 'occupation': 'Programmer'},
     'Mariam Peterson': {'age': 33, 'address': 'Tampere', 'occupation': 'Analyst'},
     'Aimee Wagner': {'age': 50,
      'address': 'Helsinki',
      'occupation': 'Researcher'},
     'Kimberly Munoz': {'age': 45, 'address': 'Oulu', 'occupation': 'Researcher'},
     'Tiffany Wagner': {'age': 19,
      'address': 'Lapland',
      'occupation': 'Programmer'},
     'Marie Kennedy': {'age': 50, 'address': 'Oulu', 'occupation': 'Researcher'},
     'Aeysha Peterson': {'age': 21, 'address': 'Turku', 'occupation': 'Nurse'},
     'Taylor Reid': {'age': 20, 'address': 'Tampere', 'occupation': 'Doctor'},
     'Jacqueline Wagner': {'age': 40,
      'address': 'Tampere',
      'occupation': 'Researcher'},
     'Charlie Kennedy': {'age': 54, 'address': 'Lapland', 'occupation': 'Doctor'},
     'Samantha Wagner': {'age': 38, 'address': 'Lapland', 'occupation': 'Nurse'},
     'Charlie Munoz': {'age': 42, 'address': 'Oulu', 'occupation': 'Doctor'},
     'Aeysha Wagner': {'age': 23, 'address': 'Helsinki', 'occupation': 'Analyst'},
     'Marie Wagner': {'age': 45, 'address': 'Tampere', 'occupation': 'Programmer'}}




```python
header = ['fullname', 'age', 'address', 'occupation']
```


```python
with open('data.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile, delimiter=',')
    writer.writerow(header)
    
    for i in content:
        try:
            writer.writerow([i, content[i]['age'], content[i]['address'], content[i]['occupation']])
        except:
            print('unable to write data for ' + i)
```


```python
csv = pd.read_csv('data.csv')
csv
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>fullname</th>
      <th>age</th>
      <th>address</th>
      <th>occupation</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>John Peterson</td>
      <td>20</td>
      <td>Turku</td>
      <td>Doctor</td>
    </tr>
    <tr>
      <th>1</th>
      <td>John Munoz</td>
      <td>26</td>
      <td>Oulu</td>
      <td>Nurse</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Samantha Kennedy</td>
      <td>27</td>
      <td>Turku</td>
      <td>Researcher</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Tiffany Munoz</td>
      <td>21</td>
      <td>Tampere</td>
      <td>Programmer</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Thea Peterson</td>
      <td>55</td>
      <td>Helsinki</td>
      <td>Programmer</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>78</th>
      <td>Charlie Kennedy</td>
      <td>54</td>
      <td>Lapland</td>
      <td>Doctor</td>
    </tr>
    <tr>
      <th>79</th>
      <td>Samantha Wagner</td>
      <td>38</td>
      <td>Lapland</td>
      <td>Nurse</td>
    </tr>
    <tr>
      <th>80</th>
      <td>Charlie Munoz</td>
      <td>42</td>
      <td>Oulu</td>
      <td>Doctor</td>
    </tr>
    <tr>
      <th>81</th>
      <td>Aeysha Wagner</td>
      <td>23</td>
      <td>Helsinki</td>
      <td>Analyst</td>
    </tr>
    <tr>
      <th>82</th>
      <td>Marie Wagner</td>
      <td>45</td>
      <td>Tampere</td>
      <td>Programmer</td>
    </tr>
  </tbody>
</table>
<p>83 rows × 4 columns</p>
</div>




```python
csv['lastname'] = csv['fullname'].apply(lambda x: x.split()[-1])
```


```python
output = dict()
```


```python
def count(df):
    n_of_people = df['lastname'].value_counts()
    
    for i in n_of_people.index:
        output[i] = {'count': int(n_of_people.loc[i])}
        
    for i in ['age', 'address', 'occupation']:
        df_pivot = pd.pivot_table(csv, index='lastname', columns=[i], aggfunc='count')
        for n in df_pivot.index:
            output[n][i] = df_pivot.loc[n].dropna().reset_index(level=0, drop=True).astype('int32').to_dict()
```


```python
count(csv)
```


```python
output
```




    {'Peterson': {'count': 18,
      'age': {20: 1,
       21: 1,
       22: 2,
       26: 2,
       28: 1,
       31: 1,
       32: 1,
       33: 1,
       34: 1,
       41: 1,
       42: 1,
       46: 1,
       48: 1,
       55: 3},
      'address': {'Helsinki': 5,
       'Lapland': 1,
       'Oulu': 3,
       'Tampere': 7,
       'Turku': 2},
      'occupation': {'Analyst': 3,
       'Doctor': 7,
       'Nurse': 4,
       'Programmer': 3,
       'Researcher': 1}},
     'Wagner': {'count': 17,
      'age': {19: 1,
       20: 1,
       23: 1,
       29: 1,
       37: 2,
       38: 1,
       40: 1,
       45: 1,
       46: 1,
       49: 1,
       50: 2,
       51: 2,
       53: 1,
       55: 1},
      'address': {'Helsinki': 2,
       'Lapland': 4,
       'Oulu': 4,
       'Tampere': 5,
       'Turku': 2},
      'occupation': {'Analyst': 3,
       'Doctor': 4,
       'Nurse': 2,
       'Programmer': 6,
       'Researcher': 2}},
     'Reid': {'count': 17,
      'age': {20: 2,
       21: 2,
       25: 1,
       32: 1,
       33: 1,
       36: 1,
       42: 1,
       44: 1,
       45: 2,
       46: 2,
       47: 2,
       50: 1},
      'address': {'Helsinki': 3,
       'Lapland': 3,
       'Oulu': 7,
       'Tampere': 2,
       'Turku': 2},
      'occupation': {'Analyst': 3,
       'Doctor': 4,
       'Nurse': 4,
       'Programmer': 3,
       'Researcher': 3}},
     'Munoz': {'count': 16,
      'age': {21: 2,
       24: 2,
       26: 1,
       28: 1,
       34: 1,
       42: 4,
       45: 2,
       47: 1,
       52: 1,
       53: 1},
      'address': {'Helsinki': 4,
       'Lapland': 2,
       'Oulu': 7,
       'Tampere': 2,
       'Turku': 1},
      'occupation': {'Analyst': 1,
       'Doctor': 4,
       'Nurse': 2,
       'Programmer': 4,
       'Researcher': 5}},
     'Kennedy': {'count': 15,
      'age': {27: 1,
       29: 1,
       30: 1,
       32: 2,
       35: 1,
       37: 1,
       41: 1,
       42: 1,
       43: 1,
       44: 1,
       45: 1,
       47: 1,
       50: 1,
       54: 1},
      'address': {'Lapland': 6, 'Oulu': 3, 'Tampere': 3, 'Turku': 3},
      'occupation': {'Analyst': 4,
       'Doctor': 4,
       'Nurse': 1,
       'Programmer': 2,
       'Researcher': 4}}}




```python
print(json.dumps(output, indent=2))
```

    {
      "Peterson": {
        "count": 18,
        "age": {
          "20": 1,
          "21": 1,
          "22": 2,
          "26": 2,
          "28": 1,
          "31": 1,
          "32": 1,
          "33": 1,
          "34": 1,
          "41": 1,
          "42": 1,
          "46": 1,
          "48": 1,
          "55": 3
        },
        "address": {
          "Helsinki": 5,
          "Lapland": 1,
          "Oulu": 3,
          "Tampere": 7,
          "Turku": 2
        },
        "occupation": {
          "Analyst": 3,
          "Doctor": 7,
          "Nurse": 4,
          "Programmer": 3,
          "Researcher": 1
        }
      },
      "Wagner": {
        "count": 17,
        "age": {
          "19": 1,
          "20": 1,
          "23": 1,
          "29": 1,
          "37": 2,
          "38": 1,
          "40": 1,
          "45": 1,
          "46": 1,
          "49": 1,
          "50": 2,
          "51": 2,
          "53": 1,
          "55": 1
        },
        "address": {
          "Helsinki": 2,
          "Lapland": 4,
          "Oulu": 4,
          "Tampere": 5,
          "Turku": 2
        },
        "occupation": {
          "Analyst": 3,
          "Doctor": 4,
          "Nurse": 2,
          "Programmer": 6,
          "Researcher": 2
        }
      },
      "Reid": {
        "count": 17,
        "age": {
          "20": 2,
          "21": 2,
          "25": 1,
          "32": 1,
          "33": 1,
          "36": 1,
          "42": 1,
          "44": 1,
          "45": 2,
          "46": 2,
          "47": 2,
          "50": 1
        },
        "address": {
          "Helsinki": 3,
          "Lapland": 3,
          "Oulu": 7,
          "Tampere": 2,
          "Turku": 2
        },
        "occupation": {
          "Analyst": 3,
          "Doctor": 4,
          "Nurse": 4,
          "Programmer": 3,
          "Researcher": 3
        }
      },
      "Munoz": {
        "count": 16,
        "age": {
          "21": 2,
          "24": 2,
          "26": 1,
          "28": 1,
          "34": 1,
          "42": 4,
          "45": 2,
          "47": 1,
          "52": 1,
          "53": 1
        },
        "address": {
          "Helsinki": 4,
          "Lapland": 2,
          "Oulu": 7,
          "Tampere": 2,
          "Turku": 1
        },
        "occupation": {
          "Analyst": 1,
          "Doctor": 4,
          "Nurse": 2,
          "Programmer": 4,
          "Researcher": 5
        }
      },
      "Kennedy": {
        "count": 15,
        "age": {
          "27": 1,
          "29": 1,
          "30": 1,
          "32": 2,
          "35": 1,
          "37": 1,
          "41": 1,
          "42": 1,
          "43": 1,
          "44": 1,
          "45": 1,
          "47": 1,
          "50": 1,
          "54": 1
        },
        "address": {
          "Lapland": 6,
          "Oulu": 3,
          "Tampere": 3,
          "Turku": 3
        },
        "occupation": {
          "Analyst": 4,
          "Doctor": 4,
          "Nurse": 1,
          "Programmer": 2,
          "Researcher": 4
        }
      }
    }

