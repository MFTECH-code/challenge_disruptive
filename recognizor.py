import speech_recognition as sr
from pygame import mixer

mixer.init()
mixer.music.load("./songs/song.mp3")
mixer.music.set_volume(0.7)


def voice_recognizor():
    recon = sr.Recognizer()
    with sr.Microphone(0) as source:
        recon.adjust_for_ambient_noise(source)
        print("Fale algo...")
        mixer.music.play()
        audio = recon.listen(source)
        print("Reconhecendo...")
        return recon.recognize_google(audio, language='pt')
