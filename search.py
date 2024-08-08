import requests
from pystyle import Colors, Write
import time

current_theme = Colors.red_to_yellow

last_search_time = 0


def api_search(req):
    global last_search_time
    try:
        current_time = time.time()
        if current_time - last_search_time < 60:
            Write.Print("\n[!] Подождите \n", current_theme, interval=0.0001)
            return

        response = requests.post("https://server.leakosint.com/",
                                 json={"token": "6607575831:mrjoz662",
                                       "request": req, "limit": 10,
                                       "lang": "ru"})
        data = response.json().get('List', {})

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
                    Write.Print(f"\n[S] {key} -> ", current_theme, interval=0.0001)
                    Write.Print(value, Colors.white, interval=0.0001)
            print()

        last_search_time = current_time
    except Exception as e:
        Write.Print(f"\n[ERROR] Произошла ошибка: {e}\n", current_theme, interval=0.0001)