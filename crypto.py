
import asyncio
from .. import loader, utils
import time
import random
import requests
import json
from lxml import etree

@loader.tds
class ClanTagsMod(loader.Module):
	"""CryptoInfo"""
	strings = {'name': 'CryptoInfo'}

	async def cpricecmd(self, message):
		"""Используй .cprice <короткое имя криптовалюты>"""
		text = utils.get_args_raw(message)
		if not text:
			await message.edit(f"There is no argument.")
			return
		await message.edit("Wait...")
		try:
			xml_response = etree.fromstring(requests.get("http://www.cbr.ru/scripts/XML_daily.asp").text.encode("1251"))
			curs = xml_response.find("Valute[@ID='R01235']/Value").text
			curs = float(curs.replace(',', '.'))
			url = f"https://api.bittrex.com/api/v1.1/public/getticker?market=USD-{text}"
			eururl = f"https://api.bittrex.com/api/v1.1/public/getticker?market=EUR-{text}"
			j = requests.get(url)
			jf = requests.get(eururl)
			data = json.loads(j.text)
			dataj = json.loads(jf.text)
			eurprice = dataj['result']['Ask']
			price = data['result']['Ask']
			oldprice = data['result']['Last']
			if price < oldprice:
				x = "📉"
			elif price > oldprice:
				x = "📈"
			else:
				x = "📊"
			alo = float(price) * float(curs)
			alo = float(round(alo, 2))
			btcproce = f"💰 Price {text} {x}: \n\n🇺🇸USD: {price}$\n" + str("🇷🇺RUB: ") + str(alo) + str("₽") + f"\n🇪🇺EUR: {eurprice} €\nCurrent courses are taken from api.bittrex.com"
			await message.edit(btcproce)
		except:
			await message.edit("<b>Error in getting the price.</b>")