class Word(object):
	"""Word structure: meaning, definition, example"""
	def __init__(self,  name, definition, example):
		self.name = name
		self.definition = definition
		self.example = example


	def __str__(self):
		return self.name + '\n' + self.definition + '\n' + self.example
		