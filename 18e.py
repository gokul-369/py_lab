import tkinter as tk
 
win = tk.Tk()
 
 
def additem():
    listbox.insert(tk.END, content.get())
 
 
def deleteAll():
    listbox.delete(0, tk.END)
 
 
def deleteselected():
    listbox.delete(tk.ANCHOR)
 
l1 = tk.Label(win,  text='Enter the item ', font=('',10)  ) # added one Label
l1.pack()
 
content = tk.StringVar()
entry = tk.Entry(win, textvariable=content)
entry.pack()
 
button = tk.Button(win, text="Add Item", command=additem)
button.pack()
 
button2 = tk.Button(win, text="Delete list", command=deleteAll)
button2.pack()
 
button3 = tk.Button(win, text="Delete selected", command=deleteselected)
button3.pack()
 
listbox = tk.Listbox(win)
listbox.pack()
 
win.mainloop()
 