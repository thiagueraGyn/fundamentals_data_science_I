import random
from os import path as p
"""
Para criar senhas aleatórias, usamos import random. A definição da função era simplesmente:
"""

word_file = "words.txt"
word_list = []

# def generate_password():
#     return random.choice(word_list) + random.choice(word_list) + random.choice(word_list)

def generate_password():
    return ''.join(random.sample(word_list,3))

with open(word_file,'r') as words:
	for line in words:
		# remove white space and make everything lowercase
		word = line.strip().lower()
		# don't include words that are too long or too short
		if 3 < len(word) < 8:
			word_list.append(word)

print(generate_password())