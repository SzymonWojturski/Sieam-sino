import sensitive_data as sd
import discord
from discord.ext import commands

intents=discord.Intents.all()
intents.message_content=True
intents.members=True

bot=commands.Bot(command_prefix="$",intents=intents,help_command=None)

@bot.event
async def on_ready():
    print("zalogowany")

bot.run(sd.TOKEN)