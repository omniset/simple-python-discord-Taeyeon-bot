import discord
from discord.ext import commands
import datetime
import random

intents = discord.Intents.all()
bot = commands.Bot(command_prefix='+', case_insensitive=True, help_command=None, description="MnD first discord bot", intens=intens)
bot.remove_command('help')#this make the basic help command been deleted

@bot.command()
async def taeng(ctx):
    await ctx.send("https://gfycat.com/acidicidlebluebreastedkookaburra")

#images link i use pinterest for the pic link because idk how to put the pic from the same directory but diferent file 
images = [ 'https://i.pinimg.com/564x/79/b2/a2/79b2a260ff97f1fa2dd26b6c1db789e1.jpg',
           'https://i.pinimg.com/564x/00/6a/10/006a10e15603d904726a531bc0a24227.jpg',
           'https://i.pinimg.com/564x/f4/38/3a/f4383a2c78a0435415bb9ee0ead25aeb.jpg',
           'https://i.pinimg.com/564x/24/f7/30/24f73093f77baf13a96835c8c89dcfe9.jpg',
         ]
secret_drop = [ 'https://cdn.discordapp.com/attachments/871739555022258208/941538212969598986/card.gif', #i stole this card i think they already making the v2 bot and make a new card design 
                'https://cdn.discordapp.com/attachments/871739555022258208/941538920691290162/card.gif', #not sure tho but i dont care since it's for my personal use 
                'https://cdn.discordapp.com/attachments/871739555022258208/941530437732429844/card.gif',
                'https://cdn.discordapp.com/attachments/871739555022258208/941555183379427338/card.gif',
                'https://cdn.discordapp.com/attachments/871739555022258208/941555238027006032/card.gif',
              ]

#custom help command to make a better help command
@bot.command()
async def help(ctx):
     embed = discord.Embed(title="help", description="first bot by MnD", color=discord.Color.green())
     embed.add_field(name="+drop",value='you can drop a new card using this command',inline=True)
     embed.add_field(name="+taeyeon",value='showing you taeyeon fan wiki',inline=True)
     embed.add_field(name="+sum",value='you can use this command for math sum function',inline=True)
     embed.add_field(name="+info", value='showing server info',inline=True)
     embed.add_field(name="+pdrop", value='premium drop only for user that already has subcription', inline=True)
     embed.add_field(name="+pradita", value='nohing i just using this for my e-learning portal lmao, this bot used to be private', inline=True)
     embed.add_field(name="+source", value='bot source code', inline=True)

     embed.set_thumbnail(url="https://c.tenor.com/a7NRALTBb8EAAAAC/angai313-snsd.gif")
    
     await ctx.send(embed=embed)#to make it pop up in the chat 

#drop command 
@bot.command()
async def drop(ctx):
    embed = discord.Embed(
    title="Drop",
    colour=discord.Colour(0x7289DA),
    description=f"{ctx.author.mention} you just drop a new card")

    embed.set_image(url=(random.choice(images)))
    embed.set_footer(text=f"{ctx.message.guild.name}")
    embed.timestamp = datetime.datetime.utcnow()

    await ctx.send( embed = embed)

#taeyeon wiki command
@bot.command()
async def taeyeon(ctx):
    await ctx.send("https://kpop.fandom.com/wiki/Taeyeon")

#premium drop only for subcribed user 
@bot.command()
async def pdrop(ctx):
    embed = discord.Embed(
    title="premium drop",colour=discord.Colour(000000),
    description=f"{ctx.author.mention} you got a new premium drop")

    embed.set_image(url=(random.choice(secret_drop)))
    embed.set_footer(text=f"{ctx.message.guild.name}")
    embed.timestamp = datetime.datetime.utcnow()

    await ctx.send(embed = embed)

#sum command 
@bot.command()
async def sum(ctx, numOne: int, numTwo: int):
    await ctx.send(numOne + numTwo)

#pradita website command 
@bot.command()
async def pradita(ctx):
    embed = discord.Embed(
    title="Pradita university",  color=discord.Color.orange(),
    description=f"{ctx.author.mention}Pradita University powered by Summarecon")

    embed.add_field(name="Pradita Web Site", value='https://www.pradita.ac.id')
    embed.set_thumbnail(url="https://i.pinimg.com/564x/90/25/d6/9025d6b6955084a95709ea3231832466.jpg")
    
    await ctx.send(embed=embed)

@bot.command()
async def source(ctx):
    await ctx.send("https://github.com/omniset/simple-python-discord-Taeyeon-bot/blob/main/main.py")

#under maintenance 
@bot.command()
async def info(ctx):
    embed = discord.Embed(title=f"{ctx.guild.name}", description="first bot by MnD", timestamp=datetime.datetime.utcnow(), color=discord.Color.blue())
    embed.add_field(name="Server created at", value=f"{ctx.guild.created_at}")
    embed.add_field(name="Server Owner", value=f"{ctx.guild.owner}")
    embed.add_field(name="Server Region", value=f"{ctx.guild.region}")
    embed.add_field(name="Server ID", value=f"{ctx.guild.id}")

    # embed.set_thumbnail(url=f"{ctx.guild.icon}") 
    embed.set_thumbnail(url="https://i.pinimg.com/564x/98/e3/db/98e3db2384d568cd30e578f5310520c0.jpg")#pinterest 

    await ctx.send(embed=embed)

# Events bot status 
@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name="Yunjin - Rise o_ur glass"))
    print('Taengoo is ready to roll')

#auto respond on someone message 
@bot.listen('on_message') 
async def stuff(message):

    if message.content.startswith("ur mom"):
        msg = await message.channel.send("no u")
        #await asyncio.sleep(10) auto delete
        #await msg.delete()

@bot.listen('on_message') 
async def stuff(message):

    if message.content.startswith("mnd"):
        msg = await message.channel.send("if im not responding in the next 5 minute i might be sleeping or going somewhere, try again in few hours have a nice day or night")
        #await asyncio.sleep(10) (auto delete)
        #await msg.delete()
        
@bot.listen('on_message')
async def stuff(message):

    if message.content.startswith("omni art"):
        await message.channel.send('https://www.youtube.com/channel/UCkz7mi8DKABGOdDS80Z-byg')#my own youtube channel 

#bot token 
bot.run('ur bot token')
