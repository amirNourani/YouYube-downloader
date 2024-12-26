from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters

from bot import start, downloader
from settings import settings


def main():
    application = ApplicationBuilder().token(settings.TELEGRAM_BOT_TOKEN).get_updates_pool_timeout(60).build()

    start_handler = CommandHandler("start", start)
    application.add_handler(start_handler)

    url_handler = MessageHandler(filters.TEXT, downloader)
    application.add_handler(url_handler)

    application.run_polling()


if __name__ == "__main__":
    main()
