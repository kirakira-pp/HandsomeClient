#! /usr/bin/python3
# So handsome :)
import discord
import os
from dotenv import load_dotenv
import re
import random
import requests
import time
from hentai import Hentai, Format, Utils, Sort, Option, Tag

class handsomeClient(discord.Client):
	def nhentai_recommander(self):
		# sage time (10s)
		if time.time() - self.nhentai_timestamp < 10:
			return f'還不可以色色<:fap:906177947193475153><:fap:906177947193475153>'
		
		# update sage time
		self.nhentai_timestamp = time.time()

		# return random nh url
		MAX_TRY = 1 
		for test in range(MAX_TRY):
			try:
				rPage = random.randrange(30)+1
				results = Utils.search_by_query('chinese uploaded:<30d -males -tomgirl', page=rPage, sort=Sort.PopularYear)
				print('[debug] rPage:', rPage)


				return random.choice(list(results)).url
			except Exception as e:
				if test == MAX_TRY-1:
					return str(e) + " Please try again later."
				# print("Page", rPage, "return 404. Random again.")


	async def fap(self, message):
		random.seed(time.time())
		await self.nsfw_channel.send(self.nhentai_recommander())


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
				string = f"<:so:906144664522981386> " + random.choice(self.emos)
				await message.channel.send(string)

		# Ehentai Recommander
		elif fap:
			await self.fap(message)

	async def on_ready(self):
		print("[Info] Start the handsome_discord_robot! HANDSOME!")
		print("[Info] Now login as", self.user)
		print("[Info] Setting variables")

		# for general
		self.emos = ["<:handsome:906144446280785960>"]*80+["<:horny:933021525597093928>"]*5+["<:fe:908710806739365890>"]*5+["<:zhai:908710875182018650>"]*5+["<:fap:906177947193475153>"]+["<:shen:906145037681827850>"]+["<:self_fella:908703249723449354>"]+["<:penibokki:906180179397840896>"]

		# for fap
		self.nhentai_timestamp = 0
		self.nsfw_channel = self.get_channel(int(os.getenv('NSFW_CHANNEL_ID')))
		random.seed(time.time())
		

def main():
	load_dotenv()
	tmp = handsomeClient()
	tmp.run(os.getenv('DISCORD_BOT_TOKEN'))


if __name__ == '__main__':
	main()
