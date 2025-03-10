from PyQt5.QtWidgets import QMessageBox
from view.Cadastro import Cadastro
from view.CadastroCategorias import CadastroCategorias
from view.CadastroEmpresas import CadastroEmpresas
from view.CadastroProdutos import CadastroProdutos
from view.CadastroProdutosGerais import CadastroProdutosGerais
from view.Principal import Principal

def abrir_cadastro(self):
    self.close()
    self.cadastro = Cadastro()
    self.cadastro.showMaximized()

def abrir_cadastro_produtos(self):
    self.close()
    self.cadastro_produtos = CadastroProdutos()
    self.cadastro_produtos.showMaximized()

def abrir_cadastro_empresas(self):
    self.close()
    self.cadastro_empresas = CadastroEmpresas()
    self.cadastro_empresas.showMaximized()

def abrir_cadastro_categorias(self):
    self.close()
    self.cadastro_categorias = CadastroCategorias()  
    self.cadastro_categorias.showMaximized()

def abrir_cadastro_produtos_gerais(self):
        self.close()
        self.cadastro_produtos_gerais = CadastroProdutosGerais()
        self.cadastro_produtos_gerais.showMaximized()

def aviso_visualizar_produtos(self):
    QMessageBox.information(self, "Aviso", "A funcionalidade de Visualizar Produtos ainda não está disponível.")

def aviso_comparar_produtos(self):
    QMessageBox.information(self, "Aviso", "A funcionalidade de Comparar Produtos ainda não está disponível.")
    
def voltar_principal(self):
    self.close()
    self.principal = Principal()
    self.principal.show()