class Word(object):
	"""Word structure: meaning, definition, example"""
	def __init__(self, name, definition, example, section):
		self.name = name
		self.definition = definition
		self.example = example
		self.section = section
		self.name = self.name.strip()
		self.definition = self.definition.strip()
		self.example = self.example.strip()


	def __str__(self):
		return self.name + '\n' + self.definition + '\n' + self.example
		
