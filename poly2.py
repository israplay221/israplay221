import discord
from discord.ext import commands
import random
import os
import requests
import json
import aiohttp
import webbrowser

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Hola, soy {bot.user}!')

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)

@bot.command()
async def suma(ctx, n1:int, n2:int):
    await ctx.send(f"La suma de {n1} con {n2} es {n1 + n2}")

@bot.command()
async def repeat(ctx, times: int, content='repeating...'):
    """Repeats a message multiple times."""
    for i in range(times):
        await ctx.send(content)

@bot.command()
async def limpiar(ctx):
    await ctx.channel.purge()
    await ctx.send("Mensajes eliminados", delete_after = 3)

@bot.command()
async def meme(ctx):
        with open('memes/meme.png', 'rb') as f:
        # ¡Vamos a almacenar el archivo de la biblioteca Discord convertido en esta variable!
            picture = discord.File(f)
        # A continuación, podemos enviar este archivo como parámetro.
        await ctx.send(file=picture)

@bot.command()
async def meme1(ctx):
        with open('memes/meme1.png', 'rb') as f:
        # ¡Vamos a almacenar el archivo de la biblioteca Discord convertido en esta variable!
            picture = discord.File(f)
        # A continuación, podemos enviar este archivo como parámetro.
        await ctx.send(file=picture)

@bot.command()
async def meme2(ctx):
        with open('memes/meme2.png', 'rb') as f:
        # ¡Vamos a almacenar el archivo de la biblioteca Discord convertido en esta variable!
            picture = discord.File(f)
        # A continuación, podemos enviar este archivo como parámetro.
        await ctx.send(file=picture)

@bot.command()
async def memes(ctx):
        imagenes = os.listdir('memes')
        with open(f'memes/{random.choice(imagenes)}', 'rb') as f:
            picture = discord.File(f)
        # A continuación, podemos enviar este archivo como parámetro.
        await ctx.send(file=picture)

def get_duck_image_url():    
    url = 'https://random-d.uk/api/random'
    res = requests.get(url)
    data = res.json()
    return data['url']


@bot.command('duck')
async def duck(ctx):
    '''Una vez que llamamos al comando duck, 
    el programa llama a la función get_duck_image_url'''
    image_url = get_duck_image_url()
    await ctx.send(image_url)

@bot.command()
async def poke(ctx,arg):
    try:
        pokemon = arg.split(" ",1)[0].lower()
        result = requests.get("https://pokeapi.co/api/v2/pokemon/"+pokemon)
        if result.text == "Not Found":
            await ctx.send("Pokemon no encontrado")
        else:
            image_url = result.json()["sprites"]["front_default"]
            print(image_url)
            await ctx.send(image_url)
    except Exception as e:
        print("Error:", e)
@poke.error
async def error_type(ctx,error):
    if isinstance(error,commands.errors.MissingRequiredArgument):
        await ctx.send("Tienes que darme un pokemon")

@bot.command('dog')
async def dog(ctx):
    async with aiohttp.ClientSession() as cd:
        async with cd.get("https://dog.ceo/api/breeds/image/random") as r:
            raw = await r.text()
            dogspic = json.loads(raw)

            embed = discord.Embed()

            embed.set_image(url=dogspic['message'])

            await ctx.send(embed=embed)

   
bot.run("TOKEN")
