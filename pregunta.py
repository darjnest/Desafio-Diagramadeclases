from alternativa import Alternativa

class Pregunta:
    def __init__(self, enunciado: str, es_requerida: bool, alternativas: list[Alternativa], ayuda: str = None):
        self.enunciado = enunciado
        self.ayuda = ayuda
        self.es_requerida = es_requerida
        self.alternativas = alternativas

    def mostrar(self):
        resultado = self.enunciado
        if self.ayuda:
            resultado += f" (Ayuda: {self.ayuda})"
        for alternativa in self.alternativas:
            resultado += f"\n  - {alternativa.mostrar()}"
        return resultado
