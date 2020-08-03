## AirBnB is a marketplace for short term rentals that allows you to list part or all of your living space for others to rent. As a host, if we try to charge above market price for a living space we'd like to rent, then renters will select more affordable alternatives which are similar to ours. If we set our nightly rent price too low, we'll miss out on potential revenue. 

### One strategy we could use is to:
- find a few listings that are similar to ours, 
- average the listed price for the ones most similar to ours,
- set our listing price to this calculated average price.

### We'll implement the k-nearest neighbors algorithm and use it to suggest 
- a price for a new, unpriced listing that can accommodate up to 3 people, 
- and later for any number of accommodates.


```python
import pandas as pd
```


```python
a= pd.read_csv('dc_airbnb.csv')
a
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
      <th>host_response_rate</th>
      <th>host_acceptance_rate</th>
      <th>host_listings_count</th>
      <th>accommodates</th>
      <th>room_type</th>
      <th>bedrooms</th>
      <th>bathrooms</th>
      <th>beds</th>
      <th>price</th>
      <th>cleaning_fee</th>
      <th>security_deposit</th>
      <th>minimum_nights</th>
      <th>maximum_nights</th>
      <th>number_of_reviews</th>
      <th>latitude</th>
      <th>longitude</th>
      <th>city</th>
      <th>zipcode</th>
      <th>state</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>92%</td>
      <td>91%</td>
      <td>26</td>
      <td>4</td>
      <td>Entire home/apt</td>
      <td>1.0</td>
      <td>1.0</td>
      <td>2.0</td>
      <td>$160.00</td>
      <td>$115.00</td>
      <td>$100.00</td>
      <td>1</td>
      <td>1125</td>
      <td>0</td>
      <td>38.890046</td>
      <td>-77.002808</td>
      <td>Washington</td>
      <td>20003</td>
      <td>DC</td>
    </tr>
    <tr>
      <th>1</th>
      <td>90%</td>
      <td>100%</td>
      <td>1</td>
      <td>6</td>
      <td>Entire home/apt</td>
      <td>3.0</td>
      <td>3.0</td>
      <td>3.0</td>
      <td>$350.00</td>
      <td>$100.00</td>
      <td>NaN</td>
      <td>2</td>
      <td>30</td>
      <td>65</td>
      <td>38.880413</td>
      <td>-76.990485</td>
      <td>Washington</td>
      <td>20003</td>
      <td>DC</td>
    </tr>
    <tr>
      <th>2</th>
      <td>90%</td>
      <td>100%</td>
      <td>2</td>
      <td>1</td>
      <td>Private room</td>
      <td>1.0</td>
      <td>2.0</td>
      <td>1.0</td>
      <td>$50.00</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>2</td>
      <td>1125</td>
      <td>1</td>
      <td>38.955291</td>
      <td>-76.986006</td>
      <td>Hyattsville</td>
      <td>20782</td>
      <td>MD</td>
    </tr>
    <tr>
      <th>3</th>
      <td>100%</td>
      <td>NaN</td>
      <td>1</td>
      <td>2</td>
      <td>Private room</td>
      <td>1.0</td>
      <td>1.0</td>
      <td>1.0</td>
      <td>$95.00</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>1</td>
      <td>1125</td>
      <td>0</td>
      <td>38.872134</td>
      <td>-77.019639</td>
      <td>Washington</td>
      <td>20024</td>
      <td>DC</td>
    </tr>
    <tr>
      <th>4</th>
      <td>92%</td>
      <td>67%</td>
      <td>1</td>
      <td>4</td>
      <td>Entire home/apt</td>
      <td>1.0</td>
      <td>1.0</td>
      <td>1.0</td>
      <td>$50.00</td>
      <td>$15.00</td>
      <td>$450.00</td>
      <td>7</td>
      <td>1125</td>
      <td>0</td>
      <td>38.996382</td>
      <td>-77.041541</td>
      <td>Silver Spring</td>
      <td>20910</td>
      <td>MD</td>
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
    </tr>
    <tr>
      <th>3718</th>
      <td>100%</td>
      <td>60%</td>
      <td>1</td>
      <td>4</td>
      <td>Entire home/apt</td>
      <td>1.0</td>
      <td>1.0</td>
      <td>2.0</td>
      <td>$135.00</td>
      <td>$45.00</td>
      <td>$400.00</td>
      <td>3</td>
      <td>60</td>
      <td>19</td>
      <td>38.885492</td>
      <td>-76.987765</td>
      <td>Washington</td>
      <td>20003</td>
      <td>DC</td>
    </tr>
    <tr>
      <th>3719</th>
      <td>100%</td>
      <td>50%</td>
      <td>1</td>
      <td>2</td>
      <td>Private room</td>
      <td>1.0</td>
      <td>2.0</td>
      <td>1.0</td>
      <td>$79.00</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>3</td>
      <td>365</td>
      <td>36</td>
      <td>38.889401</td>
      <td>-76.986646</td>
      <td>Washington</td>
      <td>20003</td>
      <td>DC</td>
    </tr>
    <tr>
      <th>3720</th>
      <td>100%</td>
      <td>100%</td>
      <td>2</td>
      <td>6</td>
      <td>Entire home/apt</td>
      <td>2.0</td>
      <td>1.0</td>
      <td>3.0</td>
      <td>$275.00</td>
      <td>$100.00</td>
      <td>$500.00</td>
      <td>2</td>
      <td>2147483647</td>
      <td>12</td>
      <td>38.889533</td>
      <td>-77.001010</td>
      <td>Washington</td>
      <td>20003</td>
      <td>DC</td>
    </tr>
    <tr>
      <th>3721</th>
      <td>88%</td>
      <td>100%</td>
      <td>1</td>
      <td>2</td>
      <td>Entire home/apt</td>
      <td>1.0</td>
      <td>1.0</td>
      <td>1.0</td>
      <td>$179.00</td>
      <td>$25.00</td>
      <td>NaN</td>
      <td>2</td>
      <td>21</td>
      <td>48</td>
      <td>38.890815</td>
      <td>-77.002283</td>
      <td>Washington</td>
      <td>20002</td>
      <td>DC</td>
    </tr>
    <tr>
      <th>3722</th>
      <td>70%</td>
      <td>100%</td>
      <td>1</td>
      <td>3</td>
      <td>Entire home/apt</td>
      <td>0.0</td>
      <td>1.0</td>
      <td>1.0</td>
      <td>$110.00</td>
      <td>$40.00</td>
      <td>$200.00</td>
      <td>2</td>
      <td>1125</td>
      <td>1</td>
      <td>38.883646</td>
      <td>-76.999810</td>
      <td>Washington</td>
      <td>20003</td>
      <td>DC</td>
    </tr>
  </tbody>
</table>
<p>3723 rows × 19 columns</p>
</div>




```python
a.info()
```

    <class 'pandas.core.frame.DataFrame'>
    RangeIndex: 3723 entries, 0 to 3722
    Data columns (total 19 columns):
     #   Column                Non-Null Count  Dtype  
    ---  ------                --------------  -----  
     0   host_response_rate    3289 non-null   object 
     1   host_acceptance_rate  3109 non-null   object 
     2   host_listings_count   3723 non-null   int64  
     3   accommodates          3723 non-null   int64  
     4   room_type             3723 non-null   object 
     5   bedrooms              3702 non-null   float64
     6   bathrooms             3696 non-null   float64
     7   beds                  3712 non-null   float64
     8   price                 3723 non-null   object 
     9   cleaning_fee          2335 non-null   object 
     10  security_deposit      1426 non-null   object 
     11  minimum_nights        3723 non-null   int64  
     12  maximum_nights        3723 non-null   int64  
     13  number_of_reviews     3723 non-null   int64  
     14  latitude              3723 non-null   float64
     15  longitude             3723 non-null   float64
     16  city                  3723 non-null   object 
     17  zipcode               3714 non-null   object 
     18  state                 3723 non-null   object 
    dtypes: float64(5), int64(5), object(9)
    memory usage: 552.8+ KB


Calculate the Euclidean distance between our living space, which can accommodate 3 people, and the first living space in the dc_listings Dataframe


```python
a['acc_distance'] = a['accommodates'].apply(lambda x: np.abs(x-3))
```

There are 461 listings that have the same number of accommodates with us.


```python
len(a[a['acc_distance']==0])
```




    461



Randomize the ordering of the dataset before sorting based on 'distance' to avoid bias


```python
np.random.seed(1)
```


```python
a = a.loc[np.random.permutation(a.index)]
a
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
      <th>host_response_rate</th>
      <th>host_acceptance_rate</th>
      <th>host_listings_count</th>
      <th>accommodates</th>
      <th>room_type</th>
      <th>bedrooms</th>
      <th>bathrooms</th>
      <th>beds</th>
      <th>price</th>
      <th>cleaning_fee</th>
      <th>security_deposit</th>
      <th>minimum_nights</th>
      <th>maximum_nights</th>
      <th>number_of_reviews</th>
      <th>latitude</th>
      <th>longitude</th>
      <th>city</th>
      <th>zipcode</th>
      <th>state</th>
      <th>acc_distance</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>149</th>
      <td>100%</td>
      <td>95%</td>
      <td>2</td>
      <td>1</td>
      <td>Private room</td>
      <td>1.0</td>
      <td>1.0</td>
      <td>1.0</td>
      <td>$109.00</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>2</td>
      <td>5</td>
      <td>1</td>
      <td>38.901571</td>
      <td>-77.015750</td>
      <td>Washington</td>
      <td>20001</td>
      <td>DC</td>
      <td>2</td>
    </tr>
    <tr>
      <th>436</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>1</td>
      <td>2</td>
      <td>Private room</td>
      <td>1.0</td>
      <td>1.0</td>
      <td>1.0</td>
      <td>$100.00</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>2</td>
      <td>1125</td>
      <td>0</td>
      <td>38.908886</td>
      <td>-77.023127</td>
      <td>Washington</td>
      <td>20001</td>
      <td>DC</td>
      <td>1</td>
    </tr>
    <tr>
      <th>1521</th>
      <td>100%</td>
      <td>100%</td>
      <td>2</td>
      <td>1</td>
      <td>Private room</td>
      <td>1.0</td>
      <td>1.0</td>
      <td>1.0</td>
      <td>$55.00</td>
      <td>$10.00</td>
      <td>NaN</td>
      <td>1</td>
      <td>1125</td>
      <td>29</td>
      <td>38.950242</td>
      <td>-76.992531</td>
      <td>Washington</td>
      <td>20017</td>
      <td>DC</td>
      <td>2</td>
    </tr>
    <tr>
      <th>3409</th>
      <td>73%</td>
      <td>100%</td>
      <td>1</td>
      <td>2</td>
      <td>Entire home/apt</td>
      <td>1.0</td>
      <td>1.0</td>
      <td>1.0</td>
      <td>$100.00</td>
      <td>$20.00</td>
      <td>NaN</td>
      <td>3</td>
      <td>1125</td>
      <td>8</td>
      <td>38.926464</td>
      <td>-77.051893</td>
      <td>Washington</td>
      <td>20008</td>
      <td>DC</td>
      <td>1</td>
    </tr>
    <tr>
      <th>905</th>
      <td>100%</td>
      <td>25%</td>
      <td>6</td>
      <td>1</td>
      <td>Entire home/apt</td>
      <td>0.0</td>
      <td>1.0</td>
      <td>1.0</td>
      <td>$95.00</td>
      <td>$50.00</td>
      <td>NaN</td>
      <td>5</td>
      <td>1125</td>
      <td>0</td>
      <td>38.905723</td>
      <td>-77.057786</td>
      <td>Washington</td>
      <td>20007</td>
      <td>DC</td>
      <td>2</td>
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
    </tr>
    <tr>
      <th>1342</th>
      <td>100%</td>
      <td>99%</td>
      <td>3</td>
      <td>4</td>
      <td>Entire home/apt</td>
      <td>0.0</td>
      <td>1.0</td>
      <td>2.0</td>
      <td>$140.00</td>
      <td>$25.00</td>
      <td>NaN</td>
      <td>1</td>
      <td>1125</td>
      <td>36</td>
      <td>38.914447</td>
      <td>-77.027642</td>
      <td>Washington</td>
      <td>20009</td>
      <td>DC</td>
      <td>1</td>
    </tr>
    <tr>
      <th>204</th>
      <td>100%</td>
      <td>0%</td>
      <td>1</td>
      <td>4</td>
      <td>Entire home/apt</td>
      <td>1.0</td>
      <td>1.0</td>
      <td>1.0</td>
      <td>$399.00</td>
      <td>$30.00</td>
      <td>$100.00</td>
      <td>1</td>
      <td>1125</td>
      <td>16</td>
      <td>38.904242</td>
      <td>-77.012616</td>
      <td>Washington</td>
      <td>20001</td>
      <td>DC</td>
      <td>1</td>
    </tr>
    <tr>
      <th>2446</th>
      <td>100%</td>
      <td>89%</td>
      <td>2</td>
      <td>4</td>
      <td>Entire home/apt</td>
      <td>2.0</td>
      <td>2.0</td>
      <td>2.0</td>
      <td>$199.00</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>1</td>
      <td>15</td>
      <td>0</td>
      <td>38.918988</td>
      <td>-77.041319</td>
      <td>Washington</td>
      <td>20009</td>
      <td>DC</td>
      <td>1</td>
    </tr>
    <tr>
      <th>3635</th>
      <td>100%</td>
      <td>50%</td>
      <td>1</td>
      <td>1</td>
      <td>Shared room</td>
      <td>1.0</td>
      <td>1.0</td>
      <td>2.0</td>
      <td>$50.00</td>
      <td>$15.00</td>
      <td>NaN</td>
      <td>1</td>
      <td>5</td>
      <td>0</td>
      <td>38.882681</td>
      <td>-76.981565</td>
      <td>Washington</td>
      <td>20003</td>
      <td>DC</td>
      <td>2</td>
    </tr>
    <tr>
      <th>2502</th>
      <td>100%</td>
      <td>70%</td>
      <td>4</td>
      <td>4</td>
      <td>Entire home/apt</td>
      <td>1.0</td>
      <td>1.0</td>
      <td>1.0</td>
      <td>$110.00</td>
      <td>$50.00</td>
      <td>NaN</td>
      <td>1</td>
      <td>1125</td>
      <td>57</td>
      <td>38.915334</td>
      <td>-77.047465</td>
      <td>Washington</td>
      <td>20008</td>
      <td>DC</td>
      <td>1</td>
    </tr>
  </tbody>
</table>
<p>3723 rows × 20 columns</p>
</div>



Top 10 listings closest to us


```python
top10 = a.sort_values('acc_distance')[:10]
top10
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
      <th>host_response_rate</th>
      <th>host_acceptance_rate</th>
      <th>host_listings_count</th>
      <th>accommodates</th>
      <th>room_type</th>
      <th>bedrooms</th>
      <th>bathrooms</th>
      <th>beds</th>
      <th>price</th>
      <th>cleaning_fee</th>
      <th>security_deposit</th>
      <th>minimum_nights</th>
      <th>maximum_nights</th>
      <th>number_of_reviews</th>
      <th>latitude</th>
      <th>longitude</th>
      <th>city</th>
      <th>zipcode</th>
      <th>state</th>
      <th>acc_distance</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>1022</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>1</td>
      <td>3</td>
      <td>Entire home/apt</td>
      <td>1.0</td>
      <td>1.0</td>
      <td>1.0</td>
      <td>$150.00</td>
      <td>$60.00</td>
      <td>NaN</td>
      <td>5</td>
      <td>1125</td>
      <td>2</td>
      <td>38.917843</td>
      <td>-77.038028</td>
      <td>Washington</td>
      <td>20009</td>
      <td>DC</td>
      <td>0</td>
    </tr>
    <tr>
      <th>2327</th>
      <td>100%</td>
      <td>100%</td>
      <td>1</td>
      <td>3</td>
      <td>Entire home/apt</td>
      <td>0.0</td>
      <td>1.0</td>
      <td>2.0</td>
      <td>$115.00</td>
      <td>$50.00</td>
      <td>NaN</td>
      <td>2</td>
      <td>7</td>
      <td>20</td>
      <td>38.920183</td>
      <td>-77.046807</td>
      <td>Washington</td>
      <td>20009</td>
      <td>DC</td>
      <td>0</td>
    </tr>
    <tr>
      <th>2622</th>
      <td>100%</td>
      <td>NaN</td>
      <td>1</td>
      <td>3</td>
      <td>Entire home/apt</td>
      <td>1.0</td>
      <td>1.0</td>
      <td>1.0</td>
      <td>$120.00</td>
      <td>$50.00</td>
      <td>$100.00</td>
      <td>2</td>
      <td>7</td>
      <td>1</td>
      <td>38.927379</td>
      <td>-76.998456</td>
      <td>Washington</td>
      <td>20017</td>
      <td>DC</td>
      <td>0</td>
    </tr>
    <tr>
      <th>2419</th>
      <td>100%</td>
      <td>71%</td>
      <td>2</td>
      <td>3</td>
      <td>Entire home/apt</td>
      <td>1.0</td>
      <td>1.0</td>
      <td>1.0</td>
      <td>$119.00</td>
      <td>$50.00</td>
      <td>$300.00</td>
      <td>1</td>
      <td>1125</td>
      <td>0</td>
      <td>38.923533</td>
      <td>-77.044134</td>
      <td>Washington</td>
      <td>20009</td>
      <td>DC</td>
      <td>0</td>
    </tr>
    <tr>
      <th>2793</th>
      <td>100%</td>
      <td>25%</td>
      <td>2</td>
      <td>3</td>
      <td>Entire home/apt</td>
      <td>2.0</td>
      <td>2.0</td>
      <td>1.0</td>
      <td>$140.00</td>
      <td>$75.00</td>
      <td>$150.00</td>
      <td>2</td>
      <td>1125</td>
      <td>7</td>
      <td>38.931681</td>
      <td>-77.044739</td>
      <td>Washington</td>
      <td>20010</td>
      <td>DC</td>
      <td>0</td>
    </tr>
    <tr>
      <th>1627</th>
      <td>90%</td>
      <td>89%</td>
      <td>1</td>
      <td>3</td>
      <td>Private room</td>
      <td>1.0</td>
      <td>1.0</td>
      <td>1.0</td>
      <td>$65.00</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>4</td>
      <td>1125</td>
      <td>3</td>
      <td>38.952541</td>
      <td>-77.030816</td>
      <td>Washington</td>
      <td>20011</td>
      <td>DC</td>
      <td>0</td>
    </tr>
    <tr>
      <th>265</th>
      <td>80%</td>
      <td>100%</td>
      <td>6</td>
      <td>3</td>
      <td>Entire home/apt</td>
      <td>1.0</td>
      <td>1.0</td>
      <td>1.0</td>
      <td>$179.00</td>
      <td>$50.00</td>
      <td>NaN</td>
      <td>2</td>
      <td>1125</td>
      <td>1</td>
      <td>38.901429</td>
      <td>-77.015959</td>
      <td>Washington</td>
      <td>20001</td>
      <td>DC</td>
      <td>0</td>
    </tr>
    <tr>
      <th>880</th>
      <td>90%</td>
      <td>60%</td>
      <td>1</td>
      <td>3</td>
      <td>Entire home/apt</td>
      <td>1.0</td>
      <td>1.0</td>
      <td>1.0</td>
      <td>$175.00</td>
      <td>$80.00</td>
      <td>$300.00</td>
      <td>1</td>
      <td>5</td>
      <td>63</td>
      <td>38.906414</td>
      <td>-77.068991</td>
      <td>Arlington</td>
      <td>22209</td>
      <td>VA</td>
      <td>0</td>
    </tr>
    <tr>
      <th>2770</th>
      <td>93%</td>
      <td>63%</td>
      <td>1</td>
      <td>3</td>
      <td>Entire home/apt</td>
      <td>0.0</td>
      <td>1.0</td>
      <td>2.0</td>
      <td>$110.00</td>
      <td>$25.00</td>
      <td>$100.00</td>
      <td>2</td>
      <td>31</td>
      <td>1</td>
      <td>38.930441</td>
      <td>-77.038170</td>
      <td>Washington</td>
      <td>20010</td>
      <td>DC</td>
      <td>0</td>
    </tr>
    <tr>
      <th>2408</th>
      <td>70%</td>
      <td>90%</td>
      <td>1</td>
      <td>3</td>
      <td>Entire home/apt</td>
      <td>1.0</td>
      <td>2.0</td>
      <td>2.0</td>
      <td>$209.00</td>
      <td>$70.00</td>
      <td>$500.00</td>
      <td>3</td>
      <td>1125</td>
      <td>9</td>
      <td>38.921265</td>
      <td>-77.040435</td>
      <td>Washington</td>
      <td>20009</td>
      <td>DC</td>
      <td>0</td>
    </tr>
  </tbody>
</table>
</div>




```python
top10.price
```




    1022    $150.00
    2327    $115.00
    2622    $120.00
    2419    $119.00
    2793    $140.00
    1627     $65.00
    265     $179.00
    880     $175.00
    2770    $110.00
    2408    $209.00
    Name: price, dtype: object



Perform some data cleaning tasks before calculating the average price for these listings


```python
top10P = top10.price.str.replace('$', '').astype('float')
top10P
```




    1022    150.0
    2327    115.0
    2622    120.0
    2419    119.0
    2793    140.0
    1627     65.0
    265     179.0
    880     175.0
    2770    110.0
    2408    209.0
    Name: price, dtype: float64




```python
np.average(top10P[:5])
```




    128.8



Generalize into a function to calculate mean prices for any number of accommodates


```python
dc_listings = pd.read_csv('dc_airbnb.csv')
stripped_commas = dc_listings['price'].str.replace(',', '')
stripped_dollars = stripped_commas.str.replace('$', '')
dc_listings['price'] = stripped_dollars.astype('float')
dc_listings = dc_listings.loc[np.random.permutation(len(dc_listings))]

def predict_price(nBedroom):
    temp_df = dc_listings.copy()
    temp_df['acc_distance'] = temp_df['accommodates'].apply(lambda x: np.abs(x - nBedroom))
    five = temp_df.sort_values('acc_distance')[:5]['price']
    return(five.mean())
```


```python
predict_price(2)
```




    121.8




```python
predict_price(6)
```




    292.8




```python
predict_price(8)
```




    218.8


