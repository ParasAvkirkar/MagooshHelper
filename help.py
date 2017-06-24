import pyttsx
import time
from speech_utilities import speak_sentences


# engine = pyttsx.init()

while True:
	s = input('Say some ')
	# engine.say(s)
	# engine.runAndWait()
	# time.sleep(5)
	speak_sentences([s])

