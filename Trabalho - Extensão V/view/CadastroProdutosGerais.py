import sys
import os
from PyQt5.QtWidgets import (QApplication, QWidget, QVBoxLayout, QPushButton,  QLabel, QLineEdit, QComboBox, QFileDialog, QHBoxLayout,  QGridLayout)
from PyQt5.QtGui import QFont, QPixmap
from PyQt5.QtCore import Qt
import Principal 

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from styles.nav import obter_estilo_nav
from styles.Estilo_botoes_de_sellecao import obter_estilo 
from styles.sel_im import (obter_estilo_borda, obter_estilo_botao_circular)

class CadastroProdutosGerais(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Cadastro de Produtos Gerais")


        # Layout principal
        geral_cadastro_layout = QVBoxLayout()
        geral_cadastro_layout.setAlignment(Qt.AlignCenter)
        geral_cadastro_layout.setSpacing(25)

        # Título
        lbl_titulo = QLabel("Cadastro de Produtos Gerais")
        lbl_titulo.setFont(QFont("Arial", 16, QFont.Bold))
        geral_cadastro_layout.addWidget(lbl_titulo, alignment=Qt.AlignCenter)
        geral_cadastro_layout.addSpacing(20)

        # Container da imagem
        img_container = QWidget()
        img_container.setFixedSize(220, 220)  # Espaço extra para margens
        layout_imagem = QGridLayout(img_container)
        layout_imagem.setContentsMargins(0, 0, 0, 0)

        # Área da imagem
        self.img_frame = QLabel()
        self.img_frame.setObjectName("area_imagem")
        self.img_frame.setStyleSheet(obter_estilo_borda())
        self.img_frame.setAlignment(Qt.AlignCenter)
        layout_imagem.addWidget(self.img_frame, 0, 0)

        # Botão centralizado
        self.btn_add_imagem = QPushButton("+")
        self.btn_add_imagem.setObjectName("botao_mais")
        self.btn_add_imagem.setStyleSheet(obter_estilo_botao_circular())
        self.btn_add_imagem.clicked.connect(self.selecionar_imagem)
        
        # Centralização absoluta do botão
        layout_imagem.addWidget(self.btn_add_imagem, 0, 0, alignment=Qt.AlignCenter)

        geral_cadastro_layout.addWidget(img_container, alignment=Qt.AlignCenter)
        geral_cadastro_layout.addSpacing(30)

        container = QVBoxLayout()
        container.setAlignment(Qt.AlignCenter)
        container.setSpacing(20)

       
        
        self.cmb_categoria = QComboBox()
        self.cmb_categoria.addItems(["Categoria 1", "Categoria 2", "Categoria 3"])
        self.cmb_categoria.setFixedWidth(200)
        container.addLayout(self.criar_linha("Categoria do Produto:", self.cmb_categoria))
        
     
        
        
        self.txt_nome = QLineEdit()
        self.txt_nome.setFixedWidth(200)
        container.addLayout(self.criar_linha("Nome do Produto:", self.txt_nome))
        
        geral_cadastro_layout.addLayout(container)
       

        # Botões de ação
        btn_layout = QVBoxLayout()
        btn_layout.setSpacing(15)

        self.btn_salvar = QPushButton("Salvar")
        self.btn_salvar.setFont(QFont("Arial", 12))
        self.btn_salvar.setStyleSheet(obter_estilo())
        btn_layout.addWidget(self.btn_salvar, alignment=Qt.AlignCenter)

        btn_voltar = QPushButton("Menu Principal")
        btn_voltar.setFont(QFont("Arial", 12))
        btn_voltar.setStyleSheet(obter_estilo_nav())
        btn_voltar.clicked.connect(self.voltar_principal)
        btn_layout.addWidget(btn_voltar, alignment=Qt.AlignCenter)

        geral_cadastro_layout.addLayout(btn_layout)
        geral_cadastro_layout.addSpacing(20)

        self.setLayout(geral_cadastro_layout)

    def criar_linha(self, texto_label, widget):
        linha = QHBoxLayout()
        label = QLabel(texto_label, self)
        label.setFixedWidth(180)  # Largura fixa para labels
        label.setFont(QFont("Arial", 12))
        linha.addWidget(label)
        linha.addWidget(widget, alignment=Qt.AlignCenter)
        return linha
        

    def selecionar_imagem(self):
        arquivo, _ = QFileDialog.getOpenFileName(
            self, 
            "Selecionar Imagem", 
            "", 
            "Imagens (*.png *.jpg *.jpeg )"
        )
        if arquivo:
            pixmap = QPixmap(arquivo)
            self.img_frame.setPixmap(
                pixmap.scaled(200, 200, Qt.KeepAspectRatio, Qt.SmoothTransformation)
            )
            self.btn_add_imagem.hide()

    def voltar_principal(self):
        self.close()
        self.principal = Principal.Principal()
        self.principal.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    janela = CadastroProdutosGerais()
    janela.showMaximized()
    sys.exit(app.exec_())