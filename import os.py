import os
#import discord
import random
from discord.ext import commands
import json
import re

bot = commands.Bot(command_prefix='!')

with open(r'dict.json', encoding='utf-8') as json_file:
    dict_text = json.load(json_file)

text = dict_text['translate']

#async def bg_task(status):
    #channel1 = bot.get_channel(665954652373909554)
    #channel2 = bot.get_channel(697147782120734760)
    #if status.user.id_str == "910955212722114560" or status.user.id_str == "1260929358895562754":
       # await channel1.send(status.text)
       # await channel2.send(status.text)


class BotStreamListener():
    def on_status(self, status):
        print(status.text)
        #bot.loop.create_task(bg_task(status))

    def on_error(self, status_code):
        print(status_code)
        return True

    def on_exception(self, exception):
        return True


TOKEN = os.getenv('DISCORD_TOKEN')
#GUILD = os.getenv('DISCORD_GUILD')
#client = discord.Client()

#consumer_token = os.getenv("consumer_token")
#consumer_secret = os.getenv("consumer_secret")
#access_token = os.getenv("access_token")
#access_secret = os.getenv("access_secret")


botStreamListener = BotStreamListener()

@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Game("Drachengame"))

@bot.command()
async def ogerfy(ctx, *, arg):
    arg = arg.splitlines()
    text_bytes = b""

    for line in arg:
        trans = line
        for key, item in text.items():
            word = re.escape(key)
            trans = re.sub(word, lambda m: re.escape(random.choice(item)), trans)

        text_bytes += trans.encode() + b'\n'
    await ctx.send(text_bytes.decode("utf-8").replace("\\", ""))

@bot.command()
async def meddl(ctx):
    await ctx.send("MEDDL LOIDE!")

@bot.command()
async def ananas(ctx):
    await ctx.send(file=discord.File('ananas.jpg'))

@bot.command()
async def lüge(ctx):
    await ctx.send(random.choice(open("lügen.txt").readlines()))
    await ctx.send("- Rainer Winkler")

bot.run(TOKEN)
