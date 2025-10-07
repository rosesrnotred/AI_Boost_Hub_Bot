# bot.py
# DO NOT put your token here. Set it as an environment variable named BOT_TOKEN (see Render steps).

import os
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes

BOT_TOKEN = os.environ.get("BOT_TOKEN")
if not BOT_TOKEN:
    print("ERROR: BOT_TOKEN environment variable not set. Exiting.")
    exit(1)

WELCOME_MESSAGE = """🎉 *Congratulations!* You've completed the offer and unlocked your AI rewards!

Welcome to *AI Boost Hub*, your gateway to the internet's most powerful and useful AI tools. 🚀

As promised, your exclusive access to 20 of the best AI websites and platforms — designed to help you write faster, create amazing content, design effortlessly, and get more done in less time.

👉 Please enter the keyword for the reward (E.g: type "Tools" for the 20 AI tools)
"""

TOOLS_MESSAGE = """🧠 *Top 20 AI Tools You Must Try*  

1. ChatGPT — https://chat.openai.com
2. Claude AI — https://claude.ai
3. Perplexity AI — https://www.perplexity.ai
4. Notion AI — https://www.notion.so/product/ai
5. Gamma App — https://gamma.app
6. Synthesia — https://www.synthesia.io
7. Copy.ai — https://www.copy.ai
8. Jasper — https://www.jasper.ai
9. Runway ML — https://runwayml.com
10. Pika Labs — https://pika.art
11. ElevenLabs — https://elevenlabs.io
12. Midjourney — https://www.midjourney.com
13. Canva Magic Studio — https://www.canva.com/magic
14. Durable AI — https://durable.co
15. Krisp — https://krisp.ai
16. Beautiful.ai — https://www.beautiful.ai
17. Tome.app — https://tome.app
18. QuillBot — https://quillbot.com
19. Descript — https://www.descript.com
20. Murf.ai — https://murf.ai
"""

ONLYFANS_MESSAGE = """thankyou you get that right keyword...
here's  the link of the website : https://bit.ly/48SFpHT
"""

UNKNOWN_MESSAGE = "It looks like it is not the keyword. Please paste a valid keyword like 'Tool' to get the response; if not, please contact the bot builder. Thank you!"

# /start command handler
async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(WELCOME_MESSAGE, parse_mode="Markdown")

# text messages handler
async def handle_text(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text.strip().lower()
    if text in ("tools", "tool"):
        await update.message.reply_text(TOOLS_MESSAGE, parse_mode="Markdown")
    elif text == "onlyfans" or text == "onlyfan" or text == "only fans":
        await update.message.reply_text(ONLYFANS_MESSAGE)
    else:
        await update.message.reply_text(UNKNOWN_MESSAGE)

def main():
    app = ApplicationBuilder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start_command))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_text))
    print("✅ AI Boost Hub Bot is running...")
    app.run_polling()

if __name__ == "__main__":
    main()
