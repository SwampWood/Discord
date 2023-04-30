import asyncio
import time
import discord
from discord.ext import commands
import logging

logger = logging.getLogger('discord')
logger.setLevel(logging.DEBUG)
handler = logging.StreamHandler()
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)

intents = discord.Intents.default()
intents.members = True
intents.message_content = True
sl = {'hours': 3600, 'minutes': 60}


class Timer(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='set_timer')
    async def set_timer(self, ctx, hours, space1, minutes, space2):
        await ctx.send(f'The timer should start in {hours} {space1} {minutes} {space2}')
        await asyncio.sleep(int(hours) * sl[space1] + int(minutes) * sl[space2])
        await ctx.send('time X has come!')


bot = commands.Bot(command_prefix='', intents=intents)

TOKEN = "BOT-TOKEN"


async def main():
    await bot.add_cog(Timer(bot))
    await bot.start(TOKEN)


asyncio.run(main())