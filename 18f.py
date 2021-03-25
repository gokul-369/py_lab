from tkinter import *

def show():
    dob=str(spinbox_day.get())+" "+str(spinbox_month.get())+" "+str(spinbox_year.get())
    print("Your Date of Birth is %s"%(dob))

master = Tk()
master.title("Date of Birth")
master.geometry("500x400")
spinbox_day = Spinbox(master, fg = "blue", font=(' ',20), from_ = 0, to = 31)
spinbox_day.grid(row = 2, column = 1)

spinbox_month = Spinbox(master, fg = "blue", font=(' ',20), values = ("January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"))
spinbox_month.grid(row = 3, column = 1)

spinbox_year = Spinbox(master, fg = "blue", font=('',20), from_ = 1900, to = 2005)
spinbox_year.grid(row = 4, column = 1)

Button(master, text = "Print", command = show, bg = "yellow", fg = "red").grid(row=5, column = 1)
Button(master, text = "Close", command = master.destroy, bg = "yellow", fg = "red").grid(row=5, column = 2)


master.mainloop()
