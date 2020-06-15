## We'll explore the fundamentals of geographic coordinate systems and how to work with the basemap library to plot geographic data points on maps. We'll be working with flight data from the openflights website, and answer 2 questions:

### 1. For each airport, which destination airport is the most common?

### 2. Which cities are the most important hubs for airports and airlines?

### Here's a breakdown of the files we'll be working with and the most pertinent columns from each dataset:

#### airlines.csv - data on each airline
- country - where the airline is headquartered.
- active - if the airline is still active.

#### airports.csv - data on each airport
- name - name of the airport.
- city - city the airport is located.
- country - country the airport is located.
- code - unique airport code.
- latitude - latitude value.
- longitude - longitude value.

#### routes.csv - data on each flight route
- airline - airline for the route.
- source - starting city for the route.
- dest - destination city for the route.


```python
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
```


```python
airline = pd.read_csv('airlines.csv')
airports = pd.read_csv('airports.csv')
routes = pd.read_csv('routes.csv')
```


```python
airline
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
      <th>id</th>
      <th>name</th>
      <th>alias</th>
      <th>iata</th>
      <th>icao</th>
      <th>callsign</th>
      <th>country</th>
      <th>active</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1</td>
      <td>Private flight</td>
      <td>\N</td>
      <td>-</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>Y</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2</td>
      <td>135 Airways</td>
      <td>\N</td>
      <td>NaN</td>
      <td>GNL</td>
      <td>GENERAL</td>
      <td>United States</td>
      <td>N</td>
    </tr>
    <tr>
      <th>2</th>
      <td>3</td>
      <td>1Time Airline</td>
      <td>\N</td>
      <td>1T</td>
      <td>RNX</td>
      <td>NEXTIME</td>
      <td>South Africa</td>
      <td>Y</td>
    </tr>
    <tr>
      <th>3</th>
      <td>4</td>
      <td>2 Sqn No 1 Elementary Flying Training School</td>
      <td>\N</td>
      <td>NaN</td>
      <td>WYT</td>
      <td>NaN</td>
      <td>United Kingdom</td>
      <td>N</td>
    </tr>
    <tr>
      <th>4</th>
      <td>5</td>
      <td>213 Flight Unit</td>
      <td>\N</td>
      <td>NaN</td>
      <td>TFU</td>
      <td>NaN</td>
      <td>Russia</td>
      <td>N</td>
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
      <th>6043</th>
      <td>19828</td>
      <td>Vuela Cuba</td>
      <td>Vuela Cuba</td>
      <td>6C</td>
      <td>6CC</td>
      <td>NaN</td>
      <td>Cuba</td>
      <td>Y</td>
    </tr>
    <tr>
      <th>6044</th>
      <td>19830</td>
      <td>All Australia</td>
      <td>All Australia</td>
      <td>88</td>
      <td>8K8</td>
      <td>NaN</td>
      <td>Australia</td>
      <td>Y</td>
    </tr>
    <tr>
      <th>6045</th>
      <td>19831</td>
      <td>Fly Europa</td>
      <td>NaN</td>
      <td>ER</td>
      <td>RWW</td>
      <td>NaN</td>
      <td>Spain</td>
      <td>Y</td>
    </tr>
    <tr>
      <th>6046</th>
      <td>19834</td>
      <td>FlyPortugal</td>
      <td>NaN</td>
      <td>PO</td>
      <td>FPT</td>
      <td>FlyPortugal</td>
      <td>Portugal</td>
      <td>Y</td>
    </tr>
    <tr>
      <th>6047</th>
      <td>19845</td>
      <td>FTI Fluggesellschaft</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>FTI</td>
      <td>NaN</td>
      <td>Germany</td>
      <td>N</td>
    </tr>
  </tbody>
</table>
<p>6048 rows × 8 columns</p>
</div>




```python
airports
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
      <th>id</th>
      <th>name</th>
      <th>city</th>
      <th>country</th>
      <th>code</th>
      <th>icao</th>
      <th>latitude</th>
      <th>longitude</th>
      <th>altitude</th>
      <th>offset</th>
      <th>dst</th>
      <th>timezone</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1</td>
      <td>Goroka</td>
      <td>Goroka</td>
      <td>Papua New Guinea</td>
      <td>GKA</td>
      <td>AYGA</td>
      <td>-6.081689</td>
      <td>145.391881</td>
      <td>5282</td>
      <td>10.0</td>
      <td>U</td>
      <td>Pacific/Port_Moresby</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2</td>
      <td>Madang</td>
      <td>Madang</td>
      <td>Papua New Guinea</td>
      <td>MAG</td>
      <td>AYMD</td>
      <td>-5.207083</td>
      <td>145.788700</td>
      <td>20</td>
      <td>10.0</td>
      <td>U</td>
      <td>Pacific/Port_Moresby</td>
    </tr>
    <tr>
      <th>2</th>
      <td>3</td>
      <td>Mount Hagen</td>
      <td>Mount Hagen</td>
      <td>Papua New Guinea</td>
      <td>HGU</td>
      <td>AYMH</td>
      <td>-5.826789</td>
      <td>144.295861</td>
      <td>5388</td>
      <td>10.0</td>
      <td>U</td>
      <td>Pacific/Port_Moresby</td>
    </tr>
    <tr>
      <th>3</th>
      <td>4</td>
      <td>Nadzab</td>
      <td>Nadzab</td>
      <td>Papua New Guinea</td>
      <td>LAE</td>
      <td>AYNZ</td>
      <td>-6.569828</td>
      <td>146.726242</td>
      <td>239</td>
      <td>10.0</td>
      <td>U</td>
      <td>Pacific/Port_Moresby</td>
    </tr>
    <tr>
      <th>4</th>
      <td>5</td>
      <td>Port Moresby Jacksons Intl</td>
      <td>Port Moresby</td>
      <td>Papua New Guinea</td>
      <td>POM</td>
      <td>AYPY</td>
      <td>-9.443383</td>
      <td>147.220050</td>
      <td>146</td>
      <td>10.0</td>
      <td>U</td>
      <td>Pacific/Port_Moresby</td>
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
    </tr>
    <tr>
      <th>8102</th>
      <td>9537</td>
      <td>Mansons Landing Water Aerodrome</td>
      <td>Mansons Landing</td>
      <td>Canada</td>
      <td>YMU</td>
      <td>\N</td>
      <td>50.066667</td>
      <td>-124.983333</td>
      <td>0</td>
      <td>-8.0</td>
      <td>A</td>
      <td>America/Vancouver</td>
    </tr>
    <tr>
      <th>8103</th>
      <td>9538</td>
      <td>Port McNeill Airport</td>
      <td>Port McNeill</td>
      <td>Canada</td>
      <td>YMP</td>
      <td>\N</td>
      <td>50.575556</td>
      <td>-127.028611</td>
      <td>225</td>
      <td>-8.0</td>
      <td>A</td>
      <td>America/Vancouver</td>
    </tr>
    <tr>
      <th>8104</th>
      <td>9539</td>
      <td>Sullivan Bay Water Aerodrome</td>
      <td>Sullivan Bay</td>
      <td>Canada</td>
      <td>YTG</td>
      <td>\N</td>
      <td>50.883333</td>
      <td>-126.833333</td>
      <td>0</td>
      <td>-8.0</td>
      <td>A</td>
      <td>America/Vancouver</td>
    </tr>
    <tr>
      <th>8105</th>
      <td>9540</td>
      <td>Deer Harbor Seaplane</td>
      <td>Deer Harbor</td>
      <td>United States</td>
      <td>DHB</td>
      <td>\N</td>
      <td>48.618397</td>
      <td>-123.005960</td>
      <td>0</td>
      <td>-8.0</td>
      <td>A</td>
      <td>America/Los_Angeles</td>
    </tr>
    <tr>
      <th>8106</th>
      <td>9541</td>
      <td>San Diego Old Town Transit Center</td>
      <td>San Diego</td>
      <td>United States</td>
      <td>OLT</td>
      <td>\N</td>
      <td>32.755200</td>
      <td>-117.199500</td>
      <td>0</td>
      <td>-8.0</td>
      <td>A</td>
      <td>America/Los_Angeles</td>
    </tr>
  </tbody>
</table>
<p>8107 rows × 12 columns</p>
</div>




```python
routes
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
      <th>airline</th>
      <th>airline_id</th>
      <th>source</th>
      <th>source_id</th>
      <th>dest</th>
      <th>dest_id</th>
      <th>codeshare</th>
      <th>stops</th>
      <th>equipment</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>2B</td>
      <td>410</td>
      <td>AER</td>
      <td>2965</td>
      <td>KZN</td>
      <td>2990</td>
      <td>NaN</td>
      <td>0</td>
      <td>CR2</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2B</td>
      <td>410</td>
      <td>ASF</td>
      <td>2966</td>
      <td>KZN</td>
      <td>2990</td>
      <td>NaN</td>
      <td>0</td>
      <td>CR2</td>
    </tr>
    <tr>
      <th>2</th>
      <td>2B</td>
      <td>410</td>
      <td>ASF</td>
      <td>2966</td>
      <td>MRV</td>
      <td>2962</td>
      <td>NaN</td>
      <td>0</td>
      <td>CR2</td>
    </tr>
    <tr>
      <th>3</th>
      <td>2B</td>
      <td>410</td>
      <td>CEK</td>
      <td>2968</td>
      <td>KZN</td>
      <td>2990</td>
      <td>NaN</td>
      <td>0</td>
      <td>CR2</td>
    </tr>
    <tr>
      <th>4</th>
      <td>2B</td>
      <td>410</td>
      <td>CEK</td>
      <td>2968</td>
      <td>OVB</td>
      <td>4078</td>
      <td>NaN</td>
      <td>0</td>
      <td>CR2</td>
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
    </tr>
    <tr>
      <th>67658</th>
      <td>ZL</td>
      <td>4178</td>
      <td>WYA</td>
      <td>6334</td>
      <td>ADL</td>
      <td>3341</td>
      <td>NaN</td>
      <td>0</td>
      <td>SF3</td>
    </tr>
    <tr>
      <th>67659</th>
      <td>ZM</td>
      <td>19016</td>
      <td>DME</td>
      <td>4029</td>
      <td>FRU</td>
      <td>2912</td>
      <td>NaN</td>
      <td>0</td>
      <td>734</td>
    </tr>
    <tr>
      <th>67660</th>
      <td>ZM</td>
      <td>19016</td>
      <td>FRU</td>
      <td>2912</td>
      <td>DME</td>
      <td>4029</td>
      <td>NaN</td>
      <td>0</td>
      <td>734</td>
    </tr>
    <tr>
      <th>67661</th>
      <td>ZM</td>
      <td>19016</td>
      <td>FRU</td>
      <td>2912</td>
      <td>OSS</td>
      <td>2913</td>
      <td>NaN</td>
      <td>0</td>
      <td>734</td>
    </tr>
    <tr>
      <th>67662</th>
      <td>ZM</td>
      <td>19016</td>
      <td>OSS</td>
      <td>2913</td>
      <td>FRU</td>
      <td>2912</td>
      <td>NaN</td>
      <td>0</td>
      <td>734</td>
    </tr>
  </tbody>
</table>
<p>67663 rows × 9 columns</p>
</div>



### 1. For each airport, which destination airport is the most common?


```python
# make a pivot table that count destinations by sources
countDest = routes.pivot_table(index='source', values='dest_id', columns='dest', aggfunc='count')
countDest
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
      <th>dest</th>
      <th>AAE</th>
      <th>AAL</th>
      <th>AAN</th>
      <th>AAQ</th>
      <th>AAR</th>
      <th>AAT</th>
      <th>AAX</th>
      <th>AAY</th>
      <th>ABA</th>
      <th>ABB</th>
      <th>...</th>
      <th>ZSA</th>
      <th>ZSE</th>
      <th>ZSJ</th>
      <th>ZTB</th>
      <th>ZTH</th>
      <th>ZUH</th>
      <th>ZUM</th>
      <th>ZVK</th>
      <th>ZYI</th>
      <th>ZYL</th>
    </tr>
    <tr>
      <th>source</th>
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
      <th>AAE</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>AAL</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>1.0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>AAN</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>AAQ</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>AAR</th>
      <td>NaN</td>
      <td>1.0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
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
      <th>ZUH</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>ZUM</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>ZVK</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>ZYI</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>ZYL</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
  </tbody>
</table>
<p>3409 rows × 3418 columns</p>
</div>




```python
# a helper function that returns the 1st question result
def mostCommonDest(pivotDf):
    result = {}
    for i in range(0, len(pivotDf)):
        temp = pivotDf.iloc[i, :]
        result[pivotDf.index[i]] = temp[[n for n in temp.index if (temp[n] == temp.max())]].index.to_list()
    return result
```

#### Since the data contains too many rows and columns, we will answer the 1st question with 10 sample rows.


```python
def first10Airports(pivotDf):
    result = {}
    for i in range(0, 11):
        temp = pivotDf.iloc[i, :]
        result[pivotDf.index[i]] = temp[[n for n in temp.index if (temp[n] == temp.max())]].index.to_list()
    return result
```


```python
first10Airports(countDest)
```




    {'AAE': ['MRS', 'ORY'],
     'AAL': ['BLL', 'OSL'],
     'AAN': ['CCJ', 'PEW'],
     'AAQ': ['DME', 'LED', 'SVO'],
     'AAR': ['AAL', 'AGP', 'BMA', 'CPH', 'GOT', 'OSL', 'PMI', 'STN'],
     'AAT': ['URC'],
     'AAX': ['POJ'],
     'AAY': ['SAH'],
     'ABA': ['DME', 'IKT', 'NSK', 'SVO'],
     'ABB': ['ABV', 'LOS'],
     'ABD': ['THR']}



### 2.1. Which cities are the most important hubs for airports?


```python
airports.groupby('city').count().max(axis=1).sort_values(ascending=False)[:11]
```




    city
    London       21
    New York     13
    Hong Kong    12
    Berlin       10
    Paris        10
    Chicago       9
    Seattle       9
    Moscow        9
    Glasgow       8
    Beijing       8
    San Diego     8
    dtype: int64



### 2.2. Which cities are the most important hubs for airlines?


```python
# top 10 source airports
source = routes.groupby('source').count().sort_values(by='airline_id', ascending=False).max(axis=1)[0:11]
source
```




    source
    ATL    915
    ORD    558
    PEK    535
    LHR    527
    CDG    524
    FRA    497
    LAX    492
    DFW    469
    JFK    456
    AMS    453
    PVG    411
    dtype: int64




```python
# top 10 destination airport
dest = routes.groupby('dest').count().sort_values(by='airline_id', ascending=False).max(axis=1)[0:11]
dest
```




    dest
    ATL    911
    ORD    550
    PEK    534
    LHR    524
    CDG    517
    LAX    498
    FRA    493
    DFW    467
    JFK    455
    AMS    450
    PVG    414
    dtype: int64




```python
# filter cities that is in both source and destination lists
airports[airports['code'].isin(np.intersect1d(source.index, dest.index))]['city']
```




    337             Frankfurt
    503                London
    575             Amsterdam
    1358                Paris
    3268              Beijing
    3307             Shanghai
    3385          Los Angeles
    3571    Dallas-Fort Worth
    3583              Atlanta
    3698             New York
    3731              Chicago
    Name: city, dtype: object



### We create a visualization on world airports.


```python
import os
os.environ["PROJ_LIB"] = "/Users/MimiHMB/anaconda3/pkgs/proj4-5.2.0-h0a44026_1/share/proj"
```


```python
from mpl_toolkits.basemap import Basemap
```


```python
m = Basemap(projection='merc',llcrnrlat=-80,urcrnrlat=80,llcrnrlon=-180,urcrnrlon=180)
```

    /Users/MimiHMB/anaconda3/lib/python3.7/site-packages/ipykernel_launcher.py:1: MatplotlibDeprecationWarning: 
    The dedent function was deprecated in Matplotlib 3.1 and will be removed in 3.3. Use inspect.cleandoc instead.
      """Entry point for launching an IPython kernel.



```python
longitudes = airports["longitude"].tolist()
latitudes = airports["latitude"].tolist()
x, y = m(longitudes, latitudes)
```


```python
x
```




    [36181909.30105094,
     36226033.53986971,
     36060037.49493744,
     36330283.404696316,
     36385192.32317709,
     35990354.44709509,
     14963941.458273921,
     14268741.541486904,
     14378684.250292266,
     12375638.020887403,
     18005485.43317323,
     18413716.731862824,
     18321888.33524768,
     18077397.938244995,
     17442553.042491462,
     17501455.413687292,
     17350292.20901023,
     17575400.005086605,
     17911640.962292437,
     17760170.414982848,
     10618060.258599434,
     9225560.732214285,
     12954264.67851546,
     13778929.009821879,
     6029820.04527255,
     10028881.874571005,
     12431092.795006035,
     12120642.599331541,
     9331720.924981104,
     6085602.844270321,
     8900933.52365312,
     8324233.650806665,
     6241349.72405515,
     6934946.3219498545,
     12737465.474640507,
     12639490.447764657,
     7211667.109238329,
     7622933.694411267,
     6456097.827279047,
     12396375.19777225,
     10745934.475221692,
     4544781.58702558,
     4554480.226350438,
     6614828.621515303,
     13633449.197559252,
     5556160.792994859,
     8889752.211874548,
     6651343.795086775,
     7385594.462163575,
     9554882.921952376,
     8565804.515190138,
     7064766.337677218,
     10472981.859832976,
     5172476.6523626065,
     12392020.25052089,
     12616479.335700689,
     12331820.457531905,
     8708597.192120796,
     7373363.025992259,
     6534197.215156006,
     11497889.812571848,
     11374772.290281741,
     12845386.327046752,
     10347856.71408766,
     13145674.200770618,
     8638575.222301625,
     9702401.381040135,
     6915641.668630414,
     9357079.583230972,
     11126715.095296621,
     11851489.512797134,
     7140625.927201462,
     12953245.466297766,
     9825333.54147481,
     11345583.63578201,
     11866593.446155846,
     13504617.593069404,
     6622272.562374291,
     11077387.825920321,
     12586672.882479435,
     7874728.371510841,
     11189540.199267467,
     10747355.212130425,
     7947900.714508248,
     7775579.571542042,
     13089798.776442565,
     6740880.354148033,
     4907215.164038412,
     8277439.067081948,
     7647767.290464763,
     11051905.630165124,
     11565317.049999585,
     11786069.787629731,
     13144438.71452244,
     11612793.591888294,
     11363807.252533654,
     4465678.776603075,
     7752568.459478075,
     6986960.837852993,
     11601053.859451067,
     8264806.106219589,
     6955548.285867571,
     9087524.6384209,
     6370354.347769385,
     9983724.412980378,
     12866513.35316084,
     11301476.409779005,
     5510292.907352429,
     7659411.840089602,
     11196953.227951404,
     12076504.683543233,
     7350598.988938953,
     10790844.750606783,
     5690675.678704272,
     9522389.222204283,
     7472326.464105627,
     12823147.352189815,
     6128320.1343447715,
     8376773.228906179,
     10082718.763268795,
     6795674.7419082895,
     8621865.190178746,
     7978942.765172553,
     13947389.244363168,
     13338072.134263294,
     6392562.41045127,
     9454961.984776543,
     12277612.956318123,
     11979517.956710024,
     7238322.966891602,
     9772268.901178926,
     11030655.066545703,
     12043362.384093437,
     12688416.192449918,
     7565483.0834941,
     10606477.533324696,
     12917107.020960372,
     6088753.328643429,
     11505704.254751952,
     9133083.735897442,
     11394354.930786889,
     10966409.11447125,
     11186630.562992059,
     5223224.769842518,
     11815474.716159943,
     10427330.248221029,
     10981204.259664072,
     11248967.632659668,
     8310488.741201462,
     7692028.854953278,
     12895115.121114094,
     11366031.150019346,
     12406351.935477694,
     5915765.350016141,
     6317598.606834264,
     7959607.08848319,
     10996370.017372886,
     11417582.205686469,
     9202500.472015884,
     12580093.926547509,
     6443279.615756131,
     6289552.70205756,
     7140718.663726617,
     7392173.418095503,
     8150615.197242183,
     7703488.265112432,
     6589377.337935155,
     9795681.537933936,
     12708060.65730517,
     11136290.19711615,
     6373813.7315032575,
     5718060.863537978,
     10991489.785535404,
     6409210.72941892,
     4996289.374812399,
     11183671.556192469,
     7336606.893128213,
     5873004.360356097,
     6382925.595476515,
     6715923.331784083,
     12996333.368888207,
     9609831.648198139,
     6290757.387325557,
     8775932.026608007,
     8040439.535175194,
     9555531.521654077,
     13296034.467260472,
     14149331.478695197,
     10845114.076170668,
     10128772.121961536,
     12430691.159120118,
     11160567.707603348,
     11178914.86186032,
     10833963.676567147,
     7289905.045928646,
     7252438.60020767,
     5358054.781825651,
     10862750.806375833,
     5852556.846118762,
     7140193.49033537,
     12646687.202418111,
     5254760.859333268,
     12796645.944216924,
     5184368.388192981,
     5019274.800860406,
     20327998.31702371,
     20482806.267290078,
     20578826.71066575,
     20372614.25957657,
     21066140.693505604,
     20334886.172316402,
     20046839.85349741,
     20973872.187578045,
     20335175.612574164,
     20621208.970583983,
     20668192.47440011,
     19988128.959875096,
     20084715.60755063,
     20883416.714075692,
     20751230.360228676,
     20918059.477159087,
     20383303.867621053,
     20177771.81796762,
     19925522.242637347,
     19106937.37988757,
     20163163.924943093,
     19955890.785948113,
     19853844.803529825,
     19946005.00564983,
     19949108.232201368,
     20031438.80743461,
     19994349.089947708,
     20653139.245904073,
     20333048.677018847,
     20436963.400494363,
     20697863.269874737,
     20294400.785758592,
     20692106.48884327,
     20340694.214184914,
     20045770.825976036,
     20616950.5404835,
     21087319.647625983,
     20280205.203327917,
     19846904.353061598,
     19533495.81775676,
     19996531.622940168,
     19919092.399031837,
     19736234.652168166,
     19756131.640582915,
     19817733.60093663,
     19578493.603507914,
     19450911.60701528,
     19295291.934166633,
     19397204.816320397,
     19171401.385110497,
     19274428.662294343,
     19418452.26648334,
     20822704.86869063,
     20604522.2893847,
     20637713.403384306,
     20943242.89228708,
     20855928.673983276,
     20759650.592083883,
     20457447.609040212,
     20514778.129493155,
     21001270.271017164,
     20829036.527222145,
     20962971.642857037,
     21469611.962016813,
     20972903.235443525,
     20384372.89514243,
     20733647.114758037,
     20787836.602402184,
     20594090.097474188,
     21397276.582838148,
     20869699.603189062,
     20807535.775135588,
     20257884.055458885,
     20600558.19211645,
     20904649.04173573,
     21446005.290206175,
     21419100.133644756,
     21014025.54624123,
     21210947.33199931,
     21152291.479839765,
     21103836.756641977,
     21169514.565112595,
     20996094.483203836,
     21138516.214033883,
     21120704.351901717,
     21213253.402497098,
     21044143.567500234,
     21203858.65876366,
     20916929.62604148,
     20136418.77780577,
     20154572.564176362,
     20511037.42272734,
     20545291.55972511,
     20623313.33357982,
     20513724.558059305,
     20595947.05187474,
     20510318.992644586,
     20441064.934627224,
     20310052.68745778,
     20531670.187625237,
     20371426.031149965,
     20620335.757236224,
     20333341.78670746,
     20636718.542844083,
     20593476.079378385,
     20615993.041421033,
     20401408.50585721,
     20566625.51950024,
     20543623.63661084,
     21629598.813552987,
     21405720.610396452,
     21369879.38895802,
     21636928.779665835,
     10361827.171375861,
     21522320.88990986,
     21342836.795531984,
     21355272.163102735,
     21500196.112188812,
     21433161.059082676,
     21562429.993013088,
     21478224.894589156,
     21427219.472170148,
     21317671.838753123,
     21396710.712122913,
     21307880.907682605,
     21677440.741798595,
     21535014.67436845,
     21630959.727619357,
     21586149.75001087,
     21518710.058757216,
     21545915.107894577,
     21233562.590310823,
     20965029.08161593,
     20869591.188186634,
     21125717.128029343,
     21505527.239241518,
     20809313.892370272,
     20767508.066680335,
     21325629.722321056,
     21245659.59187913,
     21376284.213716816,
     20805618.21952855,
     21040512.49888047,
     21492602.725418787,
     21092008.401889943,
     20992109.703688968,
     20975967.877373684,
     20822784.929000113,
     20961819.886349197,
     20980342.17253317,
     20945600.557206538,
     20921130.568391953,
     21179589.15430741,
     20913862.093044586,
     21108904.12945288,
     21143167.94040471,
     21206999.9139622,
     20740966.739747576,
     20860374.5786418,
     20893442.711110447,
     20786473.24204858,
     20965219.00246121,
     20738343.763858076,
     20973167.656854574,
     20775724.47833098,
     20861519.663457185,
     21230633.494932413,
     21100654.35933995,
     21429883.92374776,
     21185329.256107736,
     21269696.587853245,
     21407035.48978487,
     21482367.90441013,
     21128646.4457975,
     21072705.861273117,
     21325335.0559042,
     21329215.42343211,
     21156455.72788173,
     21309226.5880512,
     21253028.476197977,
     21333283.59910269,
     21185903.800023165,
     20852226.55183884,
     20769886.747431032,
     20954806.93682294,
     20837991.384032916,
     20962704.88635363,
     20886020.453251943,
     21057288.358368926,
     21103003.128669463,
     21542672.55416556,
     21188862.80682275,
     21057821.871375743,
     21120984.562984917,
     20968337.462710522,
     20818728.09520671,
     20842627.876705963,
     20910566.72175029,
     20761102.352362543,
     20819043.777454805,
     21057886.697987452,
     21082637.4538596,
     20942495.106757518,
     22706934.815932468,
     22553737.857004736,
     22518017.726784397,
     22736329.40333937,
     22776362.337953713,
     22982916.157306947,
     22619741.911236502,
     22483758.030042917,
     22771220.24218729,
     22799711.482435506,
     22790872.045904245,
     22580759.43459953,
     22581853.480967615,
     22781729.380950812,
     22645114.135261033,
     23229021.882248368,
     23359108.765674017,
     23062409.372933064,
     23307285.171370026,
     22870367.485427853,
     22578279.566513233,
     22750371.203258913,
     23094331.864611957,
     22505070.306817565,
     22588474.913341522,
     23034772.776488602,
     23266346.665699508,
     22777919.733362943,
     23106045.355058853,
     22872063.763235062,
     23144590.05747577,
     22227650.326159585,
     22630257.276912984,
     23039777.43539041,
     22716711.291669324,
     22834374.92776552,
     22482864.801617786,
     22439123.7403358,
     23011439.421678957,
     22897949.70757879,
     22761127.41703309,
     23168174.156726927,
     22887286.67510926,
     22695738.715235613,
     23233628.12991561,
     22994973.351110257,
     22974988.518744823,
     22639764.772248946,
     22686757.282849893,
     22490587.508026607,
     23010484.146513976,
     22434919.684528846,
     23113924.067876294,
     22763364.6579037,
     19323908.60223304,
     19164251.221109368,
     19362085.47200582,
     19218798.533858966,
     19820705.617536508,
     19850539.869476333,
     19900330.48789378,
     19774093.393405616,
     19763838.779709335,
     19786355.741751984,
     19893257.159550786,
     19835559.473622955,
     19762114.59198868,
     19776131.92903588,
     19553580.9478988,
     19459613.60668192,
     19793418.39538705,
     19820773.891189322,
     19430669.247321,
     19633039.58191902,
     19721654.224277582,
     19463427.257285263,
     19643315.878615785,
     19562755.192196533,
     19712728.61171875,
     19698202.89170632,
     19974120.62961271,
     19558529.78697372,
     19810200.815373085,
     19864207.832228534,
     19900157.468669392,
     19768811.636877097,
     19725751.755394977,
     19770948.1351916,
     19982027.80831797,
     20018691.204656865,
     19993919.43295347,
     20021224.00150332,
     19928753.120904565,
     19894894.281684875,
     19920839.715286344,
     19963773.279391278,
     20092419.63322057,
     20119507.927739933,
     20164758.01466084,
     19952104.04450435,
     19702712.399832938,
     19909287.790991783,
     19678311.35184041,
     19976066.539912697,
     19652174.32947055,
     19830430.610046573,
     19694495.765792545,
     19683963.720884923,
     19500924.615181293,
     19826972.67184607,
     19856134.750770845,
     19867404.351279594,
     19556556.96751416,
     19733358.37435504,
     19718404.776466362,
     19675318.986578535,
     19692056.26144561,
     19871018.184693847,
     19671145.398167133,
     19770695.722826973,
     19565016.117575362,
     19522144.26662566,
     19640072.657717526,
     19319368.0707365,
     19505063.510791916,
     19196374.1971466,
     19870956.471538622,
     19678620.25120117,
     19311090.27951525,
     19251261.21023713,
     19696121.101269964,
     19643778.89407231,
     20034536.474242434,
     19987155.11516611,
     20157715.70968777,
     20041208.166699514,
     20032219.951426458,
     19860684.84502657,
     19946507.1617021,
     19635470.413065754,
     19726990.021515008,
     19868300.137186833,
     19893226.35857061,
     20077457.695716318,
     20069163.225263927,
     20121409.02650558,
     20003086.894363873,
     19816035.432816554,
     19838987.27801253,
     19910240.06389516,
     19758708.915379085,
     19968579.34424761,
     19996617.465383116,
     19857152.51745517,
     19844348.76126591,
     19882143.899035275,
     20101024.226177342,
     19942937.583847817,
     19953827.565055758,
     19962098.239805054,
     19875778.3260671,
     19956832.27294868,
     19861395.602663,
     19961343.337803535,
     19952627.54997248,
     20076311.49895219,
     13516045.86866376,
     20544797.409703787,
     20637923.11691721,
     20656687.807927117,
     20668131.094829503,
     20696671.038432654,
     20612697.33654211,
     20746677.819685712,
     20563471.921670657,
     20546658.367119815,
     20629676.126676135,
     20655621.67147248,
     20508473.713705834,
     20601762.654994704,
     20779449.506619517,
     20506330.098919373,
     20497888.9624278,
     19070909.35106034,
     19020818.1728977,
     19317877.16986209,
     19034506.261922147,
     18956081.517843027,
     19297722.209338997,
     19022683.466913827,
     19058889.741124537,
     19227043.300202552,
     21195856.630830638,
     21032708.175433923,
     21422356.586733058,
     20966171.94253383,
     21391916.989897627,
     21029689.234597094,
     21238230.21754867,
     21287159.742859654,
     21163824.167421076,
     21046856.16645841,
     21364029.982596274,
     21656264.567550074,
     21103867.66881703,
     21045179.014169574,
     21035066.062743127,
     20983053.770737477,
     21052628.403577402,
     19205887.919395518,
     21066826.432295315,
     20943988.898698654,
     21110253.92403182,
     20705766.22317477,
     20694496.2890814,
     21810225.991238512,
     22613886.945131045,
     20738010.512819845,
     21373600.747815706,
     21612422.652517106,
     20595308.014932226,
     23316731.175940506,
     20914128.960742872,
     20961654.65076601,
     22076669.92585585,
     21869597.493608948,
     21047861.59051169,
     20573800.702348083,
     21249380.617152188,
     20594220.75145147,
     22476903.422017638,
     20885124.111370336,
     21242233.900192164,
     23338836.160973933,
     20751860.167996623,
     20822630.145735107,
     21484508.072155487,
     22792001.34104748,
     21039429.238415185,
     21082993.277457315,
     21276288.22000084,
     21214357.345208995,
     21734767.926405307,
     21078872.5066112,
     20608952.51556595,
     21401560.031785343,
     22118764.191049676,
     21155784.222035922,
     21229797.97664704,
     20641978.060397748,
     22340278.61356867,
     22068426.605045624,
     22215049.723005645,
     22131580.73464948,
     22136677.68529694,
     22401556.329668973,
     21886078.4642908,
     22463477.30811701,
     21672126.293977033,
     21917343.6830678,
     21774875.25039055,
     22346513.866144184,
     21892695.782454353,
     21771795.819542106,
     21741453.740611423,
     21805714.25921441,
     21970837.424383543,
     21712467.127198268,
     21466529.751296517,
     21380530.301186252,
     21579448.14613261,
     21525976.310207095,
     21480004.67974696,
     21335001.893495012,
     21568766.877703696,
     21387778.094287,
     21628194.644680522,
     21428852.257704146,
     22004430.841438312,
     21626949.59567316,
     21628668.779624473,
     21895626.10097638,
     21420518.53546113,
     21750246.80888011,
     21563095.38314081,
     21581316.775994964,
     21446093.578936357,
     21849567.293734804,
     21527265.281189803,
     21826172.55935455,
     21501935.088827755,
     21440619.121690698,
     21587063.994267244,
     21652754.81253815,
     21733964.765828352,
     21543697.993296213,
     21618835.483306855,
     22329558.20454401,
     21914365.773139577,
     22255340.62972833,
     21990883.080345213,
     22096224.990032174,
     21661070.410016656,
     21954752.752233643,
     22126672.370508805,
     22379173.02386521,
     22276421.287579846,
     21651039.409212563,
     22358719.727494415,
     21905714.58953048,
     22270416.097199224,
     21886884.627129365,
     22159130.710286874,
     21687220.99816118,
     21864649.655287903,
     22474929.157024715,
     22255644.858904373,
     21785750.665069964,
     22007535.068743717,
     22010096.887452364,
     21740289.307887916,
     21774550.894942258,
     21899984.94004834,
     21758669.48702255,
     21822063.241580486,
     21872965.80874078,
     22055081.99698785,
     22267577.292058736,
     20759249.06739284,
     20860189.88395561,
     21228684.137591332,
     21123300.418631643,
     21024967.789040092,
     21129487.190241966,
     20836473.907583553,
     21047614.404306155,
     21117020.688106414,
     20828504.904528193,
     21122374.498913474,
     21249359.04534658,
     21148990.21521713,
     21342763.629304707,
     21011559.799903974,
     21331192.245907143,
     21149326.913296465,
     20977858.190236524,
     20942555.374379378,
     20686963.7259076,
     21075672.651713904,
     20892256.706581324,
     21380365.065603066,
     20755431.413774025,
     21073244.822828777,
     20867645.5002764,
     21494636.36847458,
     21063330.020668305,
     21323532.142212547,
     20956163.18070459,
     20940818.844027676,
     21227768.670191348,
     20800483.796208452,
     21343707.89617713,
     21267910.019808114,
     21479254.447930157,
     21297599.051242124,
     21222783.47039254,
     21261738.704285316,
     20938699.02494431,
     21853499.255684383,
     22107083.169506073,
     23162089.0172317,
     23048374.689485475,
     22939774.32520248,
     23165909.228332624,
     22976107.250375,
     22083487.394793116,
     22208496.008310184,
     23456616.44049325,
     23109179.16020082,
     23348673.46030702,
     23118403.99816635,
     23144107.916500874,
     22503495.120228447,
     22743954.03586907,
     22961528.379212663,
     23416162.299695116,
     23001902.682091057,
     23251538.288316645,
     23467538.557019863,
     22853691.923716,
     23155887.79028772,
     22985982.35596535,
     22768837.002446745,
     23098029.427766543,
     23052449.981628012,
     22618303.716732506,
     21915843.219434198,
     23120320.2194349,
     22926667.89656542,
     23317180.848012116,
     22034407.200427473,
     23323093.969036825,
     23288672.038973764,
     23389065.554365303,
     23271210.440695595,
     23326297.04858547,
     14462194.380751919,
     23525035.647394482,
     23007217.79708186,
     23578236.501411363,
     23348354.33101783,
     23176897.394614562,
     22266849.299216792,
     22482377.990458168,
     22863587.04438372,
     22609006.713293564,
     23479397.045582827,
     23293593.9688891,
     23297526.264423303,
     23395253.3267295,
     23036615.49794525,
     23290723.917988937,
     23026445.83713292,
     23073316.366956778,
     23004240.887907512,
     23583555.619417645,
     23047486.020050194,
     22228169.828612246,
     22009870.1611037,
     23258647.86618866,
     22013174.872767437,
     23172734.70330084,
     23146839.974562045,
     22572479.197091047,
     22291749.167415366,
     23527582.343600225,
     22571800.90835791,
     22923664.411816116,
     23277399.10261878,
     23387540.73905424,
     23508433.251909908,
     22379106.974109888,
     23203511.331800226,
     22764788.28587917,
     23468612.9218952,
     22077162.852733552,
     23124170.119567256,
     23153467.189069413,
     23261080.25406364,
     23153274.710742027,
     22980598.633737106,
     22071993.18063831,
     22910851.315257415,
     23070103.72464894,
     22760586.78755432,
     22813007.275943473,
     22620494.033366166,
     22897049.25148683,
     23109493.619305298,
     21711136.235747956,
     21788646.06840146,
     21798411.535845764,
     21336806.03033028,
     23496313.010612883,
     22074271.452417526,
     21770440.687609203,
     21105418.837313298,
     20983442.06323848,
     18414575.712266672,
     26429198.02153045,
     27060493.910481434,
     28066819.309414472,
     21055920.105440848,
     21095833.83914996,
     21600422.83526893,
     21210513.116015226,
     21522795.580828182,
     21501764.29350085,
     21166453.92619791,
     21140662.94227682,
     21296427.168462038,
     23116741.634795792,
     22886428.361874655,
     23178863.764771413,
     23566261.48062015,
     22590607.07505593,
     23202472.215700038,
     23145197.29268424,
     24826685.292058192,
     24881676.717135683,
     24955496.659080923,
     25050105.038748056,
     26187539.090806544,
     26177895.492944457,
     25294477.235599376,
     25068976.921616778,
     25554342.770259157,
     25507274.202364203,
     24942968.888569638,
     25496066.98217992,
     25549663.578754384,
     25532628.857598595,
     25462289.42641334,
     25610429.35365348,
     25326165.217288405,
     25169163.058567777,
     25387437.92961936,
     24961179.71791074,
     25540165.201398112,
     25594249.165106565,
     25575129.87364256,
     25351752.38100493,
     25422788.670467325,
     25236356.230785146,
     25253660.9330957,
     25332484.53318888,
     25354840.596248437,
     25392274.350676373,
     24838214.310208656,
     24877457.205241203,
     21599273.525048323,
     21505501.330835808,
     21370359.75081493,
     12753674.017880363,
     21767569.413565423,
     21899542.94042306,
     21520280.686356485,
     21486316.54559085,
     21828933.30569329,
     21985431.974023156,
     21714994.36430101,
     21545733.52666487,
     22286997.143267933,
     21390754.113902356,
     21524550.235944394,
     22227596.507840432,
     21686094.14930518,
     21679146.91594962,
     21302865.35168312,
     21535459.676255338,
     21154349.140988406,
     21293061.74439694,
     20988519.88836756,
     21045041.466110084,
     21448480.265718002,
     21061674.996159453,
     21509318.094895635,
     20839225.091163103,
     20761434.38025716,
     23896618.67224808,
     23952325.969926216,
     23936504.94082324,
     24537565.05314336,
     23636984.200537067,
     24414295.972239602,
     24502332.623641636,
     24190674.740437537,
     24542070.89183912,
     24383012.183918603,
     24520970.77488461,
     24114732.977901194,
     23659288.002005707,
     23755693.06845153,
     23834884.72357859,
     23941734.991735224,
     25877965.77791066,
     25981332.199461076,
     25705599.489825495,
     26188821.27890192,
     26207677.48329337,
     26272929.08181085,
     22332860.358725645,
     21802136.786524046,
     21686783.22394112,
     22140131.286897346,
     23197237.716993086,
     23453746.16720334,
     23526450.26858513,
     22888242.395053737,
     23472442.58456044,
     23226939.202253018,
     23593829.025047682,
     23643057.442180745,
     23446452.339424632,
     23360734.101151437,
     23335568.81078795,
     23019678.7394737,
     23904008.461203292,
     23783807.691660546,
     23736613.80714227,
     23771351.419453427,
     23797012.527761348,
     ...]




```python
y
```




    [14843790.192350345,
     14941516.685582709,
     14872287.531036133,
     14789178.97017778,
     14466473.84037962,
     15122552.886919565,
     24174392.55652002,
     24909208.418908745,
     25670836.580797005,
     29132177.638374515,
     25294767.18348091,
     25193877.732250288,
     24935982.642348204,
     25374085.01630189,
     25402995.181388423,
     24856810.089322105,
     25266721.698466446,
     24893665.95811821,
     25423652.167509183,
     24716067.102691557,
     21373172.654869538,
     21970136.238559585,
     21080066.728274092,
     22204745.27711054,
     21803100.56078986,
     26117120.632400736,
     21811640.55978199,
     21676442.87918321,
     24936837.17348397,
     21951874.708475612,
     21944821.44417497,
     26293677.97204072,
     21798027.84435041,
     21839538.309218578,
     21458006.760857787,
     21619811.601342507,
     25902414.07000827,
     22327386.685411442,
     21815087.51223622,
     26737554.714404903,
     24909824.217430063,
     24871543.66537013,
     24223102.34674608,
     21868859.707960602,
     21824963.133896615,
     23568838.567773383,
     22153033.618167985,
     23020203.781412207,
     22553929.87422569,
     24159113.128538497,
     21824868.667437833,
     22604181.21769969,
     31039253.73657827,
     26047503.784888983,
     24799088.681230426,
     21274232.411735516,
     21746231.044822615,
     22812776.932398766,
     24179077.156255126,
     24313955.99732604,
     21015529.67467569,
     22612874.20906271,
     21751150.938807614,
     21922117.8794007,
     21526263.534234338,
     22462694.901526652,
     21931307.005191695,
     26830286.168422252,
     26147913.633313604,
     20853774.849584848,
     21218294.216642663,
     24100814.718330607,
     21117824.821532402,
     21750916.40854936,
     27511863.15040148,
     21182966.815228008,
     21712245.157646287,
     22082751.19190901,
     20897671.46044981,
     22837283.156515308,
     22227150.12086974,
     20959367.11915773,
     21591474.77010221,
     22707181.313888155,
     22553826.215191264,
     32897712.345492743,
     21952787.205039732,
     24763970.2823456,
     22017707.636355966,
     23202298.75674596,
     22186796.60675764,
     21338966.79740969,
     21244428.58386586,
     21993308.859496363,
     21218959.80023,
     21919248.728662632,
     25830313.211409993,
     22760437.848629184,
     23611250.520204306,
     21187402.501964062,
     22536166.421783887,
     23116531.391793817,
     21943622.54125599,
     21825861.38418314,
     22214452.97214698,
     21932121.050117917,
     21016262.569293227,
     22737758.205024153,
     23642458.941572595,
     21132570.605845183,
     21422747.01829667,
     22346807.774014056,
     20717838.724986307,
     23937580.490473144,
     21923840.36020616,
     21896662.433891725,
     21313176.328043308,
     21910502.91613086,
     22035435.618749678,
     21683368.107128613,
     22909860.83777692,
     22182105.592904054,
     22453960.542177707,
     21778472.755993366,
     21321066.084917158,
     22501323.174832404,
     28318581.754157282,
     21582279.550096434,
     21708187.102168906,
     22391817.290735245,
     24565332.619548492,
     21395810.630438633,
     21205783.841764383,
     21186392.16443058,
     23916162.112107564,
     27624464.69493795,
     21365998.043257315,
     27259145.236578044,
     24919196.023048516,
     23031823.18139815,
     20999036.399387605,
     21716538.22256021,
     20923238.941098996,
     26395866.845181793,
     21210847.633581694,
     25531123.286075015,
     26190950.331485875,
     21655654.639452565,
     22904345.546911165,
     22562515.75009104,
     25823111.88034367,
     21630202.184881754,
     23499909.273658577,
     25193421.406257335,
     21822079.57633201,
     23039905.492557935,
     21096664.595211044,
     21287549.96508588,
     21944827.660135232,
     22482088.040899444,
     22346959.020955965,
     24662863.60342637,
     21893563.300322123,
     22602984.922028583,
     22344742.82971609,
     21963644.25778848,
     23118754.3923961,
     21980100.736859843,
     25426859.23211953,
     21570799.489868015,
     22662559.134788156,
     22772579.976576418,
     20832368.844612777,
     21793438.73923045,
     24071169.522972938,
     21353590.885610517,
     22155345.488341685,
     22841035.333305113,
     23657306.25235174,
     21868004.23781823,
     21341737.83151125,
     26431834.678065598,
     21729524.86522065,
     23245009.624040943,
     22011033.003616344,
     23636444.81062242,
     22555687.817295924,
     21558188.804238565,
     21859596.70336967,
     22010743.219324943,
     21723076.065273013,
     20930880.59769693,
     20940922.081762936,
     21276849.851673238,
     24480993.49809886,
     22931962.466558654,
     22543628.27507392,
     20827257.130349103,
     22078948.25744908,
     22710713.688042417,
     21999100.017881446,
     23950176.144761957,
     21134098.87793293,
     24419856.596520998,
     25782956.338402852,
     19886565.00587111,
     19725763.23502454,
     19915430.351868086,
     19912520.251280762,
     18307317.857648917,
     19892407.164075207,
     18605159.627023164,
     18606831.833453275,
     19752088.896439973,
     18127629.29759997,
     19926968.596018575,
     19483523.24071125,
     19783123.252901226,
     19930730.780924,
     19855128.552636422,
     19739280.362268794,
     19403039.516519394,
     19726940.384877168,
     19780814.790478606,
     18728971.27361294,
     19846391.548454847,
     19754415.89944401,
     19682798.864044957,
     19765547.25774234,
     19703878.138685986,
     19708769.50070569,
     18746215.00978165,
     19652511.75984451,
     19094509.580922782,
     19330883.693322875,
     19237610.693409562,
     18672653.372698303,
     19421252.765828542,
     19514049.75593356,
     18923364.33801758,
     19269565.38031749,
     18773146.582427274,
     16229662.360519823,
     16905695.590613592,
     16770179.283745682,
     16145580.802095536,
     16588989.717749253,
     16648288.536204284,
     16342175.57821,
     16066396.406302609,
     16107179.413262228,
     16384459.619253218,
     16278417.416036831,
     16569824.271740476,
     16332112.894112227,
     16049731.703082496,
     16290776.94610849,
     16526975.829696938,
     16329273.568522684,
     16225159.586948873,
     16075320.980674408,
     16242759.077299874,
     16885039.4404131,
     16342246.213293253,
     16463237.315398537,
     16598308.883055001,
     16717628.306821462,
     16870928.6055399,
     16849078.635660864,
     16380541.503083372,
     16254297.69857468,
     16599701.156790432,
     16079727.13674927,
     16969866.768492226,
     16555217.15419931,
     16766794.72978499,
     17036822.069016486,
     17034422.534232177,
     17194315.68602041,
     17436037.714341406,
     17670159.629558586,
     17022001.350786917,
     17068455.987897124,
     19783920.299674325,
     19934733.166130356,
     19989682.96273255,
     19320624.194741275,
     19602353.686499186,
     19529111.95204333,
     19916726.235406794,
     19528859.092166103,
     19241702.052420676,
     19642315.715722833,
     19537526.350342356,
     16612692.576998249,
     16208227.6559773,
     22168739.34198696,
     22092656.965877358,
     22164994.775043193,
     22117792.684190117,
     21941656.56900686,
     22040194.32145507,
     22060591.41363859,
     22151164.622417655,
     22002576.690486256,
     22102966.092846543,
     22071381.489802256,
     22170415.205752138,
     22125926.81735921,
     22098518.41958707,
     21966576.8715882,
     22160704.404262513,
     22205251.20237939,
     22182105.770610265,
     22169464.47242439,
     22131985.688340846,
     22283512.61294165,
     22349548.61275817,
     20328762.17274632,
     22189819.90795599,
     22199589.08922933,
     22233317.287311435,
     22187221.40188762,
     22553314.63951261,
     22419265.74703156,
     22350623.545748476,
     22747561.10551695,
     22120221.266387217,
     22481514.291673556,
     22327143.721988987,
     22199618.829859108,
     22651860.203609224,
     22293891.983811997,
     22187710.41485801,
     22382754.971363325,
     22158690.12459739,
     22131631.393876545,
     21964947.64860636,
     22338183.774057727,
     22613832.540178888,
     22399718.17584099,
     22111540.786310565,
     22186501.80588364,
     21680328.707018994,
     21874104.62170208,
     22211966.10573999,
     21825596.34186344,
     21736753.707104713,
     22415553.360441945,
     22397533.584934644,
     22505278.319768645,
     21953603.179219503,
     21951501.443260506,
     21869655.373552687,
     22141362.74639923,
     21892583.302734107,
     21955003.017964724,
     22133925.218436807,
     22083705.623982243,
     22596131.61697171,
     22755568.048332483,
     22646711.81086691,
     22030888.48739538,
     22152787.663976006,
     22221047.0832853,
     22206596.806308944,
     22307480.326003805,
     22176001.00068176,
     22244428.014431097,
     22313078.777227838,
     22227295.57642085,
     21692280.176179856,
     21639800.47772426,
     21687423.722931918,
     21639439.600161042,
     21634866.4165126,
     21772382.069507726,
     21727543.035359282,
     21597955.032519944,
     21566887.856849905,
     22575785.03593578,
     22428017.471925724,
     21751582.05273193,
     21957682.521501787,
     21924787.51452992,
     22010492.081140857,
     21963490.2389115,
     22016875.407750502,
     21936796.365576558,
     21840627.401973218,
     21824740.501127053,
     21616904.16130473,
     21625100.08100985,
     21630285.36037393,
     21809230.6216332,
     22243248.203022547,
     22371681.02843538,
     22207677.192942094,
     22346374.54157831,
     22590744.142484903,
     22569104.920547634,
     22546836.724175386,
     22590323.84721183,
     22607293.03223149,
     22628177.874863293,
     22830821.620213635,
     22725351.65172282,
     22858141.769098625,
     23748954.17710994,
     23690550.179748446,
     23528107.667687688,
     23568163.7704123,
     23782320.0846469,
     23544509.411114927,
     26065098.046453044,
     24164163.3423971,
     24336527.28146077,
     23968481.330782812,
     23982538.832720257,
     24297407.931546994,
     23878116.522909448,
     24058654.951893035,
     24015233.758382313,
     24194858.421202466,
     24409993.028596375,
     26139285.042633604,
     24529288.828185163,
     24465779.161926907,
     24642572.83305766,
     25327731.060210347,
     24933397.88492738,
     24480927.116961095,
     24790238.110287324,
     25584775.830339678,
     25383709.612056263,
     25868440.58393836,
     24613131.38641095,
     24170622.394749038,
     24147709.083108276,
     23938878.147045366,
     24598329.122019127,
     24296691.438666202,
     23986282.30450917,
     25100554.15040388,
     24194023.00753265,
     24244152.99513823,
     25225565.727706768,
     24792937.24788016,
     25037331.345755078,
     24386067.68479293,
     25543255.980112147,
     24079167.187810466,
     24357068.967405558,
     24151806.809980236,
     25779348.852000445,
     24233096.781700313,
     24317057.997624915,
     24026890.465031836,
     24113759.146277502,
     24623796.30501998,
     24411183.88036919,
     24875988.58012074,
     22808824.752883404,
     22759270.68478541,
     22801246.317258652,
     22883238.646583352,
     22396219.72158093,
     22380882.758839868,
     22424354.500170536,
     22294737.366407637,
     22407840.99623798,
     22254097.675616615,
     22321207.59058754,
     22348621.473435204,
     22562126.56870991,
     22559204.498497218,
     22150613.884768523,
     22036939.43092352,
     22224942.51766562,
     22162132.386934668,
     21975282.14585523,
     22207038.497976467,
     22136851.456220165,
     22283733.57638611,
     22205586.958776034,
     22242860.222331062,
     22203092.640358604,
     22558376.76161762,
     22291234.432228215,
     22033835.74012757,
     22096417.705195084,
     22126414.12285621,
     22168335.3762415,
     21909690.9772555,
     21863198.118706387,
     21824471.919891022,
     22106193.473261323,
     22193862.566202313,
     22161399.752473995,
     22224966.455764737,
     22184080.503035057,
     22255541.936447073,
     22192626.88944687,
     22220005.627999227,
     22236785.28795941,
     22127446.720194258,
     22195889.630783256,
     22630591.246509567,
     22862834.20680371,
     22548503.64339055,
     22640368.76007794,
     22603348.96031383,
     22708298.816408522,
     22658117.648740336,
     22635371.314896457,
     22529463.8574965,
     22699226.379304845,
     22882214.416118737,
     22780367.58163598,
     22465353.014707007,
     22461789.375869136,
     22472728.039584212,
     22459292.44450533,
     22604684.472472273,
     23683435.66428486,
     23884766.42998613,
     23576628.625297654,
     23314089.68520522,
     23384323.12958658,
     23045848.976695992,
     23061334.675234795,
     23008284.128031395,
     22974336.926145867,
     23371614.479556877,
     24008532.55972255,
     23161781.47049757,
     23525082.539923858,
     23171177.359872848,
     23145779.814915102,
     23418111.8085474,
     22350939.61238195,
     22398811.158096652,
     22436825.52611716,
     22293085.781485986,
     22263714.962031938,
     22569677.372144125,
     22326883.9419322,
     22088410.22422213,
     22227497.50305548,
     22284433.21374274,
     22244839.887545243,
     22388099.886400264,
     22379464.36394584,
     22336850.75866856,
     22378596.587638892,
     22256627.945916176,
     22268795.764054332,
     22176672.78871714,
     22430261.868879057,
     22233496.11549078,
     22513701.467266463,
     22709441.152023803,
     22738953.224857826,
     22652167.898774296,
     22375946.862249397,
     22447814.19958479,
     22553567.9109499,
     22425229.798253924,
     22692704.19766245,
     22527258.374377728,
     22722422.18040844,
     22502106.725008316,
     22489520.62919985,
     22431787.501467895,
     8760748.415948119,
     22369761.376674153,
     22180428.04089021,
     22119603.472176086,
     22324773.809916563,
     22518545.560340397,
     22215122.224203836,
     22518648.01953704,
     22236069.709535606,
     22482347.910669826,
     22397391.604346443,
     22538848.955096282,
     22306056.733926885,
     22336853.837809008,
     22362742.011597972,
     22343891.656452175,
     22214935.41331286,
     22285211.55930494,
     22552153.15562487,
     22574728.109729026,
     22666494.562355727,
     22346564.043903388,
     22552430.76497779,
     22441621.742320225,
     22736635.170388177,
     22347710.582598627,
     23131161.780385286,
     23019806.551068142,
     22995666.485750742,
     22977577.211405262,
     23059624.392490778,
     23130648.95504481,
     23329559.608799398,
     22816872.350479607,
     22967902.80660402,
     22849838.925811697,
     22989299.1861606,
     22887215.95056168,
     22868036.34628608,
     22918790.90503387,
     23181466.933463994,
     23286807.300748132,
     22959984.10087702,
     24385627.867383577,
     23241563.67362411,
     23069306.715521574,
     23291715.61833419,
     21896026.75699707,
     24504504.509381264,
     26351434.46195586,
     26569878.937387206,
     24055117.63430936,
     25241314.88885741,
     25743033.117933214,
     23977188.494604502,
     26775666.299041286,
     23522688.55672369,
     24004902.9370825,
     26277390.510134634,
     26104023.45656628,
     24141052.09355405,
     24272586.57884091,
     23954903.244073555,
     23767464.33237118,
     26737742.46333429,
     24638810.77456151,
     23904834.90907172,
     26489069.91801105,
     23500619.40294323,
     24549126.850071557,
     25328302.493430324,
     26600050.35494344,
     23815691.124419842,
     24784648.66784158,
     24508858.660855822,
     23774810.110697873,
     30006888.69167791,
     23732594.266619835,
     23865522.188015953,
     25375313.053474046,
     26475462.15884895,
     23732963.935800426,
     24724336.83277651,
     23665989.946200795,
     22362468.363369394,
     22755199.38908648,
     21973833.318938665,
     22001675.049222346,
     22042824.456616838,
     22016313.726864167,
     22390232.502519093,
     21979419.130919565,
     22605275.608251635,
     22774566.48570969,
     22643939.0637797,
     22343821.13728626,
     22153361.03733821,
     22338885.783290848,
     23564604.78658378,
     23609003.858640626,
     23888853.25887241,
     23124481.10847337,
     23584975.81941901,
     23409297.138158094,
     23429021.171674617,
     23515428.121543333,
     23578038.701303206,
     23432591.909545407,
     23576099.569969006,
     23546752.224112473,
     23588318.842353642,
     23569735.348359626,
     23783495.190239713,
     23767595.186067797,
     24127835.591181204,
     23647052.336499386,
     23839915.319160245,
     23193692.082438685,
     23262603.32109773,
     23055713.795847762,
     23060231.377200034,
     23344636.81184601,
     23326873.47010627,
     23208814.602200758,
     22978412.348086685,
     23209947.824319176,
     23332644.465471033,
     23258295.52797334,
     24794549.432340376,
     24468044.195279732,
     24381874.72661163,
     25703789.686051637,
     24315821.927144095,
     25524106.656112377,
     24623292.61196862,
     25001083.11813602,
     24642949.95975343,
     24496727.485449024,
     24712100.40389996,
     25224526.90619575,
     25903980.69505355,
     24181199.882427596,
     25020891.83151605,
     24485466.25758029,
     24808005.685297128,
     25009046.81461482,
     25275983.62263914,
     23741006.574645013,
     23820908.83839629,
     25263477.748581316,
     25353104.539147027,
     23776480.761617154,
     23834650.932095654,
     23769450.285933264,
     24006108.03099927,
     23380870.639265694,
     24044802.410280608,
     23565426.56065893,
     23603750.90760752,
     23768731.74767264,
     23409289.03086012,
     25887152.923153915,
     21955648.91083903,
     21863532.40546504,
     21946623.058194537,
     21899727.854216192,
     22364286.68124307,
     22421319.530665994,
     22366589.152286448,
     22155453.889884867,
     21658021.841790352,
     22023932.32193539,
     21855827.873827014,
     21826098.00576767,
     22481619.96466351,
     21908414.42229638,
     21989695.278913837,
     21826192.656264734,
     21916045.87984978,
     22639616.213859074,
     22420278.847075276,
     22128277.48173629,
     22742723.311649762,
     22595685.217967812,
     22667980.318118524,
     22105420.75108485,
     22770824.66725068,
     22598367.170937832,
     22608542.26068468,
     22396854.18126877,
     21897234.464237243,
     21885218.205009654,
     21968998.446758416,
     21633058.394544683,
     21990501.51738956,
     21675067.83941205,
     21655580.560240023,
     22272005.83061701,
     21741098.79106398,
     21652216.472418413,
     21740312.30215138,
     22299904.190198176,
     12203371.139306972,
     12113577.590451572,
     12496037.822538594,
     11644001.331100032,
     12137655.611215599,
     12244661.872504726,
     12355494.352932656,
     11501743.739180114,
     11827564.27542033,
     12025528.399499375,
     11625656.074897405,
     12464143.271550704,
     12171917.730930284,
     12527291.562110215,
     11496279.490450222,
     11736805.617191523,
     11592562.087714946,
     12133928.072451027,
     12266065.540802997,
     12246343.12631884,
     12726055.442699568,
     11949302.071495073,
     12508365.44170656,
     12417422.730088681,
     12174492.022592098,
     12515570.972230569,
     12318653.187211882,
     12344233.837976348,
     12061634.071494114,
     12533197.465463774,
     12503843.001406772,
     12872915.714513082,
     11634497.046075959,
     12202527.077042332,
     12564538.90119576,
     11911117.591842536,
     12650126.468838127,
     12391447.09730284,
     26329457.223257013,
     12590571.649619518,
     12562110.085768906,
     12322987.621064877,
     12304840.414567852,
     12687259.772666274,
     11422358.143597445,
     11549618.792826641,
     11499046.875756547,
     11484909.174459415,
     12778636.65073349,
     12779984.205395503,
     11813783.846760474,
     12066679.739388127,
     12607778.34429511,
     12789808.240885831,
     12442340.331497537,
     12415143.865055121,
     11772677.61696383,
     12182331.103402944,
     12569532.118435055,
     11522187.819274645,
     12061515.033933947,
     12460609.445266396,
     11635136.126726069,
     12494827.71469055,
     12549114.654391108,
     12320160.998862421,
     11490554.687067233,
     12653581.943389704,
     12243193.001742944,
     12145262.156493193,
     12429198.644627055,
     12792347.55901459,
     12235545.869840305,
     12225625.184388416,
     11821351.781966485,
     12403536.373979215,
     12051108.042696733,
     11809203.573843358,
     12455353.00047825,
     12568353.144144895,
     12546325.762332967,
     12546609.159879599,
     12276231.440391392,
     11510396.267578634,
     12575122.018705493,
     13113096.169840898,
     12697502.284068208,
     13505579.249484386,
     13254076.164698545,
     12703262.372741079,
     13005603.376480473,
     15048114.567772878,
     15462232.056119876,
     15701030.377504718,
     14985166.953447685,
     12459995.636599805,
     16010885.27389151,
     15991159.999094319,
     15733233.752750158,
     15939182.02128691,
     14632266.489996336,
     13199849.550986065,
     13279484.548312047,
     14705901.338954268,
     15976399.994092874,
     15967135.367402812,
     16689956.47176045,
     16149126.398166075,
     16341635.503437256,
     16564043.991034133,
     16137953.835749304,
     16194095.65465793,
     15948183.198562995,
     14111931.128804205,
     13506877.986017263,
     13795894.637723986,
     14033659.509435212,
     13804687.368175138,
     14063430.499716418,
     14074574.305762831,
     14230082.090072729,
     14143206.807683403,
     14162142.89589042,
     14085494.481540695,
     13145557.272128366,
     13093955.662914664,
     13392657.303804493,
     13302495.66608254,
     13591721.78821312,
     13473240.279017832,
     13217104.479880756,
     14137368.877558302,
     13699646.731986659,
     13874073.945370378,
     14041706.21741108,
     13834074.937584817,
     13876599.226346606,
     13757085.44923048,
     14027582.527812203,
     13632626.477253886,
     13783687.392760342,
     13916913.981023027,
     14020295.222047921,
     13845660.01818632,
     14007836.494905414,
     12644121.111975217,
     13079444.696599707,
     12915748.173904892,
     12998238.550466046,
     13108066.767948683,
     13042095.217360696,
     12845867.741170095,
     14822740.254594002,
     14107801.332257688,
     14897967.29869871,
     17593176.559918217,
     14085020.566073345,
     14131081.112701949,
     14134883.551920883,
     14532362.596660722,
     14457262.981324429,
     13873393.996682733,
     14656410.467934655,
     14322069.78951584,
     14438769.768751774,
     14837147.800086621,
     13842670.15314697,
     14203466.839960374,
     14673402.081808165,
     13631062.09570155,
     15692922.746585753,
     15447346.250551613,
     15442989.88011379,
     15752167.216553623,
     15442172.535375034,
     15346192.012408756,
     15585722.690822888,
     15572310.813331988,
     15337134.591545181,
     15706252.225025596,
     15563367.726399673,
     13274904.368386878,
     12786023.850166023,
     14031933.5165345,
     13830201.287952716,
     12535383.20360194,
     14214273.91590776,
     14249581.296687867,
     14037523.411917392,
     13892850.816323755,
     13821846.459083293,
     14064729.82772551,
     13502936.323105177,
     13764527.319728497,
     13706485.832910102,
     13867987.543713788,
     13010392.06132245,
     14740472.73716356,
     14886826.549445136,
     14391300.565910941,
     15000975.900304811,
     15040577.610674592,
     14725930.859688833,
     17076242.765964977,
     16483948.083856763,
     16880719.675899073,
     17546888.257242613,
     13248767.171142297,
     13515075.12977757,
     13131152.539458096,
     13474835.493707145,
     13494020.199514639,
     13658410.812377827,
     13552361.693498239,
     13369086.845952116,
     13244281.147474399,
     13216541.728594435,
     13317404.006877847,
     13412272.48140347,
     13755710.091885587,
     14408921.026201816,
     14061548.38825501,
     13972988.06710346,
     14240170.691507122,
     ...]




```python
fig, ax = plt.subplots(figsize=(10,15))
plt.title("Scaled Up Earth With Coastlines")
m.scatter(x,y,s=1)
m.drawcoastlines()
```




    <matplotlib.collections.LineCollection at 0x7fb79b025f28>




![png](output_27_1.png)


### We also created a visualization of one sample airport which includes its flight routes.


```python
geo_routes = pd.read_csv('geo_routes.csv')
geo_routes
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
      <th>airline</th>
      <th>source</th>
      <th>dest</th>
      <th>equipment</th>
      <th>start_lon</th>
      <th>end_lon</th>
      <th>start_lat</th>
      <th>end_lat</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>2B</td>
      <td>AER</td>
      <td>KZN</td>
      <td>CR2</td>
      <td>39.956589</td>
      <td>49.278728</td>
      <td>43.449928</td>
      <td>55.606186</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2B</td>
      <td>ASF</td>
      <td>KZN</td>
      <td>CR2</td>
      <td>48.006278</td>
      <td>49.278728</td>
      <td>46.283333</td>
      <td>55.606186</td>
    </tr>
    <tr>
      <th>2</th>
      <td>2B</td>
      <td>ASF</td>
      <td>MRV</td>
      <td>CR2</td>
      <td>48.006278</td>
      <td>43.081889</td>
      <td>46.283333</td>
      <td>44.225072</td>
    </tr>
    <tr>
      <th>3</th>
      <td>2B</td>
      <td>CEK</td>
      <td>KZN</td>
      <td>CR2</td>
      <td>61.503333</td>
      <td>49.278728</td>
      <td>55.305836</td>
      <td>55.606186</td>
    </tr>
    <tr>
      <th>4</th>
      <td>2B</td>
      <td>CEK</td>
      <td>OVB</td>
      <td>CR2</td>
      <td>61.503333</td>
      <td>82.650656</td>
      <td>55.305836</td>
      <td>55.012622</td>
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
      <th>67423</th>
      <td>ZL</td>
      <td>WYA</td>
      <td>ADL</td>
      <td>SF3</td>
      <td>137.514000</td>
      <td>138.530556</td>
      <td>-33.058900</td>
      <td>-34.945000</td>
    </tr>
    <tr>
      <th>67424</th>
      <td>ZM</td>
      <td>DME</td>
      <td>FRU</td>
      <td>734</td>
      <td>37.906111</td>
      <td>74.477556</td>
      <td>55.408611</td>
      <td>43.061306</td>
    </tr>
    <tr>
      <th>67425</th>
      <td>ZM</td>
      <td>FRU</td>
      <td>DME</td>
      <td>734</td>
      <td>74.477556</td>
      <td>37.906111</td>
      <td>43.061306</td>
      <td>55.408611</td>
    </tr>
    <tr>
      <th>67426</th>
      <td>ZM</td>
      <td>FRU</td>
      <td>OSS</td>
      <td>734</td>
      <td>74.477556</td>
      <td>72.793269</td>
      <td>43.061306</td>
      <td>40.608989</td>
    </tr>
    <tr>
      <th>67427</th>
      <td>ZM</td>
      <td>OSS</td>
      <td>FRU</td>
      <td>734</td>
      <td>72.793269</td>
      <td>74.477556</td>
      <td>40.608989</td>
      <td>43.061306</td>
    </tr>
  </tbody>
</table>
<p>67428 rows × 8 columns</p>
</div>




```python
# a helper function that that draws a great circle for each route that has an absolute difference in the latitude and longitude values less than 180.
def create_great_circles(df):
    for index, row in df.iterrows():
        end_lat, start_lat = row['end_lat'], row['start_lat']
        end_lon, start_lon = row['end_lon'], row['start_lon']
        
        if abs(end_lat - start_lat) < 180:
            if abs(end_lon - start_lon) < 180:
                m.drawgreatcircle(start_lon, start_lat, end_lon, end_lat)
```


```python
fig, ax = plt.subplots(figsize=(10,15))
m = Basemap(projection='merc', llcrnrlat=-80, urcrnrlat=80, llcrnrlon=-180, urcrnrlon=180)
m.drawcoastlines()
plt.title("Airport DFW Routes")
dfw = geo_routes[geo_routes['source'] == "DFW"]
create_great_circles(dfw)
m.drawcoastlines()
plt.show()
```

    /Users/MimiHMB/anaconda3/lib/python3.7/site-packages/ipykernel_launcher.py:2: MatplotlibDeprecationWarning: 
    The dedent function was deprecated in Matplotlib 3.1 and will be removed in 3.3. Use inspect.cleandoc instead.
      



![png](output_31_1.png)

