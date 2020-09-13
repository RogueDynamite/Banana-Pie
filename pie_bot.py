import discord
import os

client = discord.Client(status="Baking Some Banana Pie!")

@client.event
async def on_ready():
    print('Banana Pie cooked! Ready to be posted!'.format(client))

@client.event
async def on_message(message):
    if message.content == 'bp!pie':
        await message.channel.send('Here\'s your pie {message.author.mention}!\nhttps://img.buzzfeed.com/video-api-prod/assets/f78b2d95fc904dfb908e21862da36534/YT_THUMB.jpg')

client.run(os.environ['BOT_TOKEN'])
