import asyncio
import time
import random
import os
from .. import loader, utils

@loader.tds
class ClanTagsMod(loader.Module):
	"""Casino"""
	strings = {'name': 'RRandom'}

	async def rdcmd(self, message):
		"""Use .rd <reply> <arg>"""
		reply = await message.get_reply_message()
		arg = utils.get_args_raw(message)
		if not arg:
			number = float(10)
		if not reply:
			await message.edit("⚡️Throwing the dice")
			time.sleep(1)
			random2 = random.randint(0, number)
			await message.edit(f"Выпавшее число:{random2}")
			return
		number = float(arg)
		zxctext = reply.sender.first_name
		await message.edit(f"⚡️Throwing the dice")
		time.sleep(1)
		random1 = random.randint(0, number)
		random2 = random.randint(0, number)
		if random1 > random2:
			await message.edit(f"Ваше число: {random1}\nЧисло игрока {zxctext}: {random2}\n✅Вы победили!")
		elif random1 < random2:
			await message.edit(f"Ваше число: {random1}\nЧисло игрока {zxctext}: {random2}\n✅Победил игрок {zxctext}!")
		elif random1 == random2:
			await message.edit(f"Ваше число: {random1}\nЧисло игрока {zxctext}: {random2}\n🔥Вы оба соснули хуйца))))")

