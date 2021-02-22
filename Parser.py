import requests
import csv

url = "https://www.vocabulary.com/lists/145774"
body = ""
words = []; definitions = []

def get_body():
	global body
	request = requests.get(url)
	body = request.text

def write_words_to_file():
	with open("site_html.txt", "w") as f:
		f.write(body)

def parse_words():
	global words, definitions
	with open("site_html.txt", "r") as f:
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

def save_data():
	with open("data.csv", "w") as f:
		writer = csv.writer(f)
		writer.writerow(["ID", "Word", "Definition"])
		for i in range(len(words)):
			writer.writerow([i + 1, words[i], definitions[i]])

get_body()
# write_words_to_file()
parse_words()
save_data()