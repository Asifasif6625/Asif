from pyrogram import filters
from aiohttp import ClientSession
from pyrogram import Client as bot
from plugins.function import make_carbon
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
aiohttpsession = ClientSession()

C = "**𝙼𝙰𝙳𝙴 𝙱𝚈 [kajal](https://t.me/Auto_filter_mvbot)**"
F = InlineKeyboardMarkup(
[[
     InlineKeyboardButton("join channel", url="https://t.me/Malayalamvibe")
]]
)




@bot.on_message(filters.command("carbon"))
async def carbon_func(_, message):
    if not message.reply_to_message:
        return await message.reply_text(
            "**teply to eny text message and create your carbon**"
        )
    if not message.reply_to_message.text:
        return await message.reply_text(
            "**reply to eny message to create carbon**"
        )
    user_id = message.from_user.id
    m = await message.reply_text("**create your carbon pic..**")
    carbon = await make_carbon(message.reply_to_message.text)
    await m.edit("**uploading your carbon...**")
    await message.reply_photo(
        photo=carbon,
        caption=C,
        reply_markup=F)
    await m.delete()
    carbon.close()
