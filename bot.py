import logging
from typing import Optional

from telegram import Update
from telegram.ext import ContextTypes

from settings import settings
from utils.url_extractor import extract_urls
from yt_downloader import download_video

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    message = (f"Hello👋, I'm a bot developed by @{settings.DEVELOPER}\n"
               "I'm here to help you download YouTube videos📽\n"
               "Please send a YouTube video URL to get started.")
    await context.bot.send_message(chat_id=update.effective_chat.id, text=message)


async def downloader(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    message = update.message.text

    url: Optional[str] = extract_urls(message)
    if not url:
        await context.bot.send_message(chat_id=update.effective_chat.id,
                                       text="Sorry, You need to provide me a valid YouTube video URL.")
        return

    # Download the video from YouTube
    video_path = None
    try:
        await context.bot.send_message(chat_id=update.effective_chat.id, text="Start downloading video...")

        video_path = download_video(url, settings.COOKIES_FILE)

        await context.bot.send_message(chat_id=update.effective_chat.id, text="Sending your video...")
        await context.bot.send_video(chat_id=update.effective_chat.id, video=video_path)

    except Exception as e:
        await context.bot.send_message(chat_id=update.effective_chat.id,
                                       text="Sorry An error occurred while sending your video!")

    finally:
        if video_path:
            # Delete the downloaded file
            import os
            os.remove(video_path)
