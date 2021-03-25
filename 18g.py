import tkinter

root = tkinter.Tk()

def color_label(any_label, user_input):
    any_label.configure(text=user_input, bg="green", fg="white")

frame1 = tkinter.Frame(root, borderwidth=2, relief='ridge')
frame2 = tkinter.Frame(root, borderwidth=2, relief='ridge')
frame3 = tkinter.Frame(root, borderwidth=2, relief='ridge')
frame4 = tkinter.Frame(root, borderwidth=2, relief='ridge')
frame5 = tkinter.Frame(root, borderwidth=2, relief='ridge')
frame6 = tkinter.Frame(root, borderwidth=2, relief='ridge')

frame1.grid(column=0, row=0, sticky="nsew")
frame2.grid(column=0, row=1, sticky="nsew")
frame3.grid(column=1, row=0, sticky="nsew")
frame4.grid(column=1, row=1, sticky="nsew")
frame5.grid(column=0, row=2, sticky="nsew", columnspan=2)
frame6.grid(column=0, row=3, sticky="nsew", columnspan=2)

label1 = tkinter.Label(frame1, text="Simple label 1")
label2 = tkinter.Label(frame2, text="Simple label 2")
button1 = tkinter.Button(frame3, text="Configure button 1", command=lambda: color_label(label1, entry.get()))
button2 = tkinter.Button(frame4, text="Configure button 2", command=lambda: color_label(label2, entry.get()))

button3 = tkinter.Button(frame5, text="Close", command=root.destroy)

entry = tkinter.Entry(frame6)
label1.pack(fill='x')
label2.pack(fill='x')
button1.pack(fill='x')
button2.pack(fill='x')
button3.pack(fill='x')
entry.pack(fill='x')
root.mainloop()
