# PyWinTTS
Python script to unlock the TTS potential of Windows

Windows has a built in Text To Speech tool but there is no way to access it without using some form of code / software. To get around this I have released a basic Python script to do this. A copy of the script can be found on [GitHub](https://github.com/kryton-me/PyWinTTS). I’ve not been able to test this as I don’t have a Windows system to debug it on. I know if you used unicode characters it would hang on windows 7 which I have attempted to mitigate. The script is cross platform and is known to run on MacOS. I have released this under the MIT license for maximum compatibility.

If you have a Mac your much better using the built in tools and not this script.

# Install Python
This script has bern tested on Python 3.9 & 3.10. The Libraries used are not supported by python 2.7

# libraries required
Command syntax for Windows users

## Copy buffer access

    py -m pip install pyperclip

This uses the BSD Licence

## Text to speech tool access

    py -m pip install pyttsx3

This uses the MIT License

# Shortcut
In order to use this in windows with a key combination a shortcut file is needed. 
* create a link file on the desktop to the script
* set the target as the above script
* set a keyboard shortcut in the link file as: crtl + ⬆️ + C

# Using the script
* Select the text to want read then press ctrl + C to copy it.
* Press the keyboard combination crtl + ⬆️ + C to have it read back.