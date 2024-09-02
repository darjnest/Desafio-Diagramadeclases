from alternativa import Alternativa

class Pregunta:
    def __init__(self, enunciado: str, es_requerida: bool, alternativas: list[Alternativa], ayuda: str = None):
        """
        Constructor de la clase Pregunta.

        Inicializa una instancia de Pregunta, que representa una pregunta de la encuesta con sus posibles
        alternativas de respuesta.

        :param enunciado: (str) El texto que describe la pregunta.
        :param es_requerida: (bool) Indica si la pregunta es obligatoria para el usuario.
        :param alternativas: (list[Alternativa]) Una lista de objetos Alternativa que representan las posibles
                              respuestas a la pregunta.
        :param ayuda: (str, opcional) Un texto de ayuda adicional que puede proporcionar información o contexto
                      sobre la pregunta.
        """
        self.enunciado = enunciado  # Almacena el enunciado de la pregunta.
        self.ayuda = ayuda  # Almacena el texto de ayuda opcional para la pregunta.
        self.es_requerida = es_requerida  # Indica si la pregunta es obligatoria.
        self.alternativas = alternativas  # Almacena la lista de alternativas de respuesta.

    def mostrar(self):
        """
        Genera una representación textual de la pregunta y sus alternativas.

        :return: (str) Una cadena de texto que representa la pregunta, incluyendo el enunciado,
                        la ayuda (si existe) y las alternativas de respuesta.
        """
        resultado = self.enunciado  # Inicia el resultado con el enunciado de la pregunta.
        if self.ayuda:  # Si hay un texto de ayuda, se agrega al resultado.
            resultado += f" (Ayuda: {self.ayuda})"
        # Agrega cada alternativa de respuesta al resultado, llamando al método mostrar() de cada Alternativa.
        for alternativa in self.alternativas:
            resultado += f"\n  - {alternativa.mostrar()}"
        return resultado  # Retorna la cadena de texto completa que representa la pregunta.

