import sys, os
import datetime
import pyttsx

# Currently age and female properties are not available
# They are just added as skeleton
# When a workaround or provision for such properties will be available,
# then at that time this function will modified to get voice property of that
# Currently only by accent voice proprety is returned
def get_voice_property(engine, age=30, gender='female', accent='english-us'):
	voices = engine.getProperty('voices')
	for voice in voices:
		if accent in str(voice.name):
			return voice

	raise ValueError('Demanded accent does not matched')


def speak_sentences(sentences, max_sentences_to_be_spoken=sys.maxsize):
	max_sentences_to_be_spoken = min(max_sentences_to_be_spoken, len(sentences))
	engine = pyttsx.init()
	engine.setProperty('rate', 140)

	i = 1
	# voice = get_voice_property(engine, age=10, gender='female', accent='hindi')
	# voice = get_voice_property(engine, age=10, gender='female', accent='english')
	voice = get_voice_property(engine, age=10, gender='female', accent='default')
	# voice = get_voice_property(engine, age=10, gender='female', accent='english-north')
	# voice = get_voice_property(engine, age=10, gender='female', accent='english_rp')
	# voice = get_voice_property(engine, age=10, gender='female', accent='english_wmids')
	# voice = get_voice_property(engine, age=10, gender='female', accent='default')

	
	engine.setProperty('voice', voice.id)
	for s in sentences:
	    if i > max_sentences_to_be_spoken:
	    	break
	    
	    # print(s)
	    engine.say(s)
	    i += 1    
	engine.runAndWait()



if __name__ == '__main__':
	pass