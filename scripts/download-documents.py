import os
import json
import requests
import textwrap
from pathlib import Path
from functools import partial
from bs4 import BeautifulSoup

LN_URL = os.getenv('LN_URL')

s = requests.Session()
s.cookies.update({
    'ezproxy': os.getenv('EZPROXY'),
    'LexisMachineId': os.getenv('MACHINE_ID'),
    'ASP.NET_SessionId': os.getenv('SESSION_ID')
})

for path in Path('data/raw/index/').glob("*json"):
    with path.open() as f:
        page = json.load(f)
    for i, row in enumerate(page['collections']['rows']):
        doc = row['props']
        doc_id = doc['docfullpath'].split(":")[-1]
        print("Downloading...", path, i, doc_id, doc['title'][0:50])
        output = f'data/raw/documents/{doc_id}.html'
        if os.path.exists(output):
            print(f'Already downloaded: {output}')
        params = {'pddocfullpath': doc['docfullpath']}
        response = s.get(f'{LN_URL}/document/documentslider/', params=params)
        with open(output, 'wb') as f:
            f.write(response.content)
