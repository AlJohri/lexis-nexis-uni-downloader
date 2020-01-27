import os
import sys
import browser_cookie3

def eprint(*args, **kwargs):
	print(*args, **kwargs, file=sys.stderr)

cj = browser_cookie3.chrome()

LN_URL = os.getenv('LN_URL')

if not LN_URL:
	eprint("missing environment variable: LN_URL")
	exit(1)

LN_DOMAIN = os.getenv('LN_URL').replace('https://', '')

if LN_DOMAIN.startswith("advance-lexis-com"):
	LN_EZPROXY_DOMAIN = LN_DOMAIN.replace('advance-lexis-com', '')
elif LN_DOMAIN.startswith("advance.lexis.com"):
	LN_EZPROXY_DOMAIN = LN_DOMAIN.replace('advance.lexis.com', '')
elif LN_DOMAIN.startswith("www.lexisnexis.com"):
	LN_EZPROXY_DOMAIN = LN_DOMAIN.replace('www.lexisnexis.com', '')
else:
	eprint(f"Unable to parse the ezproxy domain from the LN_URL: {LN_URL}")

def get(domain, path, key):
	eprint(f"Getting {key} from {domain}{path}...")
	try:
		return cj._cookies[domain][path][key].value
	except KeyError:
		eprint(f"Unable to find {key!r} cookie on Google Chrome for "
			  f"domain: {domain!r} and path: {path!r}")
		exit(1)

eprint(f'Getting cookies for domains: {LN_DOMAIN!r} and {LN_EZPROXY_DOMAIN!r}.')

print('export EZPROXY={}'.format(get(LN_EZPROXY_DOMAIN, '/', 'ezproxy')))
print('export MACHINE_ID={}'.format(get(LN_DOMAIN, '/', 'LexisMachineId')))
print('export SESSION_ID={}'.format(get(LN_DOMAIN, '/', 'ASP.NET_SessionId')))
