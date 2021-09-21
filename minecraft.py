import asyncio
from .. import loader, utils
import time
import random
import requests
from mcstatus import MinecraftServer

@loader.tds
class ClanTagsMod(loader.Module):
	"""Minecraft"""
	strings = {'name': 'Minecraft'}

	async def servercheckkcmd(self, message):
		await message.edit("Checking server ")
		code = utils.get_args_raw(message)
		if not code:
			await message.edit(f"<b>No arg</b>")
			return
		try:
			server = MinecraftServer.lookup(code)
			status = server.status()
			await message.edit(("The server has {0} players and replied in {1} ms".format(status.players.online, status.latency)))
		except Exception as f:
				await message.edit(f"<b>Error {code}</b> \n" + f'')