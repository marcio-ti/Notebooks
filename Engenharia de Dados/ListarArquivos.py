"""
Lista todos os arquivos de determinado diretório que não sejam .txt ou .pdf
"""

import os

caminho = r"C:\Users\divtec-dados\OneDrive\Estudos\Cursos\WEB"
pasta = r'\Udemy - The Flask Mega-Tutorial (Python Web Development)'
caminho = caminho + pasta

print()
for item in os.listdir(caminho):
	item = item.replace('¦', 'ã')
	if '.txt' not in item and '.pdf' not in item and '.zip' not in item and '.html' not in item:
		print(item)