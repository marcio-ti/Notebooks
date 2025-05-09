import sys

from PySide6.QtWidgets import QApplication, QPushButton

app = QApplication(sys.argv)

botao = QPushButton('Texto do Botão')
botao.setStyleSheet("font-size: 40px; color: red")
botao.show()

# botao2 = QPushButton('Botão 2')
# botao2.show()

app.exec()
