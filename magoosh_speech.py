from PyPDF2 import PdfFileReader, PdfFileWriter

input = PdfFileReader(open('input.pdf', 'rb'))
page_no = 1
all_content = ''
for page in input.pages:
	content = input.getPage(page_no).extractText()
	if 'Basic Words' in content:
		break
	all_content = all_content + content + ' '
	print('Page no: ' + str(page_no))
	print(content)
	if page > 1:
		break
	page_no += 1 
	

all_content = all_content.split(' ')
# print(str(all_content))
temp = []
for word in all_content:
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

print(str(list_of_words))