import requests
import json
from urllib.parse import urljoin
from pprint import pprint
from progress.bar import ShadyBar

host = 'https://pokeapi.co/api/v2/'
endpoint = 'pokemon/'
url = urljoin(host, endpoint)

names = []
heights = []
weights = []

bar = ShadyBar('Getting Heights and Weights: ', max = 807)
for p in range(1, 808):
    url = urljoin(url, str(p))
    response = requests.get(url)
    names.append(json.loads(response.text)['name'])
    heights.append(int(json.loads(response.text)['height']))
    weights.append(int(json.loads(response.text)['weight']))
    bar.next()
bar.finish()

avgHeight = sum(heights) / len(heights)
avgWeight = sum(weights) / len(heights)

print('The average height of all Pokémon is: ' + str(round(avgHeight, 2)) + ' decimetres')
print('The average weight of all Pokémon is: ' + str(round(avgWeight, 2)) + ' hectograms')

maxHeight = max(heights)
minHeight = min(heights)
maxWeight = max(weights)
minWeight = min(weights)

tall = names[heights.index(maxHeight)]
short = names[heights.index(minHeight)]
heavy = names[weights.index(maxWeight)]
light = names[weights.index(minWeight)]

print('The tallest Pokémon is ' + tall + ' at ' + str(maxHeight) + ' decimetres')
print('The shortest Pokémon is ' + short + ' at ' + str(minHeight) + ' decimetres')
print('The heaviest Pokémon is ' + heavy + ' at ' + str(maxWeight) + ' hectograms')
print('The lightest Pokémon is ' + light + ' at ' + str(minWeight) + ' hectograms')

endpoint = 'berry'
url = urljoin(host, endpoint)
offset = 0
limit = 20
params = {
    'offset' : offset,
    'limit' : limit
}
response = requests.get(url, params = params)
data = json.loads(response.text)['results']
pprint(data)

