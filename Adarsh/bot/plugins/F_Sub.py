from pyrogram import Client, filters, enums 
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from pyrogram.errors import UserNotParticipant
from Adrash.vars import UPDATES_CHANNEL

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
    buttons = [[ InlineKeyboardButton(text="🔅 ᴊᴏɪɴ ᴏᴜʀ ᴜᴘᴅᴀᴛᴇ ᴄʜᴀɴɴᴇʟ 🔅", url=f"https://t.me/{UPDATES_CHANNEL}") ]]
    text = "**𝙳𝚄𝙴 𝚃𝙾 𝙷𝙴𝙰𝚅𝚈 𝚃𝚁𝙰𝙵𝙵𝙸𝙲 𝚈𝙾𝚄 𝙷𝙰𝚅𝙴 𝚃𝙾 𝙹𝙾𝙸𝙽 𝙾𝚄𝚁 𝙲𝙰𝙷𝙽𝙽𝙴𝙻 𝚃𝙾 𝚄𝚂𝙴 𝚃𝙷𝙸𝚂 𝙱𝙾𝚃 😔🙏 **"
    try:
        user = await client.get_chat_member(client.force_channel, message.from_user.id)    
        if user.status == enums.ChatMemberStatus.BANNED:                                   
            return await client.send_message(message.from_user.id, text="𝚈𝙾𝚄𝚁 𝙰𝚁𝙴 𝙱𝙰𝙽𝙽𝙴𝙳 𝚃𝙾 𝚄𝚂𝙴 𝙼𝙴")  
    except UserNotParticipant:                       
        return await message.reply_text(text=text, reply_markup=InlineKeyboardMarkup(buttons))
    return await message.reply_text(text=text, reply_markup=InlineKeyboardMarkup(buttons))
          

