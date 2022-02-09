#! /usr/bin/python3
# So handsome :)
import discord
import os
from dotenv import load_dotenv
import re
import random
import requests
import time
from NHentai import NHentai

class handsomeClient(discord.Client):
	def nhentai_recommander(self, who):
		print("who:", who)

		# sage time (10s)
		if time.time() - self.ehentai_timestamp < 10:
			return f'還不可以色色<:fap:906177947193475153><:fap:906177947193475153>'
		
		# update sage time
		self.ehentai_timestamp = time.time()

		# spider
		# headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36"}
		# html = requests.get(f'https://e-hentai.org/?f_cats=1021&f_search=big+breasts+chinese&page={random.randint(1, 101)}', headers)
		# information = re.search('The ban expires in ([0-9]+) minutes and ([0-9]+) seconds', html.text)

		# re_url = re.findall('https://e-hentai.org/g/[0-9]+/[0-9a-z]+/', html.text)
		# IF_DEBUG
		# print(html.status_code, html.text)
		# print(re_url)

		# if not re_url:
		# 	return f'太色所以被 ban 了<:fap:906177947193475153><:fap:906177947193475153>'
		# 	# return f'太色所以被 ban 了，你還要{information[1]}分{information[2]}秒才可以<:fap:906177947193475153><:fap:906177947193475153>'
		# else:
		# 	return random.choice(re_url)
		nhentai = NHentai()
		random_doujin: Doujin = nhentai.get_random()

		return random_doujin.url


	async def getJasonHsu(self, message):
		match = re.search("((許|<:hsu:906145037371457537>)"
						   "(傑|<:jie:906145039883857942>)"
						   "(盛|<:shen:906145037681827850>))"
						  , message.replace(" ", ""))
		if match:
			return match

		match = re.search('<@[!&]?([0-9]+)>', message)
		if match:
			member_id = int(match[1])
			user = await self.fetch_user(member_id)

			if user and user.name == 'JasonHsu':
				return match

	async def on_message(self, message):
		if message.author == self.user:
			print(message.content)
			await message.add_reaction(random.choice(self.emos))
			await message.add_reaction(random.choice(self.emos))
			return

		print('[Chat]', message.author.display_name,' : ', message.content)
		
		fap = re.search('尻尻', message.content)

		# Handsome Bot
		if await self.getJasonHsu(message.content):
			if 'Jason' in message.author.display_name:
				await message.channel.send("<:self_fella:908703249723449354>")
			else:
				string = f"{user.mention} <:so:906144664522981386> " + random.choice(self.emos)
				await message.channel.send(string)

		# Ehentai Recommander
		elif fap:
			if 'Jason' in message.author.display_name:
				await message.channel.send(self.nhentai_recommander('futa'))
			else:
				await message.channel.send(self.nhentai_recommander(""))

	async def on_ready(self):
		print("[Info] Start the handsome_discord_robot! HANDSOME!")
		print("[Info] Now login as", self.user)
		print("[Info] Setting variables")
		self.emos = ["<:handsome:906144446280785960>"]*80+["<:horny:933021525597093928>"]*5+["<:fe:908710806739365890>"]*5+["<:zhai:908710875182018650>"]*5+["<:fap:906177947193475153>"]+["<:shen:906145037681827850>"]+["<:self_fella:908703249723449354>"]+["<:penibokki:906180179397840896>"]
		self.ehentai_timestamp = 0
		

def main():
	load_dotenv()
	tmp = handsomeClient()
	tmp.run(os.getenv('DISCORD_BOT_TOKEN'))


if __name__ == '__main__':
	main()