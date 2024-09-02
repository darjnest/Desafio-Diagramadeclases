from pregunta import Pregunta

class Encuesta:
    def __init__(self, nombre: str, preguntas: list[Pregunta]):
        self.nombre = nombre
        self.preguntas = preguntas
        self.listado_respuestas = []

    def mostrar(self):
        resultado = f"Encuesta: {self.nombre}"
        for pregunta in self.preguntas:
            resultado += f"\n{pregunta.mostrar()}"
        return resultado

    def agregar_listado_respuestas(self, listado_respuestas):
        self.listado_respuestas.append(listado_respuestas)
