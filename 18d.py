import tkinter as tk
my_w = tk.Tk()
my_w.geometry("500x500")  # Size of the window
my_w.title("Radio button")
#my_w.configure(bg = "cyan")

def my_upd():
    print('You have selected ',r1_v.get())

l1 = tk.Label(my_w,  text='Select the Course', font=('',10), width=20 ) # added one Label
l1.grid(row=1,column=2)

r1_v = tk.StringVar()  # We used string variable here
r1_v.set('Passed')     # Can assign value Appear or Failed

r1=tk.Radiobutton(my_w,text='BCA',variable=r1_v,value='BCA',
command=my_upd, bg = "yellow")
r1.grid(row=2,column=2)

r2=tk.Radiobutton(my_w,text='B.Sc',variable=r1_v,value='B.Sc',
command=my_upd, bg = "yellow")
r2.grid(row=3,column=2)

r3=tk.Radiobutton(my_w,text='B.Com',variable=r1_v,value='B.Com',
command=my_upd, bg = "yellow")
r3.grid(row=4,column=2)

my_w.mainloop()  # Keep the window open
