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
    pass

# search area
city_text = StringVar()
city_entry = Entry(app, textvariable=city_text)
city_entry.pack()

# search Button 
search_btn = Button(app, text='Search Weather', width=12, command=search)
search_btn.pack()

# Label
location_lbl = Label(app, text='Location', font=('bold', 20))
location_lbl.pack()





# gui main loop endline
app.mainloop()