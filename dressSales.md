## In this project, we'll transform a raw uncleaned data set into an organized and well-formatted data set for data analysis

### Data: Dress Attributes and Sales
http://archive.ics.uci.edu/ml/datasets/Dresses_Attribute_Sales

### 1. Dress Attributes: 
- Dress ID
- Style: Bohemia, brief, casual, cute, fashion, flare, novelty, OL, party, sexy, vintage, work
- Price: Low,Average,Medium,High,Very-High 
- Rating: 1-5 
- Size: S, M, L, XL, Free 
- Season: autumn, winter, spring, summer 
- NeckLine: O-neck, backless, board-neck, bowneck, halter, mandarin-collor, open, peterpan-collor, ruffled, scoop, slash-neck, square-collar, sweetheart, turndowncollar, V-neck. 
- SleeveLength: full, half, halfsleeves, butterfly, sleveless, short, threequarter, turndown, null
- Waiseline: dropped, empire, natural, princess, null 
- Material: wool, cotton, mix, etc 
- FabricType: shafoon, dobby, popline, satin, knitted, jersey, flannel, corduroy, etc 
- Decoration: applique, beading, bow, button, cascading, crystal, draped, embroridary, feathers, flowers, etc 
- Pattern type: solid, animal, dot, leapard, etc 
- Recommendation: 0, 1 

### 2. Dress Sales:
- Dress ID
- Sales columns by dates


```python
import pandas as pd
import numpy as np
```


```python
attr = pd.read_excel('Attribute DataSet.xlsx')
attr
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
      <th>Dress_ID</th>
      <th>Style</th>
      <th>Price</th>
      <th>Rating</th>
      <th>Size</th>
      <th>Season</th>
      <th>NeckLine</th>
      <th>SleeveLength</th>
      <th>waiseline</th>
      <th>Material</th>
      <th>FabricType</th>
      <th>Decoration</th>
      <th>Pattern Type</th>
      <th>Recommendation</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1006032852</td>
      <td>Sexy</td>
      <td>Low</td>
      <td>4.6</td>
      <td>M</td>
      <td>Summer</td>
      <td>o-neck</td>
      <td>sleevless</td>
      <td>empire</td>
      <td>NaN</td>
      <td>chiffon</td>
      <td>ruffles</td>
      <td>animal</td>
      <td>1</td>
    </tr>
    <tr>
      <th>1</th>
      <td>1212192089</td>
      <td>Casual</td>
      <td>Low</td>
      <td>0.0</td>
      <td>L</td>
      <td>Summer</td>
      <td>o-neck</td>
      <td>Petal</td>
      <td>natural</td>
      <td>microfiber</td>
      <td>NaN</td>
      <td>ruffles</td>
      <td>animal</td>
      <td>0</td>
    </tr>
    <tr>
      <th>2</th>
      <td>1190380701</td>
      <td>vintage</td>
      <td>High</td>
      <td>0.0</td>
      <td>L</td>
      <td>Automn</td>
      <td>o-neck</td>
      <td>full</td>
      <td>natural</td>
      <td>polyster</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>print</td>
      <td>0</td>
    </tr>
    <tr>
      <th>3</th>
      <td>966005983</td>
      <td>Brief</td>
      <td>Average</td>
      <td>4.6</td>
      <td>L</td>
      <td>Spring</td>
      <td>o-neck</td>
      <td>full</td>
      <td>natural</td>
      <td>silk</td>
      <td>chiffon</td>
      <td>embroidary</td>
      <td>print</td>
      <td>1</td>
    </tr>
    <tr>
      <th>4</th>
      <td>876339541</td>
      <td>cute</td>
      <td>Low</td>
      <td>4.5</td>
      <td>M</td>
      <td>Summer</td>
      <td>o-neck</td>
      <td>butterfly</td>
      <td>natural</td>
      <td>chiffonfabric</td>
      <td>chiffon</td>
      <td>bow</td>
      <td>dot</td>
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
    </tr>
    <tr>
      <th>495</th>
      <td>713391965</td>
      <td>Casual</td>
      <td>Low</td>
      <td>4.7</td>
      <td>M</td>
      <td>Spring</td>
      <td>o-neck</td>
      <td>full</td>
      <td>natural</td>
      <td>polyster</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>solid</td>
      <td>1</td>
    </tr>
    <tr>
      <th>496</th>
      <td>722565148</td>
      <td>Sexy</td>
      <td>Low</td>
      <td>4.3</td>
      <td>free</td>
      <td>Summer</td>
      <td>o-neck</td>
      <td>full</td>
      <td>empire</td>
      <td>cotton</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>0</td>
    </tr>
    <tr>
      <th>497</th>
      <td>532874347</td>
      <td>Casual</td>
      <td>Average</td>
      <td>4.7</td>
      <td>M</td>
      <td>Summer</td>
      <td>v-neck</td>
      <td>full</td>
      <td>empire</td>
      <td>cotton</td>
      <td>NaN</td>
      <td>lace</td>
      <td>solid</td>
      <td>1</td>
    </tr>
    <tr>
      <th>498</th>
      <td>655464934</td>
      <td>Casual</td>
      <td>Average</td>
      <td>4.6</td>
      <td>L</td>
      <td>winter</td>
      <td>boat-neck</td>
      <td>sleevless</td>
      <td>empire</td>
      <td>silk</td>
      <td>broadcloth</td>
      <td>applique</td>
      <td>print</td>
      <td>1</td>
    </tr>
    <tr>
      <th>499</th>
      <td>919930954</td>
      <td>Casual</td>
      <td>Low</td>
      <td>4.4</td>
      <td>free</td>
      <td>Summer</td>
      <td>v-neck</td>
      <td>short</td>
      <td>empire</td>
      <td>cotton</td>
      <td>Corduroy</td>
      <td>lace</td>
      <td>solid</td>
      <td>0</td>
    </tr>
  </tbody>
</table>
<p>500 rows × 14 columns</p>
</div>




```python
sales = pd.read_excel('Dress Sales.xlsx')
sales
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
      <th>Dress_ID</th>
      <th>29/8/2013</th>
      <th>31/8/2013</th>
      <th>2013-02-09 00:00:00</th>
      <th>2013-04-09 00:00:00</th>
      <th>2013-06-09 00:00:00</th>
      <th>2013-08-09 00:00:00</th>
      <th>2013-10-09 00:00:00</th>
      <th>2013-12-09 00:00:00</th>
      <th>14/9/2013</th>
      <th>...</th>
      <th>24/9/2013</th>
      <th>26/9/2013</th>
      <th>28/9/2013</th>
      <th>30/9/2013</th>
      <th>2013-02-10 00:00:00</th>
      <th>2013-04-10 00:00:00</th>
      <th>2013-06-10 00:00:00</th>
      <th>2010-08-10 00:00:00</th>
      <th>2013-10-10 00:00:00</th>
      <th>2013-12-10 00:00:00</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1006032852</td>
      <td>2114</td>
      <td>2274</td>
      <td>2491</td>
      <td>2660</td>
      <td>2727</td>
      <td>2887</td>
      <td>2930</td>
      <td>3119</td>
      <td>3204</td>
      <td>...</td>
      <td>3554</td>
      <td>3624.0</td>
      <td>3706</td>
      <td>3746.0</td>
      <td>3795.0</td>
      <td>3832.0</td>
      <td>3897</td>
      <td>3923.0</td>
      <td>3985.0</td>
      <td>4048</td>
    </tr>
    <tr>
      <th>1</th>
      <td>1212192089</td>
      <td>151</td>
      <td>275</td>
      <td>570</td>
      <td>750</td>
      <td>813</td>
      <td>1066</td>
      <td>1164</td>
      <td>1558</td>
      <td>1756</td>
      <td>...</td>
      <td>2710</td>
      <td>2942.0</td>
      <td>3258</td>
      <td>3354.0</td>
      <td>3475.0</td>
      <td>3654.0</td>
      <td>3911</td>
      <td>4024.0</td>
      <td>4125.0</td>
      <td>4277</td>
    </tr>
    <tr>
      <th>2</th>
      <td>1190380701</td>
      <td>6</td>
      <td>7</td>
      <td>7</td>
      <td>7</td>
      <td>8</td>
      <td>8</td>
      <td>9</td>
      <td>10</td>
      <td>10</td>
      <td>...</td>
      <td>11</td>
      <td>11.0</td>
      <td>11</td>
      <td>11.0</td>
      <td>11.0</td>
      <td>11.0</td>
      <td>11</td>
      <td>11.0</td>
      <td>11.0</td>
      <td>11</td>
    </tr>
    <tr>
      <th>3</th>
      <td>966005983</td>
      <td>1005</td>
      <td>1128</td>
      <td>1326</td>
      <td>1455</td>
      <td>1507</td>
      <td>1621</td>
      <td>1637</td>
      <td>1723</td>
      <td>1746</td>
      <td>...</td>
      <td>1878</td>
      <td>1892.0</td>
      <td>1914</td>
      <td>1924.0</td>
      <td>1929.0</td>
      <td>1941.0</td>
      <td>1952</td>
      <td>1955.0</td>
      <td>1959.0</td>
      <td>1963</td>
    </tr>
    <tr>
      <th>4</th>
      <td>876339541</td>
      <td>996</td>
      <td>1175</td>
      <td>1304</td>
      <td>1396</td>
      <td>1432</td>
      <td>1559</td>
      <td>1570</td>
      <td>1638</td>
      <td>1655</td>
      <td>...</td>
      <td>2032</td>
      <td>2156.0</td>
      <td>2252</td>
      <td>2312.0</td>
      <td>2387.0</td>
      <td>2459.0</td>
      <td>2544</td>
      <td>2614.0</td>
      <td>2693.0</td>
      <td>2736</td>
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
      <th>495</th>
      <td>713391965</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>560</td>
      <td>554</td>
      <td>544</td>
      <td>537</td>
      <td>525</td>
      <td>519</td>
      <td>...</td>
      <td>400</td>
      <td>388.0</td>
      <td>360</td>
      <td>364.0</td>
      <td>372.0</td>
      <td>377.0</td>
      <td>380</td>
      <td>382.0</td>
      <td>384.0</td>
      <td>285</td>
    </tr>
    <tr>
      <th>496</th>
      <td>722565148</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>875</td>
      <td>866</td>
      <td>861</td>
      <td>854</td>
      <td>850</td>
      <td>844</td>
      <td>...</td>
      <td>859</td>
      <td>866.0</td>
      <td>882</td>
      <td>888.0</td>
      <td>895.0</td>
      <td>898.0</td>
      <td>906</td>
      <td>913.0</td>
      <td>919.0</td>
      <td>931</td>
    </tr>
    <tr>
      <th>497</th>
      <td>532874347</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>734</td>
      <td>728</td>
      <td>726</td>
      <td>715</td>
      <td>694</td>
      <td>690</td>
      <td>...</td>
      <td>616</td>
      <td>597.0</td>
      <td>586</td>
      <td>569.0</td>
      <td>561.0</td>
      <td>555.0</td>
      <td>551</td>
      <td>546.0</td>
      <td>535.0</td>
      <td>520</td>
    </tr>
    <tr>
      <th>498</th>
      <td>655464934</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>254</td>
      <td>259</td>
      <td>261</td>
      <td>263</td>
      <td>268</td>
      <td>270</td>
      <td>...</td>
      <td>257</td>
      <td>256.0</td>
      <td>255</td>
      <td>254.0</td>
      <td>253.0</td>
      <td>250.0</td>
      <td>249</td>
      <td>249.0</td>
      <td>249.0</td>
      <td>248</td>
    </tr>
    <tr>
      <th>499</th>
      <td>919930954</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>538</td>
      <td>545</td>
      <td>558</td>
      <td>563</td>
      <td>578</td>
      <td>585</td>
      <td>...</td>
      <td>628</td>
      <td>632.0</td>
      <td>639</td>
      <td>645.0</td>
      <td>651.0</td>
      <td>655.0</td>
      <td>660</td>
      <td>668.0</td>
      <td>674.0</td>
      <td>680</td>
    </tr>
  </tbody>
</table>
<p>500 rows × 24 columns</p>
</div>



## I. Preparation

### 1. Data cleaning
- Each variable forms a column.
- Each observation forms a row.
- Each type of observational unit forms a table.
- Values are formatted with accurate data types.
- Check if NaN and duplicates are needed.

### The Dress Attributes data set has origninally fulfilled the three first requirements.


```python
# set Dress_ID as index
attr = attr.set_index('Dress_ID')
attr
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
      <th>Style</th>
      <th>Price</th>
      <th>Rating</th>
      <th>Size</th>
      <th>Season</th>
      <th>NeckLine</th>
      <th>SleeveLength</th>
      <th>waiseline</th>
      <th>Material</th>
      <th>FabricType</th>
      <th>Decoration</th>
      <th>Pattern Type</th>
      <th>Recommendation</th>
    </tr>
    <tr>
      <th>Dress_ID</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>1006032852</th>
      <td>Sexy</td>
      <td>Low</td>
      <td>4.6</td>
      <td>M</td>
      <td>Summer</td>
      <td>o-neck</td>
      <td>sleevless</td>
      <td>empire</td>
      <td>NaN</td>
      <td>chiffon</td>
      <td>ruffles</td>
      <td>animal</td>
      <td>1</td>
    </tr>
    <tr>
      <th>1212192089</th>
      <td>Casual</td>
      <td>Low</td>
      <td>0.0</td>
      <td>L</td>
      <td>Summer</td>
      <td>o-neck</td>
      <td>Petal</td>
      <td>natural</td>
      <td>microfiber</td>
      <td>NaN</td>
      <td>ruffles</td>
      <td>animal</td>
      <td>0</td>
    </tr>
    <tr>
      <th>1190380701</th>
      <td>vintage</td>
      <td>High</td>
      <td>0.0</td>
      <td>L</td>
      <td>Automn</td>
      <td>o-neck</td>
      <td>full</td>
      <td>natural</td>
      <td>polyster</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>print</td>
      <td>0</td>
    </tr>
    <tr>
      <th>966005983</th>
      <td>Brief</td>
      <td>Average</td>
      <td>4.6</td>
      <td>L</td>
      <td>Spring</td>
      <td>o-neck</td>
      <td>full</td>
      <td>natural</td>
      <td>silk</td>
      <td>chiffon</td>
      <td>embroidary</td>
      <td>print</td>
      <td>1</td>
    </tr>
    <tr>
      <th>876339541</th>
      <td>cute</td>
      <td>Low</td>
      <td>4.5</td>
      <td>M</td>
      <td>Summer</td>
      <td>o-neck</td>
      <td>butterfly</td>
      <td>natural</td>
      <td>chiffonfabric</td>
      <td>chiffon</td>
      <td>bow</td>
      <td>dot</td>
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
    </tr>
    <tr>
      <th>713391965</th>
      <td>Casual</td>
      <td>Low</td>
      <td>4.7</td>
      <td>M</td>
      <td>Spring</td>
      <td>o-neck</td>
      <td>full</td>
      <td>natural</td>
      <td>polyster</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>solid</td>
      <td>1</td>
    </tr>
    <tr>
      <th>722565148</th>
      <td>Sexy</td>
      <td>Low</td>
      <td>4.3</td>
      <td>free</td>
      <td>Summer</td>
      <td>o-neck</td>
      <td>full</td>
      <td>empire</td>
      <td>cotton</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>0</td>
    </tr>
    <tr>
      <th>532874347</th>
      <td>Casual</td>
      <td>Average</td>
      <td>4.7</td>
      <td>M</td>
      <td>Summer</td>
      <td>v-neck</td>
      <td>full</td>
      <td>empire</td>
      <td>cotton</td>
      <td>NaN</td>
      <td>lace</td>
      <td>solid</td>
      <td>1</td>
    </tr>
    <tr>
      <th>655464934</th>
      <td>Casual</td>
      <td>Average</td>
      <td>4.6</td>
      <td>L</td>
      <td>winter</td>
      <td>boat-neck</td>
      <td>sleevless</td>
      <td>empire</td>
      <td>silk</td>
      <td>broadcloth</td>
      <td>applique</td>
      <td>print</td>
      <td>1</td>
    </tr>
    <tr>
      <th>919930954</th>
      <td>Casual</td>
      <td>Low</td>
      <td>4.4</td>
      <td>free</td>
      <td>Summer</td>
      <td>v-neck</td>
      <td>short</td>
      <td>empire</td>
      <td>cotton</td>
      <td>Corduroy</td>
      <td>lace</td>
      <td>solid</td>
      <td>0</td>
    </tr>
  </tbody>
</table>
<p>500 rows × 13 columns</p>
</div>



### However, there are many duplicates with typo faults. We'll focus on 'Season' particularly as this is needed to answer some questions later. Currently, NaN values will be kept.


```python
# clean typo faults for 'Season'
attr['Season'] = attr['Season'].str.replace('summer', 'Summer')
attr['Season'] = attr['Season'].str.replace('spring', 'Spring')
attr['Season'] = attr['Season'].str.replace('Automn', 'Autumn')
attr['Season'] = attr['Season'].str.replace('winter', 'Winter')
```


```python
attr['Season'].value_counts()
```




    Summer    160
    Winter    145
    Spring    124
    Autumn     69
    Name: Season, dtype: int64



### The Dress Sales data set, however, has several issues:
- Column headers are values, not variable names.
- These values are also not well-formatted.


```python
# set Dress_ID as index
sales.set_index('Dress_ID', inplace=True)

# reformat headers as datetime
sales.columns = pd.to_datetime(sales.columns)

sales
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
      <th>2013-08-29</th>
      <th>2013-08-31</th>
      <th>2013-02-09</th>
      <th>2013-04-09</th>
      <th>2013-06-09</th>
      <th>2013-08-09</th>
      <th>2013-10-09</th>
      <th>2013-12-09</th>
      <th>2013-09-14</th>
      <th>2013-09-16</th>
      <th>...</th>
      <th>2013-09-24</th>
      <th>2013-09-26</th>
      <th>2013-09-28</th>
      <th>2013-09-30</th>
      <th>2013-02-10</th>
      <th>2013-04-10</th>
      <th>2013-06-10</th>
      <th>2010-08-10</th>
      <th>2013-10-10</th>
      <th>2013-12-10</th>
    </tr>
    <tr>
      <th>Dress_ID</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>1006032852</th>
      <td>2114</td>
      <td>2274</td>
      <td>2491</td>
      <td>2660</td>
      <td>2727</td>
      <td>2887</td>
      <td>2930</td>
      <td>3119</td>
      <td>3204</td>
      <td>3277</td>
      <td>...</td>
      <td>3554</td>
      <td>3624.0</td>
      <td>3706</td>
      <td>3746.0</td>
      <td>3795.0</td>
      <td>3832.0</td>
      <td>3897</td>
      <td>3923.0</td>
      <td>3985.0</td>
      <td>4048</td>
    </tr>
    <tr>
      <th>1212192089</th>
      <td>151</td>
      <td>275</td>
      <td>570</td>
      <td>750</td>
      <td>813</td>
      <td>1066</td>
      <td>1164</td>
      <td>1558</td>
      <td>1756</td>
      <td>1878</td>
      <td>...</td>
      <td>2710</td>
      <td>2942.0</td>
      <td>3258</td>
      <td>3354.0</td>
      <td>3475.0</td>
      <td>3654.0</td>
      <td>3911</td>
      <td>4024.0</td>
      <td>4125.0</td>
      <td>4277</td>
    </tr>
    <tr>
      <th>1190380701</th>
      <td>6</td>
      <td>7</td>
      <td>7</td>
      <td>7</td>
      <td>8</td>
      <td>8</td>
      <td>9</td>
      <td>10</td>
      <td>10</td>
      <td>10</td>
      <td>...</td>
      <td>11</td>
      <td>11.0</td>
      <td>11</td>
      <td>11.0</td>
      <td>11.0</td>
      <td>11.0</td>
      <td>11</td>
      <td>11.0</td>
      <td>11.0</td>
      <td>11</td>
    </tr>
    <tr>
      <th>966005983</th>
      <td>1005</td>
      <td>1128</td>
      <td>1326</td>
      <td>1455</td>
      <td>1507</td>
      <td>1621</td>
      <td>1637</td>
      <td>1723</td>
      <td>1746</td>
      <td>1783</td>
      <td>...</td>
      <td>1878</td>
      <td>1892.0</td>
      <td>1914</td>
      <td>1924.0</td>
      <td>1929.0</td>
      <td>1941.0</td>
      <td>1952</td>
      <td>1955.0</td>
      <td>1959.0</td>
      <td>1963</td>
    </tr>
    <tr>
      <th>876339541</th>
      <td>996</td>
      <td>1175</td>
      <td>1304</td>
      <td>1396</td>
      <td>1432</td>
      <td>1559</td>
      <td>1570</td>
      <td>1638</td>
      <td>1655</td>
      <td>1681</td>
      <td>...</td>
      <td>2032</td>
      <td>2156.0</td>
      <td>2252</td>
      <td>2312.0</td>
      <td>2387.0</td>
      <td>2459.0</td>
      <td>2544</td>
      <td>2614.0</td>
      <td>2693.0</td>
      <td>2736</td>
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
      <th>713391965</th>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>560</td>
      <td>554</td>
      <td>544</td>
      <td>537</td>
      <td>525</td>
      <td>519</td>
      <td>511</td>
      <td>...</td>
      <td>400</td>
      <td>388.0</td>
      <td>360</td>
      <td>364.0</td>
      <td>372.0</td>
      <td>377.0</td>
      <td>380</td>
      <td>382.0</td>
      <td>384.0</td>
      <td>285</td>
    </tr>
    <tr>
      <th>722565148</th>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>875</td>
      <td>866</td>
      <td>861</td>
      <td>854</td>
      <td>850</td>
      <td>844</td>
      <td>841</td>
      <td>...</td>
      <td>859</td>
      <td>866.0</td>
      <td>882</td>
      <td>888.0</td>
      <td>895.0</td>
      <td>898.0</td>
      <td>906</td>
      <td>913.0</td>
      <td>919.0</td>
      <td>931</td>
    </tr>
    <tr>
      <th>532874347</th>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>734</td>
      <td>728</td>
      <td>726</td>
      <td>715</td>
      <td>694</td>
      <td>690</td>
      <td>686</td>
      <td>...</td>
      <td>616</td>
      <td>597.0</td>
      <td>586</td>
      <td>569.0</td>
      <td>561.0</td>
      <td>555.0</td>
      <td>551</td>
      <td>546.0</td>
      <td>535.0</td>
      <td>520</td>
    </tr>
    <tr>
      <th>655464934</th>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>254</td>
      <td>259</td>
      <td>261</td>
      <td>263</td>
      <td>268</td>
      <td>270</td>
      <td>272</td>
      <td>...</td>
      <td>257</td>
      <td>256.0</td>
      <td>255</td>
      <td>254.0</td>
      <td>253.0</td>
      <td>250.0</td>
      <td>249</td>
      <td>249.0</td>
      <td>249.0</td>
      <td>248</td>
    </tr>
    <tr>
      <th>919930954</th>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>538</td>
      <td>545</td>
      <td>558</td>
      <td>563</td>
      <td>578</td>
      <td>585</td>
      <td>590</td>
      <td>...</td>
      <td>628</td>
      <td>632.0</td>
      <td>639</td>
      <td>645.0</td>
      <td>651.0</td>
      <td>655.0</td>
      <td>660</td>
      <td>668.0</td>
      <td>674.0</td>
      <td>680</td>
    </tr>
  </tbody>
</table>
<p>500 rows × 23 columns</p>
</div>




```python
# change data type to int
sales = sales.dropna().astype('int64')
sales
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
      <th>2013-08-29</th>
      <th>2013-08-31</th>
      <th>2013-02-09</th>
      <th>2013-04-09</th>
      <th>2013-06-09</th>
      <th>2013-08-09</th>
      <th>2013-10-09</th>
      <th>2013-12-09</th>
      <th>2013-09-14</th>
      <th>2013-09-16</th>
      <th>...</th>
      <th>2013-09-24</th>
      <th>2013-09-26</th>
      <th>2013-09-28</th>
      <th>2013-09-30</th>
      <th>2013-02-10</th>
      <th>2013-04-10</th>
      <th>2013-06-10</th>
      <th>2010-08-10</th>
      <th>2013-10-10</th>
      <th>2013-12-10</th>
    </tr>
    <tr>
      <th>Dress_ID</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>1006032852</th>
      <td>2114</td>
      <td>2274</td>
      <td>2491</td>
      <td>2660</td>
      <td>2727</td>
      <td>2887</td>
      <td>2930</td>
      <td>3119</td>
      <td>3204</td>
      <td>3277</td>
      <td>...</td>
      <td>3554</td>
      <td>3624</td>
      <td>3706</td>
      <td>3746</td>
      <td>3795</td>
      <td>3832</td>
      <td>3897</td>
      <td>3923</td>
      <td>3985</td>
      <td>4048</td>
    </tr>
    <tr>
      <th>1212192089</th>
      <td>151</td>
      <td>275</td>
      <td>570</td>
      <td>750</td>
      <td>813</td>
      <td>1066</td>
      <td>1164</td>
      <td>1558</td>
      <td>1756</td>
      <td>1878</td>
      <td>...</td>
      <td>2710</td>
      <td>2942</td>
      <td>3258</td>
      <td>3354</td>
      <td>3475</td>
      <td>3654</td>
      <td>3911</td>
      <td>4024</td>
      <td>4125</td>
      <td>4277</td>
    </tr>
    <tr>
      <th>1190380701</th>
      <td>6</td>
      <td>7</td>
      <td>7</td>
      <td>7</td>
      <td>8</td>
      <td>8</td>
      <td>9</td>
      <td>10</td>
      <td>10</td>
      <td>10</td>
      <td>...</td>
      <td>11</td>
      <td>11</td>
      <td>11</td>
      <td>11</td>
      <td>11</td>
      <td>11</td>
      <td>11</td>
      <td>11</td>
      <td>11</td>
      <td>11</td>
    </tr>
    <tr>
      <th>966005983</th>
      <td>1005</td>
      <td>1128</td>
      <td>1326</td>
      <td>1455</td>
      <td>1507</td>
      <td>1621</td>
      <td>1637</td>
      <td>1723</td>
      <td>1746</td>
      <td>1783</td>
      <td>...</td>
      <td>1878</td>
      <td>1892</td>
      <td>1914</td>
      <td>1924</td>
      <td>1929</td>
      <td>1941</td>
      <td>1952</td>
      <td>1955</td>
      <td>1959</td>
      <td>1963</td>
    </tr>
    <tr>
      <th>876339541</th>
      <td>996</td>
      <td>1175</td>
      <td>1304</td>
      <td>1396</td>
      <td>1432</td>
      <td>1559</td>
      <td>1570</td>
      <td>1638</td>
      <td>1655</td>
      <td>1681</td>
      <td>...</td>
      <td>2032</td>
      <td>2156</td>
      <td>2252</td>
      <td>2312</td>
      <td>2387</td>
      <td>2459</td>
      <td>2544</td>
      <td>2614</td>
      <td>2693</td>
      <td>2736</td>
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
      <th>713391965</th>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>560</td>
      <td>554</td>
      <td>544</td>
      <td>537</td>
      <td>525</td>
      <td>519</td>
      <td>511</td>
      <td>...</td>
      <td>400</td>
      <td>388</td>
      <td>360</td>
      <td>364</td>
      <td>372</td>
      <td>377</td>
      <td>380</td>
      <td>382</td>
      <td>384</td>
      <td>285</td>
    </tr>
    <tr>
      <th>722565148</th>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>875</td>
      <td>866</td>
      <td>861</td>
      <td>854</td>
      <td>850</td>
      <td>844</td>
      <td>841</td>
      <td>...</td>
      <td>859</td>
      <td>866</td>
      <td>882</td>
      <td>888</td>
      <td>895</td>
      <td>898</td>
      <td>906</td>
      <td>913</td>
      <td>919</td>
      <td>931</td>
    </tr>
    <tr>
      <th>532874347</th>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>734</td>
      <td>728</td>
      <td>726</td>
      <td>715</td>
      <td>694</td>
      <td>690</td>
      <td>686</td>
      <td>...</td>
      <td>616</td>
      <td>597</td>
      <td>586</td>
      <td>569</td>
      <td>561</td>
      <td>555</td>
      <td>551</td>
      <td>546</td>
      <td>535</td>
      <td>520</td>
    </tr>
    <tr>
      <th>655464934</th>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>254</td>
      <td>259</td>
      <td>261</td>
      <td>263</td>
      <td>268</td>
      <td>270</td>
      <td>272</td>
      <td>...</td>
      <td>257</td>
      <td>256</td>
      <td>255</td>
      <td>254</td>
      <td>253</td>
      <td>250</td>
      <td>249</td>
      <td>249</td>
      <td>249</td>
      <td>248</td>
    </tr>
    <tr>
      <th>919930954</th>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>538</td>
      <td>545</td>
      <td>558</td>
      <td>563</td>
      <td>578</td>
      <td>585</td>
      <td>590</td>
      <td>...</td>
      <td>628</td>
      <td>632</td>
      <td>639</td>
      <td>645</td>
      <td>651</td>
      <td>655</td>
      <td>660</td>
      <td>668</td>
      <td>674</td>
      <td>680</td>
    </tr>
  </tbody>
</table>
<p>225 rows × 23 columns</p>
</div>




```python
# aggregate sales data by month
sales_by_month = sales.T
sales_by_month.columns = sales.index
sales_by_month = sales_by_month.groupby(sales_by_month.index.month).sum().T

sales_by_month
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
      <th>2</th>
      <th>4</th>
      <th>6</th>
      <th>8</th>
      <th>9</th>
      <th>10</th>
      <th>12</th>
    </tr>
    <tr>
      <th>Dress_ID</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>1006032852</th>
      <td>6286</td>
      <td>6492</td>
      <td>6624</td>
      <td>11198</td>
      <td>31297</td>
      <td>6915</td>
      <td>7167</td>
    </tr>
    <tr>
      <th>1212192089</th>
      <td>4045</td>
      <td>4404</td>
      <td>4724</td>
      <td>5516</td>
      <td>22443</td>
      <td>5289</td>
      <td>5835</td>
    </tr>
    <tr>
      <th>1190380701</th>
      <td>18</td>
      <td>18</td>
      <td>19</td>
      <td>32</td>
      <td>95</td>
      <td>20</td>
      <td>21</td>
    </tr>
    <tr>
      <th>966005983</th>
      <td>3255</td>
      <td>3396</td>
      <td>3459</td>
      <td>5709</td>
      <td>16590</td>
      <td>3596</td>
      <td>3686</td>
    </tr>
    <tr>
      <th>876339541</th>
      <td>3691</td>
      <td>3855</td>
      <td>3976</td>
      <td>6344</td>
      <td>17574</td>
      <td>4263</td>
      <td>4374</td>
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
    </tr>
    <tr>
      <th>713391965</th>
      <td>372</td>
      <td>937</td>
      <td>934</td>
      <td>926</td>
      <td>4015</td>
      <td>921</td>
      <td>810</td>
    </tr>
    <tr>
      <th>722565148</th>
      <td>895</td>
      <td>1773</td>
      <td>1772</td>
      <td>1774</td>
      <td>7740</td>
      <td>1773</td>
      <td>1781</td>
    </tr>
    <tr>
      <th>532874347</th>
      <td>561</td>
      <td>1289</td>
      <td>1279</td>
      <td>1272</td>
      <td>5741</td>
      <td>1250</td>
      <td>1214</td>
    </tr>
    <tr>
      <th>655464934</th>
      <td>253</td>
      <td>504</td>
      <td>508</td>
      <td>510</td>
      <td>2364</td>
      <td>512</td>
      <td>516</td>
    </tr>
    <tr>
      <th>919930954</th>
      <td>651</td>
      <td>1193</td>
      <td>1205</td>
      <td>1226</td>
      <td>5542</td>
      <td>1237</td>
      <td>1258</td>
    </tr>
  </tbody>
</table>
<p>225 rows × 7 columns</p>
</div>



### The Dress Sales data set no longer has the issues:
- Column headers are values, not variable names: **column headers are now name of the months in 2013.**
- These values are also not well-formatted: **values are aggregated and formatted as int.**

### 2. Data Aggregation
- Add 'Season' to sales_by_month
- Group items by 'Season'


```python
sales_by_season = sales_by_month.merge(attr['Season'], on='Dress_ID').dropna().groupby('Season').sum()
sales_by_season
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
      <th>2</th>
      <th>4</th>
      <th>6</th>
      <th>8</th>
      <th>9</th>
      <th>10</th>
      <th>12</th>
    </tr>
    <tr>
      <th>Season</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Autumn</th>
      <td>6560</td>
      <td>9402</td>
      <td>9434</td>
      <td>11544</td>
      <td>43575</td>
      <td>9731</td>
      <td>10022</td>
    </tr>
    <tr>
      <th>Spring</th>
      <td>30356</td>
      <td>34150</td>
      <td>34475</td>
      <td>57915</td>
      <td>158064</td>
      <td>35022</td>
      <td>35332</td>
    </tr>
    <tr>
      <th>Summer</th>
      <td>37839</td>
      <td>45722</td>
      <td>46917</td>
      <td>66687</td>
      <td>216637</td>
      <td>49354</td>
      <td>51224</td>
    </tr>
    <tr>
      <th>Winter</th>
      <td>13344</td>
      <td>15692</td>
      <td>15815</td>
      <td>24549</td>
      <td>73591</td>
      <td>16703</td>
      <td>17315</td>
    </tr>
  </tbody>
</table>
</div>



## II. Data Analysis

### 1. What is the best-selling month in 2013?


```python
# 9/2013 is the best-selling month
sales_by_month.max().sort_values(ascending=False)
```




    9     61147
    8     28089
    2     13764
    4     13516
    6     13400
    10    13102
    12    12909
    dtype: int64



### 2. Top 5 best-selling items each month in 2013?


```python
# total sales by month
totalSales_by_month = sales_by_month.sum()
totalSales_by_month
```




    2      85197
    4      99748
    6     101378
    8     155130
    9     467791
    10    105451
    12    108456
    dtype: int64




```python
output = []
for i in totalSales_by_month.index:
    ratioSales = sales_by_month[i]/totalSales_by_month[totalSales_by_month.index == i].values[0]
    output.append(pd.DataFrame(ratioSales.sort_values(ascending=False)[:5].index))

top10_items_by_month = pd.concat(output, axis=1)
top10_items_by_month.columns = totalSales_by_month.index
top10_items_by_month
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
      <th>2</th>
      <th>4</th>
      <th>6</th>
      <th>8</th>
      <th>9</th>
      <th>10</th>
      <th>12</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>629131530</td>
      <td>629131530</td>
      <td>629131530</td>
      <td>629131530</td>
      <td>629131530</td>
      <td>629131530</td>
      <td>629131530</td>
    </tr>
    <tr>
      <th>1</th>
      <td>749031896</td>
      <td>749031896</td>
      <td>1006032852</td>
      <td>749031896</td>
      <td>1006032852</td>
      <td>1006032852</td>
      <td>1006032852</td>
    </tr>
    <tr>
      <th>2</th>
      <td>1006032852</td>
      <td>1006032852</td>
      <td>749031896</td>
      <td>1006032852</td>
      <td>749031896</td>
      <td>749031896</td>
      <td>749031896</td>
    </tr>
    <tr>
      <th>3</th>
      <td>957723897</td>
      <td>1212192089</td>
      <td>1212192089</td>
      <td>624314841</td>
      <td>1212192089</td>
      <td>1212192089</td>
      <td>1212192089</td>
    </tr>
    <tr>
      <th>4</th>
      <td>624314841</td>
      <td>957723897</td>
      <td>957723897</td>
      <td>957723897</td>
      <td>957723897</td>
      <td>957723897</td>
      <td>957723897</td>
    </tr>
  </tbody>
</table>
</div>



### 3. For all the items in these top 5 lists, are they recommended by the website or not?
- All items are recommended, except the item '1212192089'. 
- This item is ranked the third best selling items in 6 consecitive months 4, 6, 7, 8, 10, 12/2013. This is an interesting insight.


```python
top10_items = top10_items_by_month.melt()
top10_items.columns = ['Month', 'Dress_ID']
top10_items = pd.DataFrame(top10_items['Dress_ID'].unique())
top10_items.columns = ['Dress_ID']
top10_items.merge(attr['Recommendation'], how='inner', on='Dress_ID')
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
      <th>Dress_ID</th>
      <th>Recommendation</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>629131530</td>
      <td>1</td>
    </tr>
    <tr>
      <th>1</th>
      <td>749031896</td>
      <td>1</td>
    </tr>
    <tr>
      <th>2</th>
      <td>1006032852</td>
      <td>1</td>
    </tr>
    <tr>
      <th>3</th>
      <td>957723897</td>
      <td>1</td>
    </tr>
    <tr>
      <th>4</th>
      <td>624314841</td>
      <td>1</td>
    </tr>
    <tr>
      <th>5</th>
      <td>1212192089</td>
      <td>0</td>
    </tr>
  </tbody>
</table>
</div>



### 4. For all the items in these top 5 lists, what are their attributes?


```python
top10_items.merge(attr, how='inner', on='Dress_ID')
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
      <th>Dress_ID</th>
      <th>Style</th>
      <th>Price</th>
      <th>Rating</th>
      <th>Size</th>
      <th>Season</th>
      <th>NeckLine</th>
      <th>SleeveLength</th>
      <th>waiseline</th>
      <th>Material</th>
      <th>FabricType</th>
      <th>Decoration</th>
      <th>Pattern Type</th>
      <th>Recommendation</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>629131530</td>
      <td>cute</td>
      <td>Low</td>
      <td>4.7</td>
      <td>M</td>
      <td>Spring</td>
      <td>ruffled</td>
      <td>short</td>
      <td>empire</td>
      <td>chiffonfabric</td>
      <td>chiffon</td>
      <td>bow</td>
      <td>dot</td>
      <td>1</td>
    </tr>
    <tr>
      <th>1</th>
      <td>749031896</td>
      <td>vintage</td>
      <td>Average</td>
      <td>4.8</td>
      <td>M</td>
      <td>Summer</td>
      <td>o-neck</td>
      <td>short</td>
      <td>empire</td>
      <td>cotton</td>
      <td>jersey</td>
      <td>NaN</td>
      <td>animal</td>
      <td>1</td>
    </tr>
    <tr>
      <th>2</th>
      <td>1006032852</td>
      <td>Sexy</td>
      <td>Low</td>
      <td>4.6</td>
      <td>M</td>
      <td>Summer</td>
      <td>o-neck</td>
      <td>sleevless</td>
      <td>empire</td>
      <td>NaN</td>
      <td>chiffon</td>
      <td>ruffles</td>
      <td>animal</td>
      <td>1</td>
    </tr>
    <tr>
      <th>3</th>
      <td>957723897</td>
      <td>sexy</td>
      <td>Low</td>
      <td>4.7</td>
      <td>M</td>
      <td>Winter</td>
      <td>o-neck</td>
      <td>threequarter</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>chiffon</td>
      <td>lace</td>
      <td>print</td>
      <td>1</td>
    </tr>
    <tr>
      <th>4</th>
      <td>624314841</td>
      <td>cute</td>
      <td>Average</td>
      <td>4.7</td>
      <td>L</td>
      <td>Spring</td>
      <td>o-neck</td>
      <td>short</td>
      <td>NaN</td>
      <td>cotton</td>
      <td>NaN</td>
      <td>sashes</td>
      <td>solid</td>
      <td>1</td>
    </tr>
    <tr>
      <th>5</th>
      <td>1212192089</td>
      <td>Casual</td>
      <td>Low</td>
      <td>0.0</td>
      <td>L</td>
      <td>Summer</td>
      <td>o-neck</td>
      <td>Petal</td>
      <td>natural</td>
      <td>microfiber</td>
      <td>NaN</td>
      <td>ruffles</td>
      <td>animal</td>
      <td>0</td>
    </tr>
  </tbody>
</table>
</div>


