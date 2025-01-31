import sys
from PyQt5.QtWidgets import (
    QApplication, QWidget, QLabel, QLineEdit, QComboBox, QPushButton, QGridLayout, QTextEdit, QVBoxLayout, QHBoxLayout
)


class FinalizarVenda(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Finalizar Venda")
        self.setGeometry(100, 100, 600, 400)

        # Layout principal
        principal_layout = QHBoxLayout()

        # Coluna Esquerda - Valores Financeiros
        esquerda_layout = QVBoxLayout()

        esquerda_layout.addWidget(QLabel("Total da Venda:"))
        self.total_venda = QLineEdit("R$ 100,00")
        self.total_venda.setFixedSize(250,30)
        esquerda_layout.addWidget(self.total_venda)

        esquerda_layout.addWidget(QLabel("Desconto:"))
        self.desconto = QLineEdit("R$ 0,00")
        esquerda_layout.addWidget(self.desconto)

        esquerda_layout.addWidget(QLabel("Acréscimo:"))
        self.acrescimo = QLineEdit("R$ 0,00")
        esquerda_layout.addWidget(self.acrescimo)

        esquerda_layout.addWidget(QLabel("Total Líquido:"))
        self.total_liquido = QLineEdit("R$ 100,00")
        esquerda_layout.addWidget(self.total_liquido)

        esquerda_layout.addWidget(QLabel("Troco:"))
        self.troco = QLineEdit("R$ 0,00")
        esquerda_layout.addWidget(self.troco)

        # Coluna Direita - Cliente, Vendedor, Pagamento e Detalhes
        direita_layout = QVBoxLayout()

        direita_layout.addWidget(QLabel("Cliente:"))
        self.cliente = QLineEdit("1 - CONSUMIDOR FINAL")
        direita_layout.addWidget(self.cliente)

        direita_layout.addWidget(QLabel("Vendedor:"))
        self.vendedor = QLineEdit("999 - Samuel")
        direita_layout.addWidget(self.vendedor)

        direita_layout.addWidget(QLabel("Forma de Pagamento:"))
        self.forma_pagamento = QComboBox()
        self.forma_pagamento.addItems(["1-DINHEIRO"])
        direita_layout.addWidget(self.forma_pagamento)

        direita_layout.addWidget(QLabel("Detalhes:"))
        self.detalhes = QTextEdit("1 - DINHEIRO\n100,00\nSOMA\n100,00")
        direita_layout.addWidget(self.detalhes)

        # Adiciona as duas colunas ao layout principal
        principal_layout.addLayout(esquerda_layout)
        principal_layout.addLayout(direita_layout)

        # Layout para botões
        button_layout = QHBoxLayout()
        self.btn_sair = QPushButton("(Esc) Sair")
        self.btn_cupom = QPushButton("(F6) Cupom Fiscal")
        self.btn_pedido = QPushButton("(F7) Pedido de Venda")
        self.btn_nfce_online = QPushButton("(F8) NFC-e Online")
        self.btn_nfce_offline = QPushButton("(F9) NFC-e Offline")

        button_layout.addWidget(self.btn_sair)
        button_layout.addWidget(self.btn_cupom)
        button_layout.addWidget(self.btn_pedido)
        button_layout.addWidget(self.btn_nfce_online)
        button_layout.addWidget(self.btn_nfce_offline)

        # Layout final
        final_layout = QVBoxLayout()
        final_layout.addLayout(principal_layout)
        final_layout.addLayout(button_layout)

        self.setLayout(final_layout)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = FinalizarVenda()
    window.show()
    sys.exit(app.exec_())