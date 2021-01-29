import discord
from discord.ext import commands
"""Imports"""


class FunCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self._last_member = None

    @commands.command(name='smile')
    async def smile(self, ctx):
        await ctx.send(':smiley:')


""""Now you have commands to replace client!"""


def setup(bot):
    bot.add_cog(FunCog(bot))


"""Sets up the cog and adds it"""
