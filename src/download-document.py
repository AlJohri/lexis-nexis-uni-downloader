import os
import requests
from bs4 import BeautifulSoup

LN_URL = os.getenv('LN_URL')

s = requests.Session()

s.cookies.update({
	'ezproxy': os.getenv('EZPROXY'),
	'LexisMachineId': os.getenv('MACHINE_ID'),
	'ASP.NET_SessionId': os.getenv('SESSION_ID')
})

params = {'pddocfullpath': '/shared/document/news/urn:contentItem:3S7W-SJ10-0092-S3J9-00000-00'}

response = s.get(f'{LN_URL}/document/documentslider/', params=params)
soup = BeautifulSoup(response.content, 'html.parser')

print(soup.select_one('section.doc-content'))
