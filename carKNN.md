## In this project, we'll predict a car's market price using its attributes. The data set we will be working with contains information on various cars. For each car we have information about the technical aspects of the vehicle such as the motor's displacement, the weight of the car, the miles per gallon, how fast the car accelerates, and more.

## Attributes:
1. symboling: -3, -2, -1, 0, 1, 2, 3 
2. normalized-losses: continuous from 65 to 256
3. make: alfa-romero, audi, bmw, chevrolet, dodge, honda, isuzu, jaguar, mazda, mercedes-benz, mercury, mitsubishi, nissan, peugot, plymouth, porsche, renault, saab, subaru, toyota, volkswagen, volvo 
4. fuel-type: diesel, gas
5. aspiration: std, turbo
6. num-of-doors: four, two
7. body-style: hardtop, wagon, sedan, hatchback, convertible
8. drive-wheels: 4wd, fwd, rwd
9. engine-location: front, rear
10. wheel-base: continuous from 86.6 120.9
11. length: continuous from 141.1 to 208.1
12. width: continuous from 60.3 to 72.3
13. height: continuous from 47.8 to 59.8
14. curb-weight: continuous from 1488 to 4066
15. engine-type: dohc, dohcv, l, ohc, ohcf, ohcv, rotor
16. num-of-cylinders: eight, five, four, six, three, twelve, two
17. engine-size: continuous from 61 to 326
18. fuel-system: 1bbl, 2bbl, 4bbl, idi, mfi, mpfi, spdi, spfi
19. bore: continuous from 2.54 to 3.94
20. stroke: continuous from 2.07 to 4.17
21. compression-ratio: continuous from 7 to 23
22. horsepower: continuous from 48 to 288
23. peak-rpm: continuous from 4150 to 6600
24. city-mpg: continuous from 13 to 49
25. highway-mpg: continuous from 16 to 54
26. price: continuous from 5118 to 45400


```python
import pandas as pd
from sklearn.neighbors import KNeighborsRegressor
from sklearn.metrics import mean_squared_error
```


```python
cols = ['symboling', 'normalized-losses', 'make', 'fuel-type', 'aspiration', 'num-of-doors', 'body-style', 
        'drive-wheels', 'engine-location', 'wheel-base', 'length', 'width', 'height', 'curb-weight', 'engine-type', 
        'num-of-cylinders', 'engine-size', 'fuel-system', 'bore', 'stroke', 'compression-rate', 'horsepower', 'peak-rpm', 'city-mpg', 'highway-mpg', 'price']
car = pd.read_csv('imports-85.data', names=cols)
car
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
      <th>symboling</th>
      <th>normalized-losses</th>
      <th>make</th>
      <th>fuel-type</th>
      <th>aspiration</th>
      <th>num-of-doors</th>
      <th>body-style</th>
      <th>drive-wheels</th>
      <th>engine-location</th>
      <th>wheel-base</th>
      <th>...</th>
      <th>engine-size</th>
      <th>fuel-system</th>
      <th>bore</th>
      <th>stroke</th>
      <th>compression-rate</th>
      <th>horsepower</th>
      <th>peak-rpm</th>
      <th>city-mpg</th>
      <th>highway-mpg</th>
      <th>price</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>3</td>
      <td>?</td>
      <td>alfa-romero</td>
      <td>gas</td>
      <td>std</td>
      <td>two</td>
      <td>convertible</td>
      <td>rwd</td>
      <td>front</td>
      <td>88.6</td>
      <td>...</td>
      <td>130</td>
      <td>mpfi</td>
      <td>3.47</td>
      <td>2.68</td>
      <td>9.0</td>
      <td>111</td>
      <td>5000</td>
      <td>21</td>
      <td>27</td>
      <td>13495</td>
    </tr>
    <tr>
      <th>1</th>
      <td>3</td>
      <td>?</td>
      <td>alfa-romero</td>
      <td>gas</td>
      <td>std</td>
      <td>two</td>
      <td>convertible</td>
      <td>rwd</td>
      <td>front</td>
      <td>88.6</td>
      <td>...</td>
      <td>130</td>
      <td>mpfi</td>
      <td>3.47</td>
      <td>2.68</td>
      <td>9.0</td>
      <td>111</td>
      <td>5000</td>
      <td>21</td>
      <td>27</td>
      <td>16500</td>
    </tr>
    <tr>
      <th>2</th>
      <td>1</td>
      <td>?</td>
      <td>alfa-romero</td>
      <td>gas</td>
      <td>std</td>
      <td>two</td>
      <td>hatchback</td>
      <td>rwd</td>
      <td>front</td>
      <td>94.5</td>
      <td>...</td>
      <td>152</td>
      <td>mpfi</td>
      <td>2.68</td>
      <td>3.47</td>
      <td>9.0</td>
      <td>154</td>
      <td>5000</td>
      <td>19</td>
      <td>26</td>
      <td>16500</td>
    </tr>
    <tr>
      <th>3</th>
      <td>2</td>
      <td>164</td>
      <td>audi</td>
      <td>gas</td>
      <td>std</td>
      <td>four</td>
      <td>sedan</td>
      <td>fwd</td>
      <td>front</td>
      <td>99.8</td>
      <td>...</td>
      <td>109</td>
      <td>mpfi</td>
      <td>3.19</td>
      <td>3.40</td>
      <td>10.0</td>
      <td>102</td>
      <td>5500</td>
      <td>24</td>
      <td>30</td>
      <td>13950</td>
    </tr>
    <tr>
      <th>4</th>
      <td>2</td>
      <td>164</td>
      <td>audi</td>
      <td>gas</td>
      <td>std</td>
      <td>four</td>
      <td>sedan</td>
      <td>4wd</td>
      <td>front</td>
      <td>99.4</td>
      <td>...</td>
      <td>136</td>
      <td>mpfi</td>
      <td>3.19</td>
      <td>3.40</td>
      <td>8.0</td>
      <td>115</td>
      <td>5500</td>
      <td>18</td>
      <td>22</td>
      <td>17450</td>
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
      <th>200</th>
      <td>-1</td>
      <td>95</td>
      <td>volvo</td>
      <td>gas</td>
      <td>std</td>
      <td>four</td>
      <td>sedan</td>
      <td>rwd</td>
      <td>front</td>
      <td>109.1</td>
      <td>...</td>
      <td>141</td>
      <td>mpfi</td>
      <td>3.78</td>
      <td>3.15</td>
      <td>9.5</td>
      <td>114</td>
      <td>5400</td>
      <td>23</td>
      <td>28</td>
      <td>16845</td>
    </tr>
    <tr>
      <th>201</th>
      <td>-1</td>
      <td>95</td>
      <td>volvo</td>
      <td>gas</td>
      <td>turbo</td>
      <td>four</td>
      <td>sedan</td>
      <td>rwd</td>
      <td>front</td>
      <td>109.1</td>
      <td>...</td>
      <td>141</td>
      <td>mpfi</td>
      <td>3.78</td>
      <td>3.15</td>
      <td>8.7</td>
      <td>160</td>
      <td>5300</td>
      <td>19</td>
      <td>25</td>
      <td>19045</td>
    </tr>
    <tr>
      <th>202</th>
      <td>-1</td>
      <td>95</td>
      <td>volvo</td>
      <td>gas</td>
      <td>std</td>
      <td>four</td>
      <td>sedan</td>
      <td>rwd</td>
      <td>front</td>
      <td>109.1</td>
      <td>...</td>
      <td>173</td>
      <td>mpfi</td>
      <td>3.58</td>
      <td>2.87</td>
      <td>8.8</td>
      <td>134</td>
      <td>5500</td>
      <td>18</td>
      <td>23</td>
      <td>21485</td>
    </tr>
    <tr>
      <th>203</th>
      <td>-1</td>
      <td>95</td>
      <td>volvo</td>
      <td>diesel</td>
      <td>turbo</td>
      <td>four</td>
      <td>sedan</td>
      <td>rwd</td>
      <td>front</td>
      <td>109.1</td>
      <td>...</td>
      <td>145</td>
      <td>idi</td>
      <td>3.01</td>
      <td>3.40</td>
      <td>23.0</td>
      <td>106</td>
      <td>4800</td>
      <td>26</td>
      <td>27</td>
      <td>22470</td>
    </tr>
    <tr>
      <th>204</th>
      <td>-1</td>
      <td>95</td>
      <td>volvo</td>
      <td>gas</td>
      <td>turbo</td>
      <td>four</td>
      <td>sedan</td>
      <td>rwd</td>
      <td>front</td>
      <td>109.1</td>
      <td>...</td>
      <td>141</td>
      <td>mpfi</td>
      <td>3.78</td>
      <td>3.15</td>
      <td>9.5</td>
      <td>114</td>
      <td>5400</td>
      <td>19</td>
      <td>25</td>
      <td>22625</td>
    </tr>
  </tbody>
</table>
<p>205 rows × 26 columns</p>
</div>



Select only suitable columns


```python
car.info()
```

    <class 'pandas.core.frame.DataFrame'>
    RangeIndex: 205 entries, 0 to 204
    Data columns (total 26 columns):
     #   Column             Non-Null Count  Dtype  
    ---  ------             --------------  -----  
     0   symboling          205 non-null    int64  
     1   normalized-losses  205 non-null    object 
     2   make               205 non-null    object 
     3   fuel-type          205 non-null    object 
     4   aspiration         205 non-null    object 
     5   num-of-doors       205 non-null    object 
     6   body-style         205 non-null    object 
     7   drive-wheels       205 non-null    object 
     8   engine-location    205 non-null    object 
     9   wheel-base         205 non-null    float64
     10  length             205 non-null    float64
     11  width              205 non-null    float64
     12  height             205 non-null    float64
     13  curb-weight        205 non-null    int64  
     14  engine-type        205 non-null    object 
     15  num-of-cylinders   205 non-null    object 
     16  engine-size        205 non-null    int64  
     17  fuel-system        205 non-null    object 
     18  bore               205 non-null    object 
     19  stroke             205 non-null    object 
     20  compression-rate   205 non-null    float64
     21  horsepower         205 non-null    object 
     22  peak-rpm           205 non-null    object 
     23  city-mpg           205 non-null    int64  
     24  highway-mpg        205 non-null    int64  
     25  price              205 non-null    object 
    dtypes: float64(5), int64(5), object(16)
    memory usage: 41.8+ KB



```python
car.drop(['make', 'fuel-type', 'aspiration', 'num-of-doors', 'body-style', 
          'drive-wheels', 'engine-location', 'engine-type', 
          'num-of-cylinders', 'fuel-system'], axis=1, inplace=True)
```

Perform some data cleaning tasks


```python
car = car[~(car['normalized-losses'].str.contains('?', regex=False))]
car = car[~(car['bore'].str.contains('?', regex=False))]
car = car[~(car['stroke'].str.contains('?', regex=False))]
```


```python
car = car.astype('float')
car.dropna(inplace=True)
```


```python
car
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
      <th>symboling</th>
      <th>normalized-losses</th>
      <th>wheel-base</th>
      <th>length</th>
      <th>width</th>
      <th>height</th>
      <th>curb-weight</th>
      <th>engine-size</th>
      <th>bore</th>
      <th>stroke</th>
      <th>compression-rate</th>
      <th>horsepower</th>
      <th>peak-rpm</th>
      <th>city-mpg</th>
      <th>highway-mpg</th>
      <th>price</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>3</th>
      <td>2.0</td>
      <td>164.0</td>
      <td>99.8</td>
      <td>176.6</td>
      <td>66.2</td>
      <td>54.3</td>
      <td>2337.0</td>
      <td>109.0</td>
      <td>3.19</td>
      <td>3.40</td>
      <td>10.0</td>
      <td>102.0</td>
      <td>5500.0</td>
      <td>24.0</td>
      <td>30.0</td>
      <td>13950.0</td>
    </tr>
    <tr>
      <th>4</th>
      <td>2.0</td>
      <td>164.0</td>
      <td>99.4</td>
      <td>176.6</td>
      <td>66.4</td>
      <td>54.3</td>
      <td>2824.0</td>
      <td>136.0</td>
      <td>3.19</td>
      <td>3.40</td>
      <td>8.0</td>
      <td>115.0</td>
      <td>5500.0</td>
      <td>18.0</td>
      <td>22.0</td>
      <td>17450.0</td>
    </tr>
    <tr>
      <th>6</th>
      <td>1.0</td>
      <td>158.0</td>
      <td>105.8</td>
      <td>192.7</td>
      <td>71.4</td>
      <td>55.7</td>
      <td>2844.0</td>
      <td>136.0</td>
      <td>3.19</td>
      <td>3.40</td>
      <td>8.5</td>
      <td>110.0</td>
      <td>5500.0</td>
      <td>19.0</td>
      <td>25.0</td>
      <td>17710.0</td>
    </tr>
    <tr>
      <th>8</th>
      <td>1.0</td>
      <td>158.0</td>
      <td>105.8</td>
      <td>192.7</td>
      <td>71.4</td>
      <td>55.9</td>
      <td>3086.0</td>
      <td>131.0</td>
      <td>3.13</td>
      <td>3.40</td>
      <td>8.3</td>
      <td>140.0</td>
      <td>5500.0</td>
      <td>17.0</td>
      <td>20.0</td>
      <td>23875.0</td>
    </tr>
    <tr>
      <th>10</th>
      <td>2.0</td>
      <td>192.0</td>
      <td>101.2</td>
      <td>176.8</td>
      <td>64.8</td>
      <td>54.3</td>
      <td>2395.0</td>
      <td>108.0</td>
      <td>3.50</td>
      <td>2.80</td>
      <td>8.8</td>
      <td>101.0</td>
      <td>5800.0</td>
      <td>23.0</td>
      <td>29.0</td>
      <td>16430.0</td>
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
    </tr>
    <tr>
      <th>200</th>
      <td>-1.0</td>
      <td>95.0</td>
      <td>109.1</td>
      <td>188.8</td>
      <td>68.9</td>
      <td>55.5</td>
      <td>2952.0</td>
      <td>141.0</td>
      <td>3.78</td>
      <td>3.15</td>
      <td>9.5</td>
      <td>114.0</td>
      <td>5400.0</td>
      <td>23.0</td>
      <td>28.0</td>
      <td>16845.0</td>
    </tr>
    <tr>
      <th>201</th>
      <td>-1.0</td>
      <td>95.0</td>
      <td>109.1</td>
      <td>188.8</td>
      <td>68.8</td>
      <td>55.5</td>
      <td>3049.0</td>
      <td>141.0</td>
      <td>3.78</td>
      <td>3.15</td>
      <td>8.7</td>
      <td>160.0</td>
      <td>5300.0</td>
      <td>19.0</td>
      <td>25.0</td>
      <td>19045.0</td>
    </tr>
    <tr>
      <th>202</th>
      <td>-1.0</td>
      <td>95.0</td>
      <td>109.1</td>
      <td>188.8</td>
      <td>68.9</td>
      <td>55.5</td>
      <td>3012.0</td>
      <td>173.0</td>
      <td>3.58</td>
      <td>2.87</td>
      <td>8.8</td>
      <td>134.0</td>
      <td>5500.0</td>
      <td>18.0</td>
      <td>23.0</td>
      <td>21485.0</td>
    </tr>
    <tr>
      <th>203</th>
      <td>-1.0</td>
      <td>95.0</td>
      <td>109.1</td>
      <td>188.8</td>
      <td>68.9</td>
      <td>55.5</td>
      <td>3217.0</td>
      <td>145.0</td>
      <td>3.01</td>
      <td>3.40</td>
      <td>23.0</td>
      <td>106.0</td>
      <td>4800.0</td>
      <td>26.0</td>
      <td>27.0</td>
      <td>22470.0</td>
    </tr>
    <tr>
      <th>204</th>
      <td>-1.0</td>
      <td>95.0</td>
      <td>109.1</td>
      <td>188.8</td>
      <td>68.9</td>
      <td>55.5</td>
      <td>3062.0</td>
      <td>141.0</td>
      <td>3.78</td>
      <td>3.15</td>
      <td>9.5</td>
      <td>114.0</td>
      <td>5400.0</td>
      <td>19.0</td>
      <td>25.0</td>
      <td>22625.0</td>
    </tr>
  </tbody>
</table>
<p>160 rows × 16 columns</p>
</div>



Normalize the data set


```python
norm_car = (car - car.mean())/car.std()
norm_car['price'] = car['price']
norm_car
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
      <th>symboling</th>
      <th>normalized-losses</th>
      <th>wheel-base</th>
      <th>length</th>
      <th>width</th>
      <th>height</th>
      <th>curb-weight</th>
      <th>engine-size</th>
      <th>bore</th>
      <th>stroke</th>
      <th>compression-rate</th>
      <th>horsepower</th>
      <th>peak-rpm</th>
      <th>city-mpg</th>
      <th>highway-mpg</th>
      <th>price</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>3</th>
      <td>1.061360</td>
      <td>1.199357</td>
      <td>0.302953</td>
      <td>0.370653</td>
      <td>0.310093</td>
      <td>0.185034</td>
      <td>-0.254628</td>
      <td>-0.331909</td>
      <td>-0.405604</td>
      <td>0.552964</td>
      <td>-0.037379</td>
      <td>0.199995</td>
      <td>0.824754</td>
      <td>-0.412130</td>
      <td>-0.321187</td>
      <td>13950.0</td>
    </tr>
    <tr>
      <th>4</th>
      <td>1.061360</td>
      <td>1.199357</td>
      <td>0.225490</td>
      <td>0.370653</td>
      <td>0.412815</td>
      <td>0.185034</td>
      <td>0.758061</td>
      <td>0.555922</td>
      <td>-0.405604</td>
      <td>0.552964</td>
      <td>-0.552510</td>
      <td>0.624475</td>
      <td>0.824754</td>
      <td>-1.398776</td>
      <td>-1.563240</td>
      <td>17450.0</td>
    </tr>
    <tr>
      <th>6</th>
      <td>0.220679</td>
      <td>1.030829</td>
      <td>1.464896</td>
      <td>1.764730</td>
      <td>2.980870</td>
      <td>0.799984</td>
      <td>0.799650</td>
      <td>0.555922</td>
      <td>-0.405604</td>
      <td>0.552964</td>
      <td>-0.423727</td>
      <td>0.461214</td>
      <td>0.824754</td>
      <td>-1.234335</td>
      <td>-1.097470</td>
      <td>17710.0</td>
    </tr>
    <tr>
      <th>8</th>
      <td>0.220679</td>
      <td>1.030829</td>
      <td>1.464896</td>
      <td>1.764730</td>
      <td>2.980870</td>
      <td>0.887834</td>
      <td>1.302875</td>
      <td>0.391509</td>
      <td>-0.630031</td>
      <td>0.552964</td>
      <td>-0.475241</td>
      <td>1.440783</td>
      <td>0.824754</td>
      <td>-1.563217</td>
      <td>-1.873754</td>
      <td>23875.0</td>
    </tr>
    <tr>
      <th>10</th>
      <td>1.061360</td>
      <td>1.985820</td>
      <td>0.574073</td>
      <td>0.387971</td>
      <td>-0.408963</td>
      <td>0.185034</td>
      <td>-0.134020</td>
      <td>-0.364792</td>
      <td>0.753933</td>
      <td>-1.486397</td>
      <td>-0.346458</td>
      <td>0.167343</td>
      <td>1.469512</td>
      <td>-0.576571</td>
      <td>-0.476444</td>
      <td>16430.0</td>
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
    </tr>
    <tr>
      <th>200</th>
      <td>-1.460684</td>
      <td>-0.738714</td>
      <td>2.103965</td>
      <td>1.427035</td>
      <td>1.696843</td>
      <td>0.712134</td>
      <td>1.024230</td>
      <td>0.720335</td>
      <td>1.801258</td>
      <td>-0.296770</td>
      <td>-0.166162</td>
      <td>0.591823</td>
      <td>0.609834</td>
      <td>-0.576571</td>
      <td>-0.631700</td>
      <td>16845.0</td>
    </tr>
    <tr>
      <th>201</th>
      <td>-1.460684</td>
      <td>-0.738714</td>
      <td>2.103965</td>
      <td>1.427035</td>
      <td>1.645481</td>
      <td>0.712134</td>
      <td>1.225936</td>
      <td>0.720335</td>
      <td>1.801258</td>
      <td>-0.296770</td>
      <td>-0.372214</td>
      <td>2.093829</td>
      <td>0.394915</td>
      <td>-1.234335</td>
      <td>-1.097470</td>
      <td>19045.0</td>
    </tr>
    <tr>
      <th>202</th>
      <td>-1.460684</td>
      <td>-0.738714</td>
      <td>2.103965</td>
      <td>1.427035</td>
      <td>1.696843</td>
      <td>0.712134</td>
      <td>1.148997</td>
      <td>1.772580</td>
      <td>1.053169</td>
      <td>-1.248471</td>
      <td>-0.346458</td>
      <td>1.244869</td>
      <td>0.824754</td>
      <td>-1.398776</td>
      <td>-1.407984</td>
      <td>21485.0</td>
    </tr>
    <tr>
      <th>203</th>
      <td>-1.460684</td>
      <td>-0.738714</td>
      <td>2.103965</td>
      <td>1.427035</td>
      <td>1.696843</td>
      <td>0.712134</td>
      <td>1.575283</td>
      <td>0.851866</td>
      <td>-1.078884</td>
      <td>0.552964</td>
      <td>3.310972</td>
      <td>0.330605</td>
      <td>-0.679683</td>
      <td>-0.083248</td>
      <td>-0.786957</td>
      <td>22470.0</td>
    </tr>
    <tr>
      <th>204</th>
      <td>-1.460684</td>
      <td>-0.738714</td>
      <td>2.103965</td>
      <td>1.427035</td>
      <td>1.696843</td>
      <td>0.712134</td>
      <td>1.252969</td>
      <td>0.720335</td>
      <td>1.801258</td>
      <td>-0.296770</td>
      <td>-0.166162</td>
      <td>0.591823</td>
      <td>0.609834</td>
      <td>-1.234335</td>
      <td>-1.097470</td>
      <td>22625.0</td>
    </tr>
  </tbody>
</table>
<p>160 rows × 16 columns</p>
</div>



Randomize the data set


```python
np.random.seed(1)
norm_car = norm_car.reindex(np.random.permutation(norm_car.index))
```

Divide the data set into 5 folds


```python
norm_car.loc[norm_car.index[0:32], 'fold'] = 1
norm_car.loc[norm_car.index[32:64], 'fold'] = 2
norm_car.loc[norm_car.index[64:96], 'fold'] = 3
norm_car.loc[norm_car.index[96:128], 'fold'] = 4
norm_car.loc[norm_car.index[128:161], 'fold'] = 5
```

### Univariate KNN model


```python
knn = KNeighborsRegressor()
folds = list(range(1, 6))

def knn_train_test(train_col, targ_col, df):
    np.random.seed(1)
    df = df.reindex(np.random.permutation(df.index))
    avg_holder = list()
    for i in folds:
        train_df = df[df['fold'] != i]
        test_df = df[df['fold'] == i]
        knn.fit(train_df[[train_col]], train_df[targ_col])
        predictions = knn.predict(test_df[[train_col]])
        rmse = mean_squared_error(test_df[targ_col], predictions, squared=False)
        avg_holder.append(rmse)
    return np.mean(avg_holder)    
```


```python
holder = dict()

for i in list(norm_car.columns)[:-2]:
    holder[i] = knn_train_test(i, 'price', norm_car)
```

'width' performs the best using the default k = 5. Top 5 best columns include 'width', 'curb-weight', 'engine-size', 'highway-mpg' & 'horsepower'.


```python
holder
```




    {'symboling': 5773.542601956187,
     'normalized-losses': 4793.308493995757,
     'wheel-base': 3499.77608468145,
     'length': 3443.679951959828,
     'width': 2712.058218094928,
     'height': 5234.185426412528,
     'curb-weight': 2741.1853609557356,
     'engine-size': 3069.772073944786,
     'bore': 4572.138891879573,
     'stroke': 4905.637468602518,
     'compression-rate': 5038.633678117883,
     'horsepower': 3410.695242068672,
     'peak-rpm': 5917.109214483657,
     'city-mpg': 3716.0115290524673,
     'highway-mpg': 3372.2498569489426}



### Hyperparameter Tuning: k with different values 1, 3, 5, 7 & 9


```python
def knn_train_test_k(train_col, targ_col, df):
    np.random.seed(1)
    df = df.reindex(np.random.permutation(df.index))
    avg_holder = dict()
    ks = list(range(1, 10, 2))
    for n in ks:
        knn = KNeighborsRegressor(n_neighbors=n)
        for i in folds:
            train_df = df[df['fold'] != i]
            test_df = df[df['fold'] == i]
            knn.fit(train_df[[train_col]], train_df[targ_col])
            predictions = knn.predict(test_df[[train_col]])
            rmse = mean_squared_error(test_df[targ_col], predictions, squared=False)
            avg_holder[n] = rmse       
    return avg_holder 
```


```python
holder = dict()

for i in list(norm_car.columns)[:-2]:
    holder[i] = knn_train_test_k(i, 'price', norm_car)
```


```python
holder
```




    {'symboling': {1: 7151.416489934005,
      3: 6304.259896865153,
      5: 6223.538452118699,
      7: 6395.299005461762,
      9: 6834.384353849437},
     'normalized-losses': {1: 5891.841615742908,
      3: 6005.617901182192,
      5: 6933.525445074821,
      7: 7498.616880586127,
      9: 7861.857877491784},
     'wheel-base': {1: 4919.812096259368,
      3: 5440.309454599578,
      5: 5614.767477821321,
      7: 5884.882869772675,
      9: 6080.380046703141},
     'length': {1: 4180.443195703058,
      3: 4586.2623784697125,
      5: 5062.271672875725,
      7: 5198.456331718158,
      9: 5188.372216611087},
     'width': {1: 2743.6579084772943,
      3: 2683.402654384085,
      5: 3115.5053446431443,
      7: 3379.5154040293155,
      9: 3842.58142775598},
     'height': {1: 9887.29886173418,
      3: 8425.392294691355,
      5: 7944.0750753313005,
      7: 7508.472275799791,
      9: 7501.1265757794135},
     'curb-weight': {1: 2392.323236678104,
      3: 3319.7997863617884,
      5: 4091.8164152671857,
      7: 4357.250948454327,
      9: 4382.559112374503},
     'engine-size': {1: 2399.1573325336544,
      3: 3722.9050093083665,
      5: 4409.758519749125,
      7: 4544.236561967527,
      9: 4588.195929275107},
     'bore': {1: 5747.2661707545785,
      3: 5571.919232547056,
      5: 5838.175831006633,
      7: 6290.807830787955,
      9: 6302.73465400751},
     'stroke': {1: 5095.010288875774,
      3: 6402.444833865767,
      5: 7141.122542447371,
      7: 7461.6910124519445,
      9: 7342.141314164452},
     'compression-rate': {1: 5697.341479804419,
      3: 6152.143771573541,
      5: 6013.639811399582,
      7: 6640.365533106239,
      9: 7062.371761918895},
     'horsepower': {1: 4076.78584334522,
      3: 4340.324516237237,
      5: 5118.61800208318,
      7: 5617.96068824292,
      9: 6004.34278081727},
     'peak-rpm': {1: 4630.978362479143,
      3: 6712.458826689368,
      5: 7199.857347111121,
      7: 7352.288190261114,
      9: 7548.486228804462},
     'city-mpg': {1: 6067.334543994587,
      3: 5357.831823666589,
      5: 5188.944616923561,
      7: 4702.287156267682,
      9: 4935.164215359174},
     'highway-mpg': {1: 4019.775339648971,
      3: 4193.03720055973,
      5: 4948.52385502485,
      7: 4639.169095366989,
      9: 4594.1652074471485}}



A plot showing RMSE based on k values


```python
import matplotlib.pyplot as plt
%matplotlib inline

for k, v in holder.items():
    x = list(v.keys())
    y = list(v.values())
    
    plt.plot(x,y)
    plt.xlabel('k value')
    plt.ylabel('RMSE')
    plt.legend(list(norm_car.columns)[:-2], bbox_to_anchor=(1.1, 1.05))
```


![png](output_26_0.png)


### Multivariate KNN


```python
knn = KNeighborsRegressor()
folds = list(range(1, 6))

def knn_train_test_m(train_col, targ_col, df):
    np.random.seed(1)
    df = df.reindex(np.random.permutation(df.index))
    avg_holder = list()
    for i in folds:
        train_df = df[df['fold'] != i]
        test_df = df[df['fold'] == i]
        knn.fit(train_df[train_col], train_df[targ_col])
        predictions = knn.predict(test_df[train_col])
        rmse = mean_squared_error(test_df[targ_col], predictions, squared=False)
        avg_holder.append(rmse)
    return np.mean(avg_holder)  
```


```python
# top 5 best perform columns
top5 = ['width', 'curb-weight', 'engine-size', 'highway-mpg', 'horsepower']
```


```python
holder = dict()

holder[1] = knn_train_test_m([top5[0]], 'price', norm_car)
holder[2] = knn_train_test_m(top5[0:2], 'price', norm_car)
holder[3] = knn_train_test_m(top5[0:3], 'price', norm_car)
holder[4] = knn_train_test_m(top5[0:4], 'price', norm_car)
holder[5] = knn_train_test_m(top5, 'price', norm_car)
```


```python
holder
```




    {1: 2712.058218094928,
     2: 2402.507090244865,
     3: 2308.2284272317033,
     4: 2468.3587393797293,
     5: 2404.770358553838}



We see that the model performs best with 3 top columns selected as attributes.


```python
plt.plot(list(holder.keys()), list(holder.values()))
plt.xlabel('no top columns')
plt.ylabel('RMSE')
plt.show()
```


![png](output_33_0.png)


### Hyperparameter Tuning: k with different values [1, 20]


```python
def knn_train_test_m_k(train_col, targ_col, df):
    np.random.seed(1)
    df = df.reindex(np.random.permutation(df.index))
    avg_holder = dict()
    ks = list(range(1, 21))
    for n in ks:
        knn = KNeighborsRegressor(n_neighbors=n)
        for i in folds:
            train_df = df[df['fold'] != i]
            test_df = df[df['fold'] == i]
            knn.fit(train_df[train_col], train_df[targ_col])
            predictions = knn.predict(test_df[train_col])
            rmse = mean_squared_error(test_df[targ_col], predictions, squared=False)
            avg_holder[n] = rmse       
    return avg_holder 
```


```python
holder = knn_train_test_m_k(top5[0:3], 'price', norm_car)
holder
```




    {1: 1533.9219952461729,
     2: 2122.108037644997,
     3: 2840.693017459726,
     4: 3177.120146576338,
     5: 3600.5438242021164,
     6: 3807.792903166187,
     7: 4001.487266632934,
     8: 4123.836006463293,
     9: 4181.890451697653,
     10: 4305.71045335436,
     11: 4318.000317926054,
     12: 4361.653465576563,
     13: 4458.427566129793,
     14: 4503.280451933097,
     15: 4484.815115584167,
     16: 4386.567910641299,
     17: 4455.986059315395,
     18: 4504.683911834878,
     19: 4486.628228638432,
     20: 4531.258945275654}




```python
plt.plot(list(holder.keys()), list(holder.values()))
plt.xlabel('k value')
plt.ylabel('RMSE')
plt.show()
```


![png](output_37_0.png)

