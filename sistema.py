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

# El usuario contesta la encuesta
usuario.contestar_encuesta(encuesta)

# Verificar que las respuestas se guardaron
for respuesta in encuesta.listado_respuestas:
    print(f"Usuario: {respuesta.usuario.correo}, Respuestas: {respuesta.respuestas}")
