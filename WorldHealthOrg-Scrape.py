import requests
import json
from urllib.parse import urljoin
import matplotlib.pyplot as plt
import numpy as np

host = 'https://ghoapi.azureedge.net/api/'
endpoint = 'VIOLENCE_HOMICIDERATE'
url = urljoin(host, endpoint)
filters = [
    "Dim1 eq 'MLE' and TimeDim eq 2010 and SpatialDim eq 'USA'",
    "Dim1 eq 'MLE' and TimeDim eq 2010 and SpatialDim eq 'CAN'",
    "Dim1 eq 'MLE' and TimeDim eq 2010 and SpatialDim eq 'MEX'",
    "Dim1 eq 'FMLE' and TimeDim eq 2010 and SpatialDim eq 'USA'",
    "Dim1 eq 'FMLE' and TimeDim eq 2010 and SpatialDim eq 'CAN'",
    "Dim1 eq 'FMLE' and TimeDim eq 2010 and SpatialDim eq 'MEX'",
]

countries = ['USA', 'Canada', 'Mexico']
maleRate = []
femaleRate =[]
for i in range(len(countries)):
    params = {
        '$filter' : filters[i]
    }
    response = requests.get(url, params = params)
    data = json.loads(response.text)['value']
    maleRate.append(data[0].get('NumericValue'))
for i in range(len(countries), len(filters)):
    params = {
        '$filter' : filters[i]
    }
    response = requests.get(url, params = params)
    data = json.loads(response.text)['value']
    femaleRate.append(data[0].get('NumericValue'))
    
endpoint = 'SI_POV_DAY1'
url = urljoin(host, endpoint)
filters = [
    "TimeDim eq 2010 and SpatialDim eq 'USA'",
    "TimeDim eq 2010 and SpatialDim eq 'CAN'",
    "TimeDim eq 2010 and SpatialDim eq 'MEX'",
]

poverty = []
for f in filters:
    params = {
        '$filter' : f
    }
    response = requests.get(url, params = params)
    data = json.loads(response.text)['value']
    poverty.append(data[0].get('NumericValue'))

x = np.arange(len(countries))
width = 0.20
fig, ax = plt.subplots(gridspec_kw={'left': 0.11, 'bottom': 0.08, 'right': 0.90, 'top': 0.85})
rects1 = ax.bar(x - width, maleRate, width, label='Male Homicide Rate')
rects2 = ax.bar(x, femaleRate, width, label='Female Homicide Rate')
rects3 = ax.bar(x + width, poverty, width, label='Percent Below Poverty Line')

# Add some text for labels, title and custom x-axis tick labels, etc.
ax.set_ylabel('Value')
ax.set_title('Percentage of Population Below Poverty Line \n vs. \n Male and Female Homicide Rate per 100,000 population.')
ax.set_xticks(x)
ax.set_xticklabels(countries)
ax.legend()
plt.show()