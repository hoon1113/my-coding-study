#피하기
from tkinter import *
import time

W = Tk()
W.title("피하기 게임")
W.resizable(0,0)
canvas = Canvas(W, width=640, height=640, bg="white")
canvas.pack()
canvas.create_rectangle(310,310,330,330,fill="black")
W.mainloop()