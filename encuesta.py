from pregunta import Pregunta

class Encuesta:
    def __init__(self, titulo: str, preguntas: list[Pregunta]):
        """
        Constructor de la clase Encuesta.

        Inicializa una instancia de Encuesta, que contiene un conjunto de preguntas.

        :param titulo: (str) El título de la encuesta.
        :param preguntas: (list[Pregunta]) Una lista de objetos Pregunta que componen la encuesta.
        """
        self.titulo = titulo
        self.preguntas = preguntas

    def mostrar(self):
        """
        Muestra todas las preguntas de la encuesta.

        :return: (str) Una cadena que representa la encuesta completa con todas sus preguntas.
        """
        resultado = f"Encuesta: {self.titulo}\n"
        for pregunta in self.preguntas:
            resultado += pregunta.mostrar() + "\n"
        return resultado