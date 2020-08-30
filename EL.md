## Data set description
- Author: Ray Fisman and Sheena Iyengar
- Source: Columbia Business School - 2004
- Link: https://www.openml.org/d/40536

This data was gathered from participants in experimental speed dating events from 2002-2004. During the events, the attendees would have a four-minute "first date" with every other participant of the opposite sex. At the end of their four minutes, participants were asked if they would like to see their date again. They were also asked to rate their date on six attributes: Attractiveness, Sincerity, Intelligence, Fun, Ambition, and Shared Interests. The dataset also includes questionnaire data gathered from participants at different points in the process. These fields include: demographics, dating habits, self-perception across key attributes, beliefs on what others find valuable in a mate, and lifestyle information.

## Attributes
 * gender: Gender of self  
 * age: Age of self  
 * age_o: Age of partner  
 * d_age: Difference in age  
 * race: Race of self  
 * race_o: Race of partner  
 * samerace: Whether the two persons have the same race or not.  
 * importance_same_race: How important is it that partner is of same race?  
 * importance_same_religion: How important is it that partner has same religion?  
 * field: Field of study  
 * pref_o_attractive: How important does partner rate attractiveness  
 * pref_o_sinsere: How important does partner rate sincerity  
 * pref_o_intelligence: How important does partner rate intelligence  
 * pref_o_funny: How important does partner rate being funny  
 * pref_o_ambitious: How important does partner rate ambition  
 * pref_o_shared_interests: How important does partner rate having shared interests  
 * attractive_o: Rating by partner (about me) at night of event on attractiveness  
 * sincere_o: Rating by partner (about me) at night of event on sincerity  
 * intelligence_o: Rating by partner (about me) at night of event on intelligence  
 * funny_o: Rating by partner (about me) at night of event on being funny  
 * ambitous_o: Rating by partner (about me) at night of event on being ambitious  
 * shared_interests_o: Rating by partner (about me) at night of event on shared interest  
 * attractive_important: What do you look for in a partner - attractiveness  
 * sincere_important: What do you look for in a partner - sincerity  
 * intellicence_important: What do you look for in a partner - intelligence  
 * funny_important: What do you look for in a partner - being funny  
 * ambtition_important: What do you look for in a partner - ambition  
 * shared_interests_important: What do you look for in a partner - shared interests  
 * attractive: Rate yourself - attractiveness  
 * sincere: Rate yourself - sincerity   
 * intelligence: Rate yourself - intelligence   
 * funny: Rate yourself - being funny   
 * ambition: Rate yourself - ambition  
 * attractive_partner: Rate your partner - attractiveness  
 * sincere_partner: Rate your partner - sincerity   
 * intelligence_partner: Rate your partner - intelligence   
 * funny_partner: Rate your partner - being funny   
 * ambition_partner: Rate your partner - ambition   
 * shared_interests_partner: Rate your partner - shared interests  
 * sports: Your own interests [1-10] tvsports, exercise, dining, museums, art, hiking, gaming, clubbing, reading, tv, theater, movies, concerts, music, shopping, yoga  
 * interests_correlate: Correlation between participant’s and partner’s ratings of interests.  
 * expected_happy_with_sd_people: How happy do you expect to be with the people you meet during the speed-dating event?  
 * expected_num_interested_in_me: Out of the 20 people you will meet, how many do you expect will be interested in dating you?  
 * expected_num_matches: How many matches do you expect to get?  
 * like: Did you like your partner?  
 * guess_prob_liked: How likely do you think it is that your partner likes you?   
 * met: Have you met your partner before?  
 * decision: Decision at night of event.
 * decision_o: Decision of partner at night of event.  
 * match: Match (yes/no)

## ML tasks using Ensemble Learning: 
### 1. Classification: matched or unmatched
### 2. Regression: how much a participant likes his/her date


```python
import pandas as pd
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder
from sklearn.model_selection import train_test_split
import numpy as np
```


```python
data = pd.read_csv('speeddating.csv')
```


```python
data.dropna(inplace=True)
```


```python
# drop field since this attribute contains many messy values
data.drop(columns='field', index=1, inplace=True)
```


```python
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
      <th>gender</th>
      <th>age</th>
      <th>age_o</th>
      <th>d_age</th>
      <th>race</th>
      <th>race_o</th>
      <th>samerace</th>
      <th>importance_same_race</th>
      <th>importance_same_religion</th>
      <th>pref_o_attractive</th>
      <th>...</th>
      <th>interests_correlate</th>
      <th>expected_happy_with_sd_people</th>
      <th>expected_num_interested_in_me</th>
      <th>expected_num_matches</th>
      <th>like</th>
      <th>guess_prob_liked</th>
      <th>met</th>
      <th>decision</th>
      <th>decision_o</th>
      <th>match</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>female</td>
      <td>21.0</td>
      <td>27.0</td>
      <td>6</td>
      <td>'Asian/Pacific Islander/Asian-American'</td>
      <td>European/Caucasian-American</td>
      <td>0</td>
      <td>2.0</td>
      <td>4.0</td>
      <td>35.0</td>
      <td>...</td>
      <td>0.14</td>
      <td>3.0</td>
      <td>2.0</td>
      <td>4.0</td>
      <td>7.0</td>
      <td>6.0</td>
      <td>0.0</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
    </tr>
    <tr>
      <th>3</th>
      <td>female</td>
      <td>21.0</td>
      <td>23.0</td>
      <td>2</td>
      <td>'Asian/Pacific Islander/Asian-American'</td>
      <td>European/Caucasian-American</td>
      <td>0</td>
      <td>2.0</td>
      <td>4.0</td>
      <td>30.0</td>
      <td>...</td>
      <td>0.61</td>
      <td>3.0</td>
      <td>2.0</td>
      <td>4.0</td>
      <td>7.0</td>
      <td>6.0</td>
      <td>0.0</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
    </tr>
    <tr>
      <th>4</th>
      <td>female</td>
      <td>21.0</td>
      <td>24.0</td>
      <td>3</td>
      <td>'Asian/Pacific Islander/Asian-American'</td>
      <td>'Latino/Hispanic American'</td>
      <td>0</td>
      <td>2.0</td>
      <td>4.0</td>
      <td>30.0</td>
      <td>...</td>
      <td>0.21</td>
      <td>3.0</td>
      <td>2.0</td>
      <td>4.0</td>
      <td>6.0</td>
      <td>6.0</td>
      <td>0.0</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
    </tr>
    <tr>
      <th>5</th>
      <td>female</td>
      <td>21.0</td>
      <td>25.0</td>
      <td>4</td>
      <td>'Asian/Pacific Islander/Asian-American'</td>
      <td>European/Caucasian-American</td>
      <td>0</td>
      <td>2.0</td>
      <td>4.0</td>
      <td>50.0</td>
      <td>...</td>
      <td>0.25</td>
      <td>3.0</td>
      <td>2.0</td>
      <td>4.0</td>
      <td>6.0</td>
      <td>5.0</td>
      <td>0.0</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
    </tr>
    <tr>
      <th>6</th>
      <td>female</td>
      <td>21.0</td>
      <td>30.0</td>
      <td>9</td>
      <td>'Asian/Pacific Islander/Asian-American'</td>
      <td>European/Caucasian-American</td>
      <td>0</td>
      <td>2.0</td>
      <td>4.0</td>
      <td>35.0</td>
      <td>...</td>
      <td>0.34</td>
      <td>3.0</td>
      <td>2.0</td>
      <td>4.0</td>
      <td>6.0</td>
      <td>5.0</td>
      <td>0.0</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
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
      <th>1836</th>
      <td>male</td>
      <td>19.0</td>
      <td>20.0</td>
      <td>1</td>
      <td>'Asian/Pacific Islander/Asian-American'</td>
      <td>Other</td>
      <td>0</td>
      <td>4.0</td>
      <td>1.0</td>
      <td>15.0</td>
      <td>...</td>
      <td>0.35</td>
      <td>5.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>5.0</td>
      <td>1.0</td>
      <td>0.0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
    </tr>
    <tr>
      <th>1837</th>
      <td>male</td>
      <td>19.0</td>
      <td>21.0</td>
      <td>2</td>
      <td>'Asian/Pacific Islander/Asian-American'</td>
      <td>European/Caucasian-American</td>
      <td>0</td>
      <td>4.0</td>
      <td>1.0</td>
      <td>15.0</td>
      <td>...</td>
      <td>0.45</td>
      <td>5.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>5.0</td>
      <td>1.0</td>
      <td>0.0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
    </tr>
    <tr>
      <th>1838</th>
      <td>male</td>
      <td>19.0</td>
      <td>20.0</td>
      <td>1</td>
      <td>'Asian/Pacific Islander/Asian-American'</td>
      <td>'Black/African American'</td>
      <td>0</td>
      <td>4.0</td>
      <td>1.0</td>
      <td>20.0</td>
      <td>...</td>
      <td>0.13</td>
      <td>5.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>5.0</td>
      <td>1.0</td>
      <td>0.0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
    </tr>
    <tr>
      <th>1840</th>
      <td>male</td>
      <td>19.0</td>
      <td>21.0</td>
      <td>2</td>
      <td>'Asian/Pacific Islander/Asian-American'</td>
      <td>European/Caucasian-American</td>
      <td>0</td>
      <td>4.0</td>
      <td>1.0</td>
      <td>15.0</td>
      <td>...</td>
      <td>0.54</td>
      <td>5.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>5.0</td>
      <td>1.0</td>
      <td>0.0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
    </tr>
    <tr>
      <th>1843</th>
      <td>male</td>
      <td>19.0</td>
      <td>20.0</td>
      <td>1</td>
      <td>'Asian/Pacific Islander/Asian-American'</td>
      <td>'Latino/Hispanic American'</td>
      <td>0</td>
      <td>4.0</td>
      <td>1.0</td>
      <td>10.0</td>
      <td>...</td>
      <td>0.54</td>
      <td>5.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>5.0</td>
      <td>1.0</td>
      <td>0.0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
    </tr>
  </tbody>
</table>
<p>1047 rows × 65 columns</p>
</div>



### Data Pre-processing


```python
num_data = data.select_dtypes(exclude='object').reset_index(drop=True)
```


```python
o_data = data.select_dtypes(include='object')
```


```python
num_data
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
      <th>age</th>
      <th>age_o</th>
      <th>d_age</th>
      <th>samerace</th>
      <th>importance_same_race</th>
      <th>importance_same_religion</th>
      <th>pref_o_attractive</th>
      <th>pref_o_sincere</th>
      <th>pref_o_intelligence</th>
      <th>pref_o_funny</th>
      <th>...</th>
      <th>interests_correlate</th>
      <th>expected_happy_with_sd_people</th>
      <th>expected_num_interested_in_me</th>
      <th>expected_num_matches</th>
      <th>like</th>
      <th>guess_prob_liked</th>
      <th>met</th>
      <th>decision</th>
      <th>decision_o</th>
      <th>match</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>21.0</td>
      <td>27.0</td>
      <td>6</td>
      <td>0</td>
      <td>2.0</td>
      <td>4.0</td>
      <td>35.0</td>
      <td>20.0</td>
      <td>20.0</td>
      <td>20.0</td>
      <td>...</td>
      <td>0.14</td>
      <td>3.0</td>
      <td>2.0</td>
      <td>4.0</td>
      <td>7.0</td>
      <td>6.0</td>
      <td>0.0</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>21.0</td>
      <td>23.0</td>
      <td>2</td>
      <td>0</td>
      <td>2.0</td>
      <td>4.0</td>
      <td>30.0</td>
      <td>5.0</td>
      <td>15.0</td>
      <td>40.0</td>
      <td>...</td>
      <td>0.61</td>
      <td>3.0</td>
      <td>2.0</td>
      <td>4.0</td>
      <td>7.0</td>
      <td>6.0</td>
      <td>0.0</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
    </tr>
    <tr>
      <th>2</th>
      <td>21.0</td>
      <td>24.0</td>
      <td>3</td>
      <td>0</td>
      <td>2.0</td>
      <td>4.0</td>
      <td>30.0</td>
      <td>10.0</td>
      <td>20.0</td>
      <td>10.0</td>
      <td>...</td>
      <td>0.21</td>
      <td>3.0</td>
      <td>2.0</td>
      <td>4.0</td>
      <td>6.0</td>
      <td>6.0</td>
      <td>0.0</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
    </tr>
    <tr>
      <th>3</th>
      <td>21.0</td>
      <td>25.0</td>
      <td>4</td>
      <td>0</td>
      <td>2.0</td>
      <td>4.0</td>
      <td>50.0</td>
      <td>0.0</td>
      <td>30.0</td>
      <td>10.0</td>
      <td>...</td>
      <td>0.25</td>
      <td>3.0</td>
      <td>2.0</td>
      <td>4.0</td>
      <td>6.0</td>
      <td>5.0</td>
      <td>0.0</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
    </tr>
    <tr>
      <th>4</th>
      <td>21.0</td>
      <td>30.0</td>
      <td>9</td>
      <td>0</td>
      <td>2.0</td>
      <td>4.0</td>
      <td>35.0</td>
      <td>15.0</td>
      <td>25.0</td>
      <td>10.0</td>
      <td>...</td>
      <td>0.34</td>
      <td>3.0</td>
      <td>2.0</td>
      <td>4.0</td>
      <td>6.0</td>
      <td>5.0</td>
      <td>0.0</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
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
      <th>1042</th>
      <td>19.0</td>
      <td>20.0</td>
      <td>1</td>
      <td>0</td>
      <td>4.0</td>
      <td>1.0</td>
      <td>15.0</td>
      <td>15.0</td>
      <td>20.0</td>
      <td>25.0</td>
      <td>...</td>
      <td>0.35</td>
      <td>5.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>5.0</td>
      <td>1.0</td>
      <td>0.0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
    </tr>
    <tr>
      <th>1043</th>
      <td>19.0</td>
      <td>21.0</td>
      <td>2</td>
      <td>0</td>
      <td>4.0</td>
      <td>1.0</td>
      <td>15.0</td>
      <td>15.0</td>
      <td>25.0</td>
      <td>25.0</td>
      <td>...</td>
      <td>0.45</td>
      <td>5.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>5.0</td>
      <td>1.0</td>
      <td>0.0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
    </tr>
    <tr>
      <th>1044</th>
      <td>19.0</td>
      <td>20.0</td>
      <td>1</td>
      <td>0</td>
      <td>4.0</td>
      <td>1.0</td>
      <td>20.0</td>
      <td>20.0</td>
      <td>20.0</td>
      <td>20.0</td>
      <td>...</td>
      <td>0.13</td>
      <td>5.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>5.0</td>
      <td>1.0</td>
      <td>0.0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
    </tr>
    <tr>
      <th>1045</th>
      <td>19.0</td>
      <td>21.0</td>
      <td>2</td>
      <td>0</td>
      <td>4.0</td>
      <td>1.0</td>
      <td>15.0</td>
      <td>15.0</td>
      <td>25.0</td>
      <td>25.0</td>
      <td>...</td>
      <td>0.54</td>
      <td>5.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>5.0</td>
      <td>1.0</td>
      <td>0.0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
    </tr>
    <tr>
      <th>1046</th>
      <td>19.0</td>
      <td>20.0</td>
      <td>1</td>
      <td>0</td>
      <td>4.0</td>
      <td>1.0</td>
      <td>10.0</td>
      <td>10.0</td>
      <td>35.0</td>
      <td>35.0</td>
      <td>...</td>
      <td>0.54</td>
      <td>5.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>5.0</td>
      <td>1.0</td>
      <td>0.0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
    </tr>
  </tbody>
</table>
<p>1047 rows × 62 columns</p>
</div>




```python
o_data
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
      <th>gender</th>
      <th>race</th>
      <th>race_o</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>female</td>
      <td>'Asian/Pacific Islander/Asian-American'</td>
      <td>European/Caucasian-American</td>
    </tr>
    <tr>
      <th>3</th>
      <td>female</td>
      <td>'Asian/Pacific Islander/Asian-American'</td>
      <td>European/Caucasian-American</td>
    </tr>
    <tr>
      <th>4</th>
      <td>female</td>
      <td>'Asian/Pacific Islander/Asian-American'</td>
      <td>'Latino/Hispanic American'</td>
    </tr>
    <tr>
      <th>5</th>
      <td>female</td>
      <td>'Asian/Pacific Islander/Asian-American'</td>
      <td>European/Caucasian-American</td>
    </tr>
    <tr>
      <th>6</th>
      <td>female</td>
      <td>'Asian/Pacific Islander/Asian-American'</td>
      <td>European/Caucasian-American</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>1836</th>
      <td>male</td>
      <td>'Asian/Pacific Islander/Asian-American'</td>
      <td>Other</td>
    </tr>
    <tr>
      <th>1837</th>
      <td>male</td>
      <td>'Asian/Pacific Islander/Asian-American'</td>
      <td>European/Caucasian-American</td>
    </tr>
    <tr>
      <th>1838</th>
      <td>male</td>
      <td>'Asian/Pacific Islander/Asian-American'</td>
      <td>'Black/African American'</td>
    </tr>
    <tr>
      <th>1840</th>
      <td>male</td>
      <td>'Asian/Pacific Islander/Asian-American'</td>
      <td>European/Caucasian-American</td>
    </tr>
    <tr>
      <th>1843</th>
      <td>male</td>
      <td>'Asian/Pacific Islander/Asian-American'</td>
      <td>'Latino/Hispanic American'</td>
    </tr>
  </tbody>
</table>
<p>1047 rows × 3 columns</p>
</div>




```python
o_encoder = OneHotEncoder()
o_trans = o_encoder.fit_transform(o_data)
```


```python
o_att = list()

for i in o_encoder.categories_:
    for n in i:
        o_att.append(str(n).replace("'", ''))
        
for i in o_att[7:]:
    o_att.append(i+'_o')
    o_att.remove(i)
```


```python
o_att
```




    ['female',
     'male',
     'Asian/Pacific Islander/Asian-American',
     'Black/African American',
     'Latino/Hispanic American',
     'European/Caucasian-American',
     'Other',
     'Asian/Pacific Islander/Asian-American_o',
     'Black/African American_o',
     'Latino/Hispanic American_o',
     'European/Caucasian-American_o',
     'Other_o']




```python
o_data = pd.DataFrame(o_trans.toarray(), columns=o_att)
```


```python
trans_data = pd.concat([o_data, num_data], axis=1)
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
      <th>female</th>
      <th>male</th>
      <th>Asian/Pacific Islander/Asian-American</th>
      <th>Black/African American</th>
      <th>Latino/Hispanic American</th>
      <th>European/Caucasian-American</th>
      <th>Other</th>
      <th>Asian/Pacific Islander/Asian-American_o</th>
      <th>Black/African American_o</th>
      <th>Latino/Hispanic American_o</th>
      <th>...</th>
      <th>interests_correlate</th>
      <th>expected_happy_with_sd_people</th>
      <th>expected_num_interested_in_me</th>
      <th>expected_num_matches</th>
      <th>like</th>
      <th>guess_prob_liked</th>
      <th>met</th>
      <th>decision</th>
      <th>decision_o</th>
      <th>match</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1.0</td>
      <td>0.0</td>
      <td>1.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>...</td>
      <td>0.14</td>
      <td>3.0</td>
      <td>2.0</td>
      <td>4.0</td>
      <td>7.0</td>
      <td>6.0</td>
      <td>0.0</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>1.0</td>
      <td>0.0</td>
      <td>1.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>...</td>
      <td>0.61</td>
      <td>3.0</td>
      <td>2.0</td>
      <td>4.0</td>
      <td>7.0</td>
      <td>6.0</td>
      <td>0.0</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
    </tr>
    <tr>
      <th>2</th>
      <td>1.0</td>
      <td>0.0</td>
      <td>1.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>1.0</td>
      <td>...</td>
      <td>0.21</td>
      <td>3.0</td>
      <td>2.0</td>
      <td>4.0</td>
      <td>6.0</td>
      <td>6.0</td>
      <td>0.0</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
    </tr>
    <tr>
      <th>3</th>
      <td>1.0</td>
      <td>0.0</td>
      <td>1.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>...</td>
      <td>0.25</td>
      <td>3.0</td>
      <td>2.0</td>
      <td>4.0</td>
      <td>6.0</td>
      <td>5.0</td>
      <td>0.0</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
    </tr>
    <tr>
      <th>4</th>
      <td>1.0</td>
      <td>0.0</td>
      <td>1.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>...</td>
      <td>0.34</td>
      <td>3.0</td>
      <td>2.0</td>
      <td>4.0</td>
      <td>6.0</td>
      <td>5.0</td>
      <td>0.0</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
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
      <th>1042</th>
      <td>0.0</td>
      <td>1.0</td>
      <td>1.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>...</td>
      <td>0.35</td>
      <td>5.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>5.0</td>
      <td>1.0</td>
      <td>0.0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
    </tr>
    <tr>
      <th>1043</th>
      <td>0.0</td>
      <td>1.0</td>
      <td>1.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>...</td>
      <td>0.45</td>
      <td>5.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>5.0</td>
      <td>1.0</td>
      <td>0.0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
    </tr>
    <tr>
      <th>1044</th>
      <td>0.0</td>
      <td>1.0</td>
      <td>1.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>1.0</td>
      <td>0.0</td>
      <td>...</td>
      <td>0.13</td>
      <td>5.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>5.0</td>
      <td>1.0</td>
      <td>0.0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
    </tr>
    <tr>
      <th>1045</th>
      <td>0.0</td>
      <td>1.0</td>
      <td>1.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>...</td>
      <td>0.54</td>
      <td>5.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>5.0</td>
      <td>1.0</td>
      <td>0.0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
    </tr>
    <tr>
      <th>1046</th>
      <td>0.0</td>
      <td>1.0</td>
      <td>1.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>1.0</td>
      <td>...</td>
      <td>0.54</td>
      <td>5.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>5.0</td>
      <td>1.0</td>
      <td>0.0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
    </tr>
  </tbody>
</table>
<p>1047 rows × 74 columns</p>
</div>



### 1. Classification: matched or unmatched
### 1.1. Bagging with RandomForestClassifier of 100 independent DecisionTrees


```python
X_train, X_test, y_train, y_test = train_test_split(trans_data.iloc[:, :-10], trans_data.iloc[:, -1], random_state=42)
```


```python
from sklearn.ensemble import RandomForestClassifier

rf = RandomForestClassifier()
rf.fit(X_train, y_train)

y_pred = rf.predict(X_test)
```


```python
from sklearn.metrics import accuracy_score

print('Baseline Accuracy score: {:.5f}'.format(accuracy_score(y_test, y_pred)))
```

    Baseline Accuracy score: 0.82061


### Feature Importance: being attractive and funny, and sharing same interests are important for matching a partner


```python
features = pd.DataFrame(data=rf.feature_importances_, index=trans_data.columns[:-10], columns=['importance'])
```


```python
features.sort_values('importance', ascending=False)[:10]
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
      <th>importance</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>attractive_o</th>
      <td>0.060663</td>
    </tr>
    <tr>
      <th>attractive_partner</th>
      <td>0.057318</td>
    </tr>
    <tr>
      <th>shared_interests_o</th>
      <td>0.056460</td>
    </tr>
    <tr>
      <th>funny_o</th>
      <td>0.046871</td>
    </tr>
    <tr>
      <th>shared_interests_partner</th>
      <td>0.044348</td>
    </tr>
    <tr>
      <th>funny_partner</th>
      <td>0.042942</td>
    </tr>
    <tr>
      <th>age_o</th>
      <td>0.029814</td>
    </tr>
    <tr>
      <th>pref_o_attractive</th>
      <td>0.024023</td>
    </tr>
    <tr>
      <th>pref_o_funny</th>
      <td>0.023656</td>
    </tr>
    <tr>
      <th>ambitous_o</th>
      <td>0.022849</td>
    </tr>
  </tbody>
</table>
</div>



### 1.2. Stacking with 2 layers of models


```python
X, y = trans_data.iloc[:, :-10], trans_data.iloc[:, -1]
```


```python
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import RepeatedStratifiedKFold
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
from sklearn.ensemble import StackingClassifier

level_0 = [('lr', LogisticRegression()),
           ('knn', KNeighborsClassifier()),
           ('rf', RandomForestClassifier()),
           ('svm', SVC())]
level_1 = RandomForestClassifier()
stacking = StackingClassifier(estimators=level_0, final_estimator=level_1, cv=5)

models = {'lr': LogisticRegression(),
         'knn': KNeighborsClassifier(),
         'rf': RandomForestClassifier(),
         'svm': SVC(),
         'stacking': stacking}

def evaluate_model(model, X, y):
    cv = RepeatedStratifiedKFold(n_splits=5, random_state=42)
    scores = cross_val_score(model, X, y, scoring='accuracy', cv=cv, n_jobs=-1, error_score='raise')
    return scores

results = list()
names = list()

for name, model in models.items():
    scores = evaluate_model(model, X_train, y_train)
    results.append(scores)
    names.append(name)
    print((name, round(np.mean(scores), 5), round(np.std(scores), 5)))
```

    ('lr', 0.84408, 0.02193)
    ('knn', 0.81452, 0.01951)
    ('rf', 0.85618, 0.01361)
    ('svm', 0.83057, 0.00312)
    ('stacking', 0.84611, 0.02071)


### Result: Stacking Accuracy = 0.84611 < RandomForestClassifier Accuracy = 0.85618

### 2. Regression: how much a participant likes his/her date
### 2.1. Gradient Boosting with GradientBoostingRegressor of 100 independent DecisionTrees


```python
X_train, X_test, y_train, y_test = train_test_split(trans_data.iloc[:, :-3], trans_data.iloc[:, -6], random_state=42)
```


```python
from sklearn.ensemble import GradientBoostingRegressor

gbr = GradientBoostingRegressor()
gbr.fit(X_train, y_train)

y_pred = gbr.predict(X_test)
```


```python
y_pred.astype('int')
```




    array([6, 6, 6, 7, 4, 6, 8, 6, 6, 7, 6, 6, 6, 6, 8, 4, 2, 5, 6, 7, 4, 8,
           6, 6, 7, 5, 6, 6, 7, 6, 6, 8, 6, 8, 6, 7, 6, 2, 6, 6, 6, 6, 6, 6,
           6, 6, 2, 7, 5, 8, 6, 3, 7, 6, 6, 5, 7, 6, 6, 6, 9, 9, 6, 6, 6, 5,
           4, 4, 6, 7, 7, 2, 9, 7, 6, 7, 4, 5, 6, 6, 3, 8, 6, 5, 8, 3, 4, 6,
           6, 6, 6, 6, 7, 6, 1, 7, 6, 6, 0, 5, 6, 8, 6, 7, 6, 5, 6, 6, 7, 2,
           5, 8, 6, 6, 8, 6, 4, 6, 6, 6, 7, 6, 6, 7, 1, 6, 6, 7, 6, 6, 3, 6,
           6, 6, 6, 2, 6, 6, 6, 7, 6, 7, 7, 7, 6, 6, 6, 5, 6, 9, 6, 6, 6, 6,
           6, 9, 6, 6, 7, 3, 5, 6, 6, 8, 5, 8, 7, 4, 6, 5, 6, 6, 9, 6, 2, 5,
           3, 2, 8, 6, 6, 6, 6, 6, 6, 2, 4, 6, 6, 2, 5, 7, 7, 6, 5, 2, 5, 7,
           6, 6, 6, 5, 7, 6, 6, 6, 6, 6, 6, 6, 5, 6, 9, 6, 6, 6, 6, 6, 7, 5,
           6, 7, 5, 7, 6, 1, 8, 4, 6, 6, 2, 5, 7, 5, 4, 6, 6, 6, 7, 5, 6, 9,
           6, 5, 6, 6, 6, 6, 6, 6, 9, 6, 3, 7, 6, 5, 6, 2, 6, 6, 6, 6])




```python
from sklearn.metrics import mean_squared_error

print('Baseline RMSE: {:.5f}'.format(
                 mean_squared_error(y_test, y_pred.astype('int'), squared=False)))
```

    Baseline RMSE: 0.70373


### 2.2. Extreme Gradient Boosting with XGBoost and hyper parameter tuning with GridSearch 


```python
import xgboost as xgb

train = xgb.DMatrix(X_train, label=y_train)
test = xgb.DMatrix(X_test, label=y_test)
```


```python
params = {
    'max_depth':6,
    'min_child_weight': 1,
    'eta':0.3,
    'subsample': 1,
    'colsample_bytree': 1,
    'objective':'reg:squarederror',
    'eval_metric': 'rmse'
}
```


```python
cv_results = xgb.cv(
    params,
    train,
    num_boost_round=100,
    seed=42,
    nfold=5,
    metrics={'rmse'},
    early_stopping_rounds=10
)

cv_results
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
      <th>train-rmse-mean</th>
      <th>train-rmse-std</th>
      <th>test-rmse-mean</th>
      <th>test-rmse-std</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>4.211302</td>
      <td>0.009553</td>
      <td>4.211142</td>
      <td>0.029887</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2.963511</td>
      <td>0.006647</td>
      <td>2.962846</td>
      <td>0.023045</td>
    </tr>
    <tr>
      <th>2</th>
      <td>2.086589</td>
      <td>0.004590</td>
      <td>2.086106</td>
      <td>0.018931</td>
    </tr>
    <tr>
      <th>3</th>
      <td>1.469331</td>
      <td>0.003155</td>
      <td>1.469113</td>
      <td>0.011535</td>
    </tr>
    <tr>
      <th>4</th>
      <td>1.035416</td>
      <td>0.002208</td>
      <td>1.035566</td>
      <td>0.010592</td>
    </tr>
    <tr>
      <th>5</th>
      <td>0.729338</td>
      <td>0.001536</td>
      <td>0.729979</td>
      <td>0.007580</td>
    </tr>
    <tr>
      <th>6</th>
      <td>0.514014</td>
      <td>0.001038</td>
      <td>0.515827</td>
      <td>0.006285</td>
    </tr>
    <tr>
      <th>7</th>
      <td>0.362344</td>
      <td>0.000730</td>
      <td>0.364688</td>
      <td>0.005393</td>
    </tr>
    <tr>
      <th>8</th>
      <td>0.255511</td>
      <td>0.000529</td>
      <td>0.259339</td>
      <td>0.006231</td>
    </tr>
    <tr>
      <th>9</th>
      <td>0.180219</td>
      <td>0.000364</td>
      <td>0.185675</td>
      <td>0.007906</td>
    </tr>
    <tr>
      <th>10</th>
      <td>0.127121</td>
      <td>0.000253</td>
      <td>0.135551</td>
      <td>0.010946</td>
    </tr>
    <tr>
      <th>11</th>
      <td>0.089681</td>
      <td>0.000176</td>
      <td>0.101505</td>
      <td>0.014863</td>
    </tr>
    <tr>
      <th>12</th>
      <td>0.063277</td>
      <td>0.000124</td>
      <td>0.078882</td>
      <td>0.019360</td>
    </tr>
    <tr>
      <th>13</th>
      <td>0.044657</td>
      <td>0.000088</td>
      <td>0.064012</td>
      <td>0.023895</td>
    </tr>
    <tr>
      <th>14</th>
      <td>0.031525</td>
      <td>0.000064</td>
      <td>0.054265</td>
      <td>0.027993</td>
    </tr>
    <tr>
      <th>15</th>
      <td>0.022262</td>
      <td>0.000047</td>
      <td>0.047811</td>
      <td>0.031418</td>
    </tr>
    <tr>
      <th>16</th>
      <td>0.015726</td>
      <td>0.000035</td>
      <td>0.043479</td>
      <td>0.034129</td>
    </tr>
    <tr>
      <th>17</th>
      <td>0.011115</td>
      <td>0.000027</td>
      <td>0.040548</td>
      <td>0.036189</td>
    </tr>
    <tr>
      <th>18</th>
      <td>0.007860</td>
      <td>0.000023</td>
      <td>0.038538</td>
      <td>0.037721</td>
    </tr>
    <tr>
      <th>19</th>
      <td>0.005563</td>
      <td>0.000020</td>
      <td>0.037150</td>
      <td>0.038841</td>
    </tr>
    <tr>
      <th>20</th>
      <td>0.003942</td>
      <td>0.000020</td>
      <td>0.036186</td>
      <td>0.039650</td>
    </tr>
    <tr>
      <th>21</th>
      <td>0.002798</td>
      <td>0.000020</td>
      <td>0.035513</td>
      <td>0.040233</td>
    </tr>
    <tr>
      <th>22</th>
      <td>0.001991</td>
      <td>0.000020</td>
      <td>0.035042</td>
      <td>0.040650</td>
    </tr>
    <tr>
      <th>23</th>
      <td>0.001421</td>
      <td>0.000022</td>
      <td>0.034714</td>
      <td>0.040945</td>
    </tr>
    <tr>
      <th>24</th>
      <td>0.001018</td>
      <td>0.000022</td>
      <td>0.034482</td>
      <td>0.041156</td>
    </tr>
    <tr>
      <th>25</th>
      <td>0.000735</td>
      <td>0.000022</td>
      <td>0.034319</td>
      <td>0.041305</td>
    </tr>
    <tr>
      <th>26</th>
      <td>0.000534</td>
      <td>0.000023</td>
      <td>0.034204</td>
      <td>0.041410</td>
    </tr>
    <tr>
      <th>27</th>
      <td>0.000394</td>
      <td>0.000023</td>
      <td>0.034122</td>
      <td>0.041485</td>
    </tr>
    <tr>
      <th>28</th>
      <td>0.000294</td>
      <td>0.000023</td>
      <td>0.034066</td>
      <td>0.041536</td>
    </tr>
    <tr>
      <th>29</th>
      <td>0.000225</td>
      <td>0.000022</td>
      <td>0.034028</td>
      <td>0.041573</td>
    </tr>
    <tr>
      <th>30</th>
      <td>0.000175</td>
      <td>0.000021</td>
      <td>0.034000</td>
      <td>0.041598</td>
    </tr>
    <tr>
      <th>31</th>
      <td>0.000141</td>
      <td>0.000018</td>
      <td>0.033983</td>
      <td>0.041614</td>
    </tr>
    <tr>
      <th>32</th>
      <td>0.000117</td>
      <td>0.000016</td>
      <td>0.033973</td>
      <td>0.041624</td>
    </tr>
    <tr>
      <th>33</th>
      <td>0.000102</td>
      <td>0.000013</td>
      <td>0.033968</td>
      <td>0.041629</td>
    </tr>
    <tr>
      <th>34</th>
      <td>0.000092</td>
      <td>0.000010</td>
      <td>0.033960</td>
      <td>0.041636</td>
    </tr>
    <tr>
      <th>35</th>
      <td>0.000084</td>
      <td>0.000008</td>
      <td>0.033958</td>
      <td>0.041637</td>
    </tr>
    <tr>
      <th>36</th>
      <td>0.000078</td>
      <td>0.000006</td>
      <td>0.033958</td>
      <td>0.041640</td>
    </tr>
    <tr>
      <th>37</th>
      <td>0.000077</td>
      <td>0.000006</td>
      <td>0.033958</td>
      <td>0.041640</td>
    </tr>
    <tr>
      <th>38</th>
      <td>0.000077</td>
      <td>0.000006</td>
      <td>0.033958</td>
      <td>0.041641</td>
    </tr>
    <tr>
      <th>39</th>
      <td>0.000077</td>
      <td>0.000006</td>
      <td>0.033958</td>
      <td>0.041641</td>
    </tr>
    <tr>
      <th>40</th>
      <td>0.000077</td>
      <td>0.000006</td>
      <td>0.033958</td>
      <td>0.041641</td>
    </tr>
    <tr>
      <th>41</th>
      <td>0.000077</td>
      <td>0.000006</td>
      <td>0.033958</td>
      <td>0.041641</td>
    </tr>
    <tr>
      <th>42</th>
      <td>0.000077</td>
      <td>0.000006</td>
      <td>0.033958</td>
      <td>0.041641</td>
    </tr>
  </tbody>
</table>
</div>




```python
gridsearch_params = [
    (max_depth, min_child_weight)
    for max_depth in range(10,15)
    for min_child_weight in range(5,10)
]

min_rmse = float("Inf")
best_params = None

for max_depth, min_child_weight in gridsearch_params:
    print("CV with max_depth={}, min_child_weight={}".format(
                             max_depth,
                             min_child_weight))
    
    params['max_depth'] = max_depth
    params['min_child_weight'] = min_child_weight
    
    cv_results = xgb.cv(
        params,
        train,
        num_boost_round=100,
        seed=42,
        nfold=5,
        metrics={'rmse'},
        early_stopping_rounds=10
    )
    
    # update best RMSE
    mean_rmse = cv_results['test-rmse-mean'].min()
    boost_rounds = cv_results['test-rmse-mean'].argmin()
    print("\tRMSE {:.5f} for {} rounds".format(mean_rmse, boost_rounds))
    if mean_rmse < min_rmse:
        min_rmse = mean_rmse
        best_params = (max_depth, min_child_weight)

print("Best params: {}, {}, RMSE: {:.5f}".format(best_params[0], best_params[1], min_rmse))
```

    CV with max_depth=10, min_child_weight=5
    	RMSE 0.03549 for 30 rounds
    CV with max_depth=10, min_child_weight=6
    	RMSE 0.03525 for 22 rounds
    CV with max_depth=10, min_child_weight=7
    	RMSE 0.03503 for 22 rounds
    CV with max_depth=10, min_child_weight=8
    	RMSE 0.05993 for 20 rounds
    CV with max_depth=10, min_child_weight=9
    	RMSE 0.10087 for 18 rounds
    CV with max_depth=11, min_child_weight=5
    	RMSE 0.03524 for 30 rounds
    CV with max_depth=11, min_child_weight=6
    	RMSE 0.03526 for 22 rounds
    CV with max_depth=11, min_child_weight=7
    	RMSE 0.03502 for 22 rounds
    CV with max_depth=11, min_child_weight=8
    	RMSE 0.06001 for 20 rounds
    CV with max_depth=11, min_child_weight=9
    	RMSE 0.10091 for 18 rounds
    CV with max_depth=12, min_child_weight=5
    	RMSE 0.03549 for 23 rounds
    CV with max_depth=12, min_child_weight=6
    	RMSE 0.03526 for 22 rounds
    CV with max_depth=12, min_child_weight=7
    	RMSE 0.03503 for 22 rounds
    CV with max_depth=12, min_child_weight=8
    	RMSE 0.05980 for 22 rounds
    CV with max_depth=12, min_child_weight=9
    	RMSE 0.10092 for 18 rounds
    CV with max_depth=13, min_child_weight=5
    	RMSE 0.03549 for 23 rounds
    CV with max_depth=13, min_child_weight=6
    	RMSE 0.03526 for 22 rounds
    CV with max_depth=13, min_child_weight=7
    	RMSE 0.03503 for 22 rounds
    CV with max_depth=13, min_child_weight=8
    	RMSE 0.05948 for 20 rounds
    CV with max_depth=13, min_child_weight=9
    	RMSE 0.10092 for 18 rounds
    CV with max_depth=14, min_child_weight=5
    	RMSE 0.03549 for 23 rounds
    CV with max_depth=14, min_child_weight=6
    	RMSE 0.03526 for 22 rounds
    CV with max_depth=14, min_child_weight=7
    	RMSE 0.03503 for 22 rounds
    CV with max_depth=14, min_child_weight=8
    	RMSE 0.05944 for 25 rounds
    CV with max_depth=14, min_child_weight=9
    	RMSE 0.10092 for 18 rounds
    Best params: 11, 7, RMSE: 0.03502



```python
params['max_depth'] = best_params[0]
params['min_child_weight'] = best_params[1]
```


```python
model = xgb.train(
    params,
    train,
    num_boost_round=35,
    evals=[(test, "Test")],
    early_stopping_rounds=10
)

print("Best RMSE: {:.5f} in {} rounds".format(model.best_score, model.best_iteration+1))
```

    [0]	Test-rmse:4.27663
    Will train until Test-rmse hasn't improved in 10 rounds.
    [1]	Test-rmse:3.00449
    [2]	Test-rmse:2.11192
    [3]	Test-rmse:1.48495
    [4]	Test-rmse:1.04245
    [5]	Test-rmse:0.73402
    [6]	Test-rmse:0.51477
    [7]	Test-rmse:0.36311
    [8]	Test-rmse:0.25605
    [9]	Test-rmse:0.18107
    [10]	Test-rmse:0.12900
    [11]	Test-rmse:0.09295
    [12]	Test-rmse:0.06874
    [13]	Test-rmse:0.05330
    [14]	Test-rmse:0.04382
    [15]	Test-rmse:0.03871
    [16]	Test-rmse:0.03604
    [17]	Test-rmse:0.03500
    [18]	Test-rmse:0.03441
    [19]	Test-rmse:0.03440
    [20]	Test-rmse:0.03474
    [21]	Test-rmse:0.03488
    [22]	Test-rmse:0.03531
    [23]	Test-rmse:0.03549
    [24]	Test-rmse:0.03594
    [25]	Test-rmse:0.03614
    [26]	Test-rmse:0.03662
    [27]	Test-rmse:0.03685
    [28]	Test-rmse:0.03735
    [29]	Test-rmse:0.03757
    Stopping. Best iteration:
    [19]	Test-rmse:0.03440
    
    Best RMSE: 0.03440 in 20 rounds


### Result: GradientBoostingRegressor RMSE = 0.70373 > XGBoost RMSE = 0.03440
