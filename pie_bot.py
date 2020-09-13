import discord
import os

client = discord.Client(activity=discord.Game("with Banana Pie!"))

@client.event
async def on_ready():
    print('Banana Pie cooked! Ready to be posted!'.format(client))

@client.event
async def on_message(message):
    if message.content == 'bp!help':
        await message.channel.send("Type bp!pie for some banana pie! You can also visit my website for some banana pie! https://banana-pie.herokuapp.com/")
    if message.content == 'bp!pie':
        await message.channel.send(f'Here\'s your pie {message.author.mention}!\nhttps://img.buzzfeed.com/video-api-prod/assets/f78b2d95fc904dfb908e21862da36534/YT_THUMB.jpg')

client.run(os.environ['BOT_TOKEN'])
