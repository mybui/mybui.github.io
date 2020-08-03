## AirBnB is a marketplace for short term rentals that allows you to list part or all of your living space for others to rent. As a host, if we try to charge above market price for a living space we'd like to rent, then renters will select more affordable alternatives which are similar to ours. If we set our nightly rent price too low, we'll miss out on potential revenue. 

## We'll implement the k-nearest neighbors algorithm, and fine tune some hypermeters


```python
import pandas as pd
```


```python
dc_listings = pd.read_csv('dc_airbnb.csv')
stripped_commas = dc_listings['price'].str.replace(',', '')
stripped_dollars = stripped_commas.str.replace('$', '')
dc_listings['price'] = stripped_dollars.astype('float')
dc_listings = dc_listings.loc[np.random.permutation(len(dc_listings))]
```


```python
drop_columns = ['room_type', 'city', 'state', 'latitude', 'longitude', 'zipcode', 'host_response_rate', 'host_acceptance_rate', 'host_listings_count', 'cleaning_fee', 'security_deposit']
dc_listings = dc_listings.drop(drop_columns, axis=1)
dc_listings = dc_listings.dropna(axis=0)
dc_listings
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
      <th>accommodates</th>
      <th>bedrooms</th>
      <th>bathrooms</th>
      <th>beds</th>
      <th>price</th>
      <th>minimum_nights</th>
      <th>maximum_nights</th>
      <th>number_of_reviews</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>1843</th>
      <td>4</td>
      <td>1.0</td>
      <td>1.0</td>
      <td>2.0</td>
      <td>120.0</td>
      <td>2</td>
      <td>1825</td>
      <td>2</td>
    </tr>
    <tr>
      <th>1247</th>
      <td>3</td>
      <td>1.0</td>
      <td>1.0</td>
      <td>2.0</td>
      <td>209.0</td>
      <td>2</td>
      <td>1125</td>
      <td>5</td>
    </tr>
    <tr>
      <th>3503</th>
      <td>9</td>
      <td>4.0</td>
      <td>2.0</td>
      <td>7.0</td>
      <td>300.0</td>
      <td>2</td>
      <td>1125</td>
      <td>30</td>
    </tr>
    <tr>
      <th>433</th>
      <td>6</td>
      <td>1.0</td>
      <td>2.5</td>
      <td>4.0</td>
      <td>60.0</td>
      <td>1</td>
      <td>1125</td>
      <td>0</td>
    </tr>
    <tr>
      <th>1291</th>
      <td>2</td>
      <td>1.0</td>
      <td>1.0</td>
      <td>1.0</td>
      <td>134.0</td>
      <td>1</td>
      <td>1125</td>
      <td>69</td>
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
    </tr>
    <tr>
      <th>447</th>
      <td>2</td>
      <td>1.0</td>
      <td>1.0</td>
      <td>1.0</td>
      <td>110.0</td>
      <td>2</td>
      <td>1125</td>
      <td>6</td>
    </tr>
    <tr>
      <th>3098</th>
      <td>3</td>
      <td>0.0</td>
      <td>1.0</td>
      <td>1.0</td>
      <td>98.0</td>
      <td>1</td>
      <td>1125</td>
      <td>2</td>
    </tr>
    <tr>
      <th>3200</th>
      <td>7</td>
      <td>2.0</td>
      <td>2.0</td>
      <td>3.0</td>
      <td>375.0</td>
      <td>3</td>
      <td>1125</td>
      <td>0</td>
    </tr>
    <tr>
      <th>1664</th>
      <td>2</td>
      <td>1.0</td>
      <td>1.5</td>
      <td>1.0</td>
      <td>62.0</td>
      <td>3</td>
      <td>200</td>
      <td>6</td>
    </tr>
    <tr>
      <th>2429</th>
      <td>4</td>
      <td>0.0</td>
      <td>1.0</td>
      <td>1.0</td>
      <td>90.0</td>
      <td>3</td>
      <td>1125</td>
      <td>1</td>
    </tr>
  </tbody>
</table>
<p>3671 rows × 8 columns</p>
</div>



Normalize the data set


```python
normalized_dc = (dc_listings - dc_listings.mean())/(dc_listings.std())
normalized_dc['price'] = dc_listings['price']
normalized_dc
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
      <th>accommodates</th>
      <th>bedrooms</th>
      <th>bathrooms</th>
      <th>beds</th>
      <th>price</th>
      <th>minimum_nights</th>
      <th>maximum_nights</th>
      <th>number_of_reviews</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>1843</th>
      <td>0.401366</td>
      <td>-0.249467</td>
      <td>-0.439151</td>
      <td>0.297345</td>
      <td>120.0</td>
      <td>-0.065038</td>
      <td>-0.016553</td>
      <td>-0.448301</td>
    </tr>
    <tr>
      <th>1247</th>
      <td>-0.097589</td>
      <td>-0.249467</td>
      <td>-0.439151</td>
      <td>0.297345</td>
      <td>209.0</td>
      <td>-0.065038</td>
      <td>-0.016573</td>
      <td>-0.345690</td>
    </tr>
    <tr>
      <th>3503</th>
      <td>2.896140</td>
      <td>3.318561</td>
      <td>1.264998</td>
      <td>4.518363</td>
      <td>300.0</td>
      <td>-0.065038</td>
      <td>-0.016573</td>
      <td>0.509404</td>
    </tr>
    <tr>
      <th>433</th>
      <td>1.399275</td>
      <td>-0.249467</td>
      <td>2.117072</td>
      <td>1.985752</td>
      <td>60.0</td>
      <td>-0.341375</td>
      <td>-0.016573</td>
      <td>-0.516709</td>
    </tr>
    <tr>
      <th>1291</th>
      <td>-0.596544</td>
      <td>-0.249467</td>
      <td>-0.439151</td>
      <td>-0.546858</td>
      <td>134.0</td>
      <td>-0.341375</td>
      <td>-0.016573</td>
      <td>1.843350</td>
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
    </tr>
    <tr>
      <th>447</th>
      <td>-0.596544</td>
      <td>-0.249467</td>
      <td>-0.439151</td>
      <td>-0.546858</td>
      <td>110.0</td>
      <td>-0.065038</td>
      <td>-0.016573</td>
      <td>-0.311486</td>
    </tr>
    <tr>
      <th>3098</th>
      <td>-0.097589</td>
      <td>-1.438810</td>
      <td>-0.439151</td>
      <td>-0.546858</td>
      <td>98.0</td>
      <td>-0.341375</td>
      <td>-0.016573</td>
      <td>-0.448301</td>
    </tr>
    <tr>
      <th>3200</th>
      <td>1.898230</td>
      <td>0.939875</td>
      <td>1.264998</td>
      <td>1.141549</td>
      <td>375.0</td>
      <td>0.211298</td>
      <td>-0.016573</td>
      <td>-0.516709</td>
    </tr>
    <tr>
      <th>1664</th>
      <td>-0.596544</td>
      <td>-0.249467</td>
      <td>0.412923</td>
      <td>-0.546858</td>
      <td>62.0</td>
      <td>0.211298</td>
      <td>-0.016599</td>
      <td>-0.311486</td>
    </tr>
    <tr>
      <th>2429</th>
      <td>0.401366</td>
      <td>-1.438810</td>
      <td>-0.439151</td>
      <td>-0.546858</td>
      <td>90.0</td>
      <td>0.211298</td>
      <td>-0.016573</td>
      <td>-0.482505</td>
    </tr>
  </tbody>
</table>
<p>3671 rows × 8 columns</p>
</div>



Divide the data set into 5 iterations and perform the model on the training data where fold number is from 2 to 5, and the test data is 1


```python
normalized_dc.loc[dc_listings.index[0:734], "fold"] = 1
normalized_dc.loc[dc_listings.index[734:1468], "fold"] = 2
normalized_dc.loc[dc_listings.index[1468:2202], "fold"] = 3
normalized_dc.loc[dc_listings.index[2202:2936], "fold"] = 4
normalized_dc.loc[dc_listings.index[2936:3672], "fold"] = 5
```


```python
knn = KNeighborsRegressor(n_neighbors=5, algorithm='brute', metric='euclidean')
cols = ['accommodates', 'bedrooms', 'bathrooms', 'number_of_reviews']
```


```python
holder = dict()

def train_and_validate(df, folds):
    for i in folds:
        train_df = normalized_dc[normalized_dc['fold'] != i]
        test_df = normalized_dc[normalized_dc['fold'] == i]
        knn.fit(train_df[cols], train_df['price'])
        predictions = knn.predict(test_df[cols])
        rmse = mean_squared_error(test_df['price'], predictions, squared=False)
        holder[i] = rmse
    return holder
```


```python
train_and_validate(normalized_dc, list(range(1, 6)))
```




    {1: 138.44460169475593,
     2: 112.20772994495763,
     3: 114.47170824750026,
     4: 99.48535061191683,
     5: 125.52804776427539}




```python
avg_rmse = np.mean(list(train_and_validate(normalized_dc, list(range(1, 6))).values()))
```


```python
avg_rmse
```




    118.0274876526812



Continue applying the model with higher folds. The reduction in mean error metric can be observed.


```python
from sklearn.model_selection import cross_val_score, KFold

num_folds = list(range(5, 21, 5))

for i in num_folds:
    kf = KFold(i, shuffle=True, random_state=1)
    knn = KNeighborsRegressor()
    mses = cross_val_score(knn, normalized_dc[cols], normalized_dc['price'], scoring="neg_mean_squared_error", cv=kf)
    rmses = np.sqrt(np.absolute(mses))
    avg_rmse = np.mean(rmses)
    std_rmse = np.std(rmses)
    print(str(i), "folds: ", "avg RMSE: ", str(avg_rmse), "std RMSE: ", str(std_rmse))
```

    5 folds:  avg RMSE:  114.02043553013534 std RMSE:  16.125105880243964
    10 folds:  avg RMSE:  115.46486207572507 std RMSE:  27.06096806445326
    15 folds:  avg RMSE:  111.96950718674546 std RMSE:  32.59271511416034
    20 folds:  avg RMSE:  111.57559012781606 std RMSE:  38.311861651775025

