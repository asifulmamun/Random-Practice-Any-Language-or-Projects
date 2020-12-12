"""
pip install pyttsx3 #Install text to speech library
import text to speech library and initialize
"""
import pyttsx3
engine = pyttsx3.init()


engine.setProperty('voice', engine.getProperty('voices')[1].id) # Change Voice sound to female (0 for male and 1 for female)
engine.setProperty('rate', 120) # Change Voice Speaking Speed

myText = "I am testing this voice" # text which will say (Source)
engine.say(myText) # Telling Text
engine.save_to_file(myText, 'media/output.mp3') # Saving audio file to media folder as output.mp3 name

engine.runAndWait() # End