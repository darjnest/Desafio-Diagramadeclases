class Alternativa:
    def __init__(self, contenido: str, ayuda: str = None):
        self.contenido = contenido
        self.ayuda = ayuda

    def mostrar(self):
        if self.ayuda:
            return f"{self.contenido} (Ayuda: {self.ayuda})"
        return self.contenido
