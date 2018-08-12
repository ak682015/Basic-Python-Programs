import winspeech
import sys
import speech_recognition as sr

winspeech.initialize_recognizer(winspeech.INPROC_RECOGNIZER)

def speechRecog(result, listener):
	print("You Said: ",result)
	
	winspeech.say(result)
	if( result == "stop"):
		winspeech.stop_listening()
		sys.exit(0)


listener = winspeech.listen_for_anything(speechRecog)

#while listener.is_listening():
#	continue



def myCommand():
    "listens for commands"
    r = sr.Recognizer()

    with sr.Microphone() as source:
        #r.pause_threshold = 1
        print('Ready...')
        r.adjust_for_ambient_noise(source, duration=1)
        audio = r.listen(source,phrase_time_limit=10)

    try:
        command = r.recognize_google(audio).lower()
        #talkToMe('Tumne ye bola: ' + command)
        print('You Said: ' + command + '\n')

    #loop back to continue to listen for commands if unrecognizable speech is received
    except sr.UnknownValueError:
        #print('Your last command couldn\'t be heard')
        #talkToMe("missed your words")
        print("missed your words")
        command = myCommand();
    except:
        print("No Internet connection bye")
        talkToMe("No Internet connection bye")
        sys.exit()

    
    return command


while True:
	speechRecog("I am sort of new to using speech recognition in my programs, and I think you may be able to give some insight. With using Winspeech, is this module always listening once the callback is initiated? If I wanted to, let's say, allow a user to conduct a google search with their voice, how do I first call the search and then not allow the voice input for the search to impact the larger programmatic process? For instance, you start up the program, you say google search, the program activates the google search function. Now all input from the voice will be to perform the google search. But how can I differentiate these inputs: General selections from specific processes?﻿",winspeech.listen_for_anything(speechRecog))