class EncuestaLimitadaEdad(Encuesta):
    def __init__(self, nombre: str, preguntas: list[Pregunta], edad_minima: int, edad_maxima: int):
        super().__init__(nombre, preguntas)
        self.edad_minima = edad_minima
        self.edad_maxima = edad_maxima

    def modificar_edades(self, min: int, max: int):
        self.edad_minima = min
        self.edad_maxima = max