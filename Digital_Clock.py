from tkinter import *
from tkinter.ttk import *
from time import strftime

class Clock:
	def __init__(self):
		self.title = 'Clock'
		self.background = "black"
		self.foreground = "orange"
		self.font_style = "Verdana"
		self.font_size = "50"
		self.Transparent = None
		self.width = 419
		self.heigth = 80
		self.functions()

	def labels(self):
		self.label_time = Label(self.Main_Window)

	def update(self):
		time = strftime("%I:%M:%S %p")
		self.label_time.config(font=f"{self.font_style} {self.font_size}", background=self.background, foreground=self.foreground, text=time)
		self.label_time.pack()
		self.label_time.after(1000, self.update)

	def functions(self):
		self.Main_Window = Tk()
		self.Main_Window.geometry(f"{self.width}x{self.heigth}+450+250")
		self.Main_Window.maxsize(self.width, self.heigth)
		self.Main_Window.minsize(self.width, self.heigth)
		self.labels()
		self.Main_Window.wait_visibility(self.Main_Window)
		self.Main_Window.wm_attributes('-alpha', self.Transparent)
		self.Main_Window.title(self.title)
		self.update()
		self.Close = mainloop()
Clock()