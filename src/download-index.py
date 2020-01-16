import os
import math
import json
import requests
from urllib.parse import urlparse, parse_qs

LN_URL = os.getenv('LN_URL')

s = requests.Session()

s.cookies.update({
	'ezproxy': os.getenv('EZPROXY'),
	'LexisMachineId': os.getenv('MACHINE_ID'),
	'ASP.NET_SessionId': os.getenv('SESSION_ID')
})

with open('data/query.txt') as f:
	query = f.read().strip()

print('Query:')
print(query)

params = {"pdsearchterms": query}
response = s.get(f"{LN_URL}/search/", params=params)
print(response.url)
with open('debug.html', 'wb') as f:
	f.write(response.content)
crid = parse_qs(urlparse(response.url).query)['crid'][0]

MAX_PAGES = 5
i = 1
last_page = math.inf

while i < min(last_page, MAX_PAGES):

	print(f'Downloading Page {i} of {last_page}')

	response = s.patch(f"{LN_URL}/r/searchresults/sp79k/results",
		headers={'X-LN-PreviousRequestId': crid},
		json={"id":"results","props":{"action": "SpecificPageByNum", "value": i}})
	data = response.json()

	if i == 1:
		last_page = int(data['collections']['pagination']['collections']['items'][-1]['id'])

	with open(f'data/raw/index/{i}.json', 'wb') as f:
		f.write(response.content)

	crid = response.headers['X-LN-CurrentRequestId']

	i += 1
