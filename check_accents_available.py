import pyttsx

if __name__ == '__main__':
	engine = pyttsx.init()
	voices = engine.getProperty('voices')
	for voice in voices:
		print(str(voice))
		