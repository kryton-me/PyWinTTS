# -*- coding: utf-8 -*-
import pyperclip
import pyttsx
import unicodedata

class TextToSpeach:

	def __init__(self):
		self.get_copy_buffer()
		self.refine_text()
		print(self.text)
		self.say_it()

		
	def get_copy_buffer(self):
		try:
			self.data = pyperclip.paste()
		except:
			self.data = "I did not read the copy buffer"

	def refine_text(self):
		if isinstance(self.data, basestring):
		
			# Attempt to convert the copy buffer ti UTF-8, does not work. 
			self.data = unicode(self.data, 'utf-8')

               # convert a few known unicodes to words
			self.data = self.data.replace("€".decode('utf-8').encode('utf-8'), "Euros")
			self.data = self.data.replace("£".decode('utf-8').encode('utf-8'), 'Pounds')
			self.data = self.data.replace("Ω".decode('utf-8').encode('utf-8'), 'Ohms')
			self.data = self.data.replace("Ω".decode('utf-8').encode('utf-8'), 'Ohms')
			self.data = self.data.replace("μ".decode('utf-8').encode('utf-8'), 'Mu')

			# Normalize the rest
			self.text = unicodedata.normalize('NFKD', self.data).encode('ascii','ignore')

			self.text = self.data

			# Depbug statment
			#print("have cleaned text")

		else:
			
			self.text = "No Text in copy buffer"

	def say_it(self):
		# Set up the voise engine
		engine = pyttsx.init()
		# Slow it down a bit as you listing for accuracy not comprehension. (defult = 200)
		engine.rate = 120
		# load the text
		engine.say(self.text)
		# run it and hang around to confirm all is well.
		engine.runAndWait()
		# confirm it's over
		
if __name__ == '__main__':

	wibble = TextToSpeach()