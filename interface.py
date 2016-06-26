# coding: utf-8

from Tkinter import *
from tkFileDialog import askopenfilname
from compactador import *
import tkMessageBox
from threading import Thread

class Aplicacao:
	"""docstring fos Aplicacao"""
	def __init__(self, arg):
		self.frame = Frame(master)
		self.frame.pack()

root = Tk()
root.title("Compactador de arquivos")
root.iconbitmap(default="icone.ico")
root.geometry("400x300")
root.resizable(width=FALSE, height=FALSE)
Aplicacao(root)
root.mainloop()
		