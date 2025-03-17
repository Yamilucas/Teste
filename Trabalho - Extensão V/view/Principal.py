import sys
import os
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLabel, QMessageBox
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt
import Cadastro, CadastroCategorias, CadastroEmpresas, CadastroProdutos  

# Adiciona o diretório raiz ao sys.path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from styles.Estilo_botoes_de_sellecao import obter_estilo  # Importando o estilo

class Principal(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Comparador de Preços - Supermercado Marinho")
        self.showMaximized()  # Abre a janela em tela cheia

        layout = QVBoxLayout()
        layout.setAlignment(Qt.AlignCenter)
        
        # Label principal
        label = QLabel("Comparador de Preços Supermercado Marinho", self)
        label.setFont(QFont("Arial", 14, QFont.Bold))
        label.setAlignment(Qt.AlignCenter)
        layout.addSpacing(40)
        layout.addWidget(label)
        layout.addSpacing(40)

        # Lista de botões com suas respectivas funções
        botoes = [
            {"texto": "Cadastro", "funcao": self.abrir_cadastro},
            {"texto": "Visualizar Produtos", "funcao": self.aviso_visualizar_produtos},
            {"texto": "Comparar Produtos", "funcao": self.aviso_comparar_produtos}
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

        self.setLayout(layout)

    def abrir_cadastro(self):
        # Fecha a janela atual e abre a interface de cadastro
        self.close()
        self.cadastro = Cadastro.Cadastro()  # Passa a instância atual de Principal
        self.cadastro.showMaximized()  # Abre a janela em tela cheia

    def abrir_cadastro_produtos(self):
        self.close()
        self.cadastro_produtos = CadastroProdutos.CadastroProdutos()
        self.cadastro_produtos.showMaximized()

    def abrir_cadastro_empresas(self):
        self.close()
        self.cadastro_empresas = CadastroEmpresas.CadastroEmpresas()
        self.cadastro_empresas.showMaximized()

    def abrir_cadastro_categorias(self):
        self.close()
        self.cadastro_categorias = CadastroCategorias.CadastroCategorias()
        self.cadastro_categorias.showMaximized()

    def aviso_visualizar_produtos(self):
        # Exibe um aviso de que a funcionalidade não está disponível
        QMessageBox.information(self, "Aviso", "A funcionalidade de Visualizar Produtos ainda não está disponível.")

    def aviso_comparar_produtos(self):
        # Exibe um aviso de que a funcionalidade não está disponível
        QMessageBox.information(self, "Aviso", "A funcionalidade de Comparar Produtos ainda não está disponível.")
        
    def voltar_principal(self):
        # Fecha a janela atual e volta para a tela principal
        self.close()
        self.principal = Principal()
        self.principal.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Principal()
    window.show()
    sys.exit(app.exec_())