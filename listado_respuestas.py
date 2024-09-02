from usuario import Usuario

class ListadoRespuestas:
    def __init__(self, usuario: Usuario, respuestas: list[int]):
        self.usuario = usuario
        self.respuestas = respuestas
