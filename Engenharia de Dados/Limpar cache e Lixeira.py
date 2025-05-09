import os
import shutil

diretorios = [r"C:\Windows\Temp", r"C:\Users\marci\AppData\Local\Temp"]
def limpar_temporario(diretorio):
	for caminho in diretorios:
		try:
			shutil.rmtree(caminho)
			print(f"Pasta {caminho} deletada!")
		except (PermissionError, OSError) as e:
			print(f"Erro ao deletar pasta: {caminho} - {e}")

limpar_temporario(diretorios)