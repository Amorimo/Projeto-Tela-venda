import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QHBoxLayout, QVBoxLayout, QLineEdit, QPushButton, QMessageBox, QComboBox, QListWidget

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
        self.label_venda = QLabel("Total de Venda:")

        #Criando a LineEdit que recebe o total de venda
        self.edit_venda = QLineEdit("R$ 100,00")

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
        self.label_desc = QLabel("Desconto:")

        #Criando a LineEdit que recebe o total de desc
        self.edit_desc = QLineEdit("R$ 0,00")

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
        self.label_acre = QLabel("Acrescimo:")

        #Criando a LineEdit que recebe o total de acre
        self.edit_acre = QLineEdit("R$ 0,00")

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
        self.label_liquido = QLabel("Total de líquido:")

        #Criando a LineEdit que recebe o total de liquido
        self.edit_liquido = QLineEdit("R$ 100,00")

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
        self.label_trocos = QLabel("Troco:")

        #Criando a LineEdit que recebe o total de trocos
        self.edit_trocos = QLineEdit("R$ 0,00")

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


        self.label_coluna_esquerda.setStyleSheet("QLabel{"
                                                 "font-size:14px;"
                                                 "background-color:#DCDCDC""}")
    #===========================================Fim do lado esquerdo meio===========================================================

    #=================================================Lado direito meio=============================================================
        # Label da direita
        self.label_coluna_direita = QLabel()
        # Criar layout vertical
        self.layout_v_direita = QVBoxLayout()
    
        #================================================Começo do cliente==========================================================
        # Label para guardar o texto Cliente e uma caixa, ou seja irá guardar uma nova label e uma lineEdit
        self.label_cliente = QLabel()

        # Criando o layout horizontal para a label_cliente e a lineEdit
        self.layout_h_cliente = QHBoxLayout()

        # Criando a label que terá o texto Cliente
        self.label_cliente_txt = QLabel("Cliente:")

        #Criando a LineEdit que recebe o nome do cliente
        self.edit_cliente = QLineEdit("1 - CONSUMIDOR FINAL")

        # Adicionar a label_cliente_txt e a edit_cliente
        self.layout_h_cliente.addWidget(self.label_cliente_txt)
        self.layout_h_cliente.addWidget(self.edit_cliente)

        # Adicionando o layout_h_cliente a label_cliente
        self.label_cliente.setLayout(self.layout_h_cliente)

        # Adicionar a label cliente ao layout direito
        self.layout_v_direita.addWidget(self.label_cliente)

        #==================================================Fim do Cliente===========================================================

        #===============================================Começo do Vendedor==========================================================
        # Label para guardar o texto Vendedor e uma caixa, ou seja irá guardar uma nova label e uma lineEdit
        self.label_vendedor = QLabel()

        # Criando o layout horizontal para a label_vendedor e a lineEdit
        self.layout_h_vendedor = QHBoxLayout()

        # Criando a label que terá o texto vendedor
        self.label_vendedor_txt = QLabel("Vendedor:")

        #Criando a LineEdit que recebe o nome do vendedor
        self.edit_vendedor = QLineEdit("999 - SYNDATA")

        # Adicionar a label_vendedor_txt e a edit_vendedor
        self.layout_h_vendedor.addWidget(self.label_vendedor_txt)
        self.layout_h_vendedor.addWidget(self.edit_vendedor)

        # Adicionando o layout_h_vendedor a label_vendedor
        self.label_vendedor.setLayout(self.layout_h_vendedor)

        # Adicionar a label vendedor ao layout direito
        self.layout_v_direita.addWidget(self.label_vendedor)

        #=================================================Fim do Vendedor===========================================================

        #===================================================Começo Forma de Pagto===================================================
        # Label para guardar o texto Vendedor e uma caixa, ou seja irá guardar uma nova label e uma lineEdit
        self.label_fpgto = QLabel()

        # Criando o layout horizontal para a label_fpgto e a lineEdit
        self.layout_h_fpgto = QHBoxLayout()

        # Criando a label que terá o texto fpgto
        self.label_fpgto_txt = QLabel("Forma de Pgto:")

        #Criando a LineEdit que recebe o nome do fpgto
        self.combo_fpgto = QComboBox()
        self.combo_fpgto.addItems(["1 - DINHEIRO","2 - PIX", "3 - CARTÃO"])

        self.edit_fpgto = QLineEdit("R$ 0.00")

        # Adicionar a label_fpgto_txt e a edit_fpgto
        self.layout_h_fpgto.addWidget(self.label_fpgto_txt)
        self.layout_h_fpgto.addWidget(self.combo_fpgto)
        self.layout_h_fpgto.addWidget(self.edit_fpgto)
        

        # Adicionando o layout_h_fpgto a label_fpgto
        self.label_fpgto.setLayout(self.layout_h_fpgto)

        # Adicionar a label fpgto ao layout direito
        self.layout_v_direita.addWidget(self.label_fpgto)
        #======================================================Fim Forma de Pgto====================================================
        #======================================================Começo Lista=========================================================
         # Label para guardar o texto Vendedor e uma caixa, ou seja irá guardar uma nova label e uma lineEdit
        self.label_lista = QLabel()

        # Criando o layout horizontal para a label_lista e a lineEdit
        self.layout_h_lista = QHBoxLayout()

        

        #Criando a LineEdit que recebe o nome do lista
        self.list_lista = QListWidget()
        self.list_lista.addItems(["1 - DINHEIRO                                                                                                                                                 100,00",
                                  "====================================================================", 
                                  " SOMA                                                                                                                                                            100,00"])


        # Adicionar a label_lista_txt e a edit_lista
        self.layout_h_lista.addWidget(self.list_lista)

        # Adicionando o layout_h_lista a label_lista
        self.label_lista.setLayout(self.layout_h_lista)

        # Adicionar a label lista ao layout direito
        self.layout_v_direita.addWidget(self.label_lista)
        #=========================================================Fim Lista=========================================================


        self.label_coluna_direita.setLayout(self.layout_v_direita)

        self.label_coluna_direita.setStyleSheet("QLabel{background-color:#00FF00}")

        self.label_coluna_direita.setStyleSheet("QLabel{"
                                                 "font-size:14px;"
                                                 "}")
    #=================================================Fim lado direito meio=========================================================

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
