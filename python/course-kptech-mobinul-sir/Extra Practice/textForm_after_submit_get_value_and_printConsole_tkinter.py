"""
# Fist Install
pip install tkinter
"""

# import gui
from tkinter import *

# init tkinter in app
app = Tk()
# titile of app window
app.title("Weather Application")
# size of app window
app.geometry('360x360')


'''
-----------------------
=== Regular Way ===
-----------------------
'''
# # button command execute
# def search():
#     textFromForm = myTextVairable.get()
#     print('This is ' + textFromForm)

# # search area
# myTextVairable = StringVar()
# text_entry = Entry(app, textvariable=myTextVairable)
# text_entry.pack()

# # form Button 
# search_btn = Button(app, text='Search', width=12, command=search)
# search_btn.pack()


'''
-----------------------
=== Alternative ===
-----------------------
'''
# button command execute
def search():
    print('This is ' + myTextVairable.get())

# search area
myTextVairable = StringVar()
Entry(app, textvariable=myTextVairable).pack()

# form Button 
Button(app, text='Search', width=12, command=search).pack()


'''
-------
End
------
'''
# gui main loop endline
app.mainloop()