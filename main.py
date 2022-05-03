from http import client
from tokenize import Token
import discord
from yaml import safe_load
from pathlib import Path

bot = discord.Client()

@bot.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

config = safe_load(Path("config.yml").read_text())

token = config["token"]

bot.run(Token)
