import inspect

import sensitive_data as sd
import discord
from discord.ext import commands
import importlib

intents=discord.Intents.all()
intents.message_content=True
intents.members=True

bot=commands.Bot(command_prefix="$",intents=intents,help_command=None,)
# bot.description="While gambling, you can only lose 100% of your money, but you can win 20000%. Do the math"

@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Game(name=sd.BOT_STATUS))
    print("Ready")

# def to_snake_case(input):
#     return input[0].lower() + ''.join(f'_{ch.lower()}' if ch.isupper() else ch for ch in input[1:])
@bot.command()
async def load_cog(ctx,name):
    try:
        module = importlib.import_module(f"cogs")
        InputCog = getattr(module, name)
        await bot.add_cog(InputCog(bot))
    except AttributeError as e:
        await ctx.send(f"No Cog named '{e.name}'")
    except discord.ClientException as e:
        await ctx.send(*e.args)
    else:
        await ctx.send(f"Cog named '{name}' loaded")

@bot.command()
async def unload_cog(ctx,name):
    try:
        module = importlib.import_module(f"cogs")
        InputCog = getattr(module, name) #throws error from time to time
        if bot.get_cog(name):
            await bot.remove_cog(name)
            await ctx.send(f"Cog named '{name}' unloaded")
        else:
            await ctx.send(f"Cog named '{name}' already unloaded")
    except AttributeError as e:
        await ctx.send(f"No Cog named '{e.name}'")


async def _unload_all_cogs():
    bot_cogs = dict(bot.cogs)
    for cog in bot_cogs:
        await bot.remove_cog(cog)
async def _load_all_cogs():
    module = importlib.import_module(f"cogs")
    classes = inspect.getmembers(module, inspect.isclass)
    classes = [cls[0] for cls in classes]
    for cls in classes:
        InputCog = getattr(module, cls)
        await bot.add_cog(InputCog(bot))
@bot.command()
async def reload_cogs(ctx):
    await _unload_all_cogs()
    await _load_all_cogs()
    bot_cogs = dict(bot.cogs)
    await ctx.send(f"Current cogs: {', '.join(bot_cogs.keys())}")

@bot.command()
async def unload_cogs(ctx):
    await _unload_all_cogs()
    bot_cogs = dict(bot.cogs)
    await ctx.send(f"Current cogs: {', '.join(bot_cogs.keys())}")
@bot.command()
async def curr_cogs(ctx):
    bot_cogs = dict(bot.cogs)
    await ctx.send(f"Current cogs: {', '.join(bot_cogs.keys())}")

bot.run(sd.TOKEN)
