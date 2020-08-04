```python
import pandas as pd
pd.options.display.max_columns = 999
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import KFold
from sklearn.metrics import mean_squared_error
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import KFold
import seaborn as sns
```


```python
df = pd.read_csv('AmesHousing.txt', delimiter='\t')
df
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
      <th>Order</th>
      <th>PID</th>
      <th>MS SubClass</th>
      <th>MS Zoning</th>
      <th>Lot Frontage</th>
      <th>Lot Area</th>
      <th>Street</th>
      <th>Alley</th>
      <th>Lot Shape</th>
      <th>Land Contour</th>
      <th>Utilities</th>
      <th>Lot Config</th>
      <th>Land Slope</th>
      <th>Neighborhood</th>
      <th>Condition 1</th>
      <th>Condition 2</th>
      <th>Bldg Type</th>
      <th>House Style</th>
      <th>Overall Qual</th>
      <th>Overall Cond</th>
      <th>Year Built</th>
      <th>Year Remod/Add</th>
      <th>Roof Style</th>
      <th>Roof Matl</th>
      <th>Exterior 1st</th>
      <th>Exterior 2nd</th>
      <th>Mas Vnr Type</th>
      <th>Mas Vnr Area</th>
      <th>Exter Qual</th>
      <th>Exter Cond</th>
      <th>Foundation</th>
      <th>Bsmt Qual</th>
      <th>Bsmt Cond</th>
      <th>Bsmt Exposure</th>
      <th>BsmtFin Type 1</th>
      <th>BsmtFin SF 1</th>
      <th>BsmtFin Type 2</th>
      <th>BsmtFin SF 2</th>
      <th>Bsmt Unf SF</th>
      <th>Total Bsmt SF</th>
      <th>Heating</th>
      <th>Heating QC</th>
      <th>Central Air</th>
      <th>Electrical</th>
      <th>1st Flr SF</th>
      <th>2nd Flr SF</th>
      <th>Low Qual Fin SF</th>
      <th>Gr Liv Area</th>
      <th>Bsmt Full Bath</th>
      <th>Bsmt Half Bath</th>
      <th>Full Bath</th>
      <th>Half Bath</th>
      <th>Bedroom AbvGr</th>
      <th>Kitchen AbvGr</th>
      <th>Kitchen Qual</th>
      <th>TotRms AbvGrd</th>
      <th>Functional</th>
      <th>Fireplaces</th>
      <th>Fireplace Qu</th>
      <th>Garage Type</th>
      <th>Garage Yr Blt</th>
      <th>Garage Finish</th>
      <th>Garage Cars</th>
      <th>Garage Area</th>
      <th>Garage Qual</th>
      <th>Garage Cond</th>
      <th>Paved Drive</th>
      <th>Wood Deck SF</th>
      <th>Open Porch SF</th>
      <th>Enclosed Porch</th>
      <th>3Ssn Porch</th>
      <th>Screen Porch</th>
      <th>Pool Area</th>
      <th>Pool QC</th>
      <th>Fence</th>
      <th>Misc Feature</th>
      <th>Misc Val</th>
      <th>Mo Sold</th>
      <th>Yr Sold</th>
      <th>Sale Type</th>
      <th>Sale Condition</th>
      <th>SalePrice</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1</td>
      <td>526301100</td>
      <td>20</td>
      <td>RL</td>
      <td>141.0</td>
      <td>31770</td>
      <td>Pave</td>
      <td>NaN</td>
      <td>IR1</td>
      <td>Lvl</td>
      <td>AllPub</td>
      <td>Corner</td>
      <td>Gtl</td>
      <td>NAmes</td>
      <td>Norm</td>
      <td>Norm</td>
      <td>1Fam</td>
      <td>1Story</td>
      <td>6</td>
      <td>5</td>
      <td>1960</td>
      <td>1960</td>
      <td>Hip</td>
      <td>CompShg</td>
      <td>BrkFace</td>
      <td>Plywood</td>
      <td>Stone</td>
      <td>112.0</td>
      <td>TA</td>
      <td>TA</td>
      <td>CBlock</td>
      <td>TA</td>
      <td>Gd</td>
      <td>Gd</td>
      <td>BLQ</td>
      <td>639.0</td>
      <td>Unf</td>
      <td>0.0</td>
      <td>441.0</td>
      <td>1080.0</td>
      <td>GasA</td>
      <td>Fa</td>
      <td>Y</td>
      <td>SBrkr</td>
      <td>1656</td>
      <td>0</td>
      <td>0</td>
      <td>1656</td>
      <td>1.0</td>
      <td>0.0</td>
      <td>1</td>
      <td>0</td>
      <td>3</td>
      <td>1</td>
      <td>TA</td>
      <td>7</td>
      <td>Typ</td>
      <td>2</td>
      <td>Gd</td>
      <td>Attchd</td>
      <td>1960.0</td>
      <td>Fin</td>
      <td>2.0</td>
      <td>528.0</td>
      <td>TA</td>
      <td>TA</td>
      <td>P</td>
      <td>210</td>
      <td>62</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>0</td>
      <td>5</td>
      <td>2010</td>
      <td>WD</td>
      <td>Normal</td>
      <td>215000</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2</td>
      <td>526350040</td>
      <td>20</td>
      <td>RH</td>
      <td>80.0</td>
      <td>11622</td>
      <td>Pave</td>
      <td>NaN</td>
      <td>Reg</td>
      <td>Lvl</td>
      <td>AllPub</td>
      <td>Inside</td>
      <td>Gtl</td>
      <td>NAmes</td>
      <td>Feedr</td>
      <td>Norm</td>
      <td>1Fam</td>
      <td>1Story</td>
      <td>5</td>
      <td>6</td>
      <td>1961</td>
      <td>1961</td>
      <td>Gable</td>
      <td>CompShg</td>
      <td>VinylSd</td>
      <td>VinylSd</td>
      <td>None</td>
      <td>0.0</td>
      <td>TA</td>
      <td>TA</td>
      <td>CBlock</td>
      <td>TA</td>
      <td>TA</td>
      <td>No</td>
      <td>Rec</td>
      <td>468.0</td>
      <td>LwQ</td>
      <td>144.0</td>
      <td>270.0</td>
      <td>882.0</td>
      <td>GasA</td>
      <td>TA</td>
      <td>Y</td>
      <td>SBrkr</td>
      <td>896</td>
      <td>0</td>
      <td>0</td>
      <td>896</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>1</td>
      <td>0</td>
      <td>2</td>
      <td>1</td>
      <td>TA</td>
      <td>5</td>
      <td>Typ</td>
      <td>0</td>
      <td>NaN</td>
      <td>Attchd</td>
      <td>1961.0</td>
      <td>Unf</td>
      <td>1.0</td>
      <td>730.0</td>
      <td>TA</td>
      <td>TA</td>
      <td>Y</td>
      <td>140</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>120</td>
      <td>0</td>
      <td>NaN</td>
      <td>MnPrv</td>
      <td>NaN</td>
      <td>0</td>
      <td>6</td>
      <td>2010</td>
      <td>WD</td>
      <td>Normal</td>
      <td>105000</td>
    </tr>
    <tr>
      <th>2</th>
      <td>3</td>
      <td>526351010</td>
      <td>20</td>
      <td>RL</td>
      <td>81.0</td>
      <td>14267</td>
      <td>Pave</td>
      <td>NaN</td>
      <td>IR1</td>
      <td>Lvl</td>
      <td>AllPub</td>
      <td>Corner</td>
      <td>Gtl</td>
      <td>NAmes</td>
      <td>Norm</td>
      <td>Norm</td>
      <td>1Fam</td>
      <td>1Story</td>
      <td>6</td>
      <td>6</td>
      <td>1958</td>
      <td>1958</td>
      <td>Hip</td>
      <td>CompShg</td>
      <td>Wd Sdng</td>
      <td>Wd Sdng</td>
      <td>BrkFace</td>
      <td>108.0</td>
      <td>TA</td>
      <td>TA</td>
      <td>CBlock</td>
      <td>TA</td>
      <td>TA</td>
      <td>No</td>
      <td>ALQ</td>
      <td>923.0</td>
      <td>Unf</td>
      <td>0.0</td>
      <td>406.0</td>
      <td>1329.0</td>
      <td>GasA</td>
      <td>TA</td>
      <td>Y</td>
      <td>SBrkr</td>
      <td>1329</td>
      <td>0</td>
      <td>0</td>
      <td>1329</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>1</td>
      <td>1</td>
      <td>3</td>
      <td>1</td>
      <td>Gd</td>
      <td>6</td>
      <td>Typ</td>
      <td>0</td>
      <td>NaN</td>
      <td>Attchd</td>
      <td>1958.0</td>
      <td>Unf</td>
      <td>1.0</td>
      <td>312.0</td>
      <td>TA</td>
      <td>TA</td>
      <td>Y</td>
      <td>393</td>
      <td>36</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>Gar2</td>
      <td>12500</td>
      <td>6</td>
      <td>2010</td>
      <td>WD</td>
      <td>Normal</td>
      <td>172000</td>
    </tr>
    <tr>
      <th>3</th>
      <td>4</td>
      <td>526353030</td>
      <td>20</td>
      <td>RL</td>
      <td>93.0</td>
      <td>11160</td>
      <td>Pave</td>
      <td>NaN</td>
      <td>Reg</td>
      <td>Lvl</td>
      <td>AllPub</td>
      <td>Corner</td>
      <td>Gtl</td>
      <td>NAmes</td>
      <td>Norm</td>
      <td>Norm</td>
      <td>1Fam</td>
      <td>1Story</td>
      <td>7</td>
      <td>5</td>
      <td>1968</td>
      <td>1968</td>
      <td>Hip</td>
      <td>CompShg</td>
      <td>BrkFace</td>
      <td>BrkFace</td>
      <td>None</td>
      <td>0.0</td>
      <td>Gd</td>
      <td>TA</td>
      <td>CBlock</td>
      <td>TA</td>
      <td>TA</td>
      <td>No</td>
      <td>ALQ</td>
      <td>1065.0</td>
      <td>Unf</td>
      <td>0.0</td>
      <td>1045.0</td>
      <td>2110.0</td>
      <td>GasA</td>
      <td>Ex</td>
      <td>Y</td>
      <td>SBrkr</td>
      <td>2110</td>
      <td>0</td>
      <td>0</td>
      <td>2110</td>
      <td>1.0</td>
      <td>0.0</td>
      <td>2</td>
      <td>1</td>
      <td>3</td>
      <td>1</td>
      <td>Ex</td>
      <td>8</td>
      <td>Typ</td>
      <td>2</td>
      <td>TA</td>
      <td>Attchd</td>
      <td>1968.0</td>
      <td>Fin</td>
      <td>2.0</td>
      <td>522.0</td>
      <td>TA</td>
      <td>TA</td>
      <td>Y</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>0</td>
      <td>4</td>
      <td>2010</td>
      <td>WD</td>
      <td>Normal</td>
      <td>244000</td>
    </tr>
    <tr>
      <th>4</th>
      <td>5</td>
      <td>527105010</td>
      <td>60</td>
      <td>RL</td>
      <td>74.0</td>
      <td>13830</td>
      <td>Pave</td>
      <td>NaN</td>
      <td>IR1</td>
      <td>Lvl</td>
      <td>AllPub</td>
      <td>Inside</td>
      <td>Gtl</td>
      <td>Gilbert</td>
      <td>Norm</td>
      <td>Norm</td>
      <td>1Fam</td>
      <td>2Story</td>
      <td>5</td>
      <td>5</td>
      <td>1997</td>
      <td>1998</td>
      <td>Gable</td>
      <td>CompShg</td>
      <td>VinylSd</td>
      <td>VinylSd</td>
      <td>None</td>
      <td>0.0</td>
      <td>TA</td>
      <td>TA</td>
      <td>PConc</td>
      <td>Gd</td>
      <td>TA</td>
      <td>No</td>
      <td>GLQ</td>
      <td>791.0</td>
      <td>Unf</td>
      <td>0.0</td>
      <td>137.0</td>
      <td>928.0</td>
      <td>GasA</td>
      <td>Gd</td>
      <td>Y</td>
      <td>SBrkr</td>
      <td>928</td>
      <td>701</td>
      <td>0</td>
      <td>1629</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>2</td>
      <td>1</td>
      <td>3</td>
      <td>1</td>
      <td>TA</td>
      <td>6</td>
      <td>Typ</td>
      <td>1</td>
      <td>TA</td>
      <td>Attchd</td>
      <td>1997.0</td>
      <td>Fin</td>
      <td>2.0</td>
      <td>482.0</td>
      <td>TA</td>
      <td>TA</td>
      <td>Y</td>
      <td>212</td>
      <td>34</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>NaN</td>
      <td>MnPrv</td>
      <td>NaN</td>
      <td>0</td>
      <td>3</td>
      <td>2010</td>
      <td>WD</td>
      <td>Normal</td>
      <td>189900</td>
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
      <th>2925</th>
      <td>2926</td>
      <td>923275080</td>
      <td>80</td>
      <td>RL</td>
      <td>37.0</td>
      <td>7937</td>
      <td>Pave</td>
      <td>NaN</td>
      <td>IR1</td>
      <td>Lvl</td>
      <td>AllPub</td>
      <td>CulDSac</td>
      <td>Gtl</td>
      <td>Mitchel</td>
      <td>Norm</td>
      <td>Norm</td>
      <td>1Fam</td>
      <td>SLvl</td>
      <td>6</td>
      <td>6</td>
      <td>1984</td>
      <td>1984</td>
      <td>Gable</td>
      <td>CompShg</td>
      <td>HdBoard</td>
      <td>HdBoard</td>
      <td>None</td>
      <td>0.0</td>
      <td>TA</td>
      <td>TA</td>
      <td>CBlock</td>
      <td>TA</td>
      <td>TA</td>
      <td>Av</td>
      <td>GLQ</td>
      <td>819.0</td>
      <td>Unf</td>
      <td>0.0</td>
      <td>184.0</td>
      <td>1003.0</td>
      <td>GasA</td>
      <td>TA</td>
      <td>Y</td>
      <td>SBrkr</td>
      <td>1003</td>
      <td>0</td>
      <td>0</td>
      <td>1003</td>
      <td>1.0</td>
      <td>0.0</td>
      <td>1</td>
      <td>0</td>
      <td>3</td>
      <td>1</td>
      <td>TA</td>
      <td>6</td>
      <td>Typ</td>
      <td>0</td>
      <td>NaN</td>
      <td>Detchd</td>
      <td>1984.0</td>
      <td>Unf</td>
      <td>2.0</td>
      <td>588.0</td>
      <td>TA</td>
      <td>TA</td>
      <td>Y</td>
      <td>120</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>NaN</td>
      <td>GdPrv</td>
      <td>NaN</td>
      <td>0</td>
      <td>3</td>
      <td>2006</td>
      <td>WD</td>
      <td>Normal</td>
      <td>142500</td>
    </tr>
    <tr>
      <th>2926</th>
      <td>2927</td>
      <td>923276100</td>
      <td>20</td>
      <td>RL</td>
      <td>NaN</td>
      <td>8885</td>
      <td>Pave</td>
      <td>NaN</td>
      <td>IR1</td>
      <td>Low</td>
      <td>AllPub</td>
      <td>Inside</td>
      <td>Mod</td>
      <td>Mitchel</td>
      <td>Norm</td>
      <td>Norm</td>
      <td>1Fam</td>
      <td>1Story</td>
      <td>5</td>
      <td>5</td>
      <td>1983</td>
      <td>1983</td>
      <td>Gable</td>
      <td>CompShg</td>
      <td>HdBoard</td>
      <td>HdBoard</td>
      <td>None</td>
      <td>0.0</td>
      <td>TA</td>
      <td>TA</td>
      <td>CBlock</td>
      <td>Gd</td>
      <td>TA</td>
      <td>Av</td>
      <td>BLQ</td>
      <td>301.0</td>
      <td>ALQ</td>
      <td>324.0</td>
      <td>239.0</td>
      <td>864.0</td>
      <td>GasA</td>
      <td>TA</td>
      <td>Y</td>
      <td>SBrkr</td>
      <td>902</td>
      <td>0</td>
      <td>0</td>
      <td>902</td>
      <td>1.0</td>
      <td>0.0</td>
      <td>1</td>
      <td>0</td>
      <td>2</td>
      <td>1</td>
      <td>TA</td>
      <td>5</td>
      <td>Typ</td>
      <td>0</td>
      <td>NaN</td>
      <td>Attchd</td>
      <td>1983.0</td>
      <td>Unf</td>
      <td>2.0</td>
      <td>484.0</td>
      <td>TA</td>
      <td>TA</td>
      <td>Y</td>
      <td>164</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>NaN</td>
      <td>MnPrv</td>
      <td>NaN</td>
      <td>0</td>
      <td>6</td>
      <td>2006</td>
      <td>WD</td>
      <td>Normal</td>
      <td>131000</td>
    </tr>
    <tr>
      <th>2927</th>
      <td>2928</td>
      <td>923400125</td>
      <td>85</td>
      <td>RL</td>
      <td>62.0</td>
      <td>10441</td>
      <td>Pave</td>
      <td>NaN</td>
      <td>Reg</td>
      <td>Lvl</td>
      <td>AllPub</td>
      <td>Inside</td>
      <td>Gtl</td>
      <td>Mitchel</td>
      <td>Norm</td>
      <td>Norm</td>
      <td>1Fam</td>
      <td>SFoyer</td>
      <td>5</td>
      <td>5</td>
      <td>1992</td>
      <td>1992</td>
      <td>Gable</td>
      <td>CompShg</td>
      <td>HdBoard</td>
      <td>Wd Shng</td>
      <td>None</td>
      <td>0.0</td>
      <td>TA</td>
      <td>TA</td>
      <td>PConc</td>
      <td>Gd</td>
      <td>TA</td>
      <td>Av</td>
      <td>GLQ</td>
      <td>337.0</td>
      <td>Unf</td>
      <td>0.0</td>
      <td>575.0</td>
      <td>912.0</td>
      <td>GasA</td>
      <td>TA</td>
      <td>Y</td>
      <td>SBrkr</td>
      <td>970</td>
      <td>0</td>
      <td>0</td>
      <td>970</td>
      <td>0.0</td>
      <td>1.0</td>
      <td>1</td>
      <td>0</td>
      <td>3</td>
      <td>1</td>
      <td>TA</td>
      <td>6</td>
      <td>Typ</td>
      <td>0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>Y</td>
      <td>80</td>
      <td>32</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>NaN</td>
      <td>MnPrv</td>
      <td>Shed</td>
      <td>700</td>
      <td>7</td>
      <td>2006</td>
      <td>WD</td>
      <td>Normal</td>
      <td>132000</td>
    </tr>
    <tr>
      <th>2928</th>
      <td>2929</td>
      <td>924100070</td>
      <td>20</td>
      <td>RL</td>
      <td>77.0</td>
      <td>10010</td>
      <td>Pave</td>
      <td>NaN</td>
      <td>Reg</td>
      <td>Lvl</td>
      <td>AllPub</td>
      <td>Inside</td>
      <td>Mod</td>
      <td>Mitchel</td>
      <td>Norm</td>
      <td>Norm</td>
      <td>1Fam</td>
      <td>1Story</td>
      <td>5</td>
      <td>5</td>
      <td>1974</td>
      <td>1975</td>
      <td>Gable</td>
      <td>CompShg</td>
      <td>HdBoard</td>
      <td>HdBoard</td>
      <td>None</td>
      <td>0.0</td>
      <td>TA</td>
      <td>TA</td>
      <td>CBlock</td>
      <td>Gd</td>
      <td>TA</td>
      <td>Av</td>
      <td>ALQ</td>
      <td>1071.0</td>
      <td>LwQ</td>
      <td>123.0</td>
      <td>195.0</td>
      <td>1389.0</td>
      <td>GasA</td>
      <td>Gd</td>
      <td>Y</td>
      <td>SBrkr</td>
      <td>1389</td>
      <td>0</td>
      <td>0</td>
      <td>1389</td>
      <td>1.0</td>
      <td>0.0</td>
      <td>1</td>
      <td>0</td>
      <td>2</td>
      <td>1</td>
      <td>TA</td>
      <td>6</td>
      <td>Typ</td>
      <td>1</td>
      <td>TA</td>
      <td>Attchd</td>
      <td>1975.0</td>
      <td>RFn</td>
      <td>2.0</td>
      <td>418.0</td>
      <td>TA</td>
      <td>TA</td>
      <td>Y</td>
      <td>240</td>
      <td>38</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>0</td>
      <td>4</td>
      <td>2006</td>
      <td>WD</td>
      <td>Normal</td>
      <td>170000</td>
    </tr>
    <tr>
      <th>2929</th>
      <td>2930</td>
      <td>924151050</td>
      <td>60</td>
      <td>RL</td>
      <td>74.0</td>
      <td>9627</td>
      <td>Pave</td>
      <td>NaN</td>
      <td>Reg</td>
      <td>Lvl</td>
      <td>AllPub</td>
      <td>Inside</td>
      <td>Mod</td>
      <td>Mitchel</td>
      <td>Norm</td>
      <td>Norm</td>
      <td>1Fam</td>
      <td>2Story</td>
      <td>7</td>
      <td>5</td>
      <td>1993</td>
      <td>1994</td>
      <td>Gable</td>
      <td>CompShg</td>
      <td>HdBoard</td>
      <td>HdBoard</td>
      <td>BrkFace</td>
      <td>94.0</td>
      <td>TA</td>
      <td>TA</td>
      <td>PConc</td>
      <td>Gd</td>
      <td>TA</td>
      <td>Av</td>
      <td>LwQ</td>
      <td>758.0</td>
      <td>Unf</td>
      <td>0.0</td>
      <td>238.0</td>
      <td>996.0</td>
      <td>GasA</td>
      <td>Ex</td>
      <td>Y</td>
      <td>SBrkr</td>
      <td>996</td>
      <td>1004</td>
      <td>0</td>
      <td>2000</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>2</td>
      <td>1</td>
      <td>3</td>
      <td>1</td>
      <td>TA</td>
      <td>9</td>
      <td>Typ</td>
      <td>1</td>
      <td>TA</td>
      <td>Attchd</td>
      <td>1993.0</td>
      <td>Fin</td>
      <td>3.0</td>
      <td>650.0</td>
      <td>TA</td>
      <td>TA</td>
      <td>Y</td>
      <td>190</td>
      <td>48</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>0</td>
      <td>11</td>
      <td>2006</td>
      <td>WD</td>
      <td>Normal</td>
      <td>188000</td>
    </tr>
  </tbody>
</table>
<p>2930 rows × 82 columns</p>
</div>




```python
def transform_features(df):
    data = df.copy()
    # select text columns
    t_df = data.select_dtypes(include='object')
    t_isNull = t_df.isnull().sum()
    # select columns with more than 1 missing values to drop
    t_isNull_col = t_isNull[t_isNull >= 1].index
    # drop selected columns
    data = data.drop(t_isNull_col, axis=1)
    
    # keep only columns with less than 5% missing values
    isNull = data.isnull().sum()
    data = data[isNull[isNull < len(data)*0.05].index]
    
    # select numerical columns
    num_df = data.select_dtypes(exclude='object')
    # select suitable null columns to replace with mode
    num_isNull = num_df.isnull().sum()
    num_isNull_col = num_isNull[num_isNull != 0].index
    # replace with mode
    rep_val = data[num_isNull_col].mode().to_dict(orient='records')[0]
    data = data.fillna(rep_val)
    return data

def select_features(df, thred_corr):
    corr = df.corr()['SalePrice'].abs().sort_values(ascending=False)
    corr = corr[corr > thred_corr]
    sel_df = df[corr.index]
    return sel_df

def train_and_test(df, k):
    np.random.seed(1)
    num_df = df.select_dtypes(exclude='object')
    num_df = num_df.reindex(np.random.permutation(num_df.index))
    features = num_df.columns.drop('SalePrice')
    lr = LinearRegression()
    if k == 0:
        train = num_df[:int(len(num_df)/2)]
        test = df[int(len(num_df)/2):]
        lr.fit(train[features], train['SalePrice'])
        testP = lr.predict(test[features])
        rmse = mean_squared_error(test['SalePrice'], testP, squared=False)
        return rmse
    elif k == 1:
        train = num_df[:int(len(num_df)/2)]
        test = df[int(len(num_df)/2):]
        lr.fit(train[features], train['SalePrice'])
        p1 = lr.predict(test[features])
        rmse_1 = mean_squared_error(test['SalePrice'], p1, squared=False)
        lr.fit(test[features], test['SalePrice'])
        p2 = lr.predict(train[features])
        rmse_2 = mean_squared_error(train['SalePrice'], p2, squared=False)
        return np.mean([rmse_1, rmse_2])
    else:
        holder = list()
        kf = KFold(n_splits=k, shuffle=True)
        for train_index, test_index in kf.split(num_df):
            train = num_df.iloc[train_index]
            test = num_df.iloc[test_index]
            #print("TRAIN:", train_index, "TEST:", test_index)
            #print("TRAIN:", train, "TEST:", test)
            lr.fit(train[features], train['SalePrice'])
            testP = lr.predict(test[features])
            rmse = mean_squared_error(test['SalePrice'], testP, squared=False)
            holder.append(rmse)
        return np.mean(rmse)
```

### Feature Engineering


```python
clean_df = transform_features(df)
```


```python
clean_df
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
      <th>Order</th>
      <th>PID</th>
      <th>MS SubClass</th>
      <th>MS Zoning</th>
      <th>Lot Area</th>
      <th>Street</th>
      <th>Lot Shape</th>
      <th>Land Contour</th>
      <th>Utilities</th>
      <th>Lot Config</th>
      <th>Land Slope</th>
      <th>Neighborhood</th>
      <th>Condition 1</th>
      <th>Condition 2</th>
      <th>Bldg Type</th>
      <th>House Style</th>
      <th>Overall Qual</th>
      <th>Overall Cond</th>
      <th>Year Built</th>
      <th>Year Remod/Add</th>
      <th>Roof Style</th>
      <th>Roof Matl</th>
      <th>Exterior 1st</th>
      <th>Exterior 2nd</th>
      <th>Mas Vnr Area</th>
      <th>Exter Qual</th>
      <th>Exter Cond</th>
      <th>Foundation</th>
      <th>BsmtFin SF 1</th>
      <th>BsmtFin SF 2</th>
      <th>Bsmt Unf SF</th>
      <th>Total Bsmt SF</th>
      <th>Heating</th>
      <th>Heating QC</th>
      <th>Central Air</th>
      <th>1st Flr SF</th>
      <th>2nd Flr SF</th>
      <th>Low Qual Fin SF</th>
      <th>Gr Liv Area</th>
      <th>Bsmt Full Bath</th>
      <th>Bsmt Half Bath</th>
      <th>Full Bath</th>
      <th>Half Bath</th>
      <th>Bedroom AbvGr</th>
      <th>Kitchen AbvGr</th>
      <th>Kitchen Qual</th>
      <th>TotRms AbvGrd</th>
      <th>Functional</th>
      <th>Fireplaces</th>
      <th>Garage Cars</th>
      <th>Garage Area</th>
      <th>Paved Drive</th>
      <th>Wood Deck SF</th>
      <th>Open Porch SF</th>
      <th>Enclosed Porch</th>
      <th>3Ssn Porch</th>
      <th>Screen Porch</th>
      <th>Pool Area</th>
      <th>Misc Val</th>
      <th>Mo Sold</th>
      <th>Yr Sold</th>
      <th>Sale Type</th>
      <th>Sale Condition</th>
      <th>SalePrice</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1</td>
      <td>526301100</td>
      <td>20</td>
      <td>RL</td>
      <td>31770</td>
      <td>Pave</td>
      <td>IR1</td>
      <td>Lvl</td>
      <td>AllPub</td>
      <td>Corner</td>
      <td>Gtl</td>
      <td>NAmes</td>
      <td>Norm</td>
      <td>Norm</td>
      <td>1Fam</td>
      <td>1Story</td>
      <td>6</td>
      <td>5</td>
      <td>1960</td>
      <td>1960</td>
      <td>Hip</td>
      <td>CompShg</td>
      <td>BrkFace</td>
      <td>Plywood</td>
      <td>112.0</td>
      <td>TA</td>
      <td>TA</td>
      <td>CBlock</td>
      <td>639.0</td>
      <td>0.0</td>
      <td>441.0</td>
      <td>1080.0</td>
      <td>GasA</td>
      <td>Fa</td>
      <td>Y</td>
      <td>1656</td>
      <td>0</td>
      <td>0</td>
      <td>1656</td>
      <td>1.0</td>
      <td>0.0</td>
      <td>1</td>
      <td>0</td>
      <td>3</td>
      <td>1</td>
      <td>TA</td>
      <td>7</td>
      <td>Typ</td>
      <td>2</td>
      <td>2.0</td>
      <td>528.0</td>
      <td>P</td>
      <td>210</td>
      <td>62</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>5</td>
      <td>2010</td>
      <td>WD</td>
      <td>Normal</td>
      <td>215000</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2</td>
      <td>526350040</td>
      <td>20</td>
      <td>RH</td>
      <td>11622</td>
      <td>Pave</td>
      <td>Reg</td>
      <td>Lvl</td>
      <td>AllPub</td>
      <td>Inside</td>
      <td>Gtl</td>
      <td>NAmes</td>
      <td>Feedr</td>
      <td>Norm</td>
      <td>1Fam</td>
      <td>1Story</td>
      <td>5</td>
      <td>6</td>
      <td>1961</td>
      <td>1961</td>
      <td>Gable</td>
      <td>CompShg</td>
      <td>VinylSd</td>
      <td>VinylSd</td>
      <td>0.0</td>
      <td>TA</td>
      <td>TA</td>
      <td>CBlock</td>
      <td>468.0</td>
      <td>144.0</td>
      <td>270.0</td>
      <td>882.0</td>
      <td>GasA</td>
      <td>TA</td>
      <td>Y</td>
      <td>896</td>
      <td>0</td>
      <td>0</td>
      <td>896</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>1</td>
      <td>0</td>
      <td>2</td>
      <td>1</td>
      <td>TA</td>
      <td>5</td>
      <td>Typ</td>
      <td>0</td>
      <td>1.0</td>
      <td>730.0</td>
      <td>Y</td>
      <td>140</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>120</td>
      <td>0</td>
      <td>0</td>
      <td>6</td>
      <td>2010</td>
      <td>WD</td>
      <td>Normal</td>
      <td>105000</td>
    </tr>
    <tr>
      <th>2</th>
      <td>3</td>
      <td>526351010</td>
      <td>20</td>
      <td>RL</td>
      <td>14267</td>
      <td>Pave</td>
      <td>IR1</td>
      <td>Lvl</td>
      <td>AllPub</td>
      <td>Corner</td>
      <td>Gtl</td>
      <td>NAmes</td>
      <td>Norm</td>
      <td>Norm</td>
      <td>1Fam</td>
      <td>1Story</td>
      <td>6</td>
      <td>6</td>
      <td>1958</td>
      <td>1958</td>
      <td>Hip</td>
      <td>CompShg</td>
      <td>Wd Sdng</td>
      <td>Wd Sdng</td>
      <td>108.0</td>
      <td>TA</td>
      <td>TA</td>
      <td>CBlock</td>
      <td>923.0</td>
      <td>0.0</td>
      <td>406.0</td>
      <td>1329.0</td>
      <td>GasA</td>
      <td>TA</td>
      <td>Y</td>
      <td>1329</td>
      <td>0</td>
      <td>0</td>
      <td>1329</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>1</td>
      <td>1</td>
      <td>3</td>
      <td>1</td>
      <td>Gd</td>
      <td>6</td>
      <td>Typ</td>
      <td>0</td>
      <td>1.0</td>
      <td>312.0</td>
      <td>Y</td>
      <td>393</td>
      <td>36</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>12500</td>
      <td>6</td>
      <td>2010</td>
      <td>WD</td>
      <td>Normal</td>
      <td>172000</td>
    </tr>
    <tr>
      <th>3</th>
      <td>4</td>
      <td>526353030</td>
      <td>20</td>
      <td>RL</td>
      <td>11160</td>
      <td>Pave</td>
      <td>Reg</td>
      <td>Lvl</td>
      <td>AllPub</td>
      <td>Corner</td>
      <td>Gtl</td>
      <td>NAmes</td>
      <td>Norm</td>
      <td>Norm</td>
      <td>1Fam</td>
      <td>1Story</td>
      <td>7</td>
      <td>5</td>
      <td>1968</td>
      <td>1968</td>
      <td>Hip</td>
      <td>CompShg</td>
      <td>BrkFace</td>
      <td>BrkFace</td>
      <td>0.0</td>
      <td>Gd</td>
      <td>TA</td>
      <td>CBlock</td>
      <td>1065.0</td>
      <td>0.0</td>
      <td>1045.0</td>
      <td>2110.0</td>
      <td>GasA</td>
      <td>Ex</td>
      <td>Y</td>
      <td>2110</td>
      <td>0</td>
      <td>0</td>
      <td>2110</td>
      <td>1.0</td>
      <td>0.0</td>
      <td>2</td>
      <td>1</td>
      <td>3</td>
      <td>1</td>
      <td>Ex</td>
      <td>8</td>
      <td>Typ</td>
      <td>2</td>
      <td>2.0</td>
      <td>522.0</td>
      <td>Y</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>4</td>
      <td>2010</td>
      <td>WD</td>
      <td>Normal</td>
      <td>244000</td>
    </tr>
    <tr>
      <th>4</th>
      <td>5</td>
      <td>527105010</td>
      <td>60</td>
      <td>RL</td>
      <td>13830</td>
      <td>Pave</td>
      <td>IR1</td>
      <td>Lvl</td>
      <td>AllPub</td>
      <td>Inside</td>
      <td>Gtl</td>
      <td>Gilbert</td>
      <td>Norm</td>
      <td>Norm</td>
      <td>1Fam</td>
      <td>2Story</td>
      <td>5</td>
      <td>5</td>
      <td>1997</td>
      <td>1998</td>
      <td>Gable</td>
      <td>CompShg</td>
      <td>VinylSd</td>
      <td>VinylSd</td>
      <td>0.0</td>
      <td>TA</td>
      <td>TA</td>
      <td>PConc</td>
      <td>791.0</td>
      <td>0.0</td>
      <td>137.0</td>
      <td>928.0</td>
      <td>GasA</td>
      <td>Gd</td>
      <td>Y</td>
      <td>928</td>
      <td>701</td>
      <td>0</td>
      <td>1629</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>2</td>
      <td>1</td>
      <td>3</td>
      <td>1</td>
      <td>TA</td>
      <td>6</td>
      <td>Typ</td>
      <td>1</td>
      <td>2.0</td>
      <td>482.0</td>
      <td>Y</td>
      <td>212</td>
      <td>34</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>3</td>
      <td>2010</td>
      <td>WD</td>
      <td>Normal</td>
      <td>189900</td>
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
      <td>...</td>
    </tr>
    <tr>
      <th>2925</th>
      <td>2926</td>
      <td>923275080</td>
      <td>80</td>
      <td>RL</td>
      <td>7937</td>
      <td>Pave</td>
      <td>IR1</td>
      <td>Lvl</td>
      <td>AllPub</td>
      <td>CulDSac</td>
      <td>Gtl</td>
      <td>Mitchel</td>
      <td>Norm</td>
      <td>Norm</td>
      <td>1Fam</td>
      <td>SLvl</td>
      <td>6</td>
      <td>6</td>
      <td>1984</td>
      <td>1984</td>
      <td>Gable</td>
      <td>CompShg</td>
      <td>HdBoard</td>
      <td>HdBoard</td>
      <td>0.0</td>
      <td>TA</td>
      <td>TA</td>
      <td>CBlock</td>
      <td>819.0</td>
      <td>0.0</td>
      <td>184.0</td>
      <td>1003.0</td>
      <td>GasA</td>
      <td>TA</td>
      <td>Y</td>
      <td>1003</td>
      <td>0</td>
      <td>0</td>
      <td>1003</td>
      <td>1.0</td>
      <td>0.0</td>
      <td>1</td>
      <td>0</td>
      <td>3</td>
      <td>1</td>
      <td>TA</td>
      <td>6</td>
      <td>Typ</td>
      <td>0</td>
      <td>2.0</td>
      <td>588.0</td>
      <td>Y</td>
      <td>120</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>3</td>
      <td>2006</td>
      <td>WD</td>
      <td>Normal</td>
      <td>142500</td>
    </tr>
    <tr>
      <th>2926</th>
      <td>2927</td>
      <td>923276100</td>
      <td>20</td>
      <td>RL</td>
      <td>8885</td>
      <td>Pave</td>
      <td>IR1</td>
      <td>Low</td>
      <td>AllPub</td>
      <td>Inside</td>
      <td>Mod</td>
      <td>Mitchel</td>
      <td>Norm</td>
      <td>Norm</td>
      <td>1Fam</td>
      <td>1Story</td>
      <td>5</td>
      <td>5</td>
      <td>1983</td>
      <td>1983</td>
      <td>Gable</td>
      <td>CompShg</td>
      <td>HdBoard</td>
      <td>HdBoard</td>
      <td>0.0</td>
      <td>TA</td>
      <td>TA</td>
      <td>CBlock</td>
      <td>301.0</td>
      <td>324.0</td>
      <td>239.0</td>
      <td>864.0</td>
      <td>GasA</td>
      <td>TA</td>
      <td>Y</td>
      <td>902</td>
      <td>0</td>
      <td>0</td>
      <td>902</td>
      <td>1.0</td>
      <td>0.0</td>
      <td>1</td>
      <td>0</td>
      <td>2</td>
      <td>1</td>
      <td>TA</td>
      <td>5</td>
      <td>Typ</td>
      <td>0</td>
      <td>2.0</td>
      <td>484.0</td>
      <td>Y</td>
      <td>164</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>6</td>
      <td>2006</td>
      <td>WD</td>
      <td>Normal</td>
      <td>131000</td>
    </tr>
    <tr>
      <th>2927</th>
      <td>2928</td>
      <td>923400125</td>
      <td>85</td>
      <td>RL</td>
      <td>10441</td>
      <td>Pave</td>
      <td>Reg</td>
      <td>Lvl</td>
      <td>AllPub</td>
      <td>Inside</td>
      <td>Gtl</td>
      <td>Mitchel</td>
      <td>Norm</td>
      <td>Norm</td>
      <td>1Fam</td>
      <td>SFoyer</td>
      <td>5</td>
      <td>5</td>
      <td>1992</td>
      <td>1992</td>
      <td>Gable</td>
      <td>CompShg</td>
      <td>HdBoard</td>
      <td>Wd Shng</td>
      <td>0.0</td>
      <td>TA</td>
      <td>TA</td>
      <td>PConc</td>
      <td>337.0</td>
      <td>0.0</td>
      <td>575.0</td>
      <td>912.0</td>
      <td>GasA</td>
      <td>TA</td>
      <td>Y</td>
      <td>970</td>
      <td>0</td>
      <td>0</td>
      <td>970</td>
      <td>0.0</td>
      <td>1.0</td>
      <td>1</td>
      <td>0</td>
      <td>3</td>
      <td>1</td>
      <td>TA</td>
      <td>6</td>
      <td>Typ</td>
      <td>0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>Y</td>
      <td>80</td>
      <td>32</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>700</td>
      <td>7</td>
      <td>2006</td>
      <td>WD</td>
      <td>Normal</td>
      <td>132000</td>
    </tr>
    <tr>
      <th>2928</th>
      <td>2929</td>
      <td>924100070</td>
      <td>20</td>
      <td>RL</td>
      <td>10010</td>
      <td>Pave</td>
      <td>Reg</td>
      <td>Lvl</td>
      <td>AllPub</td>
      <td>Inside</td>
      <td>Mod</td>
      <td>Mitchel</td>
      <td>Norm</td>
      <td>Norm</td>
      <td>1Fam</td>
      <td>1Story</td>
      <td>5</td>
      <td>5</td>
      <td>1974</td>
      <td>1975</td>
      <td>Gable</td>
      <td>CompShg</td>
      <td>HdBoard</td>
      <td>HdBoard</td>
      <td>0.0</td>
      <td>TA</td>
      <td>TA</td>
      <td>CBlock</td>
      <td>1071.0</td>
      <td>123.0</td>
      <td>195.0</td>
      <td>1389.0</td>
      <td>GasA</td>
      <td>Gd</td>
      <td>Y</td>
      <td>1389</td>
      <td>0</td>
      <td>0</td>
      <td>1389</td>
      <td>1.0</td>
      <td>0.0</td>
      <td>1</td>
      <td>0</td>
      <td>2</td>
      <td>1</td>
      <td>TA</td>
      <td>6</td>
      <td>Typ</td>
      <td>1</td>
      <td>2.0</td>
      <td>418.0</td>
      <td>Y</td>
      <td>240</td>
      <td>38</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>4</td>
      <td>2006</td>
      <td>WD</td>
      <td>Normal</td>
      <td>170000</td>
    </tr>
    <tr>
      <th>2929</th>
      <td>2930</td>
      <td>924151050</td>
      <td>60</td>
      <td>RL</td>
      <td>9627</td>
      <td>Pave</td>
      <td>Reg</td>
      <td>Lvl</td>
      <td>AllPub</td>
      <td>Inside</td>
      <td>Mod</td>
      <td>Mitchel</td>
      <td>Norm</td>
      <td>Norm</td>
      <td>1Fam</td>
      <td>2Story</td>
      <td>7</td>
      <td>5</td>
      <td>1993</td>
      <td>1994</td>
      <td>Gable</td>
      <td>CompShg</td>
      <td>HdBoard</td>
      <td>HdBoard</td>
      <td>94.0</td>
      <td>TA</td>
      <td>TA</td>
      <td>PConc</td>
      <td>758.0</td>
      <td>0.0</td>
      <td>238.0</td>
      <td>996.0</td>
      <td>GasA</td>
      <td>Ex</td>
      <td>Y</td>
      <td>996</td>
      <td>1004</td>
      <td>0</td>
      <td>2000</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>2</td>
      <td>1</td>
      <td>3</td>
      <td>1</td>
      <td>TA</td>
      <td>9</td>
      <td>Typ</td>
      <td>1</td>
      <td>3.0</td>
      <td>650.0</td>
      <td>Y</td>
      <td>190</td>
      <td>48</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>11</td>
      <td>2006</td>
      <td>WD</td>
      <td>Normal</td>
      <td>188000</td>
    </tr>
  </tbody>
</table>
<p>2930 rows × 64 columns</p>
</div>




```python
# add new columns
clean_df['Year Since Sold'] = clean_df['Yr Sold'] - clean_df['Year Built']
clean_df['Year Since Re'] = clean_df['Yr Sold'] - clean_df['Year Remod/Add']
```


```python
# keep only valid values from these columns
clean_df = clean_df[(clean_df['Year Since Sold'] > 0) &
                   (clean_df['Year Since Re'] > 0)]
```


```python
# keep only relevant features
clean_df.drop(['Mo Sold', 'Yr Sold', 'Sale Type', 'Sale Condition', 'PID', 'Order'], 
              axis=1, inplace=True)
```

    /Users/MimiHMB/anaconda3/lib/python3.7/site-packages/pandas/core/frame.py:3997: SettingWithCopyWarning: 
    A value is trying to be set on a copy of a slice from a DataFrame
    
    See the caveats in the documentation: https://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html#returning-a-view-versus-a-copy
      errors=errors,



```python
clean_df
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
      <th>MS SubClass</th>
      <th>MS Zoning</th>
      <th>Lot Area</th>
      <th>Street</th>
      <th>Lot Shape</th>
      <th>Land Contour</th>
      <th>Utilities</th>
      <th>Lot Config</th>
      <th>Land Slope</th>
      <th>Neighborhood</th>
      <th>Condition 1</th>
      <th>Condition 2</th>
      <th>Bldg Type</th>
      <th>House Style</th>
      <th>Overall Qual</th>
      <th>Overall Cond</th>
      <th>Year Built</th>
      <th>Year Remod/Add</th>
      <th>Roof Style</th>
      <th>Roof Matl</th>
      <th>Exterior 1st</th>
      <th>Exterior 2nd</th>
      <th>Mas Vnr Area</th>
      <th>Exter Qual</th>
      <th>Exter Cond</th>
      <th>Foundation</th>
      <th>BsmtFin SF 1</th>
      <th>BsmtFin SF 2</th>
      <th>Bsmt Unf SF</th>
      <th>Total Bsmt SF</th>
      <th>Heating</th>
      <th>Heating QC</th>
      <th>Central Air</th>
      <th>1st Flr SF</th>
      <th>2nd Flr SF</th>
      <th>Low Qual Fin SF</th>
      <th>Gr Liv Area</th>
      <th>Bsmt Full Bath</th>
      <th>Bsmt Half Bath</th>
      <th>Full Bath</th>
      <th>Half Bath</th>
      <th>Bedroom AbvGr</th>
      <th>Kitchen AbvGr</th>
      <th>Kitchen Qual</th>
      <th>TotRms AbvGrd</th>
      <th>Functional</th>
      <th>Fireplaces</th>
      <th>Garage Cars</th>
      <th>Garage Area</th>
      <th>Paved Drive</th>
      <th>Wood Deck SF</th>
      <th>Open Porch SF</th>
      <th>Enclosed Porch</th>
      <th>3Ssn Porch</th>
      <th>Screen Porch</th>
      <th>Pool Area</th>
      <th>Misc Val</th>
      <th>SalePrice</th>
      <th>Year Since Sold</th>
      <th>Year Since Re</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>20</td>
      <td>RL</td>
      <td>31770</td>
      <td>Pave</td>
      <td>IR1</td>
      <td>Lvl</td>
      <td>AllPub</td>
      <td>Corner</td>
      <td>Gtl</td>
      <td>NAmes</td>
      <td>Norm</td>
      <td>Norm</td>
      <td>1Fam</td>
      <td>1Story</td>
      <td>6</td>
      <td>5</td>
      <td>1960</td>
      <td>1960</td>
      <td>Hip</td>
      <td>CompShg</td>
      <td>BrkFace</td>
      <td>Plywood</td>
      <td>112.0</td>
      <td>TA</td>
      <td>TA</td>
      <td>CBlock</td>
      <td>639.0</td>
      <td>0.0</td>
      <td>441.0</td>
      <td>1080.0</td>
      <td>GasA</td>
      <td>Fa</td>
      <td>Y</td>
      <td>1656</td>
      <td>0</td>
      <td>0</td>
      <td>1656</td>
      <td>1.0</td>
      <td>0.0</td>
      <td>1</td>
      <td>0</td>
      <td>3</td>
      <td>1</td>
      <td>TA</td>
      <td>7</td>
      <td>Typ</td>
      <td>2</td>
      <td>2.0</td>
      <td>528.0</td>
      <td>P</td>
      <td>210</td>
      <td>62</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>215000</td>
      <td>50</td>
      <td>50</td>
    </tr>
    <tr>
      <th>1</th>
      <td>20</td>
      <td>RH</td>
      <td>11622</td>
      <td>Pave</td>
      <td>Reg</td>
      <td>Lvl</td>
      <td>AllPub</td>
      <td>Inside</td>
      <td>Gtl</td>
      <td>NAmes</td>
      <td>Feedr</td>
      <td>Norm</td>
      <td>1Fam</td>
      <td>1Story</td>
      <td>5</td>
      <td>6</td>
      <td>1961</td>
      <td>1961</td>
      <td>Gable</td>
      <td>CompShg</td>
      <td>VinylSd</td>
      <td>VinylSd</td>
      <td>0.0</td>
      <td>TA</td>
      <td>TA</td>
      <td>CBlock</td>
      <td>468.0</td>
      <td>144.0</td>
      <td>270.0</td>
      <td>882.0</td>
      <td>GasA</td>
      <td>TA</td>
      <td>Y</td>
      <td>896</td>
      <td>0</td>
      <td>0</td>
      <td>896</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>1</td>
      <td>0</td>
      <td>2</td>
      <td>1</td>
      <td>TA</td>
      <td>5</td>
      <td>Typ</td>
      <td>0</td>
      <td>1.0</td>
      <td>730.0</td>
      <td>Y</td>
      <td>140</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>120</td>
      <td>0</td>
      <td>0</td>
      <td>105000</td>
      <td>49</td>
      <td>49</td>
    </tr>
    <tr>
      <th>2</th>
      <td>20</td>
      <td>RL</td>
      <td>14267</td>
      <td>Pave</td>
      <td>IR1</td>
      <td>Lvl</td>
      <td>AllPub</td>
      <td>Corner</td>
      <td>Gtl</td>
      <td>NAmes</td>
      <td>Norm</td>
      <td>Norm</td>
      <td>1Fam</td>
      <td>1Story</td>
      <td>6</td>
      <td>6</td>
      <td>1958</td>
      <td>1958</td>
      <td>Hip</td>
      <td>CompShg</td>
      <td>Wd Sdng</td>
      <td>Wd Sdng</td>
      <td>108.0</td>
      <td>TA</td>
      <td>TA</td>
      <td>CBlock</td>
      <td>923.0</td>
      <td>0.0</td>
      <td>406.0</td>
      <td>1329.0</td>
      <td>GasA</td>
      <td>TA</td>
      <td>Y</td>
      <td>1329</td>
      <td>0</td>
      <td>0</td>
      <td>1329</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>1</td>
      <td>1</td>
      <td>3</td>
      <td>1</td>
      <td>Gd</td>
      <td>6</td>
      <td>Typ</td>
      <td>0</td>
      <td>1.0</td>
      <td>312.0</td>
      <td>Y</td>
      <td>393</td>
      <td>36</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>12500</td>
      <td>172000</td>
      <td>52</td>
      <td>52</td>
    </tr>
    <tr>
      <th>3</th>
      <td>20</td>
      <td>RL</td>
      <td>11160</td>
      <td>Pave</td>
      <td>Reg</td>
      <td>Lvl</td>
      <td>AllPub</td>
      <td>Corner</td>
      <td>Gtl</td>
      <td>NAmes</td>
      <td>Norm</td>
      <td>Norm</td>
      <td>1Fam</td>
      <td>1Story</td>
      <td>7</td>
      <td>5</td>
      <td>1968</td>
      <td>1968</td>
      <td>Hip</td>
      <td>CompShg</td>
      <td>BrkFace</td>
      <td>BrkFace</td>
      <td>0.0</td>
      <td>Gd</td>
      <td>TA</td>
      <td>CBlock</td>
      <td>1065.0</td>
      <td>0.0</td>
      <td>1045.0</td>
      <td>2110.0</td>
      <td>GasA</td>
      <td>Ex</td>
      <td>Y</td>
      <td>2110</td>
      <td>0</td>
      <td>0</td>
      <td>2110</td>
      <td>1.0</td>
      <td>0.0</td>
      <td>2</td>
      <td>1</td>
      <td>3</td>
      <td>1</td>
      <td>Ex</td>
      <td>8</td>
      <td>Typ</td>
      <td>2</td>
      <td>2.0</td>
      <td>522.0</td>
      <td>Y</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>244000</td>
      <td>42</td>
      <td>42</td>
    </tr>
    <tr>
      <th>4</th>
      <td>60</td>
      <td>RL</td>
      <td>13830</td>
      <td>Pave</td>
      <td>IR1</td>
      <td>Lvl</td>
      <td>AllPub</td>
      <td>Inside</td>
      <td>Gtl</td>
      <td>Gilbert</td>
      <td>Norm</td>
      <td>Norm</td>
      <td>1Fam</td>
      <td>2Story</td>
      <td>5</td>
      <td>5</td>
      <td>1997</td>
      <td>1998</td>
      <td>Gable</td>
      <td>CompShg</td>
      <td>VinylSd</td>
      <td>VinylSd</td>
      <td>0.0</td>
      <td>TA</td>
      <td>TA</td>
      <td>PConc</td>
      <td>791.0</td>
      <td>0.0</td>
      <td>137.0</td>
      <td>928.0</td>
      <td>GasA</td>
      <td>Gd</td>
      <td>Y</td>
      <td>928</td>
      <td>701</td>
      <td>0</td>
      <td>1629</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>2</td>
      <td>1</td>
      <td>3</td>
      <td>1</td>
      <td>TA</td>
      <td>6</td>
      <td>Typ</td>
      <td>1</td>
      <td>2.0</td>
      <td>482.0</td>
      <td>Y</td>
      <td>212</td>
      <td>34</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>189900</td>
      <td>13</td>
      <td>12</td>
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
      <th>2925</th>
      <td>80</td>
      <td>RL</td>
      <td>7937</td>
      <td>Pave</td>
      <td>IR1</td>
      <td>Lvl</td>
      <td>AllPub</td>
      <td>CulDSac</td>
      <td>Gtl</td>
      <td>Mitchel</td>
      <td>Norm</td>
      <td>Norm</td>
      <td>1Fam</td>
      <td>SLvl</td>
      <td>6</td>
      <td>6</td>
      <td>1984</td>
      <td>1984</td>
      <td>Gable</td>
      <td>CompShg</td>
      <td>HdBoard</td>
      <td>HdBoard</td>
      <td>0.0</td>
      <td>TA</td>
      <td>TA</td>
      <td>CBlock</td>
      <td>819.0</td>
      <td>0.0</td>
      <td>184.0</td>
      <td>1003.0</td>
      <td>GasA</td>
      <td>TA</td>
      <td>Y</td>
      <td>1003</td>
      <td>0</td>
      <td>0</td>
      <td>1003</td>
      <td>1.0</td>
      <td>0.0</td>
      <td>1</td>
      <td>0</td>
      <td>3</td>
      <td>1</td>
      <td>TA</td>
      <td>6</td>
      <td>Typ</td>
      <td>0</td>
      <td>2.0</td>
      <td>588.0</td>
      <td>Y</td>
      <td>120</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>142500</td>
      <td>22</td>
      <td>22</td>
    </tr>
    <tr>
      <th>2926</th>
      <td>20</td>
      <td>RL</td>
      <td>8885</td>
      <td>Pave</td>
      <td>IR1</td>
      <td>Low</td>
      <td>AllPub</td>
      <td>Inside</td>
      <td>Mod</td>
      <td>Mitchel</td>
      <td>Norm</td>
      <td>Norm</td>
      <td>1Fam</td>
      <td>1Story</td>
      <td>5</td>
      <td>5</td>
      <td>1983</td>
      <td>1983</td>
      <td>Gable</td>
      <td>CompShg</td>
      <td>HdBoard</td>
      <td>HdBoard</td>
      <td>0.0</td>
      <td>TA</td>
      <td>TA</td>
      <td>CBlock</td>
      <td>301.0</td>
      <td>324.0</td>
      <td>239.0</td>
      <td>864.0</td>
      <td>GasA</td>
      <td>TA</td>
      <td>Y</td>
      <td>902</td>
      <td>0</td>
      <td>0</td>
      <td>902</td>
      <td>1.0</td>
      <td>0.0</td>
      <td>1</td>
      <td>0</td>
      <td>2</td>
      <td>1</td>
      <td>TA</td>
      <td>5</td>
      <td>Typ</td>
      <td>0</td>
      <td>2.0</td>
      <td>484.0</td>
      <td>Y</td>
      <td>164</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>131000</td>
      <td>23</td>
      <td>23</td>
    </tr>
    <tr>
      <th>2927</th>
      <td>85</td>
      <td>RL</td>
      <td>10441</td>
      <td>Pave</td>
      <td>Reg</td>
      <td>Lvl</td>
      <td>AllPub</td>
      <td>Inside</td>
      <td>Gtl</td>
      <td>Mitchel</td>
      <td>Norm</td>
      <td>Norm</td>
      <td>1Fam</td>
      <td>SFoyer</td>
      <td>5</td>
      <td>5</td>
      <td>1992</td>
      <td>1992</td>
      <td>Gable</td>
      <td>CompShg</td>
      <td>HdBoard</td>
      <td>Wd Shng</td>
      <td>0.0</td>
      <td>TA</td>
      <td>TA</td>
      <td>PConc</td>
      <td>337.0</td>
      <td>0.0</td>
      <td>575.0</td>
      <td>912.0</td>
      <td>GasA</td>
      <td>TA</td>
      <td>Y</td>
      <td>970</td>
      <td>0</td>
      <td>0</td>
      <td>970</td>
      <td>0.0</td>
      <td>1.0</td>
      <td>1</td>
      <td>0</td>
      <td>3</td>
      <td>1</td>
      <td>TA</td>
      <td>6</td>
      <td>Typ</td>
      <td>0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>Y</td>
      <td>80</td>
      <td>32</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>700</td>
      <td>132000</td>
      <td>14</td>
      <td>14</td>
    </tr>
    <tr>
      <th>2928</th>
      <td>20</td>
      <td>RL</td>
      <td>10010</td>
      <td>Pave</td>
      <td>Reg</td>
      <td>Lvl</td>
      <td>AllPub</td>
      <td>Inside</td>
      <td>Mod</td>
      <td>Mitchel</td>
      <td>Norm</td>
      <td>Norm</td>
      <td>1Fam</td>
      <td>1Story</td>
      <td>5</td>
      <td>5</td>
      <td>1974</td>
      <td>1975</td>
      <td>Gable</td>
      <td>CompShg</td>
      <td>HdBoard</td>
      <td>HdBoard</td>
      <td>0.0</td>
      <td>TA</td>
      <td>TA</td>
      <td>CBlock</td>
      <td>1071.0</td>
      <td>123.0</td>
      <td>195.0</td>
      <td>1389.0</td>
      <td>GasA</td>
      <td>Gd</td>
      <td>Y</td>
      <td>1389</td>
      <td>0</td>
      <td>0</td>
      <td>1389</td>
      <td>1.0</td>
      <td>0.0</td>
      <td>1</td>
      <td>0</td>
      <td>2</td>
      <td>1</td>
      <td>TA</td>
      <td>6</td>
      <td>Typ</td>
      <td>1</td>
      <td>2.0</td>
      <td>418.0</td>
      <td>Y</td>
      <td>240</td>
      <td>38</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>170000</td>
      <td>32</td>
      <td>31</td>
    </tr>
    <tr>
      <th>2929</th>
      <td>60</td>
      <td>RL</td>
      <td>9627</td>
      <td>Pave</td>
      <td>Reg</td>
      <td>Lvl</td>
      <td>AllPub</td>
      <td>Inside</td>
      <td>Mod</td>
      <td>Mitchel</td>
      <td>Norm</td>
      <td>Norm</td>
      <td>1Fam</td>
      <td>2Story</td>
      <td>7</td>
      <td>5</td>
      <td>1993</td>
      <td>1994</td>
      <td>Gable</td>
      <td>CompShg</td>
      <td>HdBoard</td>
      <td>HdBoard</td>
      <td>94.0</td>
      <td>TA</td>
      <td>TA</td>
      <td>PConc</td>
      <td>758.0</td>
      <td>0.0</td>
      <td>238.0</td>
      <td>996.0</td>
      <td>GasA</td>
      <td>Ex</td>
      <td>Y</td>
      <td>996</td>
      <td>1004</td>
      <td>0</td>
      <td>2000</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>2</td>
      <td>1</td>
      <td>3</td>
      <td>1</td>
      <td>TA</td>
      <td>9</td>
      <td>Typ</td>
      <td>1</td>
      <td>3.0</td>
      <td>650.0</td>
      <td>Y</td>
      <td>190</td>
      <td>48</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>188000</td>
      <td>13</td>
      <td>12</td>
    </tr>
  </tbody>
</table>
<p>2689 rows × 60 columns</p>
</div>




```python
# recheck if there is any missing value
any(clean_df.isnull().sum() > 0)
```




    False



### Feature Selection


```python
sel_df = select_features(clean_df, 0.4)
```


```python
sel_df
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
      <th>SalePrice</th>
      <th>Overall Qual</th>
      <th>Gr Liv Area</th>
      <th>Total Bsmt SF</th>
      <th>1st Flr SF</th>
      <th>Garage Cars</th>
      <th>Garage Area</th>
      <th>Full Bath</th>
      <th>Year Built</th>
      <th>Year Since Sold</th>
      <th>Year Since Re</th>
      <th>Year Remod/Add</th>
      <th>Fireplaces</th>
      <th>TotRms AbvGrd</th>
      <th>Mas Vnr Area</th>
      <th>BsmtFin SF 1</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>215000</td>
      <td>6</td>
      <td>1656</td>
      <td>1080.0</td>
      <td>1656</td>
      <td>2.0</td>
      <td>528.0</td>
      <td>1</td>
      <td>1960</td>
      <td>50</td>
      <td>50</td>
      <td>1960</td>
      <td>2</td>
      <td>7</td>
      <td>112.0</td>
      <td>639.0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>105000</td>
      <td>5</td>
      <td>896</td>
      <td>882.0</td>
      <td>896</td>
      <td>1.0</td>
      <td>730.0</td>
      <td>1</td>
      <td>1961</td>
      <td>49</td>
      <td>49</td>
      <td>1961</td>
      <td>0</td>
      <td>5</td>
      <td>0.0</td>
      <td>468.0</td>
    </tr>
    <tr>
      <th>2</th>
      <td>172000</td>
      <td>6</td>
      <td>1329</td>
      <td>1329.0</td>
      <td>1329</td>
      <td>1.0</td>
      <td>312.0</td>
      <td>1</td>
      <td>1958</td>
      <td>52</td>
      <td>52</td>
      <td>1958</td>
      <td>0</td>
      <td>6</td>
      <td>108.0</td>
      <td>923.0</td>
    </tr>
    <tr>
      <th>3</th>
      <td>244000</td>
      <td>7</td>
      <td>2110</td>
      <td>2110.0</td>
      <td>2110</td>
      <td>2.0</td>
      <td>522.0</td>
      <td>2</td>
      <td>1968</td>
      <td>42</td>
      <td>42</td>
      <td>1968</td>
      <td>2</td>
      <td>8</td>
      <td>0.0</td>
      <td>1065.0</td>
    </tr>
    <tr>
      <th>4</th>
      <td>189900</td>
      <td>5</td>
      <td>1629</td>
      <td>928.0</td>
      <td>928</td>
      <td>2.0</td>
      <td>482.0</td>
      <td>2</td>
      <td>1997</td>
      <td>13</td>
      <td>12</td>
      <td>1998</td>
      <td>1</td>
      <td>6</td>
      <td>0.0</td>
      <td>791.0</td>
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
      <th>2925</th>
      <td>142500</td>
      <td>6</td>
      <td>1003</td>
      <td>1003.0</td>
      <td>1003</td>
      <td>2.0</td>
      <td>588.0</td>
      <td>1</td>
      <td>1984</td>
      <td>22</td>
      <td>22</td>
      <td>1984</td>
      <td>0</td>
      <td>6</td>
      <td>0.0</td>
      <td>819.0</td>
    </tr>
    <tr>
      <th>2926</th>
      <td>131000</td>
      <td>5</td>
      <td>902</td>
      <td>864.0</td>
      <td>902</td>
      <td>2.0</td>
      <td>484.0</td>
      <td>1</td>
      <td>1983</td>
      <td>23</td>
      <td>23</td>
      <td>1983</td>
      <td>0</td>
      <td>5</td>
      <td>0.0</td>
      <td>301.0</td>
    </tr>
    <tr>
      <th>2927</th>
      <td>132000</td>
      <td>5</td>
      <td>970</td>
      <td>912.0</td>
      <td>970</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>1</td>
      <td>1992</td>
      <td>14</td>
      <td>14</td>
      <td>1992</td>
      <td>0</td>
      <td>6</td>
      <td>0.0</td>
      <td>337.0</td>
    </tr>
    <tr>
      <th>2928</th>
      <td>170000</td>
      <td>5</td>
      <td>1389</td>
      <td>1389.0</td>
      <td>1389</td>
      <td>2.0</td>
      <td>418.0</td>
      <td>1</td>
      <td>1974</td>
      <td>32</td>
      <td>31</td>
      <td>1975</td>
      <td>1</td>
      <td>6</td>
      <td>0.0</td>
      <td>1071.0</td>
    </tr>
    <tr>
      <th>2929</th>
      <td>188000</td>
      <td>7</td>
      <td>2000</td>
      <td>996.0</td>
      <td>996</td>
      <td>3.0</td>
      <td>650.0</td>
      <td>2</td>
      <td>1993</td>
      <td>13</td>
      <td>12</td>
      <td>1994</td>
      <td>1</td>
      <td>9</td>
      <td>94.0</td>
      <td>758.0</td>
    </tr>
  </tbody>
</table>
<p>2689 rows × 16 columns</p>
</div>




```python
# make a dictionary of value counts for all columns in clean_df (the df resulted from initial aggregation)
holder = dict()
for i in clean_df.columns:
    holder[i] = len(clean_df[i].value_counts())
```


```python
holder
```




    {'MS SubClass': 16,
     'MS Zoning': 7,
     'Lot Area': 1795,
     'Street': 2,
     'Lot Shape': 4,
     'Land Contour': 4,
     'Utilities': 3,
     'Lot Config': 5,
     'Land Slope': 3,
     'Neighborhood': 28,
     'Condition 1': 9,
     'Condition 2': 8,
     'Bldg Type': 5,
     'House Style': 8,
     'Overall Qual': 10,
     'Overall Cond': 9,
     'Year Built': 117,
     'Year Remod/Add': 60,
     'Roof Style': 6,
     'Roof Matl': 7,
     'Exterior 1st': 16,
     'Exterior 2nd': 16,
     'Mas Vnr Area': 413,
     'Exter Qual': 4,
     'Exter Cond': 5,
     'Foundation': 6,
     'BsmtFin SF 1': 942,
     'BsmtFin SF 2': 273,
     'Bsmt Unf SF': 1060,
     'Total Bsmt SF': 978,
     'Heating': 6,
     'Heating QC': 5,
     'Central Air': 2,
     '1st Flr SF': 1028,
     '2nd Flr SF': 597,
     'Low Qual Fin SF': 36,
     'Gr Liv Area': 1226,
     'Bsmt Full Bath': 4,
     'Bsmt Half Bath': 3,
     'Full Bath': 5,
     'Half Bath': 3,
     'Bedroom AbvGr': 8,
     'Kitchen AbvGr': 4,
     'Kitchen Qual': 5,
     'TotRms AbvGrd': 13,
     'Functional': 8,
     'Fireplaces': 5,
     'Garage Cars': 6,
     'Garage Area': 570,
     'Paved Drive': 3,
     'Wood Deck SF': 376,
     'Open Porch SF': 238,
     'Enclosed Porch': 181,
     '3Ssn Porch': 27,
     'Screen Porch': 119,
     'Pool Area': 13,
     'Misc Val': 37,
     'SalePrice': 864,
     'Year Since Sold': 126,
     'Year Since Re': 60}




```python
# nominal columns given by the data set description
nominal_features = ["PID", "MS SubClass", "MS Zoning", "Street", "Alley", "Land Contour", "Lot Config", "Neighborhood", 
                    "Condition 1", "Condition 2", "Bldg Type", "House Style", "Roof Style", "Roof Matl", "Exterior 1st", 
                    "Exterior 2nd", "Mas Vnr Type", "Foundation", "Heating", "Central Air", "Garage Type", 
                    "Misc Feature", "Sale Type", "Sale Condition"]
```


```python
# choose only nominal features that have at most 10 unique values
to_cat = list()
for i in holder.keys():
    if (i in nominal_features) & (holder[i] <= 10):
        to_cat.append(i)
to_cat
```




    ['MS Zoning',
     'Street',
     'Land Contour',
     'Lot Config',
     'Condition 1',
     'Condition 2',
     'Bldg Type',
     'House Style',
     'Roof Style',
     'Roof Matl',
     'Foundation',
     'Heating',
     'Central Air']




```python
# categorize these nominal features and make corresponding dummies
for i in to_cat:
    sel_df[i] = clean_df[i].astype('category')
    sel_df = pd.concat([sel_df, 
                        pd.get_dummies(sel_df.select_dtypes(include=['category']))], axis=1).drop(i, axis=1)
```

    /Users/MimiHMB/anaconda3/lib/python3.7/site-packages/ipykernel_launcher.py:3: SettingWithCopyWarning: 
    A value is trying to be set on a copy of a slice from a DataFrame.
    Try using .loc[row_indexer,col_indexer] = value instead
    
    See the caveats in the documentation: https://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html#returning-a-view-versus-a-copy
      This is separate from the ipykernel package so we can avoid doing imports until



```python
sel_df
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
      <th>SalePrice</th>
      <th>Overall Qual</th>
      <th>Gr Liv Area</th>
      <th>Total Bsmt SF</th>
      <th>1st Flr SF</th>
      <th>Garage Cars</th>
      <th>Garage Area</th>
      <th>Full Bath</th>
      <th>Year Built</th>
      <th>Year Since Sold</th>
      <th>Year Since Re</th>
      <th>Year Remod/Add</th>
      <th>Fireplaces</th>
      <th>TotRms AbvGrd</th>
      <th>Mas Vnr Area</th>
      <th>BsmtFin SF 1</th>
      <th>MS Zoning_A (agr)</th>
      <th>MS Zoning_C (all)</th>
      <th>MS Zoning_FV</th>
      <th>MS Zoning_I (all)</th>
      <th>MS Zoning_RH</th>
      <th>MS Zoning_RL</th>
      <th>MS Zoning_RM</th>
      <th>Street_Grvl</th>
      <th>Street_Pave</th>
      <th>Land Contour_Bnk</th>
      <th>Land Contour_HLS</th>
      <th>Land Contour_Low</th>
      <th>Land Contour_Lvl</th>
      <th>Lot Config_Corner</th>
      <th>Lot Config_CulDSac</th>
      <th>Lot Config_FR2</th>
      <th>Lot Config_FR3</th>
      <th>Lot Config_Inside</th>
      <th>Condition 1_Artery</th>
      <th>Condition 1_Feedr</th>
      <th>Condition 1_Norm</th>
      <th>Condition 1_PosA</th>
      <th>Condition 1_PosN</th>
      <th>Condition 1_RRAe</th>
      <th>Condition 1_RRAn</th>
      <th>Condition 1_RRNe</th>
      <th>Condition 1_RRNn</th>
      <th>Condition 2_Artery</th>
      <th>Condition 2_Feedr</th>
      <th>Condition 2_Norm</th>
      <th>Condition 2_PosA</th>
      <th>Condition 2_PosN</th>
      <th>Condition 2_RRAe</th>
      <th>Condition 2_RRAn</th>
      <th>Condition 2_RRNn</th>
      <th>Bldg Type_1Fam</th>
      <th>Bldg Type_2fmCon</th>
      <th>Bldg Type_Duplex</th>
      <th>Bldg Type_Twnhs</th>
      <th>Bldg Type_TwnhsE</th>
      <th>House Style_1.5Fin</th>
      <th>House Style_1.5Unf</th>
      <th>House Style_1Story</th>
      <th>House Style_2.5Fin</th>
      <th>House Style_2.5Unf</th>
      <th>House Style_2Story</th>
      <th>House Style_SFoyer</th>
      <th>House Style_SLvl</th>
      <th>Roof Style_Flat</th>
      <th>Roof Style_Gable</th>
      <th>Roof Style_Gambrel</th>
      <th>Roof Style_Hip</th>
      <th>Roof Style_Mansard</th>
      <th>Roof Style_Shed</th>
      <th>Roof Matl_CompShg</th>
      <th>Roof Matl_Membran</th>
      <th>Roof Matl_Metal</th>
      <th>Roof Matl_Roll</th>
      <th>Roof Matl_Tar&amp;Grv</th>
      <th>Roof Matl_WdShake</th>
      <th>Roof Matl_WdShngl</th>
      <th>Foundation_BrkTil</th>
      <th>Foundation_CBlock</th>
      <th>Foundation_PConc</th>
      <th>Foundation_Slab</th>
      <th>Foundation_Stone</th>
      <th>Foundation_Wood</th>
      <th>Heating_Floor</th>
      <th>Heating_GasA</th>
      <th>Heating_GasW</th>
      <th>Heating_Grav</th>
      <th>Heating_OthW</th>
      <th>Heating_Wall</th>
      <th>Central Air_N</th>
      <th>Central Air_Y</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>215000</td>
      <td>6</td>
      <td>1656</td>
      <td>1080.0</td>
      <td>1656</td>
      <td>2.0</td>
      <td>528.0</td>
      <td>1</td>
      <td>1960</td>
      <td>50</td>
      <td>50</td>
      <td>1960</td>
      <td>2</td>
      <td>7</td>
      <td>112.0</td>
      <td>639.0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
    </tr>
    <tr>
      <th>1</th>
      <td>105000</td>
      <td>5</td>
      <td>896</td>
      <td>882.0</td>
      <td>896</td>
      <td>1.0</td>
      <td>730.0</td>
      <td>1</td>
      <td>1961</td>
      <td>49</td>
      <td>49</td>
      <td>1961</td>
      <td>0</td>
      <td>5</td>
      <td>0.0</td>
      <td>468.0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
    </tr>
    <tr>
      <th>2</th>
      <td>172000</td>
      <td>6</td>
      <td>1329</td>
      <td>1329.0</td>
      <td>1329</td>
      <td>1.0</td>
      <td>312.0</td>
      <td>1</td>
      <td>1958</td>
      <td>52</td>
      <td>52</td>
      <td>1958</td>
      <td>0</td>
      <td>6</td>
      <td>108.0</td>
      <td>923.0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
    </tr>
    <tr>
      <th>3</th>
      <td>244000</td>
      <td>7</td>
      <td>2110</td>
      <td>2110.0</td>
      <td>2110</td>
      <td>2.0</td>
      <td>522.0</td>
      <td>2</td>
      <td>1968</td>
      <td>42</td>
      <td>42</td>
      <td>1968</td>
      <td>2</td>
      <td>8</td>
      <td>0.0</td>
      <td>1065.0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
    </tr>
    <tr>
      <th>4</th>
      <td>189900</td>
      <td>5</td>
      <td>1629</td>
      <td>928.0</td>
      <td>928</td>
      <td>2.0</td>
      <td>482.0</td>
      <td>2</td>
      <td>1997</td>
      <td>13</td>
      <td>12</td>
      <td>1998</td>
      <td>1</td>
      <td>6</td>
      <td>0.0</td>
      <td>791.0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
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
      <th>2925</th>
      <td>142500</td>
      <td>6</td>
      <td>1003</td>
      <td>1003.0</td>
      <td>1003</td>
      <td>2.0</td>
      <td>588.0</td>
      <td>1</td>
      <td>1984</td>
      <td>22</td>
      <td>22</td>
      <td>1984</td>
      <td>0</td>
      <td>6</td>
      <td>0.0</td>
      <td>819.0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
    </tr>
    <tr>
      <th>2926</th>
      <td>131000</td>
      <td>5</td>
      <td>902</td>
      <td>864.0</td>
      <td>902</td>
      <td>2.0</td>
      <td>484.0</td>
      <td>1</td>
      <td>1983</td>
      <td>23</td>
      <td>23</td>
      <td>1983</td>
      <td>0</td>
      <td>5</td>
      <td>0.0</td>
      <td>301.0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
    </tr>
    <tr>
      <th>2927</th>
      <td>132000</td>
      <td>5</td>
      <td>970</td>
      <td>912.0</td>
      <td>970</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>1</td>
      <td>1992</td>
      <td>14</td>
      <td>14</td>
      <td>1992</td>
      <td>0</td>
      <td>6</td>
      <td>0.0</td>
      <td>337.0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
    </tr>
    <tr>
      <th>2928</th>
      <td>170000</td>
      <td>5</td>
      <td>1389</td>
      <td>1389.0</td>
      <td>1389</td>
      <td>2.0</td>
      <td>418.0</td>
      <td>1</td>
      <td>1974</td>
      <td>32</td>
      <td>31</td>
      <td>1975</td>
      <td>1</td>
      <td>6</td>
      <td>0.0</td>
      <td>1071.0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
    </tr>
    <tr>
      <th>2929</th>
      <td>188000</td>
      <td>7</td>
      <td>2000</td>
      <td>996.0</td>
      <td>996</td>
      <td>3.0</td>
      <td>650.0</td>
      <td>2</td>
      <td>1993</td>
      <td>13</td>
      <td>12</td>
      <td>1994</td>
      <td>1</td>
      <td>9</td>
      <td>94.0</td>
      <td>758.0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
    </tr>
  </tbody>
</table>
<p>2689 rows × 91 columns</p>
</div>



### Multivariate Linear Regression &  Cross Validation


```python
x = list(range(0, 30))
y = [train_and_test(sel_df, i) for i in x]
```

Lowest RMSE achieved at 30 folds


```python
plt.plot(x, y)
plt.xlabel('k fold')
plt.ylabel('RMSE')
plt.show()
```


![png](output_23_0.png)

