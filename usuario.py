class Usuario:
    def __init__(self, correo: str, edad: int, region: int):
        """
        Constructor de la clase Usuario.

        Inicializa una instancia de Usuario, que representa a un usuario de la encuesta.

        :param correo: (str) La dirección de correo electrónico del usuario.
        :param edad: (int) La edad del usuario.
        :param region: (int) El identificador de la región en la que se encuentra el usuario.
        """
        self.correo = correo  # Almacena la dirección de correo electrónico del usuario.
        self.edad = edad  # Almacena la edad del usuario.
        self.region = region  # Almacena el identificador de la región del usuario.

    def contestar_encuesta(self, encuesta: Encuesta):
        """
        Método para que el usuario conteste una encuesta.

        Este método será implementado para permitir que el usuario responda a las preguntas de la encuesta.

        :param encuesta: (Encuesta) La encuesta que el usuario va a contestar.
        """
        pass  # Este método será implementado en el futuro.

