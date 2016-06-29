# coding: utf-8

from Tkinter import *
from tkFileDialog import askopenfilename 
from compactador import *
import tkMessageBox
from threading import Thread

class Aplicacao:

	def adicionar(self):
		pass

	def deletar(self):
		pass

	
	def __init__(self, master):
		self.frame = Frame(master)
		self.frame.pack()

		self.botao_adicionar = Button(self.frame, text="Adicionar", command=self.adicionar, bd=3)
		self.botao_adicionar["font"] = ('Arial',12)
		self.botao_adicionar.pack(pady=10,padx=30,side="left")

		self.botao_deletar = Button(self.frame, text="Deletar", command=self.deletar, bd=3)
		self.botao_deletar["font"] = ('Arial',12)
		self.botao_deletar.pack(padx=30,side="right")


root = Tk()
root.title("Compactador de arquivos")
root.iconbitmap(default="icone.ico")
root.geometry("400x300")
root.resizable(width=FALSE, height=FALSE)
Aplicacao(root)
root.mainloop()
		