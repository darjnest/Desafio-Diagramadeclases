class Alternativa:
    def __init__(self, contenido: str, ayuda: str = None):
        """
        Constructor de la clase Alternativa.

        :param contenido: (str) El contenido o texto de la alternativa.
        :param ayuda: (str, opcional) Texto de ayuda adicional para la alternativa. Por defecto es None.
        """
        self.contenido = contenido  # Almacena el contenido principal de la alternativa.
        self.ayuda = ayuda  # Almacena el texto de ayuda adicional, si se proporciona.

    def mostrar(self):
        """
        Muestra el contenido de la alternativa, incluyendo el texto de ayuda si está disponible.

        :return: (str) Representación en cadena de la alternativa, con o sin texto de ayuda.
        """
        if self.ayuda:
            # Si hay texto de ayuda, lo incluye en la representación.
            return f"{self.contenido} (Ayuda: {self.ayuda})"
        # Si no hay texto de ayuda, solo muestra el contenido principal.
        return self.contenido

