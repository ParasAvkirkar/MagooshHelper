from PyPDF2 import PdfFileReader, PdfFileWriter
from speech_utilities import speak_sentences

import pickle

# Common words start at page 1
# Basic Words start at page 28
# Advanced Words start at page 63

word_sections_page_nos = {
	'Common Words': (1, 27),
	'Basic Words': (28, 62),
	'Advance Words': (63, 95)
}

def worker_module():
	for section in word_sections_page_nos:
		start_page_no = word_sections_page_nos[section][0]
		end_page_no = word_sections_page_nos[section][1]
		content_string = get_string_from_pdf(start_page_no, end_page_no)
		list_of_words = get_sanitise_word_list(content_string)
		with open(section + '.pickle', 'wb') as f:
			pickle.dump(list_of_words, f)
			# for el in list_of_words:
			# 	f.write(str(el) + ',\n')
			# 	# print(el)
			# 	# print('=========================================')


def revise(section_key):
	with open(section_key + '.pickle', 'rb') as f:
		list_of_words = pickle.load(f)
		speak_sentences(list_of_words)

def get_string_from_pdf(start_page_no, end_page_no):
	input = PdfFileReader(open('input.pdf', 'rb'))
	page_no = 1
	content_string = ''
	for page in input.pages[start_page_no-1: end_page_no]:
		page_content = input.getPage(page_no).extractText()
		content_string = content_string + page_content + ' '
		# print('Page no: ' + str(page_no))
		page_no += 1 
	
	# with open('dump.txt', 'w') as f:
	# 	f.write(content_string.encode('utf-8').strip())

	return content_string.encode('utf-8').strip()


def get_sanitise_word_list(content_string):
	content_list = content_string.decode().split(' ')
	# print(str(all_content))
	temp = []
	for word in content_list:
		# Consider list member of words which are not only newline, only empty or only url-link
		# This are the anomalies
		if word != '' and word != '\n' and '.com' not in word:
			s = word
			if '\n' in s:
				s = s.replace('\n', '')
			temp.append(s)

	type_of_word = [0 for i in range(len(temp))]
	for i in range(len(temp)):
		if '(' in temp[i]:
			type_of_word[i-1] = 1

	list_of_words = []
	word_content = ''
	for i in range(len(type_of_word)):
		if type_of_word[i] == 1:
			list_of_words.append(word_content)
			word_content = temp[i]
		else:
			word_content = word_content + ' ' + temp[i]

	# Returning list sliced from second element because the first element is an empty string
	# This has been done, to avoid writing extra conditional loops for adhering with above logic
	return list_of_words[1:]


	
if __name__ == '__main__':
	worker_module()

	revise('Common Words')
