import asyncio
from telethon import events
from telethon.tl.types import ChannelParticipantsAdmins
from platform import uname
from userbot import ALIVE_NAME
from userbot.utils import admin_cmd


DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "Set ALIVE_NAME in config vars in Heroku"

#@command(outgoing=True, pattern="^.alive$")
@borg.on(admin_cmd(pattern=r"alive"))
async def amireallyalive(alive):
    """ For .alive command, check if the bot is running.  """
    await alive.edit("**xTPG A.I is online.** \n`Battery Status : ` **69%**\n\n"
                     f"`My Smartest Owner`: {DEFAULTUSER}\n\n"
                     "`Telethon version:` **6.9.0**\n`Python:` **3.7.3**\n"
                     "`Bot Community :` **xTPG**\n\n`I can do this all day.\n`"
                     "**Bot Creator:** @thePredatorGuy\n\n"
                     "**Following’s not really my style.**\n\n")
                     

