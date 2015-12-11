# -*- coding: utf-8 -*-

import re


def get_number_of_word_in_a_list(word_to_search, word_list):
	"""
	Return the number of a given word  in a given text

	:type word_to_search: str
	:param word_to_search: The given word to count instance of

	:type word_list: list(str)
	:param word_list: The list of word to search into
	"""
	number_of_occurence = 0

	for word in word_list:
		if word.lower() == word_to_search.lower():
			number_of_occurence += 1

	return number_of_occurence

def make_set_from_list(word_list):
	"""
	Make a set of unic element from a list

	:type word_list: list(str)
	:param word_list: The list of word to transform into a set
	"""
	lower_list = list()
	for word in word_list:
		lower_list.append(word.lower())

	return set(lower_list)


def get_word_list_from_a_text(text):
	"""
	get a text, and return a list of all words in it
	"""
	word_list = text.split(" ")
	return keep_only_letters(word_list)

def keep_only_letters(word_list):
	"""
	Remove all non letter charachter from each element of a list

	:type word_list: list(str)
	:param word_list: The list of word to remove all non-letters from
	"""
	new_word_list = list()
	for word in word_list:
		word = re.sub(r'[^A-Za-z-]+','',word)
		new_word_list.append(word)

	return new_word_list


if __name__ == '__main__':
	text = "Benjamin Ducol est docteur en sciences politiques et chercheur associé de la chaire de recherche du Canada sur les conflits et le terrorisme ainsi qu’au Centre International de Criminologie Comparée. Il a notamment contribué à un rapport de 255 pages sur le rôle d’Internet dans le processus de radicalisation, remis en mars 2015 au gouvernement canadien, et dont Le Monde s’est procuré une copie. Le rapport étudie la trajectoire de radicalisation d’une vingtaine d’extrémistes violents, de Mohamed Merah à Anders Breivik en passant par Michael Zehaf-Bibeau."

	word_list = get_word_list_from_a_text(text)
	word_list = keep_only_letters(word_list)

	word_set = make_set_from_list(word_list)

	counted_words = dict()

	for word in word_set:
		counted_words[word] = get_number_of_word_in_a_list(word, word_list)

	print counted_words
