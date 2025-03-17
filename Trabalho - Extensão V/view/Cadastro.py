import sys
import os
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLabel, QFrame
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt
import CadastroCategorias, CadastroEmpresas, CadastroProdutos, CadastroProdutosGerais  # Importando as interfaces de cadastro

# Importando estilos
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from styles.Estilo_botoes_de_sellecao import obter_estilo  # Importando o estilo
from styles.nav import obter_estilo_nav  # Importando o estilo de navegação

class Cadastro(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Opções de Cadastro")

        layout = QVBoxLayout()
        layout.setAlignment(Qt.AlignCenter)

        # Label principal
        label = QLabel("Opções de Cadastro", self)
        label.setFont(QFont("Arial", 14, QFont.Bold))
        label.setAlignment(Qt.AlignCenter)
        layout.addSpacing(40)
        layout.addWidget(label)
        layout.addSpacing(40)

        # Lista de botões com suas respectivas funções
        botoes = [
            {"texto": "Concorrentes", "funcao": self.abrir_cadastro_empresas},
            {"texto": "Categorias", "funcao": self.abrir_cadastro_categorias},  # Corrigido aqui
            {"texto": "Nome de um Produto", "funcao": self.abrir_cadastro_produtos_geral},
            {"texto": "Vinculação de Produtos", "funcao": self.abrir_cadastro_produtos}
        ]

        # Obtendo o estilo dos botões
        estilo_botoes = obter_estilo()

        # Criando os botões em um loop
        for botao_info in botoes:
            botao = QPushButton(botao_info["texto"], self)
            botao.setFont(QFont("Arial", 12))
            botao.setStyleSheet(estilo_botoes)
            botao.clicked.connect(botao_info["funcao"])
            layout.addWidget(botao, alignment=Qt.AlignCenter)
            layout.addSpacing(20)

        # Adicionando o separador
        separador = QFrame()
        separador.setFrameShape(QFrame.HLine)
        separador.setFrameShadow(QFrame.Sunken)
        separador.setStyleSheet("background-color: grey;")  # Cor do separador
        separador.setFixedHeight(2)  # Altura do separador
        layout.addSpacing(80)  # Espaço de 80 pixels acima do separador
        layout.addWidget(separador)

        # Botão de navegação "Menu Principal"
        botao_menu_principal = QPushButton("Menu Principal", self)
        botao_menu_principal.setFont(QFont("Arial", 12))
        botao_menu_principal.setStyleSheet(obter_estilo_nav())
        botao_menu_principal.clicked.connect(self.voltar_principal)  # Passa a instância atual
        layout.addSpacing(20)  # Espaço entre o separador e o botão
        layout.addWidget(botao_menu_principal, alignment=Qt.AlignCenter)

        self.setLayout(layout)

    def abrir_cadastro_empresas(self):
        # Fecha a janela atual e abre a interface de cadastro de empresas
        self.close()
        self.cadastro_empresas = CadastroEmpresas.CadastroEmpresas()
        self.cadastro_empresas.showMaximized()

    def abrir_cadastro_produtos(self):
        # Fecha a janela atual e abre a interface de cadastro de produtos
        self.close()
        self.cadastro_produtos = CadastroProdutos.CadastroProdutos()
        self.cadastro_produtos.showMaximized()

    def abrir_cadastro_categorias(self):  # Corrigido aqui
        # Fecha a janela atual e abre a interface de cadastro de categorias
        self.close()
        self.cadastro_categorias = CadastroCategorias.CadastroCategorias()
        self.cadastro_categorias.showMaximized()

    def abrir_cadastro_produtos_geral(self):
        # Fecha a janela atual e abre a interface de cadastro de produtos
        self.close()
        self.abrir_cadastro_produtos_geral = CadastroProdutosGerais.CadastroProdutosGerais()
        self.abrir_cadastro_produtos_geral.showMaximized()

    def voltar_principal(self):
        # Fecha a janela atual e volta para a tela principal
        self.close()
        from Principal import Principal  # Importa a classe Principal aqui para evitar importação circular
        self.principal = Principal()
        self.principal.showMaximized()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Cadastro()
    window.showMaximized()
    sys.exit(app.exec_())