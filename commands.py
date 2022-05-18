import random
import pygame

from datetime import datetime

months = ("Janeiro", "Fevereiro", "Março", "Abril", "Maio",
          "Junho", "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro")

jokes = (
    "Quando eu tiver uma ovelha, vou chamá-la de Rover. Assim, quando",
    "eu tosá-la, poderei dizer que tenho lã de Rover. KKKKK",
    "Eu tomo café. A Cláudia, leite. Eu tomo gelado. O Clark, Kent. KKKKK",
    "Por que o lagarto deixou seu filho de castigo? Porque ele réptil de ano. KKKKK"
)

now = datetime.now()
today = datetime.today()
day = today.day
month = today.month
year = today.year
hour = now.hour
minute = now.minute

pygame.mixer.init()
pygame.mixer.music.load("songs/song.mp3")


def get_time_now():
    return f"Hoje é dia {day} de {months[month-1]} de {year}, e agora são {hour} horas e {minute} minutos."


def get_only_time():
    return f"Agora são {hour} horas e {minute} minutos."


def get_only_date():
    return f"Hoje é dia {day} de {months[month-1]} de {year}"


def say_a_joke():
    return random.choice(jokes)


def play_music():
    pygame.mixer.music.play()


def pause_music():
    pygame.mixer.music.pause()


def continue_music():
    pygame.mixer.music.unpause()


def stop_music():
    pygame.mixer.music.stop()


def get_temperature():
    ...

