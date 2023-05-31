import discord
from discord.ext import commands, tasks
from check import check
from twitchcheck import isLive

key = ''

# make the intents read messages, members, and guilds 
intents = discord.Intents.default()
intents.members = True
intents.messages = True
client = commands.Bot(command_prefix='!', intents=intents)
 
@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.command()
async def get_channel(ctx):
    print(ctx.channel)
    return

@client.command()
async def delete(ctx):
    await ctx.channel.purge(limit=100)

@tasks.loop(seconds=10)
async def check_channel():
    channel_info = check()
    if channel_info is False:
        return
    channel = client.get_channel()
    await channel.send(channel_info)
    print("Message sent.")

check_channel.start()

# Run the bot client
client.run(key)