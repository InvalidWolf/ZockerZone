import asyncio
import discord
from discord.ext import commands


class Bankick(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.has_role(714057716355694633)
    async def ban(self, ctx, member: discord.Member):
        await member.ban()
        await ctx.send(f'Der User **{member.mention}** wrude gebannt!')

    @commands.command()
    @commands.has_role(714057716355694633)
    async def kick(self, ctx, member: discord.Member):
        await member.kick()
        await ctx.send(f'Der User **{member.mention}** wrude gekickt!')


def setup(bot):
    bot.add_cog(Bankick(bot))
