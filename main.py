import os
import discord
from discord.ext import commands


bot = commands.AutoShardedBot(command_prefix='!', case_insensitive=True, help_command=None, intents=discord.Intents.all())

admins = [497767671392108554]

for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        bot.load_extension(f'cogs.{filename[:-3]}')

bot.run('')
