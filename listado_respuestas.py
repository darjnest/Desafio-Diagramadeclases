from usuario import Usuario

class ListadoRespuestas:
    def __init__(self, usuario: Usuario, respuestas: list[int]):
        """
        Constructor de la clase ListadoRespuestas.

        Inicializa una instancia de ListadoRespuestas, que almacena las respuestas de un usuario
        a una encuesta en particular.

        :param usuario: (Usuario) El objeto Usuario que representa al usuario que responde la encuesta.
        :param respuestas: (list[int]) Una lista de identificadores de las respuestas seleccionadas por el usuario.
        """
        self.usuario = usuario  # Almacena el objeto Usuario asociado con este listado de respuestas.
        self.respuestas = respuestas  # Almacena la lista de respuestas seleccionadas por el usuario.

