from alternativa import Alternativa
from pregunta import Pregunta
from encuesta import Encuesta
from usuario import Usuario

def main():
    # Crear algunas alternativas de ejemplo
    alternativa1 = Alternativa("Java")
    alternativa2 = Alternativa("C#")
    alternativa3 = Alternativa("Python")

    # Crear una lista de alternativas para una pregunta
    alternativas_pregunta1 = [alternativa1, alternativa2, alternativa3]

    # Crear una instancia de Pregunta con todos los argumentos necesarios
    pregunta1 = Pregunta(
        enunciado="¿Cuál es tu lenguaje de programación favorito?",
        es_requerida=True,  # Agregar el argumento 'es_requerida'
        alternativas=alternativas_pregunta1,
        ayuda="Elige tu lenguaje preferido de la lista."
    )

    # Crear una instancia de Encuesta con una lista de preguntas
    encuesta = Encuesta(
        titulo="Encuesta de Programación",  # Asegúrate de que 'titulo' es un argumento válido
        preguntas=[pregunta1]
    )

    # Crear un usuario y contestar la encuesta
    usuario = Usuario(correo="test@example.com", edad=30, region=1)
    usuario.contestar_encuesta(encuesta)

if __name__ == "__main__":
    main()

