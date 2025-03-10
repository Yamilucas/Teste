def obter_estilo_nav():
    estilo = """
        QPushButton {
            background-color: grey;
            color: white;
            border-radius: 10px;
            width: 200px;
            height: 30px;
        }
        QPushButton:hover {
            background-color: #5d5d5d;
        }
        QPushButton:pressed {
            background-color: #404040;
        }
    """
    return estilo