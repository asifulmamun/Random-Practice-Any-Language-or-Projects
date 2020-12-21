# import gui
from tkinter import *

# init tkinter in app
app = Tk()

# titile of app window
app.title("Weather Application")

# size of app window
app.geometry('360x360')


city_text = StringVar()
city_entry = Entry(app, textvariable=city_text)

city_entry.pack()




# gui main loop endline
app.mainloop()