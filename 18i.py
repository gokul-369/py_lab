from tkinter import *
from tkinter import filedialog as fd

def NewFile():
    print("Clicked New File..!")

def OpenFile():
    print("Clicked open file..!")
    file = fd.askopenfile(mode ='r', filetypes =[('Python Files', '*.py')])
    if file is not None:
        content = file.read()
        print(content)

def About():
    print("This is a simple example of a menu..!")

root = Tk()
menu = Menu(root)
root.config(menu=menu)
filemenu = Menu(menu)
menu.add_cascade(label="File", menu=filemenu)
filemenu.add_command(label="New", command=NewFile)
filemenu.add_command(label="Open...", command=OpenFile)
filemenu.add_separator()
filemenu.add_command(label="Exit", command=root.destroy)

helpmenu = Menu(menu)
menu.add_cascade(label="Help", menu=helpmenu)
helpmenu.add_command(label="About...", command=About)

mainloop()
