import sys
import os
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLabel, QLineEdit, QHBoxLayout, QSpacerItem, QSizePolicy
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt
import Principal 
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from styles.nav import obter_estilo_nav
from styles.Estilo_botoes_de_sellecao import obter_estilo 

class CadastroCategorias(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Cadastro das Categorias dos Produtos")
        self.setGeometry(100, 100, 600, 400)

        # Layout principal renomeado
        cadastro_categorias_layout = QVBoxLayout()
        cadastro_categorias_layout.setAlignment(Qt.AlignCenter)
        cadastro_categorias_layout.setSpacing(20)

        # Label principal (título)
        label = QLabel("Cadastro das Categorias dos Produtos", self)
        label.setFont(QFont("Arial", 14, QFont.Bold))
        label.setAlignment(Qt.AlignCenter)
        cadastro_categorias_layout.addSpacing(40)
        cadastro_categorias_layout.addWidget(label)
        cadastro_categorias_layout.addSpacing(40)

        # Espaçador para empurrar o nome_layout para o centro absoluto
        cadastro_categorias_layout.addStretch()

        container = QVBoxLayout()
        container.setAlignment(Qt.AlignCenter)
        container.setSpacing(20)

        self.campo_nome = QLineEdit(self)
        self.campo_nome.setFixedWidth(200)
        container.addLayout(self.criar_linha("Nome da Categoria:", self.campo_nome))


        cadastro_categorias_layout.addLayout(container)  # Adiciona o nome_layout no centro absoluto

        # Espaçador abaixo para garantir centralização
        cadastro_categorias_layout.addStretch()

        # Botão de salvar
        self.botao_salvar = QPushButton("Salvar", self)
        self.botao_salvar.setFont(QFont("Arial", 12))
        self.botao_salvar.setStyleSheet(obter_estilo())
        cadastro_categorias_layout.addSpacing(20)
        cadastro_categorias_layout.addWidget(self.botao_salvar, alignment=Qt.AlignCenter)
        cadastro_categorias_layout.addSpacing(20)

        # Botão de voltar
        botao_voltar = QPushButton("Menu Principal", self) 
        botao_voltar.setFont(QFont("Arial", 12))
        botao_voltar.setStyleSheet(obter_estilo_nav())
        botao_voltar.clicked.connect(self.voltar_principal)
        cadastro_categorias_layout.addSpacing(20)
        cadastro_categorias_layout.addWidget(botao_voltar, alignment=Qt.AlignCenter)

        self.setLayout(cadastro_categorias_layout)



    def criar_linha(self, texto_label, widget):
        linha = QHBoxLayout()
        label = QLabel(texto_label, self)
        label.setFixedWidth(180)  # Largura fixa para labels
        label.setFont(QFont("Arial", 12))
        linha.addWidget(label)
        linha.addWidget(widget, alignment=Qt.AlignCenter)
        return linha

    def voltar_principal(self):
        # Fecha a janela atual e volta para a tela principal
        self.close()
        self.principal = Principal.Principal()
        self.principal.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = CadastroCategorias()
    window.showMaximized()
    sys.exit(app.exec_())
