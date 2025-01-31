import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QHBoxLayout, QVBoxLayout, QLineEdit, QPushButton, QMessageBox

class Caixa(QWidget):
    def __init__(self):
        super().__init__()

        # Definir posição e tamanho da janela
        self.setGeometry(0, 30, 1200, 900)
        self.setWindowTitle("Finalizar Venda")

        # Criando o título dentro da caixa de cima
        self.titulo = QLabel("Finalizar Venda")
        self.titulo.setStyleSheet("QLabel {"
                                  "font-size: 24px; "
                                  "font-weight: bold; "
                                  "text-align: center; "
                                  "color: black; "
                                  "padding: 5px; "
                                  "}")


        # Criando o layout vertical para a caixa de cima
        v_layout_topo = QVBoxLayout()
        v_layout_topo.addWidget(self.titulo)  # Adiciona o título dentro da caixa de cima

        # Criar as labels que representam as colunas esquerda e direita
    #=============================================Lado esquerdo do meio==================================================
        # Label da esquerda
        self.label_coluna_esquerda = QLabel()
        # Criar layout vertical
        self.layout_v_esquerda = QVBoxLayout()
        # =========================================Começo do Total Venda=================================================
        # Label para guardar o texto total de venda e a caixa total de venda, ou seja irá guardar uma nova label e uma lineEdit
        self.label_total_venda = QLabel()

        # Criando o layout horizontal para a label_total_venda e a lineEdit
        self.layout_h_total_venda = QHBoxLayout()

        # Criando a label que terá o texto Total de vendas
        self.label_venda = QLabel("Total de Venda")

        #Criando a LineEdit que recebe o total de venda
        self.edit_venda = QLineEdit()

        # Adicionar a label_venda e a edit_venda
        self.layout_h_total_venda.addWidget(self.label_venda)
        self.layout_h_total_venda.addWidget(self.edit_venda)

        # Adicionando o layout_h_total_venda a label_total_venda
        self.label_total_venda.setLayout(self.layout_h_total_venda)

        # Adicionar a label total venda ao layout esquerdo
        self.layout_v_esquerda.addWidget(self.label_total_venda)
        # ============================================Fim do Total Venda=================================================
        # =========================================Começo do Desconto====================================================

        # Label para guardar o texto total de venda e a caixa total de venda, ou seja irá guardar uma nova label e uma lineEdit
        self.label_desconto = QLabel()

        # Criando o layout horizontal para a label_desconto e a lineEdit
        self.layout_h_desconto = QHBoxLayout()

        # Criando a label que terá o texto Total de vendas
        self.label_desc = QLabel("Total de desc")

        #Criando a LineEdit que recebe o total de desc
        self.edit_desc = QLineEdit()

        # Adicionar a label_desc e a edit_desc
        self.layout_h_desconto.addWidget(self.label_desc)
        self.layout_h_desconto.addWidget(self.edit_desc)

        # Adicionando o layout_h_desconto a label_desconto
        self.label_desconto.setLayout(self.layout_h_desconto)

        # Adicionar a label total venda ao layout esquerdo
        self.layout_v_esquerda.addWidget(self.label_desconto)

        # ============================================Fim do Desconto====================================================
        # ============================================Começo do Acrécimo=================================================
        
        # Label para guardar o texto total de venda e a caixa total de venda, ou seja irá guardar uma nova label e uma lineEdit
        self.label_acrescimo = QLabel()

        # Criando o layout horizontal para a label_acrescimo e a lineEdit
        self.layout_h_acrescimo = QHBoxLayout()

        # Criando a label que terá o texto Total de vendas
        self.label_acre = QLabel("Total de acre")

        #Criando a LineEdit que recebe o total de acre
        self.edit_acre = QLineEdit()

        # Adicionar a label_acre e a edit_acre
        self.layout_h_acrescimo.addWidget(self.label_acre)
        self.layout_h_acrescimo.addWidget(self.edit_acre)

        # Adicionando o layout_h_acrescimo a label_acrescimo
        self.label_acrescimo.setLayout(self.layout_h_acrescimo)

        # Adicionar a label total venda ao layout esquerdo
        self.layout_v_esquerda.addWidget(self.label_acrescimo)

        # ============================================Fim do Acréscimo===================================================

        # ==========================================Começo do Total liquido==============================================

        # Label para guardar o texto total de venda e a caixa total de venda, ou seja irá guardar uma nova label e uma lineEdit
        self.label_total_liquido = QLabel()

        # Criando o layout horizontal para a label_total_liquido e a lineEdit
        self.layout_h_total_liquido = QHBoxLayout()

        # Criando a label que terá o texto Total de vendas
        self.label_liquido = QLabel("Total de liquido")

        #Criando a LineEdit que recebe o total de liquido
        self.edit_liquido = QLineEdit()

        # Adicionar a label_liquido e a edit_liquido
        self.layout_h_total_liquido.addWidget(self.label_liquido)
        self.layout_h_total_liquido.addWidget(self.edit_liquido)

        # Adicionando o layout_h_total_liquido a label_total_liquido
        self.label_total_liquido.setLayout(self.layout_h_total_liquido)

        # Adicionar a label total venda ao layout esquerdo
        self.layout_v_esquerda.addWidget(self.label_total_liquido)

        # ============================================Fim do Total Líquido===============================================

        # ==========================================Começo do Troco======================================================

        # Label para guardar o texto total de venda e a caixa total de venda, ou seja irá guardar uma nova label e uma lineEdit
        self.label_troco = QLabel()

        # Criando o layout horizontal para a label_troco e a lineEdit
        self.layout_h_troco = QHBoxLayout()

        # Criando a label que terá o texto Total de vendas
        self.label_trocos = QLabel("Total de trocos")

        #Criando a LineEdit que recebe o total de trocos
        self.edit_trocos = QLineEdit()

        # Adicionar a label_trocos e a edit_trocos
        self.layout_h_troco.addWidget(self.label_trocos)
        self.layout_h_troco.addWidget(self.edit_trocos)

        # Adicionando o layout_h_troco a label_troco
        self.label_troco.setLayout(self.layout_h_troco)

        # Adicionar a label total venda ao layout esquerdo
        self.layout_v_esquerda.addWidget(self.label_troco)

        # ============================================Fim do Troco=======================================================



        # Adicionar label no layout da esquerda
        self.label_coluna_esquerda.setLayout(self.layout_v_esquerda)

        self.label_coluna_esquerda.setStyleSheet("QLabel{background-color:#5F9EA0}")
    #===========================================Fim do lado esquerdo meio================================================

        # Label da direita
        self.label_coluna_direita = QLabel()
        self.label_coluna_direita.setStyleSheet("QLabel{background-color:#00FFFF}")

        # Criar o layout horizontal para as colunas
        self.h_layout = QHBoxLayout()
        self.h_layout.addWidget(self.label_coluna_esquerda)
        self.h_layout.addWidget(self.label_coluna_direita)

        # Criando label horizontal embaixo
        self.label_h_baixo = QLabel()
        self.label_h_baixo.setStyleSheet("QLabel{background-color:#FF007F}")

        # Criando layout vertical para label horizontal embaixo
        v_layout_baixo = QVBoxLayout()
        v_layout_baixo.addWidget(self.label_h_baixo)

        # Criando o layout principal para a janela
        main_layout = QVBoxLayout()
        main_layout.addLayout(v_layout_topo)  # Adiciona o título e a caixa de cima no topo
        main_layout.addLayout(self.h_layout)  # Adiciona as duas colunas abaixo
        main_layout.addLayout(v_layout_baixo)  # Adiciona a linha horizontal embaixo

        # Definir o layout principal da janela
        self.setLayout(main_layout)

app = QApplication(sys.argv)
cx = Caixa()
cx.show()
app.exec_()
