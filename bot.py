import discord
from discord.ext import commands, tasks
from check import check
from options import DISCORD_KEY, DISCORD_CHANNEL

# make the intents read messages, members, and guilds 
intents = discord.Intents.default()
intents.members = True
intents.messages = True
client = commands.Bot(command_prefix='!', intents=intents)
 
@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.command()
async def delete(ctx):
    await ctx.channel.purge(limit=100)

amt = 0

@tasks.loop(seconds=10)
async def check_channel():
    global amt
    if amt == 0:    # lazy implementation of skipping first check
        amt += 1    # otherwise resoults in a instant crash :)
        return

    channel_info = check()
    if not channel_info:
        return

    channel = client.get_channel(int(DISCORD_CHANNEL))
    if channel_info:
        await channel.send(channel_info)
        print("Message sent.")

check_channel.start()

# Run the bot client
client.run(DISCORD_KEY)