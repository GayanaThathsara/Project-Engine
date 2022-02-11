import psutil
import shutil
import time
from utilsbot import *
from typing import Text
from pyrogram import Client, filters
from pyrogram.types import (InlineQueryResultArticle, InputTextMessageContent,
                            InlineKeyboardMarkup, InlineKeyboardButton)
from pyrogram.types import ReplyKeyboardMarkup

import os
from os import getenv, environ
from dotenv import load_dotenv

if os.path.exists('config.env'):
  load_dotenv('config.env')

class Var(object):
    API_ID = int(getenv('API_ID'))
    API_HASH = str(getenv('API_HASH'))
    BOT_TOKEN = str(getenv('BOT_TOKEN')

bot = Client(
    "my_bot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN,)

KeyboardZ = ReplyKeyboardMarkup(
    [
        ["Start", "Ping", "Status", "DC"],
        ["A", "B", "C", "D"],
        ["E", "F", "G", "H"],
        ["Test Audio"],
        ["Devs", "Index", "DB"],
        ["Update"]

    ],
    resize_keyboard=True)


@bot.on_message((filters.command("start") | filters.regex('Start')) & filters.private & ~filters.edited)
def command(bot, message):
    bot.send_message(
        chat_id=message.chat.id,
        text="""Hi Test Buttn!""",
        parse_mode="html",
        reply_markup=KeyboardZ)

@bot.on_message(filters.incoming & filters.command("run"))
def command(bot, message):
    bot.send_message(message.chat.id, "Bot Alive")
    bot.send_dice(message.chat.id, "🏀")
    
@bot.on_message(filters.incoming & filters.command("image"))
def command(bot, message):
    bot.send_photo(message.chat.id, "https://telegra.ph/file/4089e363161303efe4b79.png", ttl_seconds=10)
  
@bot.on_message(filters.incoming & (filters.command("audio") | filters.regex('Test Audio')) )
    bot.send_audio(message.chat.id, "https://mikasalinkgen.herokuapp.com/1328/The+Book+of+Boba+Fett+-+Ludwig+Goransson+%5BUSWD12113499%5D+%28128.mp3")
  

@bot.on_inline_query()
def answer(client, inline_query):
    inline_query.answer(
        results=[
            InlineQueryResultArticle(
                title="Hunter's DataBase",
                input_message_content=InputTextMessageContent(
                    "Hunters DataBase"
                ),
                url="https://t.me/HuntersDataBase",
                description="Mostly Sci-fi Database",
                reply_markup=InlineKeyboardMarkup(
                    [
                        [InlineKeyboardButton(
                            "Join Hunter's Database",
                            url="https://t.me/HuntersDataBase"
                        )]
                    ]
                )
            ),
            InlineQueryResultArticle(
                title="Hunter's Index",
                input_message_content=InputTextMessageContent(
                    "Hunter's Index"
                ),
                url="https://t.me/HuntersIndex",
                description="Hunter DB's Index Channel",
                reply_markup=InlineKeyboardMarkup(
                    [
                        [InlineKeyboardButton(
                            "Join Hunter's Index",
                            url="https://t.me/HuntersIndex"
                        )]
                    ]
                )
            )
        ],
        cache_time=1
    )

@bot.on_message(filters.regex("DC"))
async def start(bot, update):
    text = START_TEXT.format(update.from_user.dc_id)
    await update.reply_text(
        text=text,
        disable_web_page_preview=True,
        quote=True
    )

START_TEXT = """ Your Telegram DC Is : `{}`  """

@bot.on_message(filters.regex("Ping"))
async def ping(bot, message):
    start_t = time.time()
    jv = await message.reply_text("....")
    end_t = time.time()
    time_taken_s = (end_t - start_t) * 1000
    await jv.edit(f"Ping!\n{time_taken_s:.3f} ms")


StartTime = time.time()


@bot.on_message(filters.private & filters.regex("Status"))
async def stats(bot, update):
    currentTime = readable_time((time.time() - StartTime))
    total, used, free = shutil.disk_usage('.')
    total = get_readable_file_size(total)
    used = get_readable_file_size(used)
    free = get_readable_file_size(free)
    sent = get_readable_file_size(psutil.net_io_counters().bytes_sent)
    recv = get_readable_file_size(psutil.net_io_counters().bytes_recv)
    cpuUsage = psutil.cpu_percent(interval=0.5)
    memory = psutil.virtual_memory().percent
    disk = psutil.disk_usage('/').percent
    botstats = f'<b>Bot Uptime:</b> {currentTime}\n' \
        f'<b>Total disk space:</b> {total}\n' \
        f'<b>Used:</b> {used}  ' \
        f'<b>Free:</b> {free}\n\n' \
        f'Data Usage:\n<b>Upload:</b> {sent}\n' \
        f'<b>Down:</b> {recv}\n\n' \
        f'<b>CPU:</b> {cpuUsage}% ' \
        f'<b>RAM:</b> {memory}% ' \
        f'<b>Disk:</b> {disk}%'
    await update.reply_text(botstats)

    
    
bot.run()
