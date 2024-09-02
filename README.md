# Desafio-Diagramadeclases

# Proyecto de Encuestas

Este proyecto implementa un sistema de encuestas en Python, utilizando clases para representar preguntas, respuestas, usuarios, y diferentes tipos de encuestas. Las clases se derivan de un diagrama de clases y permiten crear objetos relacionados con el manejo de encuestas y sus respectivas respuestas.

## Estructura del Proyecto

El proyecto está compuesto por los siguientes archivos Python:

- `alternativa.py`: Contiene la clase `Alternativa`, que representa una opción de respuesta en una encuesta.
- `pregunta.py`: Contiene la clase `Pregunta`, que representa una pregunta dentro de una encuesta, con sus respectivas alternativas.
- `encuesta.py`: Contiene las clases `Encuesta`, `EncuestaLimitadaEdad`, y `EncuestaLimitadaRegion`, que representan diferentes tipos de encuestas.
- `usuario.py`: Contiene la clase `Usuario`, que representa a los participantes de la encuesta.
- `listado_respuestas.py`: Contiene la clase `ListadoRespuestas`, que almacena las respuestas de un usuario a una encuesta.

## Instalación

1. Clona este repositorio en tu máquina local.
2. Asegúrate de tener Python 3 instalado.
3. No es necesario instalar paquetes adicionales, ya que el proyecto solo utiliza Python estándar.

## Uso

Puedes crear objetos de las clases para manipular encuestas y usuarios. A continuación se muestra un ejemplo básico de cómo utilizar las clases:

```python
from alternativa import Alternativa
from pregunta import Pregunta
from encuesta import Encuesta
from usuario import Usuario
from listado_respuestas import ListadoRespuestas

# Crear alternativas
alt1 = Alternativa(contenido="Sí")
alt2 = Alternativa(contenido="No")

# Crear una pregunta con alternativas
pregunta = Pregunta(enunciado="¿Te gusta el café?", es_requerida=True, alternativas=[alt1, alt2])

# Crear una encuesta con preguntas
encuesta = Encuesta(nombre="Encuesta de Café", preguntas=[pregunta])

# Crear un usuario
usuario = Usuario(correo="usuario@example.com", edad=25, region=1)

# Mostrar la encuesta
print(encuesta.mostrar())

# El usuario contesta la encuesta (lógica de implementación requerida)
usuario.contestar_encuesta(encuesta)


Contribuciones

Este es un proyecto educativo, pero si tienes sugerencias o mejoras, eres bienvenido a enviar un pull request o abrir un issue.

Licencia

Este proyecto está bajo la Licencia MIT - mira el archivo LICENSE para más detalles.