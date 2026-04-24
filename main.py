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
from config import Config API_ID, API_HASH, BOT_TOKEN,
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



# Initialize the bot
bot = Client(
    "bot",
    api_id=30296254,
    api_hash=c2b5306f4ccd2d795405a026c10b4c62
    bot_token=8697293437:AAFwdPxKY-MaVw22-e_Z7ue0yHmbm-DGCs0
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
