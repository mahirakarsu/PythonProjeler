import webbrowser
from tkinter import *


root = Tk()
root.title("WebBrowser")
root.geometry("300x200")


def copyassignment():
    webbrowser.open("www.google.com")
    
    
    
def google():
    webbrowser.open("www.google.com")
    
copyassignment = Button(root,text = "visit google",command = copyassignment).pack(pady = 20)
mygoogle = Button(root,text = "open google",command = google).pack(pady =20)
root.mainloop()









