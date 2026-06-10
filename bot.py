import requests
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, ContextTypes

# ======================
TOKEN = "8902801768:AAHW3qPXi_d6f8ozWAy_13TfYX9GWIfuBMw"
CHANNEL = "@am1razzzz"
KICK_USERNAME = "am1razzz"
IMAGE_PATH = "am1razzzz.png"
# ======================

is_live = False


def check_kick():
    try:
        url = f"https://kick.com/api/v2/channels/{KICK_USERNAME}"
        r = requests.get(url, timeout=10)
        data = r.json()

        livestream = data.get("livestream")
        if not livestream:
            livestream = data.get("data", {}).get("livestream")

        return livestream
    except Exception as e:
        print("Kick API Error:", e)
        return None


async def send_live(context: ContextTypes.DEFAULT_TYPE, title: str):
    keyboard = [
        [InlineKeyboardButton("🟢 Live 🟢", url=f"https://kick.com/{KICK_USERNAME}")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    caption = f"<b>{title}</b>"

    with open(IMAGE_PATH, "rb") as photo:
        await context.bot.send_photo(
            chat_id=CHANNEL,
            photo=photo,
            caption=caption,
            parse_mode="HTML",
            reply_markup=reply_markup
        )


async def check_loop(context: ContextTypes.DEFAULT_TYPE):
    global is_live

    livestream = check_kick()

    # اگر لایو شروع شد
    if livestream and not is_live:
        title = livestream.get("session_title", "Live Stream")

        await send_live(context, title)

        is_live = True
        print("LIVE detected → sent message")

    # اگر لایو قطع شد
    if not livestream:
        is_live = False


async def post_init(app):
    # هر 60 ثانیه چک کن
    app.job_queue.run_repeating(check_loop, interval=60, first=5)


def main():
    app = ApplicationBuilder().token(TOKEN).post_init(post_init).build()

    print("Bot started")
    app.run_polling()


if __name__ == "__main__":
    main()