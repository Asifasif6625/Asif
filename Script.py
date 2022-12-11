class script(object):
    HELP_TXT = """check buttons by help"""
    ABOUT_TXT = """• my name: {}
• creaters: <a href=https://t.me/malayalamvibead>𝓐𝓼𝓲𝓯 𝓹𝓶𝓷🤠</a>
• library: program 
• language: Python 𝟹
• data Base: mangoDB
• bot server: Nil"""
    MV_TXT = """<b>⊳ channel 1 https://t.me/+bEiUvBpP9dEwMDM1 \n⊳ channel link 2 https://t.me/+ObQLgYTfvkwyZWE9</b>"""
    PRIVATEBOT_TXT = """<b>ഞാൻ ബാല എന്താണ് സ്റ്റാർട്ട്‌ അടിച്ച് കളിക്കണ്
ദിസ്‌ ഈസ്‌ റാങ്..🪝</b>"""

    SOURCE_TXT = """<b>Donation</b>

⪼ <b>𝐘𝐨𝐮 𝐂𝐚𝐧 𝐃𝐨𝐧𝐚𝐭𝐞 𝐀𝐧𝐲 𝐀𝐦𝐨𝐮𝐧𝐭 𝐘𝐨𝐮 𝐇𝐚𝐯𝐞 💳. 

<b>━━━━━━━━━᚜ Payment Methods ᚛━━━━━━━━━

✮ 𝗚𝗼𝗼𝗴𝗹𝗲𝗣𝗮𝘆
✮ 𝗣𝗮𝘆𝘁𝗺
✮ 𝗣𝗵𝗼𝗻𝗲𝗣𝗲
✮ 𝗣𝗮𝘆𝗣𝗮𝗹

_𝐂𝐨𝐧𝐭𝐚𝐜𝐭 𝐌𝐞 𝐅𝐨𝐫 𝐊𝐧𝐨𝐰 𝐀𝐛𝐨𝐮𝐭 𝐓𝐡𝐞 𝐏𝐚𝐲𝐦𝐞𝐧𝐭 𝐈𝐧𝐟𝐨_
━━━━━━━━━━━━᚜ <a href=https://t.me/AboutAadhi><b>ꪖꪖᦔꫝỉ</b></a> ᚛━━━━━━━━━━━━"""
    MANUELFILTER_TXT = """Help: <b>Filters</b>  

- Filter is the feature were users can set automated replies for a particular keyword and ᗩᒍᗩ᙭ will respond whenever a keyword is found the message

<b>NOTE:</b>
1. ᗩᒍᗩ᙭ should have admin privillage.
2. only admins can add filters in a chat.
3. alert buttons have a limit of 64 characters.

<b>Commands and Usage:</b>
➾ /filter - <code>add a filter in chat</code>
➾ /filters - <code>list all the filters of a chat</code>
➾ /del - <code>delete a specific filter in chat</code>
➾ /delall - <code>delete the whole filters in a chat (chat owner only)</code>"""
    BUTTON_TXT = """Help: <b>Buttons</b>

- ᗩᒍᗩ᙭ Supports both url and alert inline buttons.

<b>NOTE:</b>
1. Telegram will not allows you to send buttons without any content, so content is mandatory.
2. ᗩᒍᗩ᙭ supports buttons with any telegram media type.
3. Buttons should be properly parsed as markdown format

<b>URL buttons:</b>
<code>[Button Text](buttonurl:https://t.me/source00Devil)</code>

<b>Alert buttons:</b>
<code>[Button Text](buttonalert:This is an alert message)</code>"""
    AUTOFILTER_TXT = """Help: <b>Auto Filter</b>

<b>NOTE:</b>
1. Make me the admin of your channel if it's private.
2. make sure that your channel does not contains camrips, porn and fake files.
3. Forward the last message to me with quotes.
 I'll add all the files in that channel to my db."""
    CONNECTION_TXT = """Help: <b>Connections</b>

- Used to connect bot to PM for managing filters 
- it helps to avoid spamming in groups.

<b>NOTE:</b>
1. Only admins can add a connection.
2. Send <code>/connect</code> for connecting me to ur PM

<b>Commands and Usage:</b>
➾ /connect  - <code>connect a particular chat to your PM</code>
➾ /disconnect  - <code>disconnect from a chat</code>
➾ /connections - <code>list all your connections</code>"""
    EXTRAMOD_TXT = """Help: <b>Extra Modules</b>

<b>NOTE:</b>
These are the extra features of ᗩᒍᗩ᙭

<b>Commands and Usage:</b>
➾ /id - <code>get id of a specifed user.</code>
➾ /info  - <code>get information about a user.</code>
➾ /imdb  - <code>get the film information from IMDb source.</code>
➾ /search  - <code>get the film information from various sources.</code>"""
    ADMIN_TXT = """Help: <b>Admin mods</b>

<b>NOTE:</b>
This module only works for my OᗯᑎEᖇ⚡

<b>Commands and Usage:</b>
➾ /logs - <code>to get the rescent errors</code>
➾ /stats - <code>to get status of files in db.</code>
➾ /delete - <code>to delete a specific file from db.</code>
➾ /users - <code>to get list of my users and ids.</code>
➾ /chats - <code>to get list of the my chats and ids </code>
➾ /leave  - <code>to leave from a chat.</code>
➾ /disable  -  <code>do disable a chat.</code>
➾ /ban  - <code>to ban a user.</code>
➾ /unban  - <code>to unban a user.</code>
➾ /channel - <code>to get list of total connected channels</code>
➾ /broadcast - <code>to broadcast a message to all users</code>"""
    STATUS_TXT = """• total files : <code>{}</code>
• total user's : <code>{}</code>
• total chats : <code>{}</code>
• used storage : <code>{}</code> 𝙼𝚒𝙱
• free space : <code>{}</code> 𝙼𝚒𝙱"""
    LOG_TEXT_G = """#𝐍𝐞𝐰𝐆𝐫𝐨𝐮𝐩
💞 𝐆𝐫𝐨𝐮𝐩 ›› {}(<code>{}</code>)
💞 𝐓𝐨𝐭𝐚𝐥 𝐌𝐞𝐦𝐛𝐞𝐫𝐬 ›› <code>{}</code>
💞 𝐀𝐝𝐝𝐞𝐝 𝐁𝐲 ›› {}
"""
    LOG_TEXT_P = """#new💕
💕 id ›› <code>{}</code>
💕 name ›› {}
"""
    CARBON_TXT = """ <b>𝙲𝙰𝚁𝙱𝙾𝙽 𝙼𝙾𝙳𝚄𝙻𝙴</b>

<b>𝚈𝙾𝚄 𝙲𝙰𝙽 𝙱𝙴𝙰𝚄𝚃𝙸𝙵𝚈 𝚈𝙾𝚄𝚁 𝙲𝙾𝙳𝙴𝚂 𝙱𝚈 𝚄𝚂𝙸𝙽𝙶 𝚃𝙷𝚂 𝙵𝙴𝙰𝚃𝚄𝚁𝙴...</b>

<b>👍𝙲𝙾𝙼𝙼𝙰𝙽𝙳.!</b>
<b>/carbon ›› 𝚁𝙴𝙿𝙻𝚈 𝚃𝙾 𝙰𝙽𝚈 𝚃𝙴𝚇𝚃 𝙼𝙴𝚂𝚂𝙰𝙶𝙴</b>

<b>𝚆𝙾𝚁𝙺𝚂 𝙾𝙽 𝙱𝙾𝚃𝙷 𝙶𝚁𝙾𝚄𝙿 𝙰𝙽𝙳 𝙿𝙼</b>
<b>𝙲𝚁𝙴𝙳𝙸𝚃𝚂 ›› @malayalamvibe"""
