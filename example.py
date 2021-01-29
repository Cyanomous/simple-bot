import discord
from discord.ext import commands
"""Imports"""


def get_prefix(bot, message):
    prefixes = ['c', 'C']
    if not message.guild:
        return '?'
    return commands.when_mentioned_or(*prefixes)(bot, message)


initial_extensions = ['cogs.fun',
                      'cogs.utility', ]
"""List of cogs"""

if __name__ == '__main__':
    for extension in initial_extensions:
        bot.load_extension(extension)
"""Loads your cogs"""

bot = commands.Bot(command_prefix=get_prefix, description='A secret bot!')


@bot.event
async def on_ready():
    print(f'We have logged in as {client.user}'.format(client))

bot.run(TOKEN)
"""TOKEN should be your bot's token"""
