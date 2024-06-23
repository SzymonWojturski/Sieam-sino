import discord
from discord.ext import commands


class TestCog2(commands.Cog):
    def __init__(self,bot):
        self.bot=bot

    @commands.command()
    async def ping(self,ctx):
        await ctx.channel.send("sieam")

async def setup(bot):
    await bot.add_cog(TestCog2(bot))