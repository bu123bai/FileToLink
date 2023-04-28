from pyrogram import Client, filters, enums 
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from pyrogram.errors import UserNotParticipant
from config import FORCE_SUB

async def not_subscribed(_, client, message):
    if not client.force_channel:
        return False
    try:             
        user = await client.get_chat_member(client.force_channel, message.from_user.id) 
        if user.status == enums.ChatMemberStatus.BANNED:
            return True 
        else:
            return False                
    except UserNotParticipant:
        pass
    return True


@Client.on_message(filters.private & filters.create(not_subscribed))
async def forces_sub(client, message):
    buttons = [[ InlineKeyboardButton(text="🔅 ᴊᴏɪɴ ᴏᴜʀ ᴜᴘᴅᴀᴛᴇ ᴄʜᴀɴɴᴇʟ 🔅", url=f"https://t.me/{FORCE_SUB}") ]]
    text = "**𝙳𝚞𝚎 𝚃𝚘 𝙷𝚎𝚊𝚟𝚢 𝚃𝚛𝚊𝚏𝚏𝚒𝚌 𝚈𝚘𝚞 𝙷𝚊𝚟𝚎 𝚃𝚘 𝙹𝙾𝙸𝙽 𝙾𝚄𝚁 𝙲𝙰𝙷𝙽𝙽𝙴𝙻 😔. 𝙿𝙻𝙴𝙰𝚂𝙴 𝙹𝙾𝙸𝙽 𝙼𝚈 𝙲𝙷𝙰𝙽𝙽𝙴𝙻 𝚃𝙾 𝚄𝚂𝙴 𝚃𝙷𝙸𝚂 𝙱𝙾𝚃 🙏 **"
    try:
        user = await client.get_chat_member(client.force_channel, message.from_user.id)    
        if user.status == enums.ChatMemberStatus.BANNED:                                   
            return await client.send_message(message.from_user.id, text="𝚈𝙾𝚄𝚁 𝙰𝚁𝙴 𝙱𝙰𝙽𝙽𝙴𝙳 𝚃𝙾 𝚄𝚂𝙴 𝙼𝙴")  
    except UserNotParticipant:                       
        return await message.reply_text(text=text, reply_markup=InlineKeyboardMarkup(buttons))
    return await message.reply_text(text=text, reply_markup=InlineKeyboardMarkup(buttons))
          

