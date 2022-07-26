"""
# Install text to speech Module
pip install pyttsx3

# Linux Dependencys
sudo apt install espeak
sudo apt install espeak-ng
sudo apt install ffmpeg
"""

# import text to speech library and initialize
import pyttsx3
engine = pyttsx3.init()

# Change Voice sound to female (0 for male and 1 for female)
engine.setProperty('voice', engine.getProperty('voices')[1].id)

# Change Voice Speaking Speed
engine.setProperty('rate', 120)

# text which will say (Source)
myText = "I am al mamun"

# Telling Text/ Speak Out
engine.say(myText)

# Saving audio file to media folder as output.mp3 name
engine.save_to_file(myText, 'media/textToSpech_pyttsx3.mp3')

# End
engine.runAndWait()
# if need to stop pyttsx3 module
engine.stop()