# -*- coding: utf-8 -*-

#This software has an MIT Licence, and the libaries are as follows:
import pyperclip as copyBuffer # BSD Licence
import easy_pyttsx3 as tts # MIT licence
import platform #built in to python
#import unicodedata

class TextToSpeach:

	def __init__(self):
		
		# Some magic numbers!
		# I would sugest a config file but fear it would slow it down.
		
		# Add custom words, this has an electronics bias
		self.customWords = {"€": "Euros", 
		"£": 'Pounds',
		"Ω": 'Ohms',
		"μ": 'Mu',
		"ü": 'ur'}
		
		self.get_copy_buffer()
		self.refine_text()
		print(self.text)
		self.say_it()

	def get_copy_buffer(self):
		try:
			
			# extract text from the copy buffer, this libarty only uses text.
			self.data = copyBuffer.paste()
	
		except:
			self.data = "Failed to ready copy buffer"

	def refine_text(self):
		
		#Convert some symbols to custom words
		self.tweekSymbols()
		
		# if your running windows
		if platform.system() == "Windows" :
		
			#... we need to do some formatting. Well I'm basing this on Windows 7
			self.iHateUniCode()

		# if your running MacOS
		elif platform.system() == "Darwin" :
			
			# No faffing around just send it the full utf-8!
			self.text = self.data

		# if it's linux / solaris / BSD risk utf-8! this is full of future development.
		elif platform.system() == "Linux" :
		
			# Go the full utf-8!
			self.text = self.data

	def tweekSymbols(self):

		for symbol in self.customWords :

			# convert a few known unicodes to words
			self.data = self.data.replace(symbol, self.customWords[symbol])

	def iHateUniCode(self):
		
		# Normalize the text to ascii
		string_encode = self.data.encode("ascii","ignore")
		self.text = string_encode.decode()
	
	def say_it(self):
		
		try:
			# off you go.
			tts.say(self.text)
			
		except:
		
			print("failed to get system to speak")
		
if __name__ == '__main__':

	TextToSpeach()
