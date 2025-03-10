import sys
import os
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLabel, QLineEdit, QComboBox, QHBoxLayout, QRadioButton
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt
import Principal
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from styles.nav import obter_estilo_nav
from styles.Estilo_botoes_de_sellecao import obter_estilo 

class CadastroProdutos(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Cadastro de Vinculação de Produtos")

        # Layout principal (renomeado)
        vincular_produtos_layout = QVBoxLayout()
        vincular_produtos_layout.setAlignment(Qt.AlignCenter)

        # Título com espaçamento de 40 pixels abaixo
        titulo = QLabel("Cadastro de Vinculação de Produtos", self)
        titulo.setFont(QFont("Arial", 14, QFont.Bold))
        vincular_produtos_layout.addSpacing(20)  # Espaço acima do título
        vincular_produtos_layout.addWidget(titulo, alignment=Qt.AlignCenter)
        vincular_produtos_layout.addSpacing(40)  # 40 pixels abaixo do título

        # Container para os campos (centralizado)
        container = QVBoxLayout()
        container.setAlignment(Qt.AlignCenter)
        container.setSpacing(20)

        # Função para criar linhas alinhadas
        def criar_linha(texto_label, widget):
            linha = QHBoxLayout()
            label = QLabel(texto_label, self)
            label.setFixedWidth(180)  
            label.setFont(QFont("Arial", 12))
            linha.addWidget(label)
            linha.addWidget(widget, alignment=Qt.AlignCenter)
            return linha

        # Nome da Empresa vendendo
        self.combo_empresa = QComboBox(self)
        self.combo_empresa.addItems(["Supermercado Marinho", "Concorrente"])
        self.combo_empresa.setFixedWidth(200)
        container.addLayout(criar_linha("Nome da Empresa:", self.combo_empresa))

        # Nome do Produto
        self.combo_nome = QComboBox(self)
        self.combo_nome.addItems(["Produto 1", "Produto 2", "Produto 3"])
        self.combo_nome.setFixedWidth(200)
        container.addLayout(criar_linha("Nome do Produto:", self.combo_nome))

        # Categoria do Produto
        self.combo_categoria = QComboBox(self)
        self.combo_categoria.addItems(["Categoria 1", "Categoria 2", "Categoria 3"])
        self.combo_categoria.setFixedWidth(200)
        container.addLayout(criar_linha("Categoria do Produto:", self.combo_categoria))

        # Preço
        self.campo_preco = QLineEdit(self)
        self.campo_preco.setFixedWidth(200)
        container.addLayout(criar_linha("Preço:", self.campo_preco))

        # Promoção
        promo_layout = QHBoxLayout()
        promo_label = QLabel("Está em promoção?", self)
        promo_label.setFixedWidth(180)
        promo_label.setFont(QFont("Arial", 12))
        self.radio_sim = QRadioButton("Sim", self)
        self.radio_nao = QRadioButton("Não", self)
        self.radio_nao.setChecked(True)
        promo_layout.addWidget(promo_label)
        promo_layout.addWidget(self.radio_sim)
        promo_layout.addWidget(self.radio_nao)
        container.addLayout(promo_layout)

        # Adicionar container ao layout principal
        vincular_produtos_layout.addLayout(container)
        vincular_produtos_layout.addSpacing(40)  # 40 pixels abaixo do container

        # Botão Salvar
        botao_salvar = QPushButton("Salvar", self)
        botao_salvar.setFont(QFont("Arial", 12))
        botao_salvar.setStyleSheet(obter_estilo())  
        vincular_produtos_layout.addWidget(botao_salvar, alignment=Qt.AlignCenter)

        # Espaçamento para o botão Voltar (40 pixels acima)
        vincular_produtos_layout.addSpacing(40)  # Empurra o botão "Voltar" 40px para cima

        # Botão Voltar
        botao_voltar = QPushButton("Menu Principal", self)
        botao_voltar.setFont(QFont("Arial", 12))
        botao_voltar.setStyleSheet(obter_estilo_nav())
        botao_voltar.clicked.connect(self.voltar_principal)
        vincular_produtos_layout.addWidget(botao_voltar, alignment=Qt.AlignCenter)

        self.setLayout(vincular_produtos_layout)

    def voltar_principal(self):
        self.close()
        self.principal = Principal.Principal()
        self.principal.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = CadastroProdutos()
    window.showMaximized()
    sys.exit(app.exec_())