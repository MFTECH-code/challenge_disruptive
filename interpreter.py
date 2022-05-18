# Comandos
# Comando pra pesquisar uma música no youtube
# Comando pra agendar alguma tarefa na agenda
# Comando pra falar a temperatura atual
# Comando pra falar a hora atual
# Comando pra contar uma piada aleatória

import pyttsx3

en = pyttsx3.init()
en.setProperty('rate', 155)
en.setProperty('volume', 0.5)
voices = en.getProperty('voices')
en.setProperty('voice', voices[2].id)


def speak(msg):
    en.say(msg)
    en.runAndWait()

