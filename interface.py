# coding: utf-8

from Tkinter import *
from tkFileDialog import askopenfilename 
from compactador import *
import tkMessageBox
from threading import Thread

class Aplicacao:

	def adicionar(self):
		nome_arquivo = askopenfilename()
		if nome_arquivo != "":
			self.listbox.insert(END, nome_arquivo)


	def deletar(self):
		items = self.listbox.curselection() # obtem lista de índices dos itens
		if len(items) == 0:
			tkMessageBox.showinfo("Compactador", "Selecione pelo menos um item!")
		else:
			pos = 0
			for i in items: # percorre a lista de indices
				item_pos = int(i) - pos # obtem a posição do item selecionado
				self.listbox.delete(item_pos, item_pos) # deleta um item selecionado
				pos = pos + 1 # incrementa pos

	# função associada ao evento do botão compactar
	def compactar(self):
		# pega todos os itens da listbox
		lista_arquivos = self.listbox.get(0, END)
		if len(lista_arquivos) == 0:
			tkMessageBox.showinfo("Compactador", "Adicione algum arquivo para compactar!")
			return # sai da função
		def executar():
			self.botao_compactar.configure(state=DISABLED) # desabilita o botão
			# se a lista não estiver vazia, compacta
			compactador = Compactador() # obtém instância de Compactador
			compactador.compactar(lista_arquivos) # compacta todos os arquivos
			self.botao_compactar.configure(state=NORMAL) # habilita o botão
		t = Thread(target=executar) # cria thread
		t.start() # inicia a thread
		
	
	def __init__(self, master):
		self.frame = Frame(master)
		self.frame.pack()

		self.botao_adicionar = Button(self.frame, text="Adicionar", command=self.adicionar, bd=3)
		self.botao_adicionar["font"] = ('Arial',12)
		self.botao_adicionar.pack(pady=10,padx=30,side="left")

		self.botao_deletar = Button(self.frame, text="Deletar", command=self.deletar, bd=3)
		self.botao_deletar["font"] = ('Arial',12)
		self.botao_deletar.pack(padx=30,side="right")

		self.frame2 = Frame(master)
		self.frame2.pack()

		self.sby = Scrollbar(self.frame2)
		self.sby.pack(side=RIGHT, fill=Y)

		self.sbx = Scrollbar(self.frame2, orient=HORIZONTAL)
		self.sbx.pack(side=BOTTOM, fill=X)

		self.listbox = Listbox(self.frame2, width=50, height=10, selectmode=EXTENDED)
		self.listbox.pack()

		self.listbox.config(yscrollcommand=self.sby.set)
		self.sby.config(command=self.listbox.yview)
		self.listbox.config(xscrollcommand=self.sbx.set)
		self.sbx.config(command=self.listbox.xview)

		# cria outro frame
		self.frame3 = Frame(master)
		self.frame3.pack() 

		self.botao_compactar = Button(self.frame3, text="Compactar", command=self.compactar, bd=3)
		self.botao_compactar['font'] = ('Arial', 12)
		self.botao_compactar.pack(pady=10)

		
root = Tk()
root.title("Compactador de arquivos")
root.iconbitmap(default="icone.ico")
root.geometry("400x300")
root.resizable(width=FALSE, height=FALSE)
Aplicacao(root)
root.mainloop()
		