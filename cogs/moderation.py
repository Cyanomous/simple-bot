import discord
from discord.ext import commands
"""Imports"""


class ModerationCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self._last_member = None

    @commands.command(aliases=['add'], pass_context=True)
    @commands.has_permissions(manage_roles=True)
    async def addrole(self, ctx, user: discord.Member, *, role: discord.Role):
        await user.add_roles(role)
        await ctx.send(f"Hey {ctx.author.name}, I have sucesfully given {user.name} the role {role.name}!")


"""Adds a role"""


def setup(bot):
    bot.add_cog(ModerationCog(bot))
    """Set up"""
