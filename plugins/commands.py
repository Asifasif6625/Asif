import os
import logging
import random
import asyncio
from Script import script
from pyrogram import Client, filters
from pyrogram.errors.exceptions.bad_request_400 import ChatAdminRequired
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from database.ia_filterdb import Media, get_file_details, unpack_new_file_id
from database.users_chats_db import db
from info import CHANNELS, ADMINS, AUTH_CHANNEL, CUSTOM_FILE_CAPTION, LOG_CHANNEL
from utils import get_size, is_subscribed, temp
import re
logger = logging.getLogger(__name__)

@Client.on_message(filters.command("start"))
async def start(client, message):
    if message.chat.type in ['group', 'supergroup']:
        buttons = [
            [
                InlineKeyboardButton('Any help🤝', url=f"https://t.me/malayalamvibead")
            ]
            ]
        reply_markup = InlineKeyboardMarkup(buttons)
        await message.reply(script.PRIVATEBOT_TXT.format(message.from_user.mention if message.from_user else message.chat.title, temp.U_NAME, temp.B_NAME), reply_markup=reply_markup)
        await asyncio.sleep(2) # 😢 https://github.com/EvamariaTG/EvaMaria/blob/master/plugins/p_ttishow.py#L17 😬 wait a bit, before checking.
        if not await db.get_chat(message.chat.id):
            total=await client.get_chat_members_count(message.chat.id)
            await client.send_message(LOG_CHANNEL, script.LOG_TEXT_G.format(message.chat.title, message.chat.id, total, "Unknown"))       
            await db.add_chat(message.chat.id, message.chat.title)
        return 
    if not await db.is_user_exist(message.from_user.id):
        await db.add_user(message.from_user.id, message.from_user.first_name)
        await client.send_message(LOG_CHANNEL, script.LOG_TEXT_P.format(message.from_user.id, message.from_user.mention))
    if len(message.command) != 2:
        buttons = [[
            InlineKeyboardButton('•ᴀᴅᴅ ᴍᴇ ᴛᴏ yᴏᴜʀ ɢʀᴏᴜᴩ•\nᴀɴᴅ ᴇɴᴊᴏy', url=f'http://t.me/{temp.U_NAME}?startgroup=true')
            ],[
            InlineKeyboardButton('• ᴄʜᴀɴɴᴇʟ •', url='https://t.me/malayalamvibe'),
            InlineKeyboardButton('• ᴜᴩᴅᴀᴛᴇꜱ •', url='https://t.me/mlavib')
            ],[      
            InlineKeyboardButton('• ʜᴇʟᴩ •', callback_data='help'),
            InlineKeyboardButton('• ᴀʙᴏᴜᴛ •', callback_data='about')
            ],[
            InlineKeyboardButton('• ʀᴇqᴜꜱᴛ ɢʀᴏᴜᴩ • ', url='https://t.me/+dezh9OsvdKk1OTRl'),
            InlineKeyboardButton('• ᴩᴍ ᴏᴡɴʀ •', url='https://t.me/malayalamvibead')
            ],[
            InlineKeyboardButton('• ᴍᴏᴠɪᴇ ᴄʜᴀɴɴᴇʟꜱ •', callback_data='mvmovie')
            ],[
            InlineKeyboardButton('× ᴄʟᴏꜱᴇ ᴍꜱɢ ×', callback_data='close_data')
        ]]
        k = await message.reply_photo(https://telegra.ph/file/78f3d720291089608de70.jpg)
        await k.delete()
        reply_markup = InlineKeyboardMarkup(buttons)      
        k = await message.reply_text(" hi i am auto filter bot, add me your groups \n ഞാൻ മലയാളം വൈബ്ന്റെ ഗ്രൂപ്പിൽ ആണ് വർക്ക്‌ ചെയ്യുന്നത് നിങ്ങൾക്കും എന്നെ നിങ്ങളുടെ ഗ്രൂപ്പിൽ ആഡ് ചെയ്യാം.. ")
        await k.delete()   
  
        )
        return
    if AUTH_CHANNEL and not await is_subscribed(client, message):
        try:
            invite_link = await client.create_chat_invite_link(int(AUTH_CHANNEL))
        except ChatAdminRequired:
            logger.error("Make sure Bot is admin in Forcesub channel")
            return
        btn = [
            [
                InlineKeyboardButton(
                    "• ᴊᴏɪɴ ᴄʜᴀɴɴᴇʟ •", url=invite_link.invite_link
                )
            ]
        ]

        if message.command[1] != "subscribe":
            btn.append([InlineKeyboardButton("• ᕼY ᗷᖇO TᖇY ᗩGᗩIᑎ •", callback_data=f"checksub#{message.command[1]}")])
        await message.reply_photo('https://telegra.ph/file/684c2e364354bbd6a91e2.jpg') 
        await client.send_message(
            chat_id=message.from_user.id,
            text="click the button and join channel",
            reply_markup=InlineKeyboardMarkup(btn),
            parse_mode="markdown"
            )
        return
    if len(message.command) ==2 and message.command[1] in ["subscribe", "error", "okay", "help"]:
        buttons = [[
            InlineKeyboardButton('•ᴀᴅᴅ ᴍᴇ ᴛᴏ yᴏᴜʀ ɢʀᴏᴜᴩ•\nᴀɴᴅ ᴇɴᴊᴏy', url=f'http://t.me/{temp.U_NAME}?startgroup=true')
            ],[
            InlineKeyboardButton('• ᴄʜᴀɴɴᴇʟ •', url='https://t.me/malayalamvibe'),
            InlineKeyboardButton('• ᴜᴩᴅᴀᴛᴇꜱ •', url='https://t.me/mlavib')
            ],[      
            InlineKeyboardButton('• ʜᴇʟᴩ •', callback_data='help'),
            InlineKeyboardButton('• ᴀʙᴏᴜᴛ •', callback_data='about')
            ],[
            InlineKeyboardButton('• ʀᴇqᴜꜱᴛ ɢʀᴏᴜᴩ • ', url='https://t.me/+dezh9OsvdKk1OTRl'),
            InlineKeyboardButton('• ᴩᴍ ᴏᴡɴʀ •', url='https://t.me/malayalamvibead')
            ],[
            InlineKeyboardButton('• ᴍᴏᴠɪᴇ ᴄʜᴀɴɴᴇʟꜱ •', callback_data='mvmovie')
            ],[
            InlineKeyboardButton('× ᴄʟᴏꜱᴇ ᴍꜱɢ ×', callback_data='close_data')
        ]]
        reply_markup = InlineKeyboardMarkup(buttons)
        await message.reply_photo(
            photo=random.choice(PICS),
            caption=script.START_TXT.format(message.from_user.mention, temp.U_NAME, temp.B_NAME),
            reply_markup=reply_markup,
            parse_mode='html'
        )
        return
    file_id = message.command[1]
    files_ = await get_file_details(file_id)
    if not files_:
        return await message.reply('No such file exist.')
    files = files_[0]
    title = files.file_name
    size=get_size(files.file_size)
    f_caption=files.caption
    if CUSTOM_FILE_CAPTION:
        try:
            f_caption=CUSTOM_FILE_CAPTION.format(file_name=title, file_size=size, file_caption=f_caption)
        except Exception as e:
            logger.exception(e)
            f_caption=f_caption
    if f_caption is None:
        f_caption = f"{files.file_name}"
    await client.send_cached_media(
        chat_id=message.from_user.id,
        file_id=file_id,
        caption=f_caption,
        )
                    

@Client.on_message(filters.command('channel') & filters.user(ADMINS))
async def channel_info(bot, message):
           
    """Send basic information of channel"""
    if isinstance(CHANNELS, (int, str)):
        channels = [CHANNELS]
    elif isinstance(CHANNELS, list):
        channels = CHANNELS
    else:
        raise ValueError("Unexpected type of CHANNELS")

    text = '📑 **Indexed channels/groups**\n'
    for channel in channels:
        chat = await bot.get_chat(channel)
        if chat.username:
            text += '\n@' + chat.username
        else:
            text += '\n' + chat.title or chat.first_name

    text += f'\n\n**Total:** {len(CHANNELS)}'

    if len(text) < 4096:
        await message.reply(text)
    else:
        file = 'Indexed channels.txt'
        with open(file, 'w') as f:
            f.write(text)
        await message.reply_document(file)
        os.remove(file)


@Client.on_message(filters.command('logs') & filters.user(ADMINS))
async def log_file(bot, message):
    """Send log file"""
    try:
        await message.reply_document('TelegramBot.log')
    except Exception as e:
        await message.reply(str(e))

@Client.on_message(filters.command('delete') & filters.user(ADMINS))
async def delete(bot, message):
    """Delete file from database"""
    reply = message.reply_to_message
    if reply and reply.media:
        msg = await message.reply("𝗖𝗵𝗲𝗰𝗸𝗶𝗻𝗴...⏳😜", quote=True)
    else:
        await message.reply('Reply to file with /delete which you want to delete', quote=True)
        return

    for file_type in ("document", "video", "audio"):
        media = getattr(reply, file_type, None)
        if media is not None:
            break
    else:
        await msg.edit('This is not supported file format')
        return
    
    file_id, file_ref = unpack_new_file_id(media.file_id)

    result = await Media.collection.delete_one({
        '_id': file_id,
    })
    if result.deleted_count:
        await msg.edit('File is successfully deleted from database')
    else:
        file_name = re.sub(r"(_|\-|\.|\+)", " ", str(media.file_name))
        result = await Media.collection.delete_one({
            'file_name': file_name,
            'file_size': media.file_size,
            'mime_type': media.mime_type
            })
        if result.deleted_count:
            await msg.edit('File is successfully deleted from database')
        else:
            # files indexed before https://github.com/EvamariaTG/EvaMaria/commit/f3d2a1bcb155faf44178e5d7a685a1b533e714bf#diff-86b613edf1748372103e94cacff3b578b36b698ef9c16817bb98fe9ef22fb669R39 
            # have original file name.
            result = await Media.collection.delete_one({
                'file_name': media.file_name,
                'file_size': media.file_size,
                'mime_type': media.mime_type
            })
            if result.deleted_count:
                await msg.edit('File is successfully deleted from database')
            else:
                await msg.edit('File not found in database')


@Client.on_message(filters.command('deleteall') & filters.user(ADMINS))
async def delete_all_index(bot, message):
    await message.reply_text(
        'This will delete all indexed files.\nDo you want to continue??',
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        text="𝗬𝗘𝗦😘", callback_data="autofilter_delete"
                    )
                ],
                [
                    InlineKeyboardButton(
                        text="𝗖𝗔𝗡𝗖𝗘𝗟☹️", callback_data="close_data"
                    )
                ],
            ]
        ),
        quote=True,
    )


@Client.on_callback_query(filters.regex(r'^autofilter_delete'))
async def delete_all_index_confirm(bot, message):
    await Media.collection.drop()
    await message.answer()
    await message.message.edit('Succesfully Deleted All The Indexed Files.')

