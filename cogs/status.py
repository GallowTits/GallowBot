import discord
from discord.ext import commands
import asyncio
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import settings

class Status(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        statuses = settings.bot.status.statuses
        pos = 0
        
        while True:
            await self.bot.change_presence(activity=discord.Game(name=statuses[pos]))
            if settings.bot.status.change_interval != 0:
                await asyncio.sleep(settings.bot.status.change_interval)
                pos += 1
                if pos == len(statuses):
                    pos = 0
            else:
                break

def setup(client):
    client.add_cog(Status(client))