from pregunta import Pregunta

class Encuesta:
    def __init__(self, nombre: str, preguntas: list[Pregunta]):
        """
        Constructor de la clase Encuesta.

        :param nombre: (str) El nombre de la encuesta.
        :param preguntas: (list[Pregunta]) Una lista de objetos de tipo Pregunta que forman parte de la encuesta.
        """
        self.nombre = nombre  # Almacena el nombre de la encuesta.
        self.preguntas = preguntas  # Almacena la lista de preguntas asociadas a la encuesta.
        self.listado_respuestas = []  # Inicializa un listado vacío para almacenar las respuestas.

    def mostrar(self):
        """
        Muestra la encuesta, incluyendo el nombre y todas las preguntas.

        :return: (str) Una cadena que representa la encuesta con su nombre y todas las preguntas.
        """
        resultado = f"Encuesta: {self.nombre}"  # Empieza la representación de la encuesta con su nombre.
        for pregunta in self.preguntas:
            # Agrega la representación de cada pregunta a la cadena de resultado.
            resultado += f"\n{pregunta.mostrar()}"
        return resultado  # Devuelve la cadena completa que representa la encuesta.

    def agregar_listado_respuestas(self, listado_respuestas):
        """
        Agrega un conjunto de respuestas al listado de respuestas de la encuesta.

        :param listado_respuestas: El conjunto de respuestas que se desea agregar al listado.
        """
        self.listado_respuestas.append(listado_respuestas)  # Añade las respuestas al listado de respuestas.

