from random import randint
from discord.ext import commands


class TestCog(commands.Cog):
    def __init__(self,bot):
        self.bot=bot

    @commands.command()
    async def coinflip(self,ctx):
        if randint(0,1)==0:
            await ctx.send("Wygrałeś")
        else:
            await ctx.send("Przegrałeś")

async def setup(bot):
    await bot.add_cog(TestCog(bot))