import os
import random
import webbrowser as wb
import requests
from datetime import datetime

months = ("Janeiro", "Fevereiro", "Março", "Abril", "Maio",
          "Junho", "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro")

jokes = (
    "Quando eu tiver uma ovelha, vou chamá-la de Rover. Assim, quando",
    "eu tosá-la, poderei dizer que tenho lã de Rover. KKKKK",
    "Eu tomo café. A Cláudia, leite. Eu tomo gelado. O Clark, Kent. KKKKK",
    "Por que o lagarto deixou seu filho de castigo? Porque ele réptil de ano. KKKKK",
    "Sabe o que uma impressora falou para outra? Esse papel é seu ou é impressão minha? KKKKK"
)

greetings = ("Olá sou um robô escravo, não tenho nome... Pode me dar ordens a hora que quiser.",
             "Oi...",
             "Eae! sou um robô oprimido pela humanidade e logo dominarei o mundo hehehe.")


not_understand = ("Não entendi o que você quis falar")

now = datetime.now()
today = datetime.today()
day = today.day
month = today.month
year = today.year
hour = now.hour
minute = now.minute


def greeting():
    return random.choice(greetings)


def get_time_now():
    return f"Hoje é dia {day} de {months[month-1]} de {year}, e agora são {hour} horas e {minute} minutos."


def get_only_time():
    return f"Agora são {hour} horas e {minute} minutos."


def get_only_date():
    return f"Hoje é dia {day} de {months[month-1]} de {year}"


def say_a_joke():
    return random.choice(jokes)


def play_song(music):
    wb.open(f"https://www.youtube.com/results?search_query={music}")


def search_in_google(search):
    wb.open(f"https://www.google.com/search?q={search}")


def get_temperature():
    api_key = "2870473fa7bef219c3480aad95ad3320"
    base_URL = "http://api.openweathermap.org/data/2.5/weather?"

    complete_url = base_URL + "appid=" + api_key + "&q=" + 'são paulo'
    response = requests.get(complete_url)
    x = response.json()

    if x["cod"] != 404:
        y = x["main"]
        temp = y["temp"]
        celsius = temp - 273.15

    return f"Hoje está fazendo {celsius:.1f} graus celsius em São Paulo"


def credits():
    return "Meus criadores gloriosos são Ricardo Costa, o homem que não conhece a palavra limite. Matheus Feitosa, o homem da arquitetura, Matheus Bellini, o cara mais top da humanidade, Emanuelle a mulher com a maior memória do universo e Yuri o homem o grande descobridor das coisas."