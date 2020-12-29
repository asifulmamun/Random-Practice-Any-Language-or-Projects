"""
# Fist Install gtts with Command
pip install gTTS

# for play sound module
pip install playsound
"""

# import
from gtts import gTTS # gTTs
from playsound import playsound # playsound

# Assign Text
myText = "I am al mamun"

# Text Input in Variable, lang #en or #bn is for language
tts = gTTS(myText, lang="en")

# Save Txt as Audio
tts.save('textToSpech_gTTsAndPlay.mp3')

# playing sound
playsound('textToSpech_gTTsAndPlay.mp3')
