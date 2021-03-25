from tkinter import *

fen =Tk()

class tclass:
    def __init__(self):
        self.varA = IntVar()
        a = Checkbutton(
            fen, text=" Python ",
            variable=self.varA,
            command=self.cba)
        a.pack()

        self.varB = IntVar()
        b = Checkbutton(
            fen, text=" Scala ",
            variable=self.varB,
            command=self.cbb)
        b.pack()

        self.varC = IntVar()
        c = Checkbutton(
            fen, text=" Go Language ",
            variable=self.varC,
            command=self.cbc)
        c.pack()

        self.varD = IntVar()
        d = Checkbutton(
            fen, text=" R programming",
            variable=self.varD,
            command=self.cbd)
        d.pack()

    def cba(self):
        if(self.varA.get()):
            print("You know Python...!")
        else:
            print("You don't know Python...!")
    def cbb(self):
        if(self.varB.get()):
            print("You know Scala...!")
        else:
            print("You don't know Scala...!")
    def cbc(self):
        if(self.varC.get()):
            print("You know Go Language...!")
        else:
            print("You don't know Go Language...!")
    def cbd(self):
        if(self.varD.get()):
            print("You know R programming...!")
        else:
            print("You don't know R programming...!")

a = tclass()
fen.mainloop()
