from PyPDF2 import PdfFileReader, PdfFileWriter
from word import Word
from constants import word_sections_page_nos

import pickle

def worker_module():
	for section in word_sections_page_nos:
		start_page_no = word_sections_page_nos[section][0]
		end_page_no = word_sections_page_nos[section][1]
		print('Section {0} Start page no: {1} End page no: {2}'.format(
			section ,str(start_page_no), str(end_page_no)))
		
		content_string = get_string_from_pdf(start_page_no, end_page_no)
		list_of_words = get_sanitise_word_list(content_string)
		print('Total {0} words are found!'.format(str(len(list_of_words))))
		new_list_of_words = []
		for word in list_of_words:
			new_list_of_words.append(partition_word_content(word_string=word, section=section))

		with open(section + '.csv', 'w') as f:
			for word_obj in new_list_of_words:
				f.write(word_obj.name + ',' + word_obj.definition + ',' + word_obj.example + '\n')
				# print(str(word_obj))

		with open(section + '.pickle', 'wb')	as f:
			pickle.dump(new_list_of_words, f)
		

def partition_word_content(word_string, section):
	word_name = ''
	word_definition = ''
	word_example = ''
	content = ''
	for word in word_string.split(' '):
		if word_name == '' and ':' in word:
			word_name = content + word + ' '
			content = ''
		elif word_definition == '' and word[0].isupper():
			word_definition = content + '.'
			content = word + ' '
		else:
			content = content +  word + ' '

	word_example = content
	return Word(word_name, word_definition, word_example, section=section)


def get_string_from_pdf(start_page_no, end_page_no):
	input = PdfFileReader(open('input.pdf', 'rb'))
	content_string = ''
	for page_no in range(start_page_no - 1, end_page_no):
		page_content = input.getPage(page_no).extractText()
		content_string = content_string + page_content + ' '
	
	# Minor glitch inside input.pdf related to double quotes
	# hence following line, which replaces "s at the end of word in 's
	content_string = content_string.replace('"s ', "'s ")

	return content_string.encode('utf-8').strip()


def get_sanitise_word_list(content_string):
	content_list = content_string.decode().split(' ')
	temp = []
	for word in content_list:
		# Consider list member of words which are not: single newline character, single empty character
		# or having url-link
		if word != '' and word != '\n' and '.com' not in word:
			s = word
			if '\n' in s:
				s = s.replace('\n', '')
			temp.append(s)

	type_of_word = [0 for i in range(len(temp))]
	for i in range(len(temp)):
		if '):' in temp[i]:
			type_of_word[i-1] = 1

	list_of_words = []
	word_content = ''
	for i in range(len(type_of_word)):
		if type_of_word[i] == 1:
			list_of_words.append(word_content)
			word_content = temp[i]
		else:
			word_content = word_content + ' ' + temp[i]

	list_of_words.append(word_content)


	# Returning list sliced from second element because the first element is an empty string
	# This has been done, to avoid writing extra conditional loops for adhering with above logic
	return list_of_words[1:]

