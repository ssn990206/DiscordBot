import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.typing = False
intents.presences = False

bot=commands.Bot(command_prefix=']',intents=intents)

@bot.event
async def on_ready():
    print(">> bot is online <<")

bot.run("MTAxNTA5MjczOTAyNjcxODcyMA.GCWmmA.vY0fTMrPdbMNiAbui-an-H0_IOTTndN6OrKedc")