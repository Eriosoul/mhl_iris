import nltk
from nltk.chat.util import Chat, reflections
from nltk.text import *

# Definir patrones y respuestas para el chatbot
pares = [
    ["Hola", ["¡Hola!", "¿Cómo estás?"]],
    ["¿Cómo te llamas?", ["Soy un chatbot.", "Mi nombre es Chatbot."]],
    ["¿Qué puedes hacer?", ["Puedo responder preguntas simples.", "Intenta preguntarme algo."]],
    ["Adiós", ["¡Hasta luego!", "Adiós, que tengas un buen día."]],
    ["", ["Lo siento, no entiendo esa pregunta.", "Por favor, intenta preguntarme algo más."]],
]

# Crear el chatbot
chatbot = Chat(pares, reflections)

# Iniciar el chat
print("Hola, soy un chatbot. Puedes empezar a hacer preguntas o simplemente saludar. Para salir, escribe 'salir'.")
while True:
    usuario_input = input("Tú: ")
    if usuario_input.lower() == 'salir':
        print("Chat finalizado.")
        break
    respuesta = chatbot.respond(usuario_input)
    print("Chatbot:", respuesta)