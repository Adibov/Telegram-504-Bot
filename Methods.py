import requests
import json
from Private import token
from GetUpdates import getUpdates

url = f"https://api.telegram.org/bot{token}/"

def sendMessage(chat_id, message):
	request = requests.post(url + "sendMessage", data={'chat_id': chat_id, 'text': message})
	if request.json()['ok'] == False:
		raise Exception("Cannot send message")

def setMyCommands(commands):
	request = requests.post(url + "setMyCommands", data={'commands': commands})
	if request.json()['ok'] == False:
		raise Exception("Cannot set commands")

	request = requests.get(url + "getMyCommands")
	if request.json()['ok'] == False or len(request.json()['result']) != len(json.loads(commands)):
		raise Exception("Cannot set commands")

def Add_Commands():
	global commands
	commands = [
		{
			'command': 'help',
			'description': 'Show help'
		},

		{
			'command': 'new_word',
			'description': 'To get a new word'
		}
	]
	commands = json.dumps(commands)
	setMyCommands(commands)

def init():
	pass
	# Add_Commands()

init()

last_update_id = -1
while True:
	result = getUpdates(-1)
	if not len(result):
		continue
	result = result[0]
	if (result['update_id'] == last_update_id):
		continue

	last_update_id = result['update_id']
	chat = result['message']['chat']
	chat_id = chat['id']

	print(result['message']['text'])
	send_message = input()
	sendMessage(chat_id, send_message)