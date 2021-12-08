# pysony

Pysony is a package written in the Python language for analysing datasets that include coordinate data.

## Instalation

Install package
```bash
python3 -m pip install git+ssh://git@github.com/rojo1997/pysony.git
```

Update package
```bash
python3 -m pip install git+ssh://git@github.com/rojo1997/pysony.git --upgrade
```

Force update package
```bash
python3 -m pip install --upgrade --force-reinstall git+ssh://git@github.com/rojo1997/pysony.git
```

## Quick start

```python
import numpy as np
import pandas as pd

from pysony.feature_extraction import (
    ReverseGeocoder,
    OpenWeatherMap
)

from pysony.graph import GraphDistance

X = np.random.rand(10,2) / 2
X[:,0] += -0.1729636 # lon
X[:,1] += 51.5214588 # lat

myReverseGeocoder = ReverseGeocoder(mode = 1)
myOpenWeatherMap = OpenWeatherMap(
    appid = "apikey"
)

Y = myReverseGeocoder.transform(X)
df = pd.DataFrame(Y, columns = ReverseGeocoder.columns)
print(df)
"""
              name   admin1          admin2
0         East Ham  England  Greater London
1          Takeley  England           Essex
2  Watton at Stone  England   Hertfordshire
3           Harlow  England           Essex
4      Hadley Wood  England  Greater London
5     Great Dunmow  England           Essex
6          Cuffley  England   Hertfordshire
7         Elsenham  England           Essex
8          Takeley  England           Essex
9    Waltham Cross  England   Hertfordshire
"""


Y = myOpenWeatherMap.transform(X)
df = pd.DataFrame(Y, columns = OpenWeatherMap.columns)
print(df)
"""
     temp  feels_like  temp_min  ...  humidity  wind_deg  wind_speed
0  278.63      276.85    277.91  ...      83.0     190.0        2.24
1  279.40      278.73    278.38  ...      76.0     198.0        1.34
2  279.04      275.11    278.08  ...      75.0     220.0        6.17
3  279.15      276.77    278.18  ...      75.0     212.0        3.13
4  278.56      273.08    277.91  ...      81.0     200.0       10.80
5  279.22      278.53    278.29  ...      76.0     213.0        1.34
6  278.40      277.60    277.80  ...      82.0     182.0        1.34
7  279.15      277.09    278.16  ...      75.0     221.0        2.68
8  278.93      276.50    278.01  ...      75.0     212.0        3.13
9  279.10      276.71    278.14  ...      75.0     212.0        3.13
"""

myGraphDistance = GraphDistance(
    threshold = 20
)

node, edge = myGraphDistance.compute(X)
print(node)
"""
[
    {
        '_key': '4630749269486329968', 
        'lon': 0.1006591339173672, 
        'lat': 51.68475507121363
    }, 
    {
        '_key': '-5026963679244352995', 
        'lon': 0.012806647114927683,
        'lat': 51.56462585311571
    }, 
    ...
]
"""
print(edge)
"""
[
    {
        '_from': 'node/4630749269486329968', 
        '_to': 'node/-5026963679244352995', 
        'distance': 14.685114751012092
    }, 
    {
        '_from': 'node/4630749269486329968', 
        '_to': 'node/-6188015243388749057', 
        'distance': 14.304432606569964
    },
    ...
]
"""
```