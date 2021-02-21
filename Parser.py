import requests
import re

url = "https://www.vocabulary.com/lists/145774"
body = ""
words = []; definitions = []

def get_body():
	global body
	request = requests.get(url)
	body = request.text

def write_words_to_file():
	with open("tmp.txt", "w") as f:
		f.write(body)

def parse_words():
	global words, definitions
	with open("tmp.txt", "r") as f:
		num = 0
		while True:
			line = str(f.readline())
			if line == '':
				break

			if "word dynamictext" in line:
				line = line.split('/')[2]
				line = line.split('"')[0]
				words.append(line)
			elif "definition" in line and num > 1:
				line = line.split('>')[1]
				line = line.split('<')[0]
				definitions.append(line)
				num += 1
			elif "definition" in line:
				num += 1

get_body()
# write_words_to_file()
parse_words()
