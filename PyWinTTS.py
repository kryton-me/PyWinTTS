# -*- coding: utf-8 -*-
import win32clipboard
import pyttsx
import sys
import unicodedata

#Think I need to migrate to Python 3 to get Unicode bit working. 

class TextToSpeach:

	def __init__(self):
		self.get_copy_buffer()
		self.refine_text()
		print self.text
		self.say_it()

		
	def get_copy_buffer(self):
		try:
			win32clipboard.OpenClipboard()
			self.data = win32clipboard.GetClipboardData()
			win32clipboard.CloseClipboard()
		except:
			win32clipboard.CloseClipboard()
			self.data = sys.exc_info()[0]

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

			#print "have cleaned text"

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