import requests
from Private import token

url = f"https://api.telegram.org/bot{token}/"

def getUpdates(offset=None, limit=None, timeout=None, allowed_updates=None):
	request = requests.post(url + 'getUpdates', data={'offset': offset, 'limit': limit, 'timeout': timeout, 'allowed_updates': allowed_updates})
	if request.json()['ok'] == False:
		raise Exception("Cannot get updates")
	return request.json()['result']