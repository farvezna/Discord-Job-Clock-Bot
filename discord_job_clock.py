import discord
from discord.ext import commands

bot = commands.Bot(command_prefix='$')

@bot.event
async def on_ready():
    print("Bot is ready and let's goooo!")
    await bot.change_presence(activity=discord.Game(name="at work but getting paid!"))

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    if message.content == 'ping':
        await message.channel.send('pong')

bot.run(TOKEN)