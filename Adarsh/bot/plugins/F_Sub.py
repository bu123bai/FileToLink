
import logging
logger = logging.getLogger(__name__)

import datetime
from ..vars import vars
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from pyrogram.errors import UserNotParticipant, ChatAdminRequired, UsernameNotOccupied


@Client.on_message(filters.private & filters.incoming)
async def force_sub(c, m):
    if Config.FORCE_SUB:
        try:
            chat = await c.get_chat_member(Config.FORCE_SUB, m.from_user.id)
            if chat.status=='kicked':
                return await m.reply_text('Hai Brooh!You Where Banned🤭Kicked From Server Contact Admin🤧',  quote=True)

        except UserNotParticipant:
            button = [[InlineKeyboardButton('🔥 𝙹𝙾𝙸𝙽 𝙲𝙷𝙰𝙽𝙽𝙴𝙻 🔥', url=f'https://t.me/{Config.FORCE_SUB}')]]
            markup = InlineKeyboardMarkup(button)
            return await m.reply_text(text="Hai Brooh!Join My Main Channel🤣Then Use....\n 🤭ഡെയ് പാക്കര ചാനലിൽ Join ചെയ്തിട്ട് ബാക്കി പണിയ്", parse_mode='markdown', reply_markup=markup, quote=True)

        except ChatAdminRequired:
            logger.warning(f"Make me admin in @{Config.FORCE_SUB}")
            if m.from_user.id in Config.AUTH_USERS:
                return await m.reply_text(f"Make me admin in @{Config.FORCE_SUB}")

        except UsernameNotOccupied:
            logger.warning("The forcesub username was Incorrect. Please give the correct username.")
            if m.from_user.id in Config.AUTH_USERS:
                return await m.reply_text("The forcesub username was Incorrect. Please give the correct username.")

        except Exception as e:
            if "belongs to a user" in str(e):
                logger.warning("Forcesub username must be a channel username Not yours or any other users username")
                if m.from_user.id in Config.AUTH_USERS:
                    return await m.reply_text("Forcesub username must be a channel username Not yours or any other users username")
            logger.error(e)
            return await m.reply_text("Some thing went wrong. Try again and if same issue occur contact [Channel](https://t.me/MW_BOTS)", disable_web_page_preview=True, quote=True)

    await m.continue_propagation()
