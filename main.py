import discord
from discord.ext import commands
import os, random
import requests
from model import get_class
# from model import get_class
from PIL import Image, ImageOps

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'Zalogowaliśmy się jako {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Cześć! Jestem botem, {bot.user}!')

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)
    
@bot.command()
async def check(ctx):
    files = ctx.message.attachments 
    if files:
        for file in files:  
            file_name = file.filename
            await file.save(f'./{file_name}')
            image = Image.open(f'./{file_name}') 
            await ctx.send(get_class(image, 'keras_model.h5', 'labels.txt'))
    else:
        await ctx.send('Załącz plik do sprawdzenia')
        
    
        

    

bot.run("")