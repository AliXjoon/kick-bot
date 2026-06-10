import asyncio
import requests
from telegram import Bot, InlineKeyboardButton, InlineKeyboardMarkup

TOKEN = "8902801768:AAHW3qPXi_d6f8ozWAy_13TfYX9GWIfuBMw"
CHANNEL = "@am1razzzz"
USERNAME = "am1razzz"

bot = Bot(token=TOKEN)

def is_live():
    try:
        url = f"https://kick.com/api/v1/channels/{USERNAME}"

        print("Checking:", url)

        r = requests.get(url, timeout=10)

        print("Status Code:", r.status_code)
        print("Response:", r.text[:500])

        data = r.json()

        live = data.get("livestream") is not None

        print("Live =", live)

        return live

    except Exception as e:
        print("ERROR:", str(e))
        return False

async def send_live():
    try:
        keyboard = [
            [InlineKeyboardButton("🟢Live🟢", url=f"https://kick.com/{USERNAME}")]
        ]

        reply_markup = InlineKeyboardMarkup(keyboard)

        caption = "<b>🔴 LIVE STARTED</b>\n\nStream is now live 👇"

        print("Sending Telegram message...")

        with open("am1razzzz.png", "rb") as photo:
            await bot.send_photo(
                chat_id=CHANNEL,
                photo=photo,
                caption=caption,
                parse_mode="HTML",
                reply_markup=reply_markup
            )

        print("Message sent successfully!")

    except Exception as e:
        print("SEND ERROR:", str(e))

async def main():
    print("Bot started")

    was_live = False

    while True:
        live = is_live()

        print("Current status =", live)

        if live and not was_live:
            print("LIVE DETECTED!")
            await send_live()

        was_live = live

        await asyncio.sleep(60)

if __name__ == "__main__":
    asyncio.run(main())
