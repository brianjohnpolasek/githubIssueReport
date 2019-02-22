'''
Author: Brian Polasek
Program: githubIssuesTracker
Input: List of github repositories in format 'owner/repository' specified through a text file command line argument
Output: A string representation of a json map of the issues in the specified repos,
	as well as the top day of issues and all of the corresponding repos.
'''

import sys
import requests
import re
import json

# check to see if command line arguments were made
if (len(sys.argv) == 2):
	fileName = str(sys.argv[1])
else:
	print('Program will exit since no file specified through CLI')

#fileName = 'github_repos.txt'

# attempt to open the file given
try:
	with open(fileName, 'r') as fileIn:
		input_data = fileIn.readlines()
except: OSError

fileIn.close()

# remove any new lines produced by reading the file
input_github_repos = [None] * len(input_data)

for i in range(0, len(input_github_repos)):
	input_github_repos[i] = input_data[i].replace('\n', '')

# copy the list into a new list in order to correct the url
github_repos = list(input_github_repos)

# convert to correct url
for i in range(0, len(github_repos)):
	if (type(github_repos[i]) is str):
		github_repos[i] = ('https://api.github.com/repos/' + github_repos[i] + '/issues')
	else:
		print(str(github_repos[i]) + ' ignored, must be a string.')

# variables used to keep track of the top day and occurences
date_matrix = []
overall_top_day = 0
output_string = ""

# beginning of output string
print('{\n\t"issues": [\n\t{')

# r = requests.get('https://api.github.com/repos/jwasham/coding-interview-university/issues')
for i in range(0, len(github_repos)):
	r = requests.get(github_repos[i])

	x = str(r.json())

	# regrex patterns
	idMatch = re.findall("\'id\':\s?[0-9]*", x)
	stateMatch = re.findall("\'state\':\s?u'[a-z]\w+\'", x)
	titleMatch = re.findall("\'title\'.+?\',", x)
	repoMatch = re.findall("\'repository_url\':\s?u\'[a-z:/\-\.]*\'", x)
	timeMatch = re.findall("\'created_at\':\s?u\'[A-Z:0-9\-]*\'", x)

	# Extracting the date for analysis
	dateMatch = [None] * len(timeMatch)

	for k in range (0, len(timeMatch)):
		dateMatch[k] = re.findall("[0-9]{4}-[0-9]{2}-[0-9]{2}", str(timeMatch[k]))
		dateMatch[k] = str(dateMatch[k])

	# matrix for finding all occurences
	date_matrix.append(dateMatch)

	# determining top day
	date_counter = {}

	for date in dateMatch:
		if date in date_counter:
			date_counter[date] += 1
		else:
			date_counter[date] = 1
	
	if (len(dateMatch) > 0):
		top_day = sorted(date_counter, key = date_counter.get, reverse = True)

		if (top_day[0] > overall_top_day):
			overall_top_day = top_day[0]

	# printing
	
	for j in range(0, len(idMatch)/2):
		print('\t\t'),
		print(idMatch[2*j]),
		print(',\n\t\t'),
		print(stateMatch[j]),
		print(',\n\t\t'),
		print(titleMatch[j]),
		print(',\n\t\t'),
		print(repoMatch[j]),
		print(',\n\t\t'),
		print(timeMatch[j]),
		print('\n\t')

# arrays used to calculate the repos with occurences and their corresponding number
occurences = []
num_occurs = []

for i in range(0, len(date_matrix)):
	num_occurs.append(0)
	for j in range(0, len(date_matrix[i])):
		if (date_matrix[i][j] == overall_top_day):
			num_occurs[i] = num_occurs[i] + 1
		if (input_github_repos[i] not in occurences):
			occurences.append(input_github_repos[i])
	

print('\t}\n\t],\n\t"top_day:" {\n\t\t"day": '),
print(overall_top_day)
print('\t\t"occurences:" {\n\t\t'),

for i in range(0, len(occurences)):
	print(occurences[i] + ': ' + str(num_occurs[i]))

print('\t\t}\n\t}\n}')
