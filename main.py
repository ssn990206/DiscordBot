import discord
from discord.ext import commands

bot = commands.Bot(command_prefix='>')

@bot.event
async def on_ready():
    print(">> bot is online <<")

bot.run("MTAxNTA5MjczOTAyNjcxODcyMA.GbzzwN.sXbfMWPqpW-m36KGVWaXumGATfLuOQfNYPYQ5s")