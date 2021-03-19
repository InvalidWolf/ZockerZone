import asyncio
import discord
from discord.ext import commands


class Knast(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.has_role(714057716355694633)
    async def knast(self, ctx, member: discord.Member):
        for role in member.roles[1:]:
            await asyncio.sleep(0.15)
            await member.remove_roles(role)
        knastrole = discord.utils.get(ctx.guild.roles, id=752977315838951484)
        await member.add_roles(knastrole)
        await ctx.send(f'Der User **{member.mention}** wurde geknastet!')

    @commands.command()
    @commands.has_role(714057716355694633)
    async def unknast(self, ctx, member: discord.Member):
        knastrole1 = discord.utils.get(ctx.guild.roles, id=718181392131031050)
        knastrole2 = discord.utils.get(ctx.guild.roles, id=771060201314320394)
        knastrole3 = discord.utils.get(ctx.guild.roles, id=789237195469750332)
        knastrole4 = discord.utils.get(ctx.guild.roles, id=789849737557835806)
        knastrole5 = discord.utils.get(ctx.guild.roles, id=755017131229315113)
        knastrole6 = discord.utils.get(ctx.guild.roles, id=717076831551094814)
        role1 = discord.utils.get(ctx.guild.roles, id=752977315838951484)
        await member.add_roles(knastrole1)
        await member.add_roles(knastrole2)
        await member.add_roles(knastrole3)
        await member.add_roles(knastrole4)
        await member.add_roles(knastrole5)
        await member.add_roles(knastrole6)
        await member.remove_roles(role1)
        await ctx.send(f'Der User **{member.mention}** wurde entknastet!')


def setup(bot):
    bot.add_cog(Knast(bot))
