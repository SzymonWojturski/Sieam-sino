import discord
from discord.ext import commands


class TestCog2(commands.Cog):
    def __init__(self,bot):
        self.bot=bot

    @commands.Cog.listener()
    async def siema(self,msg):
        await msg.channel.send("ema")