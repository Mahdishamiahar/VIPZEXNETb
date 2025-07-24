import json
from rubpy import Client, filters
from rubpy.types import Update

# بارگذاری توکن از فایل config.json
with open("config.json", "r", encoding="utf-8") as f:
    cfg = json.load(f)

bot = Client(token=cfg["token"])

@bot.on_message_updates(filters.text)
async def on_msg(update: Update):
    text = update.text.strip().lower()
    if text == "/start":
        await update.reply("🎉 سلام! به ربات خوش آمدید!")
    else:
        await update.reply("❓ فقط دستور /start قبول است.")

if __name__ == "__main__":
    bot.run()