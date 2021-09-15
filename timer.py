import asyncio
from asyncio import sleep, gather
from .. import loader, utils
import time
import random

@loader.tds
class ClanTagsMod(loader.Module):
	"""RTimer"""
	strings = {'name': 'RTimer'}

	async def timercmd(self, message):
		"""Используй .timer <time(in sec)> <comment>"""
		args = utils.get_args_raw(message)
		reply = await message.get_reply_message()
		time = int(args.split(' ', 2)[0])
		zxc = str(args.split(' ', 2)[1])
		try:
			await message.edit(f"✅Timer Enable on {time} sec.✅\n✅With comment {zxc}✅")
			await sleep(time)
			await message.client.send_message(message.to_id,f"📛The timer is out!📛\n📛Comment: {zxc}📛")
		except Exception as f:
			await message.edit(f"<b>Error:\n{f}</b>")