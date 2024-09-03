from alternativa import Alternativa
from pregunta import Pregunta
from encuesta import Encuesta
from usuario import Usuario

def main():
    # Crear algunas alternativas de ejemplo
    alternativa1 = Alternativa("C#")
    alternativa2 = Alternativa("Java")
    alternativa3 = Alternativa("Python")

    # Crear una lista de alternativas para una pregunta
    alternativas_pregunta1 = [alternativa1, alternativa2, alternativa3]

    # Crear una instancia de Pregunta con todos los argumentos necesarios
    pregunta1 = Pregunta(
        enunciado="¿Cuál es tu lenguaje de programación favorito?",
        es_requerida=True,
        alternativas=alternativas_pregunta1,
        ayuda="Elige tu lenguaje preferido de la lista."
    )

    # Crear una instancia de Encuesta con una lista de preguntas
    encuesta = Encuesta(
        titulo="Encuesta de Programación",
        preguntas=[pregunta1]
    )

    # Crear un usuario y contestar la encuesta
    usuario = Usuario(correo="test@example.com", edad=30, region=1)
    usuario.contestar_encuesta(encuesta)

    # Mostrar las respuestas del usuario al finalizar
    usuario.mostrar_respuestas()

if __name__ == "__main__":
    main()

