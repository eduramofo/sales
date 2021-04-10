import telegram

from django.conf import settings

TOKEN = settings.TELEGRAM_BOT_API
CHAT_ID = settings.TELEGRAM_BOT_CHAT_ID


def setup():
    msg = 'Agendamento agora! Corra =D'
    send(msg)


def send(msg):
    """
    Send a message to a telegram user or group specified on chatId
    chat_id must be a number!
    """
    bot = telegram.Bot(token=TOKEN)
    bot.sendMessage(chat_id=CHAT_ID, text=msg)
