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

# button command execute
def search():
    # print('This is ' + myTextVairable.get())
    # # Label
    # Label(app, text=myTextVairable.get(), font=('bold', 20)).pack()
    
    # # Inject Value to Varibale in gui
    # printLebelValue['text'] = myTextVairable.get()

    # Format - Inject Value to Varibale in gui
    printLebelValue['text'] = '{}'.format(myTextVairable.get())

# search area
myTextVairable = StringVar()
Entry(app, textvariable=myTextVairable).pack()

# form Button 
Button(app, text='Search', width=12, command=search).pack()

'''
---------
Gui Result
----------
'''
# Label
printLebelValue = Label(app, text='', font=('bold', 20))
printLebelValue.pack()

'''
-------
End
------
'''
# gui main loop endline
app.mainloop()