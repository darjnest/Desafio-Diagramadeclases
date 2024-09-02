class EncuestaLimitadaRegion(Encuesta):
    def __init__(self, nombre: str, preguntas: list[Pregunta], regiones: list[int]):
        super().__init__(nombre, preguntas)
        self.regiones = regiones

    def modificar_regiones(self, regiones: list[int]):
        self.regiones = regiones