# sel_im.py - Estilos específicos para imagem
def obter_estilo_borda():
    return """
        QLabel#area_imagem {
            border: 2px dashed #808080;
            background-color: #FFFFFF;
            border-radius: 10px;
            min-width: 200px;
            max-width: 200px;
            min-height: 200px;
            max-height: 200px;
        }
    """

def obter_estilo_botao_circular():
    return """
        QPushButton#botao_mais {
            background-color: #000000;
            color: #FFFFFF;
            border: none;
            border-radius: 25px;
            min-width: 50px;
            max-width: 50px;
            min-height: 50px;
            max-height: 50px;
            font-size: 24px;
            font-weight: bold;
        }
        QPushButton#botao_mais:hover {
            background-color: #333333;
        }
        QPushButton#botao_mais:pressed {
            background-color: #666666;
        }
    """