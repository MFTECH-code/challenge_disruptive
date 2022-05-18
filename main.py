import interpreter
import recognizor
import commands



while True:
    entrada = recognizor.voice_recognizor()
    if str(entrada).upper() in ["OI", "OLÁ", "OLA", "BOM DIA", "BOA TARDE", "BOA NOITE"]:
        interpreter.speak("Olá meu nome é Chavez em que posso ajudar")
        continue
    if str(entrada).upper() in ["TOQUE UMA MUSICA", "TOQUE UMA MÚSICA", "COLOCA UMA MÚSICA", "COLOCA UMA MUSICA"]:
        commands.play_music()
        while True:
            controle_musica = recognizor.voice_recognizor()
            if str(controle_musica).upper() in ["PAUSAR MUSICA", "PAUSAR MÚSICA", "PAUSE A MÚSICA"]:
                commands.pause_music()
                interpreter.speak("Música pausada...")
                continue
            if str(controle_musica).upper() in ["TOCAR MUSICA", "VOLTAR A TOCAR MÚSICA", "VOLTAR A TOCAR A MUSICA"]:
                commands.continue_music()
                continue
            if str(controle_musica).upper() in ["PARAR MUSICA", "PARAR MÚSICA"]:
                commands.stop_music()
                break
            else:
                continue
        continue
    else:
        interpreter.speak("Desculpe não entendi o que você falou...")
    break
