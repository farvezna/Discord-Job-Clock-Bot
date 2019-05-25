import discord
from discord.ext import commands
import datetime

bot = commands.Bot(command_prefix='$')

employeeDict = {}

@bot.event
async def on_ready():
    #TODO: add users as keys and allow command to update Name--hide users but add name to spreadsheet
    print("Bot is ready and let's goooo!")
    await bot.change_presence(activity=discord.Game(name="at work but getting paid!"))

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    if message.content == 'ping':
        timestamp = datetime.datetime.now()
        with open("datalog.csv", 'a') as fout:
            fout.write(timestamp.strftime('%x'))
        await message.channel.send('pong: **' + timestamp.strftime('%x') + "**")
        await message.channel.send('**' + timestamp.strftime('%X') + '**')

bot.run(TOKEN)