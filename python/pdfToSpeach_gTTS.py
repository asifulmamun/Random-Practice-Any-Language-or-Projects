"""
# Fist Install gTTS with Command
pip install gTTS

# pdf reader
pip install PyPDF2

# for play sound module
pip install playsound
"""

# import
from gtts import gTTS # gTTS
from playsound import playsound # playsound
import PyPDF2

# file location
pdfFileLocation = open('media/economics_supply.pdf', 'rb')

# pdf reading init (book)-means reading from this location
fullPdf = PyPDF2.PdfFileReader(pdfFileLocation)

# # total pages count
# print(fullPdf.numPages)

# Which pages will get from pdf = page Number (fullPdf.numPage here numPages collect the total number of pdf)
# range 0 to totalpage number or actual number like as 0-3 (4 pages) example range(0, 3)
for pages in range(0, fullPdf.numPages):
    # Target pages from fullPdf
    targetPage = fullPdf.getPage(pages)

    # text Extract form targetPage
    text = targetPage.extractText()

    # # test this text extract or not
    # print(text)

    # Text Input in Variable, lang #en or #bn  or #ar is for language
    tts = gTTS(text, lang="en")

    # Save Txt as Audio
    tts.save('media/textToSpech_gTTSandPlay.mp3')

    # playing sound
    playsound('media/textToSpech_gTTSandPlay.mp3')