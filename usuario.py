from encuesta import Encuesta


class Usuario:
    def __init__(self, correo: str, edad: int, region: int):
        self.correo = correo
        self.edad = edad
        self.region = region

    def contestar_encuesta(self, encuesta: Encuesta):
        """
        Método para que el usuario conteste una encuesta.

        Permite al usuario seleccionar respuestas a las preguntas de la encuesta
        y almacena las respuestas en el listado de respuestas de la encuesta.

        :param encuesta: (Encuesta) La encuesta que el usuario va a contestar.
        """
        respuestas = []
        for pregunta in encuesta.preguntas:
            print(pregunta.mostrar())  # Muestra la pregunta y sus alternativas
            respuesta = None
            while respuesta not in range(1, len(pregunta.alternativas) + 1):
                try:
                    respuesta = int(input("Selecciona una opción (número): "))
                except ValueError:
                    print("Por favor, ingrese un número válido.")
            respuestas.append(respuesta - 1)  # Guardamos la opción seleccionada, ajustando a índice 0
