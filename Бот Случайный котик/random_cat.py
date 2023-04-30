import discord
import logging
import requests


logger = logging.getLogger('discord')
logger.setLevel(logging.DEBUG)
handler = logging.StreamHandler()
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)

TOKEN = "BOT-TOKEN"


class YLBotClient(discord.Client):
    async def on_message(self, message):
        if message.author == self.user:
            return
        if "кот" in message.content.lower():
            response = requests.get('https://api.thecatapi.com/v1/images/search')
            json_object = response.json()
            await message.channel.send(json_object[0]['url'])
        elif "собак" in message.content.lower():
            response = requests.get('https://dog.ceo/api/breeds/image/random')
            json_object = response.json()
            await message.channel.send(json_object['message'])


intents = discord.Intents.default()
intents.members = True
intents.message_content = True
client = YLBotClient(intents=intents)
client.run(TOKEN)