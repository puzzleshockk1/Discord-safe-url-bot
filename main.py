import discord
from subprocess import call
import time
import os
from discord.ext import commands

print("Starting...")

client = discord.Client()
TOKEN = os.getenv("TOKEN")

@client.event
async def on_ready():
  await client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name="Netybot"))

print("-------------------------------")
print("Your Bot is online")
print("Made by Puzzle_Shock1")
print("Need help? Join our discord server: https://discord.gg/TT9gUCKVnb")
print("-------------------------------")

#Dangerous links
keywords = [
    "17ebook.co", "aladel.net", "bpwhamburgorchardpark.org", "clicnews.com",
    "iplogger", "2no.co", "yip.su", "ipgrabber", "iplis.ru", "02ip.ru", "partpicker.shop","sportshub.bar", "locations.quest", "lovebird.guru", "trulove.guru", "dateing.club", "shrekis.life", "headshot.monster", "gaming-at-my.best", "progaming.monster", "yourmy.monster", "imageshare.best", "screenshot.best", "gamingfun.me", "catsnthing.com", "catsnthings.fun", "yt118.com", "stock888.cn", "curiouscat.club", "joinmy.site", "fortnitechat.site", "fortnight.space", "freegiftcards.co", "leancoding.co", "grabify.link", "youareanidiot.org", "fantasticfilms.ru", "gardensrestaurantandcatering.com", "clicnews.com", "ginedis.com", "dfwdiesel.net", "seksburada.net", "tathli.com", "teamclouds.com", "xnescat.info", "magic4you.nu", "Homicide.igarape.org.br", "Goodbyewarden.com", "kekma.net", "Worldsbirthsanddeaths.com", "ctbto.org", "www.ps3cfw.com", ".zip"
, ".gq", ".work", ".review", ".kim"] 


@client.event
async def on_message(message):
  if 'https://' or 'http://' in message.content:
     for i in range(len(keywords)):
        if keywords[i] in message.content.lower():
            for j in range(1):
                print(f"{message.author} sent dangerous message in {message.channel} from {message.guild}")
                await message.delete()
                embed = discord.Embed(title="!!Dangerous link detected!!", color=discord.Color.red())
                embed.set_footer(text=f"{message.author} sent dangerous link in {message.channel}     Dangerous link: {message.content}")
                await message.channel.send(embed=embed)




client.run('YOUR BOT TOKEN HERE')
