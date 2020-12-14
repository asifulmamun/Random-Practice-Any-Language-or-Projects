"""
Fist Install gtts with Command: pip install gTTS
"""
# import
from gtts import gTTS

# Assign Text
myText = "আমি আল মামুন"

# Text Input in Variable, lang #en or #bn is for language
tts = gTTS(myText, lang="bn")

# Save Txt as Audio
tts.save("media/hello.mp3")