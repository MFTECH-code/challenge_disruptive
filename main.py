import interpreter
import recognizor
import commands
import utils


while True:
    entrada = recognizor.voice_recognizor()
    if str(entrada).upper() in utils.greetings:
        interpreter.speak("Olá sou um robô escravo, não tenho nome... Pode me dar ordens a hora que quiser.")
        break
    if str(entrada).upper() in utils.ask_joke:
        interpreter.speak(commands.say_a_joke())
        break
    if str(entrada).upper() in utils.ask_date:
        interpreter.speak(commands.get_only_date())
        break
    if str(entrada).upper() in utils.ask_time:
        interpreter.speak(commands.get_only_time())
        break
    if str(entrada).upper() in utils.ask_date_time:
        interpreter.speak(commands.get_time_now())
        break
    if str(entrada).upper() in utils.ask_music:
        interpreter.speak("Qual música você deseja?")
        music = recognizor.voice_recognizor()
        commands.play_song(str(music).replace(" ", "+"))
        interpreter.speak("Aqui está o resultado da minha busca.")
        break
    if str(entrada).upper() in utils.google_search:
        pesquisar = True
        while pesquisar:
            interpreter.speak("Qual pesquisa você deseja fazer?")
            search = recognizor.voice_recognizor()
            commands.search_in_google(str(search).replace(" ", "+"))
            interpreter.speak("Aqui está a pesquisa que você pediu, deseja fazer mais uma pesquisa?")
            repetir = recognizor.voice_recognizor()
            if not str(repetir).upper() in utils.repeat_search:
                pesquisar = False
                interpreter.speak("Sua pesquisa acaba aqui!")
        break
    if str(entrada).upper() in utils.ask_weather:
        temperature = commands.get_temperature()
        interpreter.speak(temperature)
        break
    if str(entrada).upper() in utils.ask_about_creators:
        interpreter.speak(commands.credits())
    else:
        interpreter.speak("Desculpe não entendi o que você falou...")
    break
