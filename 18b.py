import tkinter as tk
from tkinter import BOTH, END, LEFT
my_w = tk.Tk()
my_w.geometry("500x400")  

def my_upd():
    my_str1=t1.get("1.0",END)  # read from one text box t1
    t2.insert(tk.END, my_str1) # Add to another text box t2
    
    
my_str = tk.StringVar()

l1 = tk.Label(my_w,  text='Your Name', width=10 ) # added one Label 
l1.grid(row=1,column=1) 

t1 = tk.Text(my_w,  height=1, width=20,bg='yellow')# added one text box
#t1=Entry(my_w, width=10)
t1.grid(row=1,column=2) 

b1 = tk.Button(my_w, text='Update', width=10,bg='red',command=lambda: my_upd()) # button added
b1.grid(row=1,column=3) 

t2 = tk.Text(my_w, height=1, width=15, bg='#00f000' ) # added one textbox to read 
t2.grid(row=1,column=4) 

my_w.mainloop()
