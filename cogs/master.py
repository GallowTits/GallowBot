import discord
from discord.ext import commands
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import settings

class Master(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self._last_member = None
    
    @commands.Cog.listener()
    async def on_ready(self):
        print(f"\nLOGGED IN")
        print("="*25)
        print(f"ID = {self.bot.user.id}")
        print(f"NAME = {self.bot.user.name}#{self.bot.user.discriminator}")
        print(f"PING = {round(self.bot.latency*1000)}ms")
        print(f"GUILDS = {len(self.bot.guilds)}")
        print("="*25)
    
    @commands.Cog.listener()
    async def on_message(self,message):
        if message.author.id != self.bot.user.id:
            print(f"MESSAGE")

    @commands.Cog.listener()
    async def on_message_edit(self,before, after):
        print(f"EDIT")

    @commands.command()
    async def ping(self,ctx):
        ping = round(self.bot.latency*1000)
        if ping > 250:
            c = 0xff0008
        elif ping > 150:
            c = 0xffae00
        else:
            c = 0x00ff15
        embed = discord.Embed(
            color=c)
        embed.add_field(name="Ping", value=f"{ping}ms", inline=False)
        embed.set_footer(text=f"Requested by {ctx.message.author.name}#{ctx.message.author.discriminator}")
        await ctx.message.channel.send(embed=embed)

    @commands.command()
    async def info(self,ctx):
        embed = discord.Embed(title="Info")
        embed.add_field(name="Version", value=settings.bot.version, inline=False)
        embed.add_field(name="Prefixes", value=settings.bot.prefixes, inline=False)

        embed.add_field(name="Developer", value="github.com/mirandaniel")
        embed.set_footer(text=f"Requested by {ctx.message.author.name}#{ctx.message.author.discriminator}")
        await ctx.message.channel.send(embed=embed)

    @commands.command()
    async def help(self,ctx):
        pass
def setup(client):
    client.add_cog(Master(client))