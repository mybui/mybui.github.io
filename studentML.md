## Attributes
### Demographic
- school - student's school (binary: 'GP' - Gabriel Pereira or 'MS' - Mousinho da Silveira) 
- sex - student's sex (binary: 'F' - female or 'M' - male) 
- age - student's age (numeric: from 15 to 22) 
- address - student's home address type (binary: 'U' - urban or 'R' - rural) 
- famsize - family size (binary: 'LE3' - less or equal to 3 or 'GT3' - greater than 3)  
- Pstatus - parent's cohabitation status (binary: 'T' - living together or 'A' - apart) 
- Medu - mother's education (numeric: 0 - none, 1 - primary education (4th grade), 2 - 5th to 9th grade, 3 - secondary education or 4 - higher education) 
- Fedu - father's education (numeric: 0 - none, 1 - primary education (4th grade), 2 - 5th to 9th grade, 3 - secondary education or 4 - higher education) 
- Mjob - mother's job (nominal: 'teacher', 'health' care related, civil 'services' (e.g. administrative or police), 'at_home' or 'other') 
- Fjob - father's job (nominal: 'teacher', 'health' care related, civil 'services' (e.g. administrative or police), 'at_home' or 'other') 
- reason - reason to choose this school (nominal: close to 'home', school 'reputation', 'course' preference or 'other') 
- guardian - student's guardian (nominal: 'mother', 'father' or 'other') 
- traveltime - home to school travel time (numeric: 1 - <15 min., 2 - 15 to 30 min., 3 - 30 min. to 1 hour, or 4 - >1 hour) 
- studytime - weekly study time (numeric: 1 - <2 hours, 2 - 2 to 5 hours, 3 - 5 to 10 hours, or 4 - >10 hours) 
- failures - number of past class failures (numeric: n if 1<=n<3, else 4) 
- schoolsup - extra educational support (binary: yes or no) 
- famsup - family educational support (binary: yes or no) 
- paid - extra paid classes within the course subject (Math or Portuguese) (binary: yes or no) 
- activities - extra-curricular activities (binary: yes or no) 
- nursery - attended nursery school (binary: yes or no) 
- higher - wants to take higher education (binary: yes or no) 
- internet - Internet access at home (binary: yes or no) 
- romantic - with a romantic relationship (binary: yes or no) 
- famrel - quality of family relationships (numeric: from 1 - very bad to 5 - excellent) 
- freetime - free time after school (numeric: from 1 - very low to 5 - very high) 
- goout - going out with friends (numeric: from 1 - very low to 5 - very high) 
- Dalc - workday alcohol consumption (numeric: from 1 - very low to 5 - very high) 
- Walc - weekend alcohol consumption (numeric: from 1 - very low to 5 - very high) 
- health - current health status (numeric: from 1 - very bad to 5 - very good) 
- absences - number of school absences (numeric: from 0 to 93) 

### School performance
- G1 - first period grade (numeric: from 0 to 20) 
- G2 - second period grade (numeric: from 0 to 20) 
- G3 - final grade (numeric: from 0 to 20, output target)

## ML task: 
1. Regression - final grade G3
2. Binary classification – pass if G3 ≥ 10 else fail
3. 5-Level classification – based on the Erasmus grade conversion system


```python
import pandas as pd
import numpy as np
from sklearn.linear_model import Ridge
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.linear_model import Lasso
```


```python
data = pd.read_csv('student/student-mat.csv', sep=';')
data
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
      <th>school</th>
      <th>sex</th>
      <th>age</th>
      <th>address</th>
      <th>famsize</th>
      <th>Pstatus</th>
      <th>Medu</th>
      <th>Fedu</th>
      <th>Mjob</th>
      <th>Fjob</th>
      <th>...</th>
      <th>famrel</th>
      <th>freetime</th>
      <th>goout</th>
      <th>Dalc</th>
      <th>Walc</th>
      <th>health</th>
      <th>absences</th>
      <th>G1</th>
      <th>G2</th>
      <th>G3</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>GP</td>
      <td>F</td>
      <td>18</td>
      <td>U</td>
      <td>GT3</td>
      <td>A</td>
      <td>4</td>
      <td>4</td>
      <td>at_home</td>
      <td>teacher</td>
      <td>...</td>
      <td>4</td>
      <td>3</td>
      <td>4</td>
      <td>1</td>
      <td>1</td>
      <td>3</td>
      <td>6</td>
      <td>5</td>
      <td>6</td>
      <td>6</td>
    </tr>
    <tr>
      <th>1</th>
      <td>GP</td>
      <td>F</td>
      <td>17</td>
      <td>U</td>
      <td>GT3</td>
      <td>T</td>
      <td>1</td>
      <td>1</td>
      <td>at_home</td>
      <td>other</td>
      <td>...</td>
      <td>5</td>
      <td>3</td>
      <td>3</td>
      <td>1</td>
      <td>1</td>
      <td>3</td>
      <td>4</td>
      <td>5</td>
      <td>5</td>
      <td>6</td>
    </tr>
    <tr>
      <th>2</th>
      <td>GP</td>
      <td>F</td>
      <td>15</td>
      <td>U</td>
      <td>LE3</td>
      <td>T</td>
      <td>1</td>
      <td>1</td>
      <td>at_home</td>
      <td>other</td>
      <td>...</td>
      <td>4</td>
      <td>3</td>
      <td>2</td>
      <td>2</td>
      <td>3</td>
      <td>3</td>
      <td>10</td>
      <td>7</td>
      <td>8</td>
      <td>10</td>
    </tr>
    <tr>
      <th>3</th>
      <td>GP</td>
      <td>F</td>
      <td>15</td>
      <td>U</td>
      <td>GT3</td>
      <td>T</td>
      <td>4</td>
      <td>2</td>
      <td>health</td>
      <td>services</td>
      <td>...</td>
      <td>3</td>
      <td>2</td>
      <td>2</td>
      <td>1</td>
      <td>1</td>
      <td>5</td>
      <td>2</td>
      <td>15</td>
      <td>14</td>
      <td>15</td>
    </tr>
    <tr>
      <th>4</th>
      <td>GP</td>
      <td>F</td>
      <td>16</td>
      <td>U</td>
      <td>GT3</td>
      <td>T</td>
      <td>3</td>
      <td>3</td>
      <td>other</td>
      <td>other</td>
      <td>...</td>
      <td>4</td>
      <td>3</td>
      <td>2</td>
      <td>1</td>
      <td>2</td>
      <td>5</td>
      <td>4</td>
      <td>6</td>
      <td>10</td>
      <td>10</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>390</th>
      <td>MS</td>
      <td>M</td>
      <td>20</td>
      <td>U</td>
      <td>LE3</td>
      <td>A</td>
      <td>2</td>
      <td>2</td>
      <td>services</td>
      <td>services</td>
      <td>...</td>
      <td>5</td>
      <td>5</td>
      <td>4</td>
      <td>4</td>
      <td>5</td>
      <td>4</td>
      <td>11</td>
      <td>9</td>
      <td>9</td>
      <td>9</td>
    </tr>
    <tr>
      <th>391</th>
      <td>MS</td>
      <td>M</td>
      <td>17</td>
      <td>U</td>
      <td>LE3</td>
      <td>T</td>
      <td>3</td>
      <td>1</td>
      <td>services</td>
      <td>services</td>
      <td>...</td>
      <td>2</td>
      <td>4</td>
      <td>5</td>
      <td>3</td>
      <td>4</td>
      <td>2</td>
      <td>3</td>
      <td>14</td>
      <td>16</td>
      <td>16</td>
    </tr>
    <tr>
      <th>392</th>
      <td>MS</td>
      <td>M</td>
      <td>21</td>
      <td>R</td>
      <td>GT3</td>
      <td>T</td>
      <td>1</td>
      <td>1</td>
      <td>other</td>
      <td>other</td>
      <td>...</td>
      <td>5</td>
      <td>5</td>
      <td>3</td>
      <td>3</td>
      <td>3</td>
      <td>3</td>
      <td>3</td>
      <td>10</td>
      <td>8</td>
      <td>7</td>
    </tr>
    <tr>
      <th>393</th>
      <td>MS</td>
      <td>M</td>
      <td>18</td>
      <td>R</td>
      <td>LE3</td>
      <td>T</td>
      <td>3</td>
      <td>2</td>
      <td>services</td>
      <td>other</td>
      <td>...</td>
      <td>4</td>
      <td>4</td>
      <td>1</td>
      <td>3</td>
      <td>4</td>
      <td>5</td>
      <td>0</td>
      <td>11</td>
      <td>12</td>
      <td>10</td>
    </tr>
    <tr>
      <th>394</th>
      <td>MS</td>
      <td>M</td>
      <td>19</td>
      <td>U</td>
      <td>LE3</td>
      <td>T</td>
      <td>1</td>
      <td>1</td>
      <td>other</td>
      <td>at_home</td>
      <td>...</td>
      <td>3</td>
      <td>2</td>
      <td>3</td>
      <td>3</td>
      <td>3</td>
      <td>5</td>
      <td>5</td>
      <td>8</td>
      <td>9</td>
      <td>9</td>
    </tr>
  </tbody>
</table>
<p>395 rows × 33 columns</p>
</div>



### Feature Engineering


```python
o = list(data.select_dtypes(include='object').columns)
o
```




    ['school',
     'sex',
     'address',
     'famsize',
     'Pstatus',
     'Mjob',
     'Fjob',
     'reason',
     'guardian',
     'schoolsup',
     'famsup',
     'paid',
     'activities',
     'nursery',
     'higher',
     'internet',
     'romantic']




```python
num_data = data.copy().drop(o, axis=1)
```


```python
txt_data = data.loc[:, o]
```


```python
# categorize these nominal features and make corresponding dummies
for i in o:
    txt_data[i] = data[i].astype('category')
    txt_data = pd.concat([txt_data, 
                        pd.get_dummies(txt_data.select_dtypes(include=['category']))], axis=1).drop(i, axis=1)
```


```python
trans_data = pd.concat([txt_data, num_data], axis=1)
```


```python
trans_data
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
      <th>school_GP</th>
      <th>school_MS</th>
      <th>sex_F</th>
      <th>sex_M</th>
      <th>address_R</th>
      <th>address_U</th>
      <th>famsize_GT3</th>
      <th>famsize_LE3</th>
      <th>Pstatus_A</th>
      <th>Pstatus_T</th>
      <th>...</th>
      <th>famrel</th>
      <th>freetime</th>
      <th>goout</th>
      <th>Dalc</th>
      <th>Walc</th>
      <th>health</th>
      <th>absences</th>
      <th>G1</th>
      <th>G2</th>
      <th>G3</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>1</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>...</td>
      <td>4</td>
      <td>3</td>
      <td>4</td>
      <td>1</td>
      <td>1</td>
      <td>3</td>
      <td>6</td>
      <td>5</td>
      <td>6</td>
      <td>6</td>
    </tr>
    <tr>
      <th>1</th>
      <td>1</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>...</td>
      <td>5</td>
      <td>3</td>
      <td>3</td>
      <td>1</td>
      <td>1</td>
      <td>3</td>
      <td>4</td>
      <td>5</td>
      <td>5</td>
      <td>6</td>
    </tr>
    <tr>
      <th>2</th>
      <td>1</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>1</td>
      <td>...</td>
      <td>4</td>
      <td>3</td>
      <td>2</td>
      <td>2</td>
      <td>3</td>
      <td>3</td>
      <td>10</td>
      <td>7</td>
      <td>8</td>
      <td>10</td>
    </tr>
    <tr>
      <th>3</th>
      <td>1</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>...</td>
      <td>3</td>
      <td>2</td>
      <td>2</td>
      <td>1</td>
      <td>1</td>
      <td>5</td>
      <td>2</td>
      <td>15</td>
      <td>14</td>
      <td>15</td>
    </tr>
    <tr>
      <th>4</th>
      <td>1</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>...</td>
      <td>4</td>
      <td>3</td>
      <td>2</td>
      <td>1</td>
      <td>2</td>
      <td>5</td>
      <td>4</td>
      <td>6</td>
      <td>10</td>
      <td>10</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>390</th>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>1</td>
      <td>1</td>
      <td>0</td>
      <td>...</td>
      <td>5</td>
      <td>5</td>
      <td>4</td>
      <td>4</td>
      <td>5</td>
      <td>4</td>
      <td>11</td>
      <td>9</td>
      <td>9</td>
      <td>9</td>
    </tr>
    <tr>
      <th>391</th>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>1</td>
      <td>...</td>
      <td>2</td>
      <td>4</td>
      <td>5</td>
      <td>3</td>
      <td>4</td>
      <td>2</td>
      <td>3</td>
      <td>14</td>
      <td>16</td>
      <td>16</td>
    </tr>
    <tr>
      <th>392</th>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>1</td>
      <td>1</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>...</td>
      <td>5</td>
      <td>5</td>
      <td>3</td>
      <td>3</td>
      <td>3</td>
      <td>3</td>
      <td>3</td>
      <td>10</td>
      <td>8</td>
      <td>7</td>
    </tr>
    <tr>
      <th>393</th>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>1</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>1</td>
      <td>...</td>
      <td>4</td>
      <td>4</td>
      <td>1</td>
      <td>3</td>
      <td>4</td>
      <td>5</td>
      <td>0</td>
      <td>11</td>
      <td>12</td>
      <td>10</td>
    </tr>
    <tr>
      <th>394</th>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>1</td>
      <td>...</td>
      <td>3</td>
      <td>2</td>
      <td>3</td>
      <td>3</td>
      <td>3</td>
      <td>5</td>
      <td>5</td>
      <td>8</td>
      <td>9</td>
      <td>9</td>
    </tr>
  </tbody>
</table>
<p>395 rows × 59 columns</p>
</div>



### 1. Linear Regression (LR)


```python
X = trans_data.iloc[:, :58].values
y = trans_data.iloc[:, 58].values
```


```python
X_train, X_test, y_train, y_test = train_test_split(X, y, shuffle=True, random_state=0)
```


```python
lr = LinearRegression()
lr.fit(X_train, y_train)
y_pred = lr.predict(X_test)
mse = mean_squared_error(y_test, y_pred)
mse
```




    6.14478692382273



### Regularization with Ridge Regression (RR) which sets some features to be close to zero

Try out different values of alpha for regularization


```python
ridge_df = pd.DataFrame()
ridge_mse = []

for alpha in np.arange(1, 200, 1):
    ridge = Ridge(alpha=alpha)
    ridge.fit(X_train, y_train)
    ridge_df[alpha] = ridge.coef_
    ridge_mse.append(mean_squared_error(ridge.predict(X_test), y_test))

ridge_df = ridge_df.T
ridge_df
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
      <th>0</th>
      <th>1</th>
      <th>2</th>
      <th>3</th>
      <th>4</th>
      <th>5</th>
      <th>6</th>
      <th>7</th>
      <th>8</th>
      <th>9</th>
      <th>...</th>
      <th>48</th>
      <th>49</th>
      <th>50</th>
      <th>51</th>
      <th>52</th>
      <th>53</th>
      <th>54</th>
      <th>55</th>
      <th>56</th>
      <th>57</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>1</th>
      <td>-0.175165</td>
      <td>0.175165</td>
      <td>-0.103920</td>
      <td>0.103920</td>
      <td>-0.081354</td>
      <td>0.081354</td>
      <td>-0.056786</td>
      <td>0.056786</td>
      <td>0.145694</td>
      <td>-0.145694</td>
      <td>...</td>
      <td>-0.157074</td>
      <td>0.158110</td>
      <td>0.042826</td>
      <td>-0.061411</td>
      <td>-0.212318</td>
      <td>0.233830</td>
      <td>0.094764</td>
      <td>0.053072</td>
      <td>0.155966</td>
      <td>0.952054</td>
    </tr>
    <tr>
      <th>2</th>
      <td>-0.172091</td>
      <td>0.172091</td>
      <td>-0.101828</td>
      <td>0.101828</td>
      <td>-0.079433</td>
      <td>0.079433</td>
      <td>-0.056676</td>
      <td>0.056676</td>
      <td>0.142775</td>
      <td>-0.142775</td>
      <td>...</td>
      <td>-0.157279</td>
      <td>0.157483</td>
      <td>0.042661</td>
      <td>-0.061260</td>
      <td>-0.208337</td>
      <td>0.231553</td>
      <td>0.094180</td>
      <td>0.052949</td>
      <td>0.155394</td>
      <td>0.952180</td>
    </tr>
    <tr>
      <th>3</th>
      <td>-0.169075</td>
      <td>0.169075</td>
      <td>-0.099830</td>
      <td>0.099830</td>
      <td>-0.077643</td>
      <td>0.077643</td>
      <td>-0.056511</td>
      <td>0.056511</td>
      <td>0.139965</td>
      <td>-0.139965</td>
      <td>...</td>
      <td>-0.157385</td>
      <td>0.156832</td>
      <td>0.042499</td>
      <td>-0.061107</td>
      <td>-0.204515</td>
      <td>0.229363</td>
      <td>0.093608</td>
      <td>0.052826</td>
      <td>0.154913</td>
      <td>0.952247</td>
    </tr>
    <tr>
      <th>4</th>
      <td>-0.166125</td>
      <td>0.166125</td>
      <td>-0.097920</td>
      <td>0.097920</td>
      <td>-0.075970</td>
      <td>0.075970</td>
      <td>-0.056303</td>
      <td>0.056303</td>
      <td>0.137262</td>
      <td>-0.137262</td>
      <td>...</td>
      <td>-0.157407</td>
      <td>0.156162</td>
      <td>0.042341</td>
      <td>-0.060955</td>
      <td>-0.200841</td>
      <td>0.227253</td>
      <td>0.093050</td>
      <td>0.052703</td>
      <td>0.154511</td>
      <td>0.952261</td>
    </tr>
    <tr>
      <th>5</th>
      <td>-0.163244</td>
      <td>0.163244</td>
      <td>-0.096091</td>
      <td>0.096091</td>
      <td>-0.074401</td>
      <td>0.074401</td>
      <td>-0.056062</td>
      <td>0.056062</td>
      <td>0.134660</td>
      <td>-0.134660</td>
      <td>...</td>
      <td>-0.157361</td>
      <td>0.155477</td>
      <td>0.042186</td>
      <td>-0.060803</td>
      <td>-0.197303</td>
      <td>0.225217</td>
      <td>0.092506</td>
      <td>0.052580</td>
      <td>0.154178</td>
      <td>0.952231</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>195</th>
      <td>-0.030416</td>
      <td>0.030416</td>
      <td>-0.029442</td>
      <td>0.029442</td>
      <td>-0.030304</td>
      <td>0.030304</td>
      <td>-0.023686</td>
      <td>0.023686</td>
      <td>0.032109</td>
      <td>-0.032109</td>
      <td>...</td>
      <td>-0.098194</td>
      <td>0.072108</td>
      <td>0.031251</td>
      <td>-0.043248</td>
      <td>-0.037198</td>
      <td>0.112158</td>
      <td>0.055302</td>
      <td>0.042920</td>
      <td>0.213843</td>
      <td>0.863639</td>
    </tr>
    <tr>
      <th>196</th>
      <td>-0.030254</td>
      <td>0.030254</td>
      <td>-0.029375</td>
      <td>0.029375</td>
      <td>-0.030265</td>
      <td>0.030265</td>
      <td>-0.023620</td>
      <td>0.023620</td>
      <td>0.031990</td>
      <td>-0.031990</td>
      <td>...</td>
      <td>-0.098020</td>
      <td>0.071881</td>
      <td>0.031214</td>
      <td>-0.043190</td>
      <td>-0.036993</td>
      <td>0.111923</td>
      <td>0.055201</td>
      <td>0.042896</td>
      <td>0.214141</td>
      <td>0.863209</td>
    </tr>
    <tr>
      <th>197</th>
      <td>-0.030093</td>
      <td>0.030093</td>
      <td>-0.029308</td>
      <td>0.029308</td>
      <td>-0.030227</td>
      <td>0.030227</td>
      <td>-0.023555</td>
      <td>0.023555</td>
      <td>0.031871</td>
      <td>-0.031871</td>
      <td>...</td>
      <td>-0.097846</td>
      <td>0.071656</td>
      <td>0.031176</td>
      <td>-0.043131</td>
      <td>-0.036789</td>
      <td>0.111688</td>
      <td>0.055100</td>
      <td>0.042872</td>
      <td>0.214438</td>
      <td>0.862781</td>
    </tr>
    <tr>
      <th>198</th>
      <td>-0.029933</td>
      <td>0.029933</td>
      <td>-0.029242</td>
      <td>0.029242</td>
      <td>-0.030189</td>
      <td>0.030189</td>
      <td>-0.023490</td>
      <td>0.023490</td>
      <td>0.031754</td>
      <td>-0.031754</td>
      <td>...</td>
      <td>-0.097674</td>
      <td>0.071432</td>
      <td>0.031139</td>
      <td>-0.043073</td>
      <td>-0.036587</td>
      <td>0.111456</td>
      <td>0.055000</td>
      <td>0.042848</td>
      <td>0.214734</td>
      <td>0.862353</td>
    </tr>
    <tr>
      <th>199</th>
      <td>-0.029774</td>
      <td>0.029774</td>
      <td>-0.029177</td>
      <td>0.029177</td>
      <td>-0.030152</td>
      <td>0.030152</td>
      <td>-0.023426</td>
      <td>0.023426</td>
      <td>0.031638</td>
      <td>-0.031638</td>
      <td>...</td>
      <td>-0.097502</td>
      <td>0.071209</td>
      <td>0.031102</td>
      <td>-0.043015</td>
      <td>-0.036387</td>
      <td>0.111224</td>
      <td>0.054900</td>
      <td>0.042824</td>
      <td>0.215029</td>
      <td>0.861926</td>
    </tr>
  </tbody>
</table>
<p>199 rows × 58 columns</p>
</div>



Among the last 10 features, G2 is given the highest importance, and secondly G1.


```python
fig, ax = plt.subplots(figsize=(10, 5))
ax.plot(ridge_df.iloc[:, 50:])
ax.axhline(y=0, color='black', linestyle='--')
ax.set_xlabel("alpha")
ax.set_ylabel("coeficients")
ax.set_title("RR for the last 10 features")
ax.legend(labels=list(trans_data.iloc[:, 50:-1].columns))
ax.grid(True)
```


![png](output_19_0.png)


The plot of MSE shows the optimum alpha is in [70, 80].


```python
fig, ax = plt.subplots(figsize=(10, 5))
plt.plot(ridge_mse)
ax.set_xlabel("alpha")
ax.set_ylabel("mse")
ax.set_title("RR MSE trace")
ax.axhline(y=mse, color='red', linestyle='--')
ax.legend(['RR', 'OLS'])
plt.show()
```


![png](output_21_0.png)


### Regularization with Lasso which ignores some features completely

Try out different values of alpha for regularization. The model uses more features when alpha is smaller.


```python
lasso_df = pd.DataFrame()
lasso_mse = []
a_range = list(reversed([1, 0.1, 0.01, 0.001, 0.0001, 0.00001, 0.000001]))
for alpha in a_range:
    lasso = Lasso(alpha=alpha, max_iter=100000)
    lasso.fit(X_train, y_train)
    print(lasso.coef_)
    lasso_df[alpha] = lasso.coef_
    lasso_mse.append(mean_squared_error(lasso.predict(X_test), y_test))

lasso_df = lasso_df.T
lasso_df
```


```python
fig, ax = plt.subplots(figsize=(10, 5))
ax.plot(lasso_df.iloc[:, 50:])
ax.axhline(y=0, color='black', linestyle='--')
ax.set_xlabel("alpha")
ax.set_ylabel("coeficients")
ax.set_title("Lasso for the last 10 features")
labels = [item.get_text() for item in ax.get_xticklabels()]
for i in range(0, len(labels)-1):
    labels[i] = a_range[i] 
ax.set_xticklabels(labels, rotation=45)
ax.legend(labels=list(trans_data.iloc[:, 50:-1].columns))
ax.grid(True)
```


![png](output_25_0.png)


At alpha = 0.01, the model achieves the best performance which uses 42 features.


```python
fig, ax = plt.subplots(figsize=(10, 5))
plt.plot(lasso_mse)
ax.set_xlabel("alpha")
ax.set_ylabel("mse")
ax.set_title("Lasso MSE trace")
ax.axhline(y=mse, color='red', linestyle='--')
labels = [item.get_text() for item in ax.get_xticklabels()]
for i in range(0, len(labels)-2):
    labels[i+1] = a_range[i] 
ax.set_xticklabels(labels, rotation=45)
ax.legend(['Lasso', 'OLS'])
plt.show()
```


![png](output_27_0.png)



```python
a_001 = lasso_df.iloc[4, :]
len(a_001[a_001 != 0])
```




    42



### Robust Regression (RbR) for outliers


```python
# make some strong outliers for X
X_errors = X.copy()
X_errors[::3] = 100
```


```python
from sklearn.model_selection import train_test_split
X_train_error, X_test_error, y_train, y_test = train_test_split(X_errors, y, shuffle=True, random_state=0)
```


```python
from sklearn.linear_model import (LinearRegression, TheilSenRegressor, RANSACRegressor, HuberRegressor)
from sklearn.metrics import mean_squared_error
estimators = [('OLS', LinearRegression()),
              ('Theil-Sen', TheilSenRegressor(random_state=42, max_iter=10000)),
              ('RANSAC', RANSACRegressor(random_state=42, max_trials=10000)),
              ('HuberRegressor', HuberRegressor(max_iter=10000))]
```

TheilSen is good for strong outliers, both in direction X and y.


```python
for e in estimators:
    m = e[1].fit(X_train_error, y_train)
    print("For " + e[0] + " technique:")
    print("Training set score: {:.2f}".format(m.score(X_train_error, y_train))) 
    print("Test set score: {:.2f}".format(m.score(X_test_error, y_test))) 
    print("MSE: {:.2f} \n".format(mean_squared_error(y_test, m.predict(X_test_error))))
```

    For OLS technique:
    Training set score: 0.66
    Test set score: 0.47
    MSE: 15.04 
    
    For Theil-Sen technique:
    Training set score: 0.66
    Test set score: 0.48
    MSE: 14.73 
    
    For RANSAC technique:
    Training set score: 0.61
    Test set score: 0.43
    MSE: 16.09 
    
    For HuberRegressor technique:
    Training set score: 0.64
    Test set score: 0.46
    MSE: 15.39 
    



```python
# make some strong outliers for y
y_errors = y.copy()
y_errors[::2] = 100
```


```python
from sklearn.model_selection import train_test_split
X_train, X_test, y_train_error, y_test_error = train_test_split(X, y_errors, shuffle=True, random_state=0)
```


```python
for e in estimators:
    m = e[1].fit(X_train, y_train_error)
    print("For " + e[0] + " technique:")
    print("Training set score: {:.2f}".format(m.score(X_train, y_train_error))) 
    print("Test set score: {:.2f}".format(m.score(X_test, y_test_error))) 
    print("MSE: {:.2f} \n".format(mean_squared_error(y_test_error, m.predict(X_test))))
```

    For OLS technique:
    Training set score: 0.10
    Test set score: -0.25
    MSE: 2508.31 
    
    For Theil-Sen technique:
    Training set score: 0.09
    Test set score: -0.27
    MSE: 2547.76 
    
    For RANSAC technique:
    Training set score: -1.51
    Test set score: -2.12
    MSE: 6232.98 
    
    For HuberRegressor technique:
    Training set score: 0.10
    Test set score: -0.30
    MSE: 2592.34 
    


### Polynomial Regression with features G1 & G2 to predict G3


```python
X = trans_data.iloc[:, 56:58].values
y = trans_data.iloc[:, 58].values
```


```python
from sklearn.preprocessing import PolynomialFeatures
pol_mse = []
d_range = np.arange(2, 8, 1)

for d in d_range:
    pol = PolynomialFeatures(degree=d)
    pol.fit(X_train, y_train)
    X_2 = pol.fit_transform(X)
    X_train, X_test, y_train, y_test = train_test_split(X_2, y, random_state=0)
    # OLS
    lr = LinearRegression()
    lr.fit(X_train, y_train)
    y_pred = lr.predict(X_test)
    pol_mse.append(mean_squared_error(y_test, y_pred))
```


```python
pol_mse
```




    [6.273301123930405,
     6.155807238512367,
     6.229853804336613,
     6.375376965526311,
     6.949451552084533,
     6.519870726895505]



Polynomial Regression with 2 features so far performs the best compared to other models


```python
fig, ax = plt.subplots(figsize=(10, 5))
plt.plot(pol_mse)
ax.set_xlabel("degree")
ax.set_ylabel("mse")
ax.set_title("PR MSE trace")
ax.axhline(y=mse, color='red', linestyle='--')
ax.set_xticklabels(np.arange(1, 8, 1))
ax.legend(['PR', 'OLS'])
plt.show()
```


![png](output_43_0.png)


### 2. Binary classification for G3

Create a new column that categorizes the feature G3 as fail if < 10, and pass otherwise


```python
def pass_grade(x):
    if x <= 10:
        return 0
    else:
        return 1
    
trans_data['pass'] = trans_data['G3'].apply(lambda x: pass_grade(x))
```


```python
trans_data[['G3', 'pass']]
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
      <th>G3</th>
      <th>pass</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>6</td>
      <td>0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>6</td>
      <td>0</td>
    </tr>
    <tr>
      <th>2</th>
      <td>10</td>
      <td>0</td>
    </tr>
    <tr>
      <th>3</th>
      <td>15</td>
      <td>1</td>
    </tr>
    <tr>
      <th>4</th>
      <td>10</td>
      <td>0</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>390</th>
      <td>9</td>
      <td>0</td>
    </tr>
    <tr>
      <th>391</th>
      <td>16</td>
      <td>1</td>
    </tr>
    <tr>
      <th>392</th>
      <td>7</td>
      <td>0</td>
    </tr>
    <tr>
      <th>393</th>
      <td>10</td>
      <td>0</td>
    </tr>
    <tr>
      <th>394</th>
      <td>9</td>
      <td>0</td>
    </tr>
  </tbody>
</table>
<p>395 rows × 2 columns</p>
</div>




```python
from sklearn.svm import LinearSVC
lsvc = LinearSVC(max_iter=100000).fit(X_train, y_train)
print("Training set score: {:.3f}".format(lsvc.score(X_train, y_train))) 
print("Test set score: {:.3f}".format(lsvc.score(X_test, y_test)))
```

    Training set score: 0.986
    Test set score: 0.899



```python
X = trans_data.iloc[:, :58].values
y = trans_data['pass'].values

X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=0) 
```

The model performance is best acheived when c is from 3 to 9, with 7 type-1 faults and 1 type-2 faults.


```python
for c in list(range(1, 11)) + [100]:
    logReg = LogisticRegression(C=c, max_iter=1000000)
    logReg.fit(X_train, y_train)
    print("c is " + str(c))
    print(confusion_matrix(y_test, logReg.predict(X_test)))
    print('\n')
```

    c is 1
    [[46  5]
     [ 0 48]]
    
    
    c is 2
    [[46  5]
     [ 1 47]]
    
    
    c is 3
    [[44  7]
     [ 1 47]]
    
    
    c is 4
    [[44  7]
     [ 1 47]]
    
    
    c is 5
    [[44  7]
     [ 1 47]]
    
    
    c is 6
    [[44  7]
     [ 1 47]]
    
    
    c is 7
    [[44  7]
     [ 1 47]]
    
    
    c is 8
    [[44  7]
     [ 1 47]]
    
    
    c is 9
    [[44  7]
     [ 1 47]]
    
    
    c is 10
    [[43  8]
     [ 1 47]]
    
    
    c is 100
    [[43  8]
     [ 1 47]]
    
    


### 3. Multi-value classification for G3 

Create a new column that categorizes the feature G3 according to ERASMUS scale


```python
def pass_grade_5(x):
    if 0 <= x <= 9:
        return 5
    elif 10 <= x <= 11:
        return 4
    elif 12 <= x <= 13:
        return 3
    elif 14 <= x <= 15:
        return 2
    else:
        return 1
    
trans_data['pass_5'] = trans_data['G3'].apply(lambda x: pass_grade_5(x))
```


```python
trans_data
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
      <th>school_GP</th>
      <th>school_MS</th>
      <th>sex_F</th>
      <th>sex_M</th>
      <th>address_R</th>
      <th>address_U</th>
      <th>famsize_GT3</th>
      <th>famsize_LE3</th>
      <th>Pstatus_A</th>
      <th>Pstatus_T</th>
      <th>...</th>
      <th>goout</th>
      <th>Dalc</th>
      <th>Walc</th>
      <th>health</th>
      <th>absences</th>
      <th>G1</th>
      <th>G2</th>
      <th>G3</th>
      <th>pass</th>
      <th>pass_5</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>1</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>...</td>
      <td>4</td>
      <td>1</td>
      <td>1</td>
      <td>3</td>
      <td>6</td>
      <td>5</td>
      <td>6</td>
      <td>6</td>
      <td>0</td>
      <td>5</td>
    </tr>
    <tr>
      <th>1</th>
      <td>1</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>...</td>
      <td>3</td>
      <td>1</td>
      <td>1</td>
      <td>3</td>
      <td>4</td>
      <td>5</td>
      <td>5</td>
      <td>6</td>
      <td>0</td>
      <td>5</td>
    </tr>
    <tr>
      <th>2</th>
      <td>1</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>1</td>
      <td>...</td>
      <td>2</td>
      <td>2</td>
      <td>3</td>
      <td>3</td>
      <td>10</td>
      <td>7</td>
      <td>8</td>
      <td>10</td>
      <td>0</td>
      <td>4</td>
    </tr>
    <tr>
      <th>3</th>
      <td>1</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>...</td>
      <td>2</td>
      <td>1</td>
      <td>1</td>
      <td>5</td>
      <td>2</td>
      <td>15</td>
      <td>14</td>
      <td>15</td>
      <td>1</td>
      <td>2</td>
    </tr>
    <tr>
      <th>4</th>
      <td>1</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>...</td>
      <td>2</td>
      <td>1</td>
      <td>2</td>
      <td>5</td>
      <td>4</td>
      <td>6</td>
      <td>10</td>
      <td>10</td>
      <td>0</td>
      <td>4</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>390</th>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>1</td>
      <td>1</td>
      <td>0</td>
      <td>...</td>
      <td>4</td>
      <td>4</td>
      <td>5</td>
      <td>4</td>
      <td>11</td>
      <td>9</td>
      <td>9</td>
      <td>9</td>
      <td>0</td>
      <td>5</td>
    </tr>
    <tr>
      <th>391</th>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>1</td>
      <td>...</td>
      <td>5</td>
      <td>3</td>
      <td>4</td>
      <td>2</td>
      <td>3</td>
      <td>14</td>
      <td>16</td>
      <td>16</td>
      <td>1</td>
      <td>1</td>
    </tr>
    <tr>
      <th>392</th>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>1</td>
      <td>1</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>...</td>
      <td>3</td>
      <td>3</td>
      <td>3</td>
      <td>3</td>
      <td>3</td>
      <td>10</td>
      <td>8</td>
      <td>7</td>
      <td>0</td>
      <td>5</td>
    </tr>
    <tr>
      <th>393</th>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>1</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>1</td>
      <td>...</td>
      <td>1</td>
      <td>3</td>
      <td>4</td>
      <td>5</td>
      <td>0</td>
      <td>11</td>
      <td>12</td>
      <td>10</td>
      <td>0</td>
      <td>4</td>
    </tr>
    <tr>
      <th>394</th>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>1</td>
      <td>...</td>
      <td>3</td>
      <td>3</td>
      <td>3</td>
      <td>5</td>
      <td>5</td>
      <td>8</td>
      <td>9</td>
      <td>9</td>
      <td>0</td>
      <td>5</td>
    </tr>
  </tbody>
</table>
<p>395 rows × 61 columns</p>
</div>




```python
X = trans_data.iloc[:, :58].values
y = trans_data['pass_5'].values
```

The model performance is best acheived when c is >= 8, with 6 type-1 faults and 1 type-2 faults.


```python
for c in list(range(1, 11)) + [100]:
    lsvc = LinearSVC(C=c, max_iter=1000000)
    lsvc.fit(X_train, y_train)
    print("c is " + str(c))
    print(confusion_matrix(y_test, lsvc.predict(X_test)))
    print('\n')
```

    c is 1
    [[43  8]
     [ 2 46]]
    
    
    c is 2
    [[43  8]
     [ 2 46]]
    
    
    c is 3
    [[44  7]
     [ 2 46]]
    
    
    c is 4
    [[44  7]
     [ 1 47]]
    
    
    c is 5
    [[44  7]
     [ 1 47]]
    
    
    c is 6
    [[44  7]
     [ 1 47]]
    
    
    c is 7
    [[44  7]
     [ 1 47]]
    
    
    c is 8
    [[45  6]
     [ 1 47]]
    
    
    c is 9
    [[45  6]
     [ 1 47]]
    
    
    c is 10
    [[45  6]
     [ 1 47]]
    
    
    c is 100
    [[45  6]
     [ 1 47]]
    
    

