```python
import pandas as pd
```


```python
# read inputs
google = pd.read_csv('googleplaystore.csv')
apple = pd.read_csv('AppleStore.csv')
```


```python
google
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
      <th>App</th>
      <th>Category</th>
      <th>Rating</th>
      <th>Reviews</th>
      <th>Size</th>
      <th>Installs</th>
      <th>Type</th>
      <th>Price</th>
      <th>Content Rating</th>
      <th>Genres</th>
      <th>Last Updated</th>
      <th>Current Ver</th>
      <th>Android Ver</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Photo Editor &amp; Candy Camera &amp; Grid &amp; ScrapBook</td>
      <td>ART_AND_DESIGN</td>
      <td>4.1</td>
      <td>159</td>
      <td>19M</td>
      <td>10,000+</td>
      <td>Free</td>
      <td>0</td>
      <td>Everyone</td>
      <td>Art &amp; Design</td>
      <td>January 7, 2018</td>
      <td>1.0.0</td>
      <td>4.0.3 and up</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Coloring book moana</td>
      <td>ART_AND_DESIGN</td>
      <td>3.9</td>
      <td>967</td>
      <td>14M</td>
      <td>500,000+</td>
      <td>Free</td>
      <td>0</td>
      <td>Everyone</td>
      <td>Art &amp; Design;Pretend Play</td>
      <td>January 15, 2018</td>
      <td>2.0.0</td>
      <td>4.0.3 and up</td>
    </tr>
    <tr>
      <th>2</th>
      <td>U Launcher Lite – FREE Live Cool Themes, Hide ...</td>
      <td>ART_AND_DESIGN</td>
      <td>4.7</td>
      <td>87510</td>
      <td>8.7M</td>
      <td>5,000,000+</td>
      <td>Free</td>
      <td>0</td>
      <td>Everyone</td>
      <td>Art &amp; Design</td>
      <td>August 1, 2018</td>
      <td>1.2.4</td>
      <td>4.0.3 and up</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Sketch - Draw &amp; Paint</td>
      <td>ART_AND_DESIGN</td>
      <td>4.5</td>
      <td>215644</td>
      <td>25M</td>
      <td>50,000,000+</td>
      <td>Free</td>
      <td>0</td>
      <td>Teen</td>
      <td>Art &amp; Design</td>
      <td>June 8, 2018</td>
      <td>Varies with device</td>
      <td>4.2 and up</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Pixel Draw - Number Art Coloring Book</td>
      <td>ART_AND_DESIGN</td>
      <td>4.3</td>
      <td>967</td>
      <td>2.8M</td>
      <td>100,000+</td>
      <td>Free</td>
      <td>0</td>
      <td>Everyone</td>
      <td>Art &amp; Design;Creativity</td>
      <td>June 20, 2018</td>
      <td>1.1</td>
      <td>4.4 and up</td>
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
      <th>10836</th>
      <td>Sya9a Maroc - FR</td>
      <td>FAMILY</td>
      <td>4.5</td>
      <td>38</td>
      <td>53M</td>
      <td>5,000+</td>
      <td>Free</td>
      <td>0</td>
      <td>Everyone</td>
      <td>Education</td>
      <td>July 25, 2017</td>
      <td>1.48</td>
      <td>4.1 and up</td>
    </tr>
    <tr>
      <th>10837</th>
      <td>Fr. Mike Schmitz Audio Teachings</td>
      <td>FAMILY</td>
      <td>5.0</td>
      <td>4</td>
      <td>3.6M</td>
      <td>100+</td>
      <td>Free</td>
      <td>0</td>
      <td>Everyone</td>
      <td>Education</td>
      <td>July 6, 2018</td>
      <td>1.0</td>
      <td>4.1 and up</td>
    </tr>
    <tr>
      <th>10838</th>
      <td>Parkinson Exercices FR</td>
      <td>MEDICAL</td>
      <td>NaN</td>
      <td>3</td>
      <td>9.5M</td>
      <td>1,000+</td>
      <td>Free</td>
      <td>0</td>
      <td>Everyone</td>
      <td>Medical</td>
      <td>January 20, 2017</td>
      <td>1.0</td>
      <td>2.2 and up</td>
    </tr>
    <tr>
      <th>10839</th>
      <td>The SCP Foundation DB fr nn5n</td>
      <td>BOOKS_AND_REFERENCE</td>
      <td>4.5</td>
      <td>114</td>
      <td>Varies with device</td>
      <td>1,000+</td>
      <td>Free</td>
      <td>0</td>
      <td>Mature 17+</td>
      <td>Books &amp; Reference</td>
      <td>January 19, 2015</td>
      <td>Varies with device</td>
      <td>Varies with device</td>
    </tr>
    <tr>
      <th>10840</th>
      <td>iHoroscope - 2018 Daily Horoscope &amp; Astrology</td>
      <td>LIFESTYLE</td>
      <td>4.5</td>
      <td>398307</td>
      <td>19M</td>
      <td>10,000,000+</td>
      <td>Free</td>
      <td>0</td>
      <td>Everyone</td>
      <td>Lifestyle</td>
      <td>July 25, 2018</td>
      <td>Varies with device</td>
      <td>Varies with device</td>
    </tr>
  </tbody>
</table>
<p>10841 rows × 13 columns</p>
</div>




```python
apple
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
      <th>Unnamed: 0</th>
      <th>id</th>
      <th>track_name</th>
      <th>size_bytes</th>
      <th>currency</th>
      <th>price</th>
      <th>rating_count_tot</th>
      <th>rating_count_ver</th>
      <th>user_rating</th>
      <th>user_rating_ver</th>
      <th>ver</th>
      <th>cont_rating</th>
      <th>prime_genre</th>
      <th>sup_devices.num</th>
      <th>ipadSc_urls.num</th>
      <th>lang.num</th>
      <th>vpp_lic</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1</td>
      <td>281656475</td>
      <td>PAC-MAN Premium</td>
      <td>100788224</td>
      <td>USD</td>
      <td>3.99</td>
      <td>21292</td>
      <td>26</td>
      <td>4.0</td>
      <td>4.5</td>
      <td>6.3.5</td>
      <td>4+</td>
      <td>Games</td>
      <td>38</td>
      <td>5</td>
      <td>10</td>
      <td>1</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2</td>
      <td>281796108</td>
      <td>Evernote - stay organized</td>
      <td>158578688</td>
      <td>USD</td>
      <td>0.00</td>
      <td>161065</td>
      <td>26</td>
      <td>4.0</td>
      <td>3.5</td>
      <td>8.2.2</td>
      <td>4+</td>
      <td>Productivity</td>
      <td>37</td>
      <td>5</td>
      <td>23</td>
      <td>1</td>
    </tr>
    <tr>
      <th>2</th>
      <td>3</td>
      <td>281940292</td>
      <td>WeatherBug - Local Weather, Radar, Maps, Alerts</td>
      <td>100524032</td>
      <td>USD</td>
      <td>0.00</td>
      <td>188583</td>
      <td>2822</td>
      <td>3.5</td>
      <td>4.5</td>
      <td>5.0.0</td>
      <td>4+</td>
      <td>Weather</td>
      <td>37</td>
      <td>5</td>
      <td>3</td>
      <td>1</td>
    </tr>
    <tr>
      <th>3</th>
      <td>4</td>
      <td>282614216</td>
      <td>eBay: Best App to Buy, Sell, Save! Online Shop...</td>
      <td>128512000</td>
      <td>USD</td>
      <td>0.00</td>
      <td>262241</td>
      <td>649</td>
      <td>4.0</td>
      <td>4.5</td>
      <td>5.10.0</td>
      <td>12+</td>
      <td>Shopping</td>
      <td>37</td>
      <td>5</td>
      <td>9</td>
      <td>1</td>
    </tr>
    <tr>
      <th>4</th>
      <td>5</td>
      <td>282935706</td>
      <td>Bible</td>
      <td>92774400</td>
      <td>USD</td>
      <td>0.00</td>
      <td>985920</td>
      <td>5320</td>
      <td>4.5</td>
      <td>5.0</td>
      <td>7.5.1</td>
      <td>4+</td>
      <td>Reference</td>
      <td>37</td>
      <td>5</td>
      <td>45</td>
      <td>1</td>
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
    </tr>
    <tr>
      <th>7192</th>
      <td>11081</td>
      <td>1187617475</td>
      <td>Kubik</td>
      <td>126644224</td>
      <td>USD</td>
      <td>0.00</td>
      <td>142</td>
      <td>75</td>
      <td>4.5</td>
      <td>4.5</td>
      <td>1.3</td>
      <td>4+</td>
      <td>Games</td>
      <td>38</td>
      <td>5</td>
      <td>1</td>
      <td>1</td>
    </tr>
    <tr>
      <th>7193</th>
      <td>11082</td>
      <td>1187682390</td>
      <td>VR Roller-Coaster</td>
      <td>120760320</td>
      <td>USD</td>
      <td>0.00</td>
      <td>30</td>
      <td>30</td>
      <td>4.5</td>
      <td>4.5</td>
      <td>0.9</td>
      <td>4+</td>
      <td>Games</td>
      <td>38</td>
      <td>0</td>
      <td>1</td>
      <td>1</td>
    </tr>
    <tr>
      <th>7194</th>
      <td>11087</td>
      <td>1187779532</td>
      <td>Bret Michaels Emojis + Lyric Keyboard</td>
      <td>111322112</td>
      <td>USD</td>
      <td>1.99</td>
      <td>15</td>
      <td>0</td>
      <td>4.5</td>
      <td>0.0</td>
      <td>1.0.2</td>
      <td>9+</td>
      <td>Utilities</td>
      <td>37</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
    </tr>
    <tr>
      <th>7195</th>
      <td>11089</td>
      <td>1187838770</td>
      <td>VR Roller Coaster World - Virtual Reality</td>
      <td>97235968</td>
      <td>USD</td>
      <td>0.00</td>
      <td>85</td>
      <td>32</td>
      <td>4.5</td>
      <td>4.5</td>
      <td>1.0.15</td>
      <td>12+</td>
      <td>Games</td>
      <td>38</td>
      <td>0</td>
      <td>2</td>
      <td>1</td>
    </tr>
    <tr>
      <th>7196</th>
      <td>11097</td>
      <td>1188375727</td>
      <td>Escape the Sweet Shop Series</td>
      <td>90898432</td>
      <td>USD</td>
      <td>0.00</td>
      <td>3</td>
      <td>3</td>
      <td>5.0</td>
      <td>5.0</td>
      <td>1.0</td>
      <td>4+</td>
      <td>Games</td>
      <td>40</td>
      <td>0</td>
      <td>2</td>
      <td>1</td>
    </tr>
  </tbody>
</table>
<p>7197 rows × 17 columns</p>
</div>




```python
google.describe()
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
      <th>Rating</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>count</th>
      <td>9367.000000</td>
    </tr>
    <tr>
      <th>mean</th>
      <td>4.193338</td>
    </tr>
    <tr>
      <th>std</th>
      <td>0.537431</td>
    </tr>
    <tr>
      <th>min</th>
      <td>1.000000</td>
    </tr>
    <tr>
      <th>25%</th>
      <td>4.000000</td>
    </tr>
    <tr>
      <th>50%</th>
      <td>4.300000</td>
    </tr>
    <tr>
      <th>75%</th>
      <td>4.500000</td>
    </tr>
    <tr>
      <th>max</th>
      <td>19.000000</td>
    </tr>
  </tbody>
</table>
</div>




```python
apple.describe()
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
      <th>Unnamed: 0</th>
      <th>id</th>
      <th>size_bytes</th>
      <th>price</th>
      <th>rating_count_tot</th>
      <th>rating_count_ver</th>
      <th>user_rating</th>
      <th>user_rating_ver</th>
      <th>sup_devices.num</th>
      <th>ipadSc_urls.num</th>
      <th>lang.num</th>
      <th>vpp_lic</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>count</th>
      <td>7197.000000</td>
      <td>7.197000e+03</td>
      <td>7.197000e+03</td>
      <td>7197.000000</td>
      <td>7.197000e+03</td>
      <td>7197.000000</td>
      <td>7197.000000</td>
      <td>7197.000000</td>
      <td>7197.000000</td>
      <td>7197.000000</td>
      <td>7197.000000</td>
      <td>7197.000000</td>
    </tr>
    <tr>
      <th>mean</th>
      <td>4759.069612</td>
      <td>8.631310e+08</td>
      <td>1.991345e+08</td>
      <td>1.726218</td>
      <td>1.289291e+04</td>
      <td>460.373906</td>
      <td>3.526956</td>
      <td>3.253578</td>
      <td>37.361817</td>
      <td>3.707100</td>
      <td>5.434903</td>
      <td>0.993053</td>
    </tr>
    <tr>
      <th>std</th>
      <td>3093.625213</td>
      <td>2.712368e+08</td>
      <td>3.592069e+08</td>
      <td>5.833006</td>
      <td>7.573941e+04</td>
      <td>3920.455183</td>
      <td>1.517948</td>
      <td>1.809363</td>
      <td>3.737715</td>
      <td>1.986005</td>
      <td>7.919593</td>
      <td>0.083066</td>
    </tr>
    <tr>
      <th>min</th>
      <td>1.000000</td>
      <td>2.816565e+08</td>
      <td>5.898240e+05</td>
      <td>0.000000</td>
      <td>0.000000e+00</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>9.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
    </tr>
    <tr>
      <th>25%</th>
      <td>2090.000000</td>
      <td>6.000937e+08</td>
      <td>4.692275e+07</td>
      <td>0.000000</td>
      <td>2.800000e+01</td>
      <td>1.000000</td>
      <td>3.500000</td>
      <td>2.500000</td>
      <td>37.000000</td>
      <td>3.000000</td>
      <td>1.000000</td>
      <td>1.000000</td>
    </tr>
    <tr>
      <th>50%</th>
      <td>4380.000000</td>
      <td>9.781482e+08</td>
      <td>9.715302e+07</td>
      <td>0.000000</td>
      <td>3.000000e+02</td>
      <td>23.000000</td>
      <td>4.000000</td>
      <td>4.000000</td>
      <td>37.000000</td>
      <td>5.000000</td>
      <td>1.000000</td>
      <td>1.000000</td>
    </tr>
    <tr>
      <th>75%</th>
      <td>7223.000000</td>
      <td>1.082310e+09</td>
      <td>1.819249e+08</td>
      <td>1.990000</td>
      <td>2.793000e+03</td>
      <td>140.000000</td>
      <td>4.500000</td>
      <td>4.500000</td>
      <td>38.000000</td>
      <td>5.000000</td>
      <td>8.000000</td>
      <td>1.000000</td>
    </tr>
    <tr>
      <th>max</th>
      <td>11097.000000</td>
      <td>1.188376e+09</td>
      <td>4.025970e+09</td>
      <td>299.990000</td>
      <td>2.974676e+06</td>
      <td>177050.000000</td>
      <td>5.000000</td>
      <td>5.000000</td>
      <td>47.000000</td>
      <td>5.000000</td>
      <td>75.000000</td>
      <td>1.000000</td>
    </tr>
  </tbody>
</table>
</div>




```python
# more to add later
```
