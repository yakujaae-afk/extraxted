#  MIT License
#
#  Copyright (c) 2019-present Dan <https://github.com/delivrance>
#
#  Permission is hereby granted, free of charge, to any person obtaining a copy
#  of this software and associated documentation files (the "Software"), to deal
#  in the Software without restriction, including without limitation the rights
#  to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
#  copies of the Software, and to permit persons to whom the Software is
#  furnished to do so, subject to the following conditions:
#
#  The above copyright notice and this permission notice shall be included in all
#  copies or substantial portions of the Software.
#
#  THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#  IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#  FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#  AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#  LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
#  OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
#  SOFTWARE

# main.py में यह जोड़ें

# बाकी बॉट कोड...
import os
from config import Config
from pyrogram import Client, idle
import asyncio, logging
import tgcrypto
from pyromod import listen
from logging.handlers import RotatingFileHandler
LOGGER = logging.getLogger(__name__)
logging.basicConfig(
    level=logging.INFO,
    format="%(name)s - %(message)s",
    datefmt="%d-%b-%y %H:%M:%S",
    handlers=[
        RotatingFileHandler(
            "log.txt", maxBytes=5000000, backupCount=10
        ),
        logging.StreamHandler(),
    ],
)

# Auth Users
AUTH_USERS = [ int(chat) for chat in Config.AUTH_USERS.split(",") if chat != '']

# Prefixes 
prefixes = ["/", "~", "?", "!"]

plugins = dict(root="plugins")
if __name__ == "__main__" :
    bot = Client(
        "StarkBot",
        bot_token=os.environ.get("BOT_TOKEN"),
        api_id=int(os.environ.get("API_ID")),
        api_hash=os.environ.get("API_HASH"),
        sleep_threshold=20,
        plugins=plugins,
        workers = 50
    )
bot = Client(
    "my_bot",
    api_id=26729193,       # Replace with your API ID
    api_hash="a94598ef642481e35466292df95f251e",  # Replace with your API Hash
    bot_token="7706795279:AAE_KSUZaElgXpN3lVura8GD6OXZWr0-lGM"  # <-- Replace with the new token
)

async def main():
    try:
        await bot.start()
        bot_info = await bot.get_me()
        print(f"Bot started: @{bot_info.username}")
        await idle()  # Keeps the bot running
    except Exception as e:
        print(f"Error: {e}")
    finally:
        if await bot.is_initialized():  # Check if bot is running before stopping
            await bot.stop()
        print("Bot stopped")

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("Bot stopped by user")
    except Exception as e:
        print(f"Unexpected error: {e}")
