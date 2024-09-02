class EncuestaLimitadaRegion(Encuesta):
    def __init__(self, nombre: str, preguntas: list[Pregunta], regiones: list[int]):
        """
        Constructor de la clase EncuestaLimitadaRegion.

        Inicializa una instancia de EncuestaLimitadaRegion, que hereda de la clase Encuesta,
        y añade una restricción de regiones para poder participar en la encuesta.

        :param nombre: (str) El nombre de la encuesta.
        :param preguntas: (list[Pregunta]) Una lista de objetos de tipo Pregunta que conforman la encuesta.
        :param regiones: (list[int]) Una lista de identificadores de regiones donde es válida la encuesta.
        """
        super().__init__(nombre, preguntas)  # Llama al constructor de la clase base Encuesta.
        self.regiones = regiones  # Establece las regiones permitidas para participar en la encuesta.

    def modificar_regiones(self, regiones: list[int]):
        """
        Modifica las regiones en las que se permite participar en la encuesta.

        :param regiones: (list[int]) La nueva lista de identificadores de regiones permitidas.
        """
        self.regiones = regiones  # Actualiza las regiones permitidas para participar en la encuesta.
