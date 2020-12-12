import discord
from discord.ext import commands

class Staff(commands.Converter):
    async def convert(self, ctx, argument):
        argument = await commands.MemberConverter().convert(ctx, argument)
        permission = argument.guild_permissions.manage_messages
        if not permission:
            return argument
        else:
            return None

class Mod(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self._last_member = None

    @commands.command()
    @commands.has_permissions(ban_members=True)
    async def ban(self, ctx, user: Staff=None, reason=None):
        if not user:
            return await ctx.send("You must specify a user.")
        try:
            await ctx.guild.ban(user)
            await ctx.send(f"{user.mention} has been banned.")
        except discord.Forbidden:
            return await ctx.send("Access Denied, can't ban users that are above me.")

    @commands.command()
    @commands.has_permissions(kick_members=True)
    async def kick(self, ctx, user: Staff=None, reason=None):
        if not user:
            return await ctx.send("You must specify a user.")
        try:
            await ctx.guild.kick(user)
            await ctx.send(f"{user.mention} has been kicked.")
        except discord.Forbidden:
            return await ctx.send("Access Denied, can't kick users that are above me.")

    @commands.command()
    @commands.has_permissions(kick_members=True)
    async def purge(self, ctx, count: int):
        try:
            await ctx.channel.purge(limit=count)
            await ctx.channel.send(f"Deleted {count}", delete_after=2)
        except discord.Forbidden:
            return await ctx.send("Access Denied")

def setup(client):
    client.add_cog(Mod(client))