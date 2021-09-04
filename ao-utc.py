import os
import discord
import asyncio
import datetime

client = discord.Client()

from dotenv import load_dotenv
load_dotenv()

token = os.getenv('DISCORD_TOKEN')

# Must be Voice Channels
timechannel = int(os.getenv('VC'))

@client.event
async def on_ready():
	print('We have logged in as {0.user}'.format(client))
	while True:
		now = datetime.datetime.now()
		time = now.strftime("%H:%M")
		await client.get_channel(timechannel).edit(name="UTC:"+time) # The channel gets changed here
		await asyncio.sleep(600)

client.run(token)
