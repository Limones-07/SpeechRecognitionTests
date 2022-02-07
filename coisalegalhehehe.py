import platform
import speech_recognition as sr
from gtts import gTTS
from playsound import playsound
import os
import shutil
import pyaudio


def ouvir_microfone():

    mic = sr.Recognizer()

    with sr.Microphone() as source:
        mic.adjust_for_ambient_noise(source)
        if platform.system() == "Linux":
            os.system("clear")
        print("Diga algo: ")
        audio = mic.listen(source)
    try:
        frase = mic.recognize_google(audio,language="pt-br")

        print("Você disse: " + frase)

    except sr.UnknownValueError:
        print("Não entendi")
        exit()

    return frase

def cria_audio(audio):
    tts = gTTS(audio,lang='pt-br')
    try:
        os.mkdir("73821065873801256784106578134056780413654308167805137485067834165430781657804316578064387165843716578430615870341")
    except FileExistsError:
        pass

    print("Estou aprendendo o que você disse... ")
    tts.save("73821065873801256784106578134056780413654308167805137485067834165430781657804316578064387165843716578430615870341/latest.mp3")
    print("Ouça o que você ouviu.")

    playsound("73821065873801256784106578134056780413654308167805137485067834165430781657804316578064387165843716578430615870341/latest.mp3")
    shutil.rmtree('73821065873801256784106578134056780413654308167805137485067834165430781657804316578064387165843716578430615870341')

frase = ouvir_microfone()
cria_audio(frase)
