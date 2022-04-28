#!/bin/python3
# -*- coding: utf-8 -*-

#This software has an MIT Licence, and the libaries are as follows:
import pyperclip as copyBuffer # BSD Licence
import easy_pyttsx3 as tts # MIT licence

class TextToSpeach:

	def __init__(self):
		
		# Some magic numbers!
		# I would sugest a config file but fear it would slow it down.
		
		# Add custom words, this has an electronics bias
		self.customWords = {"€" = "Euros", 
		"£" = 'Pounds',
		"Ω" = 'Ohms',
		"μ" = 'Mu'}
		
		# Pick your speed
		self.speed = 120 # nice slow & clear.
		
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
		
		for symbol, word in self.customWords :
		
			# convert a few known unicodes to words
			self.data = self.data.replace(symbol, word)

		# if your running windows
		if platform.system() == "Windows" :
		
			# Normalize the text to ascii
			self.text = unicodedata.normalize('NFKD', self.data).encode('ascii','ignore')

		# if your running MacOS
		elif platform.system() == "MacOS" :
		
			self.data.append(", also you should try the Native MacOS tool it's much better!")
			
			# Go the full utf-8!
			self.text = self.data

		# if it's linux / solaris / BSD risk utf-8! this is full of future development.
		else :
		
			# Go the full utf-8!
			self.text = self.data
		
		# Depbug statment
		print(self.text)

	def say_it(self):
	
		# Set up the voise engine
		engine = pyttsx3.init()
		
		# Set preffered listing speed.
		engine.rate = self.speed
		
		try:
		
			# load the text
			engine.say(self.text)
		
			# off you go.
			engine.runAndWait()
			
		except:
		
			print("failed to get system to speak")
		
if __name__ == '__main__':

	TextToSpeach()