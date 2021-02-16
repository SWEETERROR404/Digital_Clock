from tkinter import Tk,Label,mainloop
from time import strftime
from playsound import playsound

class Clock:

    def __init__(self):
        self.title = "Clock"
        self.background = "black"
        self.foreground = "orange"
        self.font = "Verdana 50"
        self.width = 420
        self.height = 80
        self.functions()

    def update(self):
        self.label.config(text=strftime("%I:%M:%S %p"),background=self.background,foreground=self.foreground,font=self.font)
        playsound("sound.wav")
        self.label.pack()
        self.label.after(900,self.update)

    def functions(self):
        self.root = Tk()
        self.root.geometry(f"{self.width}x{self.height}+450+320")
        self.root.maxsize(self.width,self.height)
        self.root.minsize(self.width,self.height)
        self.title = self.root.title(self.title)
        self.label = Label(self.root)
        self.update()
        self.close = mainloop()
Clock()