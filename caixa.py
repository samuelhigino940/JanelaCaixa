import sys
#importar os componentes para a
#contrução da janela
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QTableView, QHBoxLayout, QVBoxLayout
#Construção da classe janela com o nome de caixa
class caixa(QWidget):
    #Criação do método __init__ que inicia a janela
    #e exibe ela em tela
    def __init__(self):
        super().__init__()
        #Vamos definir a posição e o tamanho da tela
        self.setGeometry(0,30,1200,900)

        #Vamos definir o titulo da nossa janela
        self.setWindowTitle("Caixa da Loja")

        #Vamos criar as labels que representam as colunas esqueda e direita

        #Label da esquerda
        self.label_coluna_esquerda = QLabel()
        self.label_coluna_esquerda.setStyleSheet("QLabel{background-color:#5F9EA0}")


        #Label da direita
        self.label_coluna_direita = QLabel()
        self.label_coluna_direita.setStyleSheet("QLabel{background-color:#00FFFF}")

        #Criar o layout horizontal para as colunas
        self.h_layout = QHBoxLayout()

        #Vamos adicionar as colunas esquerda e direita ao layout horizontal
        self.h_layout.addWidget(self.label_coluna_esquerda)
        self.h_layout.addWidget(self.label_coluna_direita)

        #Adicionar o layout na tela
        self.setLayout(self.h_layout)



app=QApplication(sys.argv)
cx=caixa()
cx.show()
app.exec_()

