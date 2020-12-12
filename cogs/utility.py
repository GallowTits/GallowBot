import discord
from discord.ext import commands
import sys

class Mod(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self._last_member = None

    @commands.command()
    async def calc(self, ctx, i):
        await ctx.message.channel.send(eval(i))

    @commands.command()
    async def avatar(self, ctx, member: discord.Member=None):
        if not member:
            member = ctx.message.author
        await ctx.message.channel.send(member.avatar_url)

def setup(client):
    client.add_cog(Mod(client))