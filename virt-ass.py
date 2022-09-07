'''
virtual assistant
programming hero youtube

pip install speachrecognition, pyttx3, pyaudio, pywhatkit, wikipedia, pyjokes
'''

import speach_recognition as sr
import pyttx3
import pywhatkit
import datetime
import wikipedia
import pyjokes


listener = sr.Recognizer()
engine = pyttx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
def talk(text):
	engine.say(text)
	engine.runAndWait()


def take_command():
	try:
		with sr.Microphone as source:
			print('Sir, awaiting instruction....')
			voice = listener.listen(source)
			command = listener.Recognize_google(voice)
			command = command.lower()
			if 'curie' in command:
				command = command.replace('curie')

				print(command)
	except:
		pass
	return command

def run_curie():
	command = take_command()
	print(command)
	if 'on youtube play' in command:
		ytube = command.replace('on youtube play', '')

		talk('Sir, Playing ' + ytube + ' on youtube.')
		pywhatkit.playonyt(ytube)
	elif 'time' in command:
		time = datetime.datetime.now().strftime('%H:%M:%S:%p')# returns hour - minuit - second - and am/pm
		talk('Sir, The exact current time is ' + time)
	elif 'get info on ' in command:
		subject = command.replace('get info on ', '')
		info = wikipedia.summary(suject, 5)
		print(info)
		talk('Sir, wikipedia states ' + info)
	elif 'joke' in command:
		talk(pyjokes.get_joke())

	else:
		talk('Sorry Sir, I didnt understand, could you say that again?')


while True:
	run_curie()