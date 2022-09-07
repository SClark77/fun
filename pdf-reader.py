'''
	 a pdf audiobook reader project from programming-hero on youtube

	 pip install pyttsx3
	 pip install PyPDF2

'''

import pyttsx3
import PyPDF2

book = open('pdf-name.pdf', 'rb')
pdfReader = PyPDF2.PdfFileReader(book)
pages = pdfReader.numPages
print(pages)




speaker = pyttsx3.init()
for num in range(1, pages):

	page = pdfReader.getPage(7)
	text = page.extractText()
	speaker.say(text)
	speaker.runAndWait()