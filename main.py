import discord
from discord.ext import commands
intents = discord.Intents.default()
intents.typing = False
intents.presences = False

bot=commands.Bot(command_prefix=']')

@bot.event
async def on_ready():
    print(">> bot is online <<")

bot.run("MTAxNTA5MjczOTAyNjcxODcyMA.GhVVjk.NNOEUTH43vSGkhJq2KM4Jv3XyeFuaWONau27kM")