import pyshorteners
import asyncio
import requests
from .. import loader, utils
@loader.tds
class ClanTagsMod(loader.Module):
    """LinkShorter"""
    strings = {'name': 'LinkShorter'}

    async def lscmd(self, message):
        """Используй .ls <url>"""
        text = utils.get_args_raw(message)
        if not text:
            await message.edit(f"There is no argument")
            return
        await message.edit("Wait...")
        try:
            s = pyshorteners.Shortener()
            await message.edit(s.tinyurl.short(text))
        except Exception as x:
            await message.edit(f'Error:{x}\n\nEnter the link to the site with https://')
    async def lsdcmd(self, message):
        """Используй .lsd <сокращенная ссылка>"""
        text = utils.get_args_raw(message)
        if not text:
            await message.edit(f"There is no argument")
            return
        await message.edit("Wait...")
        try:
            s = pyshorteners.Shortener()
            await message.edit(s.tinyurl.expand(text))
        except Exception as x:
            await message.edit(f"Error:{x}")
