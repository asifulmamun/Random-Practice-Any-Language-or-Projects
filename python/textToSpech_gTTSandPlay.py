"""
# Fist Install gtts with Command
pip install gTTS

# for play sound module
pip install playsound
"""

# import
from gtts import gTTS # gTTS
from playsound import playsound # playsound

# Assign Text
# myText = "I am Ummay Habiba Mim"
# myText = "আমি উম্মে হাবীবা মীম"
myText = "أنا أمي حبيبة ميم"

# Text Input in Variable, lang #en or #bn  or #ar is for language
tts = gTTS(myText, lang="ar")

# Save Txt as Audio
tts.save('media/textToSpech_gTTSandPlay.mp3')

# playing sound
playsound('media/textToSpech_gTTSandPlay.mp3')