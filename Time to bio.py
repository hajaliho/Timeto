import asyncio , telethon , logging , time , random , os , html
from telethon import utils
from telethon import client
from telethon import events 
from telethon import TelegramClient
from telethon.events import NewMessage
from telethon.sync import TelegramClient
from telethon import functions, types
from telethon.tl.functions.photos import GetUserPhotosRequest
from telethon.tl.functions.users import GetFullUserRequest
from telethon.tl.types import MessageEntityMentionName
from telethon.utils import get_input_location
Download_path = './DOWNLOAD/'


api_id = 9641916
api_hash = 'bac3b20d4957929cf4b12ba05aa3e347'

client = TelegramClient('python' , api_id , api_hash)
client.start()

@client.on(events.NewMessage(pattern=r"\.edit (.*)", outgoing=True))
async def SAY(event):
    if event.fwd_from:
        return
    
    input_str = event.pattern_match.group(1)
    typing_symbol = "|"
    DELAY_BETWEEN_EDITS = 0.1
    previous_text = ""
    await event.edit(typing_symbol)
    await asyncio.sleep(DELAY_BETWEEN_EDITS)
    for character in input_str:
        previous_text = previous_text + "" + character
        typing_text = previous_text + "" + typing_symbol
        await event.edit(typing_text)
        await asyncio.sleep(DELAY_BETWEEN_EDITS)
        await event.edit(previous_text)
        await asyncio.sleep(DELAY_BETWEEN_EDITS)


import subprocess
from datetime import datetime
from gtts import gTTS

@client.on(events.NewMessage(pattern=".timebio"))  # pylint:disable=E0602
async def bioclock(event):
    if event.fwd_from:
        return
    while True:
        DMY = time.strftime("%d.%m.%Y")
        HM = time.strftime("%H:%M:%S")
        bio = f" {DMY} | {HM}"
        logger.info(bio)
        await event.edit('''complete''')
        try:
            await client(functions.account.UpdateProfileRequest(  # pylint:disable=E0602
                about=bio
            ))
        except FloodWaitError as ex:
            logger.warning(str(e))
            await asyncio.sleep(ex.seconds)
        # else:
            # logger.info(r.stringify())
            # await client.send_message(  # pylint:disable=E0602
            #     Config.PRIVATE_GROUP_BOT_API_ID,  # pylint:disable=E0602
            #     "Successfully Changed Profile Bio"
            # )
        await asyncio.sleep(DEL_TIME_OUT)    
asyncio.get_event_loop().run_forever()
client. run_until_disconnected()
