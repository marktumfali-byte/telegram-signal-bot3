import telegram
import schedule
import time
import random
from datetime import datetime

# ======= НАСТРОЙКИ БОТА =======
TOKEN = '8162965975:AAHclXgLYZ-nKTxi2VB-ihfFNbozYuCin6A'
CHANNEL_ID = '@Pvtbinary_bott'  # Имя твоего Telegram-канала

bot = telegram.Bot(token=TOKEN)

# ======= ФУНКЦИЯ ОТПРАВКИ СИГНАЛОВ =======
def send_signal(asset):
    direction = random.choice(['🟢 ВВЕРХ', '🔴 ВНИЗ'])
    expiration = random.randint(1, 5)
    
    message = f"🔹Актив: {asset}\n🔹Направление: {direction}\n⏱️ Экспирация: {expiration} минут"
    
    try:
        bot.send_message(chat_id=CHANNEL_ID, text=message)
        print(f"[{datetime.now().strftime('%H:%M:%S')}] Отправлено: {message}")
    except Exception as e:
        print(f"Ошибка при отправке: {e}")

# ======= РАСПИСАНИЕ =======

def schedule_signals():
    now = datetime.now()
    hour = now.hour
    weekday = now.weekday()  # 0 = Пн, 6 = Вс

    # Только с 10:00 до 19:00
    if 10 <= hour <= 19:
        # EUR/USD только по будням (Пн-Пт)
        if weekday < 5:
            send_signal("EUR/USD")
        # BIN/IDX каждый день
        send_signal("BIN/IDX")

# Каждые 30 минут
schedule.every(30).minutes.do(schedule_signals)

# ======= ЦИКЛ ЗАПУСКА =======
print("Бот запущен. Ожидание следующего сигнала...")
while True:
    schedule.run_pending()
    time.sleep(1)
