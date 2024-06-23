import asyncio
import inspect

import sensitive_data as sd
import discord
from discord.ext import commands
import importlib

intents=discord.Intents.all()
intents.message_content=True
intents.members=True

bot=commands.Bot(command_prefix="$",intents=intents,help_command=None,)
def to_snake_case(name):
    return "".join([ch if ch.lower()==ch else f"_{ch.lower()}" for ch in name])
async def id_admin(ctx):
    if ctx.author.id in [sd.MACIEK_ID,sd.SZYWOJ_ID]:
        return True
    else:
        await ctx.send("You are not allowed to use this command")
        return False
@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Game(name=sd.BOT_STATUS))
    print("Ready")
@bot.event
async def on_message(msg):
    await bot.process_commands(msg)
@bot.command()
@commands.check(id_admin)
async def info(ctx):
    await ctx.send(bot.extensions.keys())
@bot.command()
@commands.check(id_admin)
async def load(ctx,name):
    try:
        await bot.load_extension(f'cogs.{name}')
    except discord.ext.commands.ExtensionAlreadyLoaded:
        await ctx.send(f"{name} already loaded")
    except discord.ext.commands.ExtensionNotFound:
        await ctx.send(f"{name} not found")
    else:
        await ctx.send(f"{name} loaded")
@bot.command()
@commands.check(id_admin)
async def unload(ctx,name):
    try:
        await bot.unload_extension(f'cogs.{name}')
    except discord.ext.commands.ExtensionNotLoaded:
        await ctx.send(f"{name} already unloaded or not found")
    else:
        await ctx.send(f"{name} unloaded")
    # ExtensionNotLoaded
async def _load_all():
    module = importlib.import_module(f"cogs")
    classes = inspect.getmembers(module, inspect.isclass)
    classes = [cls[0] for cls in classes]
    names = tuple(bot.extensions.keys())
    for cls in classes:
        if not f"cogs.{cls}" in names:
            await bot.load_extension(f"cogs.{cls}")
@bot.command()
@commands.check(id_admin)
async def load_all(ctx):
    await _load_all()
    names = tuple(bot.extensions.keys())
    await ctx.send(f"Actual cogs: {' '.join([name[5:] for name in names]) }")

@bot.command()
@commands.check(id_admin)
async def unload_all(ctx):
    names=tuple(bot.extensions.keys())
    for ext_name in names:
        await bot.unload_extension(ext_name)
    names = tuple(bot.extensions.keys())
    await ctx.send(f"Actual cogs: {' '.join([name[5:] for name in names]) }")
@bot.command()
@commands.check(id_admin)
async def reload_all(ctx):
    names=tuple(bot.extensions.keys())
    for ext_name in names:
        await bot.reload_extension(ext_name)
    names = tuple(bot.extensions.keys())
    await ctx.send(f"Actual cogs: {' '.join([name[5:] for name in names]) }")

asyncio.run(_load_all())
bot.run(sd.TOKEN)