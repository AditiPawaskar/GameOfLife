from Tkinter import *
from plot import *

import json
import tkMessageBox 

indicator = 0

def page2():
	page1obj.destroy()
	page2obj = Tk()
	
	page2obj.geometry("700x600")

	img1 = tk.PhotoImage(file="/media/aditi/New Volume/New folder/Internships/2017/GSOC2017/jde/python_challenge/final/resources/images/mode1.png")
	img2 = tk.PhotoImage(file="/media/aditi/New Volume/New folder/Internships/2017/GSOC2017/jde/python_challenge/final/resources/images/mode2.png")
	img3 = tk.PhotoImage(file="/media/aditi/New Volume/New folder/Internships/2017/GSOC2017/jde/python_challenge/final/resources/images/mode3.png")
	img4 = tk.PhotoImage(file="/media/aditi/New Volume/New folder/Internships/2017/GSOC2017/jde/python_challenge/final/resources/images/mode4.png")

	B1 = Button(page2obj, text = "config 1", command = func1,image = img1)
	B1.place(x = 150,y = 70)
	B2 = Button(page2obj, text = "config 2", command = func2,image = img2)
	B2.place(x = 650,y = 70)
	B3 = Button(page2obj, text = "config 3", command = func3,image = img3)
	B3.place(x = 150,y = 470)
	B4 = Button(page2obj, text = "config 4", command = func4,image = img4)
	B4.place(x = 650,y = 470)

	#root = Tk()
	var = StringVar()
	label = Label( page2obj, textvariable=var, relief=RAISED ,height = 5, width = 20)
	var.set("CHOOSE MODE:")
	label.pack()
	label.place(x = 450, y = 20);
	#root.mainloop()
	page2obj.mainloop()
	
	
def func1():
	indicator = 1 
	obj = Starte()
	obj.jsondef(indicator)
	page2obj.destroy()

def func2():
	indicator = 2 
	obj = Starte()
	obj.jsondef(indicator)
	page2obj.destroy()	

def func3():
	indicator = 3 
	obj = Starte()
	obj.jsondef(indicator)
	page2obj.destroy()

def func4():
	indicator = 4 
	obj = Starte()	
	obj.jsondef(indicator)
	page2obj.destroy()	


def exitfn():
	page1obj.destroy()
	

if __name__ == "__main__":
	page1obj = Tk()
	
	page1obj.geometry("700x600")

	Bn = Button(page1obj, text = "New Game", command = page2)
	Bn.place(x = 350,y = 150)
	Be = Button(page1obj, text = "Exit Game", command = exitfn)
	Be.place(x = 350,y = 450)
	
	page1obj.mainloop()
