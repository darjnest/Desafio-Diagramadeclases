class EncuestaLimitadaEdad(Encuesta):
    def __init__(self, nombre: str, preguntas: list[Pregunta], edad_minima: int, edad_maxima: int):
        """
        Constructor de la clase EncuestaLimitadaEdad.

        Inicializa una instancia de EncuestaLimitadaEdad, la cual hereda de la clase Encuesta,
        y añade restricciones de edad mínima y máxima para poder participar en la encuesta.

        :param nombre: (str) El nombre de la encuesta.
        :param preguntas: (list[Pregunta]) Una lista de objetos de tipo Pregunta que conforman la encuesta.
        :param edad_minima: (int) La edad mínima requerida para poder participar en la encuesta.
        :param edad_maxima: (int) La edad máxima permitida para participar en la encuesta.
        """
        super().__init__(nombre, preguntas)  # Llama al constructor de la clase base Encuesta.
        self.edad_minima = edad_minima  # Establece la edad mínima para participar.
        self.edad_maxima = edad_maxima  # Establece la edad máxima para participar.

    def modificar_edades(self, min: int, max: int):
        """
        Modifica las edades mínima y máxima para la participación en la encuesta.

        :param min: (int) La nueva edad mínima.
        :param max: (int) La nueva edad máxima.
        """
        self.edad_minima = min  # Actualiza la edad mínima para participar.
        self.edad_maxima = max  # Actualiza la edad máxima para participar.
