from PyPDF2 import PdfFileReader, PdfFileWriter
from speech_utilities import speak_sentences
from word import Word
from random import shuffle
from extraction_transformation import worker_module
from constants import word_sections_page_nos

import pickle

import traceback


def meaning_to_word_match(meaning_keywords):
	total_results_found = 0
	for section in word_sections_page_nos:
		with open(section + '.pickle', 'rb') as f:
			list_of_words = pickle.load(f)
			match_word_objects = []
			for word_obj in list_of_words:
				for keyword in meaning_keywords:
					if keyword in word_obj.definition:
						match_word_objects.append(word_obj)
						break

			# print(str(len(list_of_words)) + ' ' + str(len(list(set(list_of_words)))))
			for word_obj in match_word_objects:
				print('***************************************')
				print(word_obj.section)
				print(word_obj.name)
				print(word_obj.definition)
				print(word_obj.example)
				print('=======================================')

			total_results_found += len(match_word_objects)
			# print(str(len(match_word_objects)) + ' ' + str(len(list(set(match_word_objects)))))
		
	print('{0} results are found!'.format(str(total_results_found)))


def check_words_collected():
	with open('check.txt', 'w') as c:
		for section in word_sections_page_nos:
			with open(section + '.pickle', 'rb') as f:
				list_of_words = pickle.load(f)
				match_word_objects = []
				for word_obj in list_of_words:
					# print(str(word_obj.name))
					c.write(str(word_obj.name) + '\n')


def find_meaning(word):
	match_word_objects = []
	for section in word_sections_page_nos:
		with open(section + '.pickle', 'rb') as f:
			list_of_words = pickle.load(f)
			for word_obj in list_of_words:
				if word in word_obj.name:
					match_word_objects.append(word_obj)

	for word_obj in match_word_objects:
		print('***************************************')
		print(word_obj.section)
		print(word_obj.name)	
		print(word_obj.definition)
		print(word_obj.example)
		print('=======================================')	


def revise(section_key):
	with open(section_key + '.pickle', 'rb') as f:
		list_of_words = pickle.load(f)
		shuffle(list_of_words)
		sentences = []
		sentences.append(section_key)
		for word_obj in list_of_words:
			sentences.append(word_obj.name)
			sentences.append(word_obj.definition)
			sentences.append(word_obj.example)

		print('{0} section: Words are shuffled and will come in random worder!'.format(section_key))
		speak_sentences(sentences)

def revise_all():
	print('Words are shuffled and will come in random worder!')
	all_words = []
	for section in word_sections_page_nos:
		with open(section + '.pickle', 'rb') as f:
			list_of_words = pickle.load(f)
			all_words.extend(list_of_words)

	shuffle(all_words)
	sentences = []
	for word_obj in list_of_words:
		sentences.append(word_obj.name)
		sentences.append(word_obj.definition)
		sentences.append(word_obj.example)

	speak_sentences(sentences)

	
if __name__ == '__main__':
	try:
		while True:
			print('------------------------------------------------------------------------------')
			print('Enter 1 for generating vocabulary data')
			print('Enter 2 for finding word from the keywords in its definition')
			print('Enter 3 for finding meaning of word')
			print('Enter 4 to start revision')
			choice = int(input('?: '))
			if choice == 1:
				worker_module()
			elif choice == 2:
				meaning_to_word_match(input('Enter the keywords in definition separated by space: ').split())
			elif choice == 3:
				find_meaning(input('Enter the word whose meaning to be search: '))
			elif choice == 4:
				s = input('Enter c for common section, b for basic section, a for advance section,'
							+ ' Or Enter any other character for all sections: ')
				s = s.lower()
				if 'c' in s:
					revise('Common Words')
				elif 'b' in s:
					revise('Basic Words')
				elif 'a' in s:
					revise('Advance Words')
				else:
					revise_all()
			else:
				print('Wrong Choice!')

			print('------------------------------------------------------------------------------')	

	except Exception as e:
		print(str(e))
		print(str(traceback.format_exc()))
