import time
from telegram import Bot, InlineKeyboardButton, InlineKeyboardMarkup

TOKEN = "8902801768:AAHW3qPXi_d6f8ozWAy_13TfYX9GWIfuBMw"
CHANNEL = "@am1razzzz"

bot = Bot(token=TOKEN)

def send_live():
    keyboard = [
        [InlineKeyboardButton("🟢 Live 🟢", url="https://kick.com/am1razzzz")]
    ]

    reply_markup = InlineKeyboardMarkup(keyboard)

    with open("am1razzzz.png", "rb") as photo:
        bot.send_photo(
            chat_id=CHANNEL,
            photo=photo,
            caption="<b>🔴 LIVE STREAM STARTED</b>",
            parse_mode="HTML",
            reply_markup=reply_markup
        )

print("Bot started")

send_live()

# 🔥 این قسمت باعث میشه Railway نزنه ببنده
while True:
    time.sleep(60)
