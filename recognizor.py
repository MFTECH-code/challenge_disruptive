import speech_recognition as sr


def voice_recognizor():
    recon = sr.Recognizer()
    with sr.Microphone(0) as source:
        recon.adjust_for_ambient_noise(source, duration=3)
        print("Fale algo...")
        audio = recon.listen(source)
        print("Reconhecendo...")
        return recon.recognize_google(audio, language='pt')
