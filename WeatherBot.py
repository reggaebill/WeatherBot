import discord

from discord.ext import commands

#TODO declare bot functions here

#token: MTM0MzM1NzIzMDMwNDU5MjAwNQ.GjVA4D.FtCugN4KGMi0JCFpPq-HQLSuHuag00DQCQRn0w

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='>', intents=intents)
client = discord.Client(intents=intents)



@client.event
async def on_message(message):
    if message.author == client.user:
        return

@client.event
async def on_ready():
    message.send('dis the bot')

@bot.command()
async def ping(message):
    await message.send('pong')

    #message.send('https://tenor.com/view/wouldnt-you-like-to-know-weather-boy-gif-15559185')
bot.run('MTM0MzM1NzIzMDMwNDU5MjAwNQ.GjVA4D.FtCugN4KGMi0JCFpPq-HQLSuHuag00DQCQRn0w')
