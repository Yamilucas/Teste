from model_categorias import Categoria  # Importa a classe Categoria

class ProdutoGeral(Categoria):  # Herda de Categoria
    def __init__(self):
        super().__init__()  # Inicializa a classe base (Categoria)
        self._nome_produto: str = ""  # Nome do produto (String)
        self._imagem_produto: str = ""  # Caminho da imagem do produto (String)

    def set_nome_produto(self, nome_produto: str):
        self._nome_produto = nome_produto

    def get_nome_produto(self) -> str:
        return self._nome_produto

    def set_imagem_produto(self, imagem_produto: str):
        self._imagem_produto = imagem_produto

    def get_imagem_produto(self) -> str:
        return self._imagem_produto