import speech_recognition as sr
import sys

# obtain audio from the microphone
r = sr.Recognizer()
with sr.Microphone() as source:
	r.adjust_for_ambient_noise(source) #adapt to the noise
	print("Say something!")

	while True:
		audio = r.listen(source)

		# recognize speech using Sphinx
		try:
			print("Sphinx thinks you said " + r.recognize_sphinx(audio))
			if(str(r.recognize_google(audio))=='exit'):
				print("TRUE")
				break
		except:
			print("Firse")

	sys.exit()