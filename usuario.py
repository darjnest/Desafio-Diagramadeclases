

from encuesta import Encuesta

class Usuario:
    def __init__(self, correo: str, edad: int, region: int):
        """
        Constructor de la clase Usuario.
        
        Inicializa un usuario con su correo, edad y región.
        
        :param correo: (str) Correo electrónico del usuario.
        :param edad: (int) Edad del usuario.
        :param region: (int) Región del usuario.
        """
        self.correo = correo
        self.edad = edad
        self.region = region
        self.respuestas = {}  # Diccionario para almacenar las respuestas del usuario

    def contestar_encuesta(self, encuesta: Encuesta):
        """
        Permite al usuario contestar una encuesta.
        
        :param encuesta: (Encuesta) La encuesta a ser contestada.
        """
        print(f"\nUsuario: {self.correo}")
        print(f"Edad: {self.edad}, Región: {self.region}\n")
        print(f"Comenzando la encuesta: {encuesta.titulo}\n")

        # Iterar sobre las preguntas de la encuesta y obtener las respuestas del usuario
        for pregunta in encuesta.preguntas:
            print(pregunta.mostrar())
            respuesta = input("Tu respuesta: ")
            self.respuestas[pregunta.enunciado] = respuesta  # Guardar la respuesta en el diccionario

    def mostrar_respuestas(self):
        """
        Muestra las respuestas del usuario a la encuesta.
        """
        print(f"\nRespuestas del usuario {self.correo}:")
        for pregunta, respuesta in self.respuestas.items():
            print(f"{pregunta}: {respuesta}")

