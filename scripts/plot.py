import Tkinter as tk
import time
import numpy as np
import json

a = np.zeros((17,17))
b = np.zeros((17,17))

class GameBoard(tk.Frame):
	def __init__(self, parent, rows=17, columns=17, size=32, color1="white", color2="black"):
		'''size is the size of a square, in pixels'''

		self.rows = rows
		self.columns = columns
		self.size = size
		self.color1 = color1
		self.color2 = color2
		self.pieces = {}
		self.squareID = [[None for i in range(rows)] for j in range(columns)]

		canvas_width = columns * size
		canvas_height = rows * size

		tk.Frame.__init__(self, parent)
		self.canvas = tk.Canvas(self, borderwidth=0, highlightthickness=0,
								width=canvas_width, height=canvas_height, background="bisque")
		self.canvas.pack(side="top", fill="both", expand=True, padx=2, pady=2)

		# this binding will cause a refresh if the user interactively
		# changes the window size
		self.canvas.bind("<Configure>", self.refresh)


	def changeColor(self,a):
		'''Change color of given square'''
		for row in range(16):
			for column in range(16): 
				#rectifying random error on last line of input
				#for k in range(16):
				#	a[16][k] = 0

				if (a[row][column]) == 1:
					color = 'black'
				else:
					color = 'white'
				self.canvas.itemconfig(self.squareID[row][column], fill=color)
		pass

	def check(self,a,r2,c2):
		if a[r2][c2] == 1: 
			sum = a[r2][(c2+1)%17] + a[r2][(c2-1)%17] + a[(r2-1)%17][c2] + a[(r2+1)%17][c2] + a[(r2-1)%17][c2-1] + a[(r2-1)%17][(c2+1)%17] + a[(r2+1)%17][(c2-1)%17] + a[(r2+1)%17][(c2+1)%17]
			if (sum == 3 or sum == 2): #assuming cell lives on if it
				return 1
			else:
				return 0
		
		else:
			sum = a[r2][(c2+1)%17] + a[r2][(c2-1)%17] + a[(r2-1)%17][c2] + a[(r2+1)%17][c2] + a[(r2-1)%17][c2-1] + a[r2-1][c2+1] + a[r2+1][c2-1] + a[r2+1][c2+1]
			if sum == 3:
				return 1
			else: 
				return 0

	def refresh(self, event):
		'''Redraw the board, possibly in response to window being resized'''
		xsize = int((event.width-1) / self.columns)
		ysize = int((event.height-1) / self.rows)
		self.size = min(xsize, ysize)
		self.canvas.delete("square")
		color = self.color2
		for row in range(self.rows):
			color = self.color1 if color == self.color2 else self.color2
			for col in range(self.columns):
				x1 = (col * self.size)
				y1 = (row * self.size)
				x2 = x1 + self.size
				y2 = y1 + self.size
				self.squareID[row][col] = self.canvas.create_rectangle(x1, y1, x2, y2, outline="black", fill=color, tags="square")
				color = self.color1 if color == self.color2 else self.color2
		# for name in self.pieces:
			# self.placepiece(name, self.pieces[name][0], self.pieces[name][1])
		self.canvas.tag_raise("piece")
		self.canvas.tag_lower("square")



class Starte():
	def startex(self,a):
		root = tk.Tk()
		board = GameBoard(root)
		board.pack(side="top", fill="both", expand="true", padx=4, pady=4)
		color = "black"
		
		
		while True:
			

			root.update_idletasks()
			root.update()
			
			for r in range(16):
				for c in range(16):
					if board.check(a,r,c) == 1:
						b[r][c] = 1
					else:
						b[r][c] = 0            

			board.changeColor(b)

			for k in range(16):
				for l in range(16):
					a[k][l] = b[k][l]

			time.sleep(0.5)

	
	def jsondef(self,ind):#ind corresponds to the value of the input 
		
		#json file will be read and converted to array 
		
		inputind = str(ind)

		with open("/media/aditi/New Volume/New folder/Internships/2017/GSOC2017/jde/python_challenge/final/resources/data.json") as json_file:
			json_data = json.load(json_file)
			
			for i in range(15):
				instr = "00000000000000000"

				instr = json_data[inputind][i]
				
				for j in range(15):
					a[i][j] = instr[j]

		self.startex(a)