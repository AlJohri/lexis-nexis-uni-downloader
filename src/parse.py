import json
from pprint import pprint as pp

with open('src/sample2.json') as f:
	page = json.load(f)

for row in page['collections']['rows']:
	print(row['props']['title'])

last_page = int(page['collections']['pagination']['collections']['items'][-1]['id'])
