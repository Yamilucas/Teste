from model_empresas import Empresa  # Importa a classe Empresa
from model_categorias import Categoria  # Importa a classe Categoria
from model_nome_produtos import ProdutoGeral  # Importa a classe ProdutoGeral

class ProdutoVinculado(Empresa, Categoria, ProdutoGeral):  # Herda de Empresa, Categoria e ProdutoGeral
    def __init__(self):
        super().__init__()  # Inicializa as classes base
        self._preco_produto: float = 0.0  # Preço do produto (Float)
        self._promocao_produto: bool = False  # Status de promoção (Boolean)

    def set_preco(self, preco_produto: float):
        self._preco_produto = preco_produto

    def get_preco(self) -> float:
        return self._preco_produto

    def set_promocao(self, promocao_produto: bool):
        self._promocao_produto = promocao_produto

    def get_promocao(self) -> bool:
        return self._promocao_produto