# virtual talking friend - programming hero youtube
# check ttsx3 docs for ideas

# pip install pyttsx3

import pyttsx3

friend = pyttsx3.init()
speech = input ('Say something: ')
friend.say(speech)
friend.runAndWait()
