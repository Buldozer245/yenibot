import discord
import os
import random
from discord.ext import commands
from fonksiyonlar import *

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'{bot.user} olarak giriş yaptık')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Merhaba {bot.user}! Ben bir botum!')

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)

@bot.command()
async def money(ctx):
    await ctx.send(yazi_tura())

@bot.command()
async def sifre(ctx, sifre_uzunluğu = 15):
    await ctx.send(gen_pass(sifre_uzunluğu))

@bot.command()
async def sayi(ctx, sayi_uzunluğu = 3):
    await ctx.send(gen_pas(sayi_uzunluğu))

@bot.command()
async def thebestmusic(ctx):
    await ctx.send("https://youtu.be/dQw4w9WgXcQ?t=42")

@bot.command()
async def randomemoji(ctx):
    await ctx.send(emoji_olusturucu())    

@bot.command()
async def mem(ctx):
    with open('m1l3\\m1l4\\images\\TR1y5bql.png', 'rb') as f:
        # Dönüştürülen Discord kütüphane dosyasını bu değişkende saklayalım!
        picture = discord.File(f)
   # Daha sonra bu dosyayı bir parametre olarak gönderebiliriz!
    await ctx.send(file=picture)

@bot.command()
async def rastgelemem(ctx):
    resimler = os.listdir("m1l3\\m1l4\\images")
    resim = random.choice(resimler)

    # Dosya adını bir değişkenden bu şekilde değiştirebilirsiniz!
    with open(f'm1l3\\m1l4\\images\\/{resim}', 'rb') as f:
            picture = discord.File(f)


   # Daha sonra bu dosyayı bir parametre olarak gönderebiliriz!
    await ctx.send(file=picture)

oneriler = [
    "turmepa benim hedef kitlem.tuzlu suyun tatlı suya çevirme. bütün dünyadaki arıtma makinelerini birleştirip mega arıtma makinesi yapıp tuzlu suyun yüzde 50sini tatlı suya çevirmek.kalan balıkları da yeriz.",
    "nasa benim hedef kitlem. uzaydaki çöpler benim sorunum. uzay mekikleri arasına balık ağı dizilir. daha sonra çöpler toplanır ve mekiklerle dünyaya indirilir. Bu sayede çok fazla miktarda bir geri dönüşüm sağladık."]


@bot.command()
async def banafikirver(ctx):
    oneri = random.choice(oneriler)
    await ctx.send(oneri)
    





bot.run("")
print(os.listdir('m1l3\\m1l4'))
