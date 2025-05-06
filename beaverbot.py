import random
import discord
from discord.ext import commands

#biggestbeaver/lopy here, i hope you enjoy the bot!

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="$", intents=intents)

@bot.command()
async def random_kat(context):
    random_nummer = random.randint(1, 10000)
    await context.send(f"https://cataas.com/cat?{random_nummer}")

@bot.command()
async def random_hond(context):
    random_nummer = random.randint(1, 10000)
    await context.send(f"https://place.dog/600/600?{random_nummer}")
@bot.event
async def on_ready():
    print(f'we are logged in as {bot.user}')

@bot.event
async def on_message(message):
    await bot.process_commands(message)

    if message.author == bot.user: 
        return

    if message.content.lower() == 'ping':
        await message.channel.send('pong')
    else:
        await message.channel.send(f"you said {message.content}")

@bot.event
async def on_message_delete(message):
    await message.channel.send(f"message by {message.author} was just deleted msg: {message.content}")




discord_token = "INSERT PRIVATE OAUTH2 DISCORD TOKEN"
bot.run(discord_token)
