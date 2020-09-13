import discord
import os
import aiohttp
import io

client = discord.Client(activity=discord.Game("with Banana Pie!"))

banana_url = 'https://img.buzzfeed.com/video-api-prod/assets/f78b2d95fc904dfb908e21862da36534/YT_THUMB.jpg'

@client.event
async def on_ready():
    print('Banana Pie cooked! Ready to be posted!'.format(client))

@client.event
async def on_message(message):
    if message.content == 'bp!help':
        await message.channel.send("Type bp!pie for some banana pie! You can also visit my website for some banana pie! https://banana-pie.herokuapp.com/")
    if message.content == 'bp!pie':
        async with aiohttp.ClientSession() as session:
            async with session.get(banana_url) as resp:
                if resp.status != 200:
                    return await channel.send('Banana Pie failed to cook. :-(')
                data = io.BytesIO(await resp.read())
                await message.channel.send(f'Here\'s your pie {message.author.mention}!', file=discord.File(data, 'banana_pie.jpg'))

client.run(os.environ['BOT_TOKEN'])
