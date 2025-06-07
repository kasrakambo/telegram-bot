import asyncio
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

AUTHORIZED_USER_ID = 2019819486
TOKEN = "6624991021:AAEsU4t8Cqy8wmb7SXEzDbzwZHXUmMskM7E"

async def spam(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.effective_user.id != AUTHORIZED_USER_ID:
        return
    if len(context.args) < 2:
        await update.message.reply_text("فرمت: /spam تعداد پیام")
        return
    try:
        count = int(context.args[0])
        if not (1 <= count <= 100):
            await update.message.reply_text("عدد بین 1 تا 100 بده")
            return
    except:
        await update.message.reply_text("عدد معتبر بده")
        return

    text = " ".join(context.args[1:])
    for _ in range(count):
        try:
            await update.message.reply_text(text)
            await asyncio.sleep(0.05)
        except:
            pass

app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(CommandHandler("spam", spam))
app.run_polling()
