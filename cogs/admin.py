import discord
from discord.ext import commands
import settings
import sys

async def is_owner(ctx):
    return ctx.author.id in settings.bot.admins


class Admin(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.check(is_owner)
    @commands.command()
    async def shutdown(self, ctx):
        print("Shutting down...")
        await self.bot.logout()

def setup(client):
    client.add_cog(Admin(client))