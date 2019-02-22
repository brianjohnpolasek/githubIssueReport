'''
with open('github_repos.txt', 'r') as fileIn:
	input_data = fileIn.readlines()

fileIn.close()

input_github_repos = [None] * len(input_data)

for i in range(0, len(input_github_repos)):
	input_github_repos[i] = input_data[i].replace('\n', '')


output_string +=  input_github_repos
'''