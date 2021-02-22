import requests
import json
from Private import token

url = f"https://api.telegram.org/bot{token}/"

def sendMessage(chat_id, message):
	request = requests.post(url + "sendMessage", data={'chat_id': chat_id, 'text': message})
	if request['ok'] == False:
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
	Add_Commands()

init()