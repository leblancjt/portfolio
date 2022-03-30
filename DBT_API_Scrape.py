# Author: John LeBlanc
# Date: 09/24/2020

import requests
import json
from urllib.parse import urljoin
import pandas as pd
import os
import time
from progress.bar import IncrementalBar

with open('DBT_Key.txt', 'r') as fp:
    key = fp.read().strip()

params = {
    'key': key,
	'media' : 'text',
	'language' : 'English',
	'sort_by' : 'version_code',
	'v' : 2
}

base = 'https://dbt.io/'
endpoint = 'library/volume'

url = urljoin(base, endpoint)
response = requests.get(url, params = params)
data = json.loads(response.text)

DAM_IDs = []
version_codes = []

for d in data:
	DAM_IDs.append(d['dam_id'])
	version_codes.append(d['version_code'])
	
numCodes = []
versionCodes = list(dict.fromkeys(version_codes))
for v in versionCodes:
	numCodes.append(version_codes.count(v))

s = 0
for i in numCodes:
	if i == 1:
		s += i
		continue
	elif i == 2:
		first = DAM_IDs.pop(s)
		second = DAM_IDs.pop(s)
		DAM_IDs.insert(s, second)
		DAM_IDs.insert(s + 1, first)
		s += i
	elif i == 4:
		first = DAM_IDs.pop(s)
		second = DAM_IDs.pop(s)
		third = DAM_IDs.pop(s)
		forth = DAM_IDs.pop(s)
		DAM_IDs.insert(s, third)
		DAM_IDs.insert(s + 1, forth)
		DAM_IDs.insert(s + 2, first)
		DAM_IDs.insert(s + 3, second)
		s += i
		
bar = IncrementalBar('Scraping', max = len(DAM_IDs))		

for d in DAM_IDs:
	bar.next()
	time.sleep(1)
	books = []
	chapterNums = []
	verseNums = []
	text = []
	versionCode = d[2:8]
	params = {
		'key': key,
		'dam_id' : d,
		'v' : 2
	}
	endpoint = 'text/verse'
	url = urljoin(base, endpoint)
	response = requests.get(url, params = params)
	data = json.loads(response.text)
	
	for d in data:
		books.append(d['book_name'])
		chapterNums.append(int(d['chapter_id']))
		verseNums.append(int(d['verse_id']))
		text.append(d['verse_text'])
	columns = {'Book': books, 'Chapter': chapterNums, 'Verse': verseNums, 'Text': text}
	df = pd.DataFrame(columns)
	df.to_csv(versionCode + '.csv', index = False)
bar.finish()

bar = IncrementalBar('Creating CSVs', max = len(numCodes))
s = 0
for i in numCodes:
	bar.next()
	time.sleep(1)
	if i == 1:
		df = pd.read_csv(DAM_IDs[s][2:8] + '.csv')
		df.to_csv(DAM_IDs[s][2:6] + '.csv', index = False)
		os.remove(DAM_IDs[s][2:8] + '.csv')
		s += i
		continue
	elif i == 2:
		df = pd.read_csv(DAM_IDs[s][2:8] + '.csv')
		cf = pd.read_csv(DAM_IDs[s + 1][2:8] + '.csv')
		new = pd.concat([df, cf])
		new.to_csv(DAM_IDs[s][2:6] + '.csv', index = False)
		os.remove(DAM_IDs[s][2:8] + '.csv')
		os.remove(DAM_IDs[s + 1][2:8] + '.csv')
		s += i
		continue
	elif i == 4:
		df = pd.read_csv(DAM_IDs[s][2:8] + '.csv')
		cf = pd.read_csv(DAM_IDs[s + 1][2:8] + '.csv')
		bf = pd.read_csv(DAM_IDs[s + 2][2:8] + '.csv')
		af = pd.read_csv(DAM_IDs[s + 3][2:8] + '.csv')
		new = pd.concat([df, cf, bf, af])
		new.to_csv(DAM_IDs[s][2:6] + '.csv', index = False)
		os.remove(DAM_IDs[s][2:8] + '.csv')
		os.remove(DAM_IDs[s + 1][2:8] + '.csv')
		os.remove(DAM_IDs[s + 2][2:8] + '.csv')
		os.remove(DAM_IDs[s + 3][2:8] + '.csv')
		s += i
		continue
bar.finish()

