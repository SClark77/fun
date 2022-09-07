''' 
translation program using google translate api

pip install googletrans==3.1.0a0, SpeechRecognition, PyAudio, gTTS, playsound

'''

import googletrans
import speech_recognition as sr
import gTTS
import playsound


# to print to console the list of languages
#print(googletrans.LANGUAGES)

recognizer = sr.Recognizer()
translator = googletrans.Translator()

# set input language
input_lang = 'fr-FR'
# set translation language here:
out_lang = 'en'

try:
	with sr.Microphone() as source:
		print('Speak Now')
		voice = recognizer.listen(source)
		text = recognizer.recognize_google(voice, language=input_lang)
		print(text)
except:
	pass	

# [variable to hold translation] = [call translator to translate](['text to translate', dest='language code to translate to'])  
translated = translator.translate(text, dest=out_lang)
print(translated.text)
converted_audio = gtts.gTTS(translated.text, lang=out_lang)
converted_audio.save('tranlate.mp3')
playsound.playsound('translate.mp3')