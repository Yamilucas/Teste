import sys
import os
from PyQt5.QtWidgets import (QApplication, QWidget, QVBoxLayout, QPushButton, 
                            QLabel, QLineEdit, QFileDialog, QHBoxLayout,
                            QSpacerItem, QSizePolicy, QGridLayout)
from PyQt5.QtGui import QFont, QPixmap
from PyQt5.QtCore import Qt
import Principal

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from styles.Estilo_botoes_de_sellecao import obter_estilo
from styles.nav import obter_estilo_nav
from styles.sel_im import obter_estilo_borda, obter_estilo_botao_circular

class CadastroEmpresas(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Cadastro das Empresas Concorrentes")

        # Layout principal
        empresa_layout = QVBoxLayout()
        empresa_layout.setAlignment(Qt.AlignCenter)
        empresa_layout.setSpacing(25)

        # Título
        lbl_titulo = QLabel("Cadastro das Empresas Concorrentes")
        lbl_titulo.setFont(QFont("Arial", 14, QFont.Bold))
        empresa_layout.addWidget(lbl_titulo, alignment=Qt.AlignCenter)
        empresa_layout.addSpacing(40)

        # Container da logo
        logo_container = QWidget()
        logo_container.setFixedSize(220, 220)
        layout_logo = QGridLayout(logo_container)
        layout_logo.setContentsMargins(0, 0, 0, 0)

        # Área da logo
        self.lbl_area_logo = QLabel()
        self.lbl_area_logo.setObjectName("area_imagem")
        self.lbl_area_logo.setStyleSheet(obter_estilo_borda())
        self.lbl_area_logo.setAlignment(Qt.AlignCenter)
        layout_logo.addWidget(self.lbl_area_logo, 0, 0)

        # Botão de adicionar logo
        self.btn_add_logo = QPushButton("+")
        self.btn_add_logo.setObjectName("botao_mais")
        self.btn_add_logo.setStyleSheet(obter_estilo_botao_circular())
        self.btn_add_logo.clicked.connect(self.selecionar_logo)
        layout_logo.addWidget(self.btn_add_logo, 0, 0, alignment=Qt.AlignCenter)

        empresa_layout.addWidget(logo_container, alignment=Qt.AlignCenter)
        empresa_layout.addSpacing(40)

        # Container para os campos (centralizado)
        container = QVBoxLayout()
        container.setAlignment(Qt.AlignCenter)
        container.setSpacing(20)

        self.campo_nome = QLineEdit(self)
        self.campo_nome.setFixedWidth(200)
        container.addLayout(self.criar_linha("Nome da Empresa:", self.campo_nome))

        empresa_layout.addLayout(container)
        empresa_layout.addSpacing(40)

        # Botão Salvar
        btn_salvar = QPushButton("Salvar", self)
        btn_salvar.setFont(QFont("Arial", 12))
        btn_salvar.setStyleSheet(obter_estilo())
        empresa_layout.addWidget(btn_salvar, alignment=Qt.AlignCenter)
        empresa_layout.addSpacing(20)

        # Botão Voltar
        btn_voltar = QPushButton("Menu Principal", self)
        btn_voltar.setFont(QFont("Arial", 12))
        btn_voltar.setStyleSheet(obter_estilo_nav())
        btn_voltar.clicked.connect(self.voltar_principal)
        empresa_layout.addWidget(btn_voltar, alignment=Qt.AlignCenter)

        # Espaçador final
        empresa_layout.addItem(QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding))

        self.setLayout(empresa_layout)

    def criar_linha(self, texto_label, widget):
        linha = QHBoxLayout()
        label = QLabel(texto_label, self)
        label.setFixedWidth(180)  # Largura fixa para labels
        label.setFont(QFont("Arial", 12))
        linha.addWidget(label)
        linha.addWidget(widget, alignment=Qt.AlignCenter)
        return linha

    def selecionar_logo(self):
        arquivo, _ = QFileDialog.getOpenFileName(
            self,
            "Selecionar Logo",
            "",
            "Imagens (*.png *.jpg *.jpeg)"
        )
        if arquivo:
            pixmap = QPixmap(arquivo)
            self.lbl_area_logo.setPixmap(
                pixmap.scaled(200, 200, Qt.KeepAspectRatio, Qt.SmoothTransformation)
            )
            self.btn_add_logo.hide()

    def voltar_principal(self):
        self.close()
        self.principal = Principal.Principal()
        self.principal.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = CadastroEmpresas()
    window.showMaximized()
    sys.exit(app.exec_())
