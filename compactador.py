# coding: utf-8

import zipfile
import os.path

class Compactador:
	"""docstring for Compactador"""
	def compactar(self, lista_arquivos):
		# abre o arquivo para escrita para escrita
		# primeiro parâmetro é o nome do arquivo ZIP
		# segundo parâmetro é o modo de abertura, 'w' é para escrita
		arquivo_zip = zipfile.ZipFile("arquivo.zip", "w")
		# percorre a lista
		for arquivo in lista_arquivos:
			# testa se é arquivo e se o arquivo existe
			if(os.path.isfile(arquivo) and os.path.exists(arquivo)):
				# pega o nome do arquivo base, sem o diretório
				base = os.path.basename(arquivo)
				# passa o diretório e o nome do arquivo a ser gravado
				arquivo_zip.write(arquivo, base)
		arquivo_zip.close() # fecha o arquivo
				
		
		
