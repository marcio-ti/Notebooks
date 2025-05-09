"""
    O programa recebe dois arquivos, processa-os e retorna os boletos que foram pagos através do Banrisul
"""

import os
import sys
import threading

from PySide6.QtCore import Qt
from PySide6.QtGui import QCursor, Qt
from PySide6.QtGui import QFont
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QProgressBar, QLabel, QVBoxLayout, \
    QWidget, QFileDialog
from openpyxl import Workbook


class RecebimentosBoletos(QMainWindow):
    """
        Classe Principal do Aplicativo.
    """

    def __init__(self):
        super().__init__()
        # -------------------------------------------------------------------------------------- #
        # Especificações do Aplicativo
        self.setWindowTitle("CEASA RS - Financeiro")
        self.resize(650, 300)

        # -------------------------------------------------------------------------------------- #
        # -------------------------------------------------------------------------------------- #
        # Criando os widgets
        self.label1 = QLabel("Selecione o arquivo de remessa", self)
        self.label2 = QLabel("Selecione o arquivo de retorno bancário", self)
        self.botao1 = QPushButton("Arquivo de remessa", self)
        self.botao1.setCursor(QCursor(Qt.PointingHandCursor))
        self.botao2 = QPushButton("Arquivo de retorno", self)
        self.botao2.setCursor(QCursor(Qt.PointingHandCursor))
        self.progresso = QProgressBar(self)
        self.botao_executar = QPushButton("Executar Verificação", self)

        self.botao_executar.setCursor(QCursor(Qt.PointingHandCursor))

        # -------------------------------------------------------------------------------------- #
        # -------------------------------------------------------------------------------------- #
        # Criação do Label que recebe os valores dos arquivos selecionados em cada botão
        self.nome_arquivo_remessa = QLabel("", self)
        self.nome_arquivo_retorno = QLabel("", self)

        # -------------------------------------------------------------------------------------- #
        # -------------------------------------------------------------------------------------- #
        # Adicionando estilos
        self.label1.setFont(QFont('Roboto ', 15))
        self.label2.setFont(QFont('Roboto', 15))
        self.botao1.setFont(QFont('Roboto', 12))
        self.botao2.setFont(QFont('Roboto', 12))
        self.botao_executar.setFont(QFont('Roboto', 13))
        self.progresso.setValue(0)
        self.progresso.setAlignment(Qt.AlignCenter)

        # Estilizando os botões
        self.botao1.setStyleSheet("""
            QPushButton { 
                margin: 10px; 
                color: white; 
                background-color: #337ab7; 
                height: 25px; 
                border-radius: 2px;
            }
            QPushButton:hover { 
                background-color: #5b94c5; 
                opacity: 0.9 
            }
        """)
        self.botao2.setStyleSheet("""
            QPushButton { 
                margin-top: 10px; 
                color: white; 
                background-color: #337ab7;
                height: 25px; 
                border-radius: 2px 
            }
            QPushButton:hover { 
                background-color: #5b94c5; 
                opacity: 0.9 
            }
        """)
        self.botao_executar.setStyleSheet("""
            QPushButton { 
                margin: 10px; 
                color: white; 
                background-color: #3c763d; 
                height: 25px; 
                border-radius: 2px 
            }
            QPushButton:hover { 
                background-color: #629163; 
                opacity: 0.9 ;
                border: solid 1px white;
            }
        """)

        self.progresso.setStyleSheet(
            """
            QProgressBar { 
                margin: 10px; 
                height: 25px; 
                border-radius: 3px
                }
            """
        )
        self.nome_arquivo_remessa.setStyleSheet("margin-bottom : 30px; font-style : italic")
        self.nome_arquivo_retorno.setStyleSheet("margin-bottom : 30px; font-style : italic")

        # -------------------------------------------------------------------------------------- #
        # -------------------------------------------------------------------------------------- #
        # Configurando layout vertical
        layout = QVBoxLayout()

        # Adicionando margens
        layout.setContentsMargins(25, 25, 25, 25)

        # Adicionando os elementos no Layout
        layout.addWidget(self.label1)
        layout.addWidget(self.botao1)
        layout.addWidget(self.nome_arquivo_remessa)
        layout.addWidget(self.label2)
        layout.addWidget(self.botao2)
        layout.addWidget(self.nome_arquivo_retorno)
        layout.addWidget(self.progresso)
        layout.addWidget(self.botao_executar)

        # Outras configurações do Layout
        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

        # -------------------------------------------------------------------------------------- #
        # -------------------------------------------------------------------------------------- #
        # Conectando sinais aos slots
        self.botao1.clicked.connect(self.selecionar_arquivo_remessa)
        self.botao2.clicked.connect(self.selecionar_arquivo_retorno)
        self.botao_executar.clicked.connect(self.executar_funcao)

    # -------------------------------------------------------------------------------------- #
    # -------------------------------------------------------------------------------------- #
    # -------------------------------------------------------------------------------------- #
    def selecionar_arquivo_remessa(self):
        """
            Função destinada.
        :return: Arquvi
        """
        arquivo_remessa, _ = QFileDialog.getOpenFileName(
            self,
            caption="Selecione o arquivo de remessa",
            dir="",
            filter="Arquivos de Documento (*.txt)"
        )
        if arquivo_remessa:
            self.nome_arquivo_remessa.setText(arquivo_remessa)

    # -------------------------------------------------------------------------------------- #
    # -------------------------------------------------------------------------------------- #
    # -------------------------------------------------------------------------------------- #
    def selecionar_arquivo_retorno(self):
        """
            Função destinada.
        """
        arquivo_retorno, _ = QFileDialog.getOpenFileName(self, "Selecione o arquivo de retorno bancário", "",
                                                         "Arquivos de Documento (*.txt)")
        if arquivo_retorno:
            self.nome_arquivo_retorno.setText(arquivo_retorno)

    # -------------------------------------------------------------------------------------- #
    # -------------------------------------------------------------------------------------- #
    # -------------------------------------------------------------------------------------- #
    def executar_funcao(self):
        """
            Função destinada.
        """

        # -------------------------------------------------------------------------------------- #
        # -------------------------------------------------------------------------------------- #
        # Função de Processamento de Dados
        def validar_dados_pagamento():
            """
                Função destinada.
            """
            nome_arquivo = "Financeiro Recebimentos - Validação Retorno"
            path = os.path.join(os.path.expanduser("~"), "Desktop", f"{nome_arquivo}.xlsx")
            planilha = Workbook()
            planilha.save(path)

            print("Função executada com os arquivos selecionados!")
            self.progresso.setValue(100)

        # Iniciando a função em uma thread separada
        thread = threading.Thread(target=validar_dados_pagamento)
        thread.start()


# -------------------------------------------------------------------------------------- #
# -------------------------------------------------------------------------------------- #
# -------------------------------------------------------------------------------------- #
# -------------------------------------------------------------------------------------- #
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = RecebimentosBoletos()
    window.show()
    sys.exit(app.exec())
