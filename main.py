import os
import discord
from discord.ext import commands


bot = commands.AutoShardedBot(command_prefix='!', case_insensitive=True, help_command=None, intents=discord.Intents.all())

admins = [497767671392108554]

for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        bot.load_extension(f'cogs.{filename[:-3]}')


@bot.command(aliases=['rla'])
async def reloadall(ctx):
    await ctx.message.delete()
    if ctx.author.id in admins:

        for dateiname in os.listdir('./fun'):
            if dateiname.endswith('.py'):
                bot.reload_extension(f'cogs.{dateiname[:-3]}')

        reload_em = discord.Embed(title=f'All cogs have been reloaded',
                                  color=0x007797)
        reload_em.set_author(name='Reload', icon_url='https://media.discordapp.net/attachments/808353707288428554/810922772589969458/loading.png')
        reload_em.set_footer(text=f'Requested by: {ctx.author.name}', icon_url=f'{ctx.author.avatar_url}')
        await ctx.send(embed=reload_em)


@bot.command(aliases=['rl'])
async def reload(ctx, cogname):
    await ctx.message.delete()
    if ctx.author.id in admins:
            bot.reload_extension(f'{cogname}')
            reload_em = discord.Embed(title=f'{cogname} has been reloaded',
                                      color=0x007797)
            reload_em.set_author(name='Reload', icon_url='https://media.discordapp.net/attachments/808353707288428554/810922772589969458/loading.png')
            reload_em.set_footer(text=f'Requested by: {ctx.author.name}', icon_url=f'{ctx.author.avatar_url}')
            await ctx.send(embed=reload_em)


@bot.command()
async def stopall(ctx):
    await ctx.message.delete()
    if ctx.author.id in admins:

        for dateiname in os.listdir('./cogs'):
            if dateiname.endswith('.py'):
                bot.unload_extension(f'cogs.{dateiname[:-3]}')

        em = discord.Embed(title=f"Alle Cogs have been stoped!!", color=discord.Colour.red())
        em.set_author(name='Stop', icon_url='https://media.discordapp.net/attachments/808353707288428554/810922772589969458/loading.png')
        em.set_footer(text=f'Requested by: {ctx.author.name}', icon_url=f'{ctx.author.avatar_url}')
        await ctx.send(embed=em)


@bot.command(aliases=['loadall'])
async def startall(ctx):
    await ctx.message.delete()
    if ctx.author.id in admins:

        for dateiname in os.listdir('./cogs'):
            if dateiname.endswith('.py'):
                bot.load_extension(f'cogs.{dateiname[:-3]}')

        em = discord.Embed(title=f"All cogs have been loaded")
        em.set_author(name='Load', icon_url='https://media.discordapp.net/attachments/808353707288428554/810922772589969458/loading.png')
        em.set_footer(text=f'Requested by: {ctx.author.name}', icon_url=f'{ctx.author.avatar_url}')
        await ctx.send(embed=em)


@bot.command(aliases=['load'])
async def start(ctx, arg_extention):
    await ctx.message.delete()
    if ctx.author.id in admins:
        bot.load_extension(f'{arg_extention}')
        em = discord.Embed(title=f"{arg_extention} has been loaded!")
        em.set_author(name='Load', icon_url='https://media.discordapp.net/attachments/808353707288428554/810922772589969458/loading.png')
        em.set_footer(text=f'Requested by: {ctx.author.name}', icon_url=f'{ctx.author.avatar_url}')
        await ctx.send(embed=em)


@bot.command()
async def stop(ctx, arg_extention):
    await ctx.message.delete()
    if ctx.author.id in admins:
        bot.unload_extension(f'{arg_extention}')
        em = discord.Embed(title=f"{arg_extention} has been stoped!")
        em.set_author(name='Stop', icon_url='https://media.discordapp.net/attachments/808353707288428554/810922772589969458/loading.png')
        em.set_footer(text=f'Requested by: {ctx.author.name}', icon_url=f'{ctx.author.avatar_url}')
        await ctx.send(embed=em)

bot.run('')
