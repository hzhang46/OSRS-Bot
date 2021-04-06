import discord
from Highscores import get_total_xp
import config

client = discord.Client()

TOKEN = config.TOKEN

@client.event
async def on_ready():
    print("We have logged in as {0.user}".format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$totalxp'):
        username = message.content.split(" ")[1]
        xp = get_total_xp(username)
        await message.channel.send(username+" has "+str(int(xp))+" Total XP")

client.run(TOKEN)
