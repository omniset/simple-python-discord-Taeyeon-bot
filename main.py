from async_timeout import asyncio
import discord 
from discord.ext import commands
import datetime
import random

intents = discord.Intents.all()
intents.members = True
intents.typing = True
intents.presences = True

bot = commands.Bot(command_prefix='+', case_insensitive=True, help_command=None, description="MnD first discord bot", intents=intents)
bot.remove_command('help')#removing basic "help" command

@bot.command()
async def taeng(ctx):
    await ctx.send("https://gfycat.com/acidicidlebluebreastedkookaburra")

#images of the card
#using pinterest 
images = [ 'https://i.pinimg.com/564x/79/b2/a2/79b2a260ff97f1fa2dd26b6c1db789e1.jpg',
           'https://i.pinimg.com/564x/00/6a/10/006a10e15603d904726a531bc0a24227.jpg',
           'https://i.pinimg.com/564x/f4/38/3a/f4383a2c78a0435415bb9ee0ead25aeb.jpg',
           'https://i.pinimg.com/564x/24/f7/30/24f73093f77baf13a96835c8c89dcfe9.jpg',
           'https://i.pinimg.com/564x/03/cf/99/03cf995cf1e6980ef5599e9de4429458.jpg',
           'https://i.pinimg.com/564x/fd/f3/02/fdf302ff849d2737a523b6660afd74b9.jpg'
         ]
premium_drop = [ 'https://cdn.discordapp.com/attachments/871739555022258208/941538212969598986/card.gif', 
                'https://cdn.discordapp.com/attachments/871739555022258208/941538920691290162/card.gif', 
                'https://cdn.discordapp.com/attachments/871739555022258208/941530437732429844/card.gif',
                'https://cdn.discordapp.com/attachments/871739555022258208/941555183379427338/card.gif',
                'https://cdn.discordapp.com/attachments/871739555022258208/941555238027006032/card.gif',
              ]

#help command
@bot.command() 
async def help(ctx):
     embed = discord.Embed(title="help", description="MnD personal bot", color=discord.Color.green())
     embed.add_field(name="+drop",value='you can get a new card using this command',inline=True)
     embed.add_field(name="+taeyeon",value='showing you kim taeyeon wiki website',inline=True)
     embed.add_field(name="+sum",value='just type which number u want to sum, example: 20 20',inline=True)
     embed.add_field(name="+serverinfo", value='showing server info',inline=True)
     embed.add_field(name="+pdrop", value='premium drop only for user that already has subscription', inline=True)
     embed.add_field(name="+pradita", value='nohing i just using this for my e-learning portal lmao.', inline=True)
     embed.add_field(name="+source", value='bot source code', inline=True)
     embed.add_field(name="auto respond word list", value='absen, mnd, ommni art', inline=True)

     embed.set_thumbnail(url="https://c.tenor.com/a7NRALTBb8EAAAAC/angai313-snsd.gif")
     await ctx.send(embed=embed)

#basic drop command
@bot.command()
async def drop(ctx):
    embed = discord.Embed(
        title="Drop",
        colour=discord.Colour(0x7289DA),
        description=f"{ctx.author.mention} you just dropped a new card"
    )

    url = random.choice(images)
    embed.set_image(url=url)
    embed.set_footer(text=ctx.guild.name)
    embed.timestamp = datetime.datetime.utcnow()

    if url == "https://i.pinimg.com/564x/fd/f3/02/fdf302ff849d2737a523b6660afd74b9.jpg":
        specific_embed = discord.Embed(
            title="You just got a special card, Congrats!!",
            colour=discord.Colour(0xFF0000),
            description="Special card is rare don't forgot to consider keeping it :)"
        )
        specific_embed.set_image(url=url)
        specific_embed.set_footer(text=ctx.guild.name)
        specific_embed.timestamp = datetime.datetime.utcnow()
        await ctx.send(embed=specific_embed)
    else:
        await ctx.send(embed=embed)

#about taeyeon wiki command
@bot.command()
async def taeyeon(ctx):
    await ctx.send("https://kpop.fandom.com/wiki/Taeyeon")

#premium drop only for subcribed user 
@bot.command()
async def pdrop(ctx):
    embed = discord.Embed(
    title="premium drop",colour=discord.Colour(000000),
    description=f"{ctx.author.mention} you just drop a premium card")

    embed.set_image(url=(random.choice(premium_drop)))
    embed.set_footer(text=f"{ctx.message.guild.name}")
    embed.timestamp = datetime.datetime.utcnow()

    await ctx.send(embed = embed)

#sum command
@bot.command()
async def sum(ctx, numOne: int, numTwo: int):
    await ctx.send(numOne + numTwo)

#pradita university website command 
@bot.command()
async def pradita(ctx):
    embed = discord.Embed(
    title="Pradita university",  color=discord.Color.orange(),
    description=f"{ctx.author.mention}Pradita University powered by summarecon")

    embed.add_field(name="Pradita Web Site", value='https://www.pradita.ac.id')
    embed.set_thumbnail(url="https://i.pinimg.com/564x/90/25/d6/9025d6b6955084a95709ea3231832466.jpg")
    
    await ctx.send(embed=embed)

#bot source code
@bot.command()
async def source(ctx):
    await ctx.send("https://github.com/omniset/simple-python-discord-Taeyeon-bot/blob/main/main.py")

#fixed server info command
@bot.command()
async def serverinfo(ctx):
    embed = discord.Embed(title = f"{ctx.guild.name} Info",  description="first bot by MnD", timestamp=datetime.datetime.utcnow(), color=discord.Color.blue())
    embed.add_field(name = "🆔Server ID", value = f"{ctx.guild.id}", inline = True)
    embed.add_field(name = "📆Created On", value = ctx.guild.created_at.strftime("%b %d %Y"), inline = True)
    embed.add_field(name = "👥Members", value = f"{ctx.guild.member_count} Members", inline = True)
    embed.add_field(name = '👑Owner', value = f"{ctx.guild.owner}", inline = True)

    # embed.set_thumbnail(url=f"{ctx.guild.icon}") 
    embed.set_thumbnail(url="https://i.pinimg.com/564x/98/e3/db/98e3db2384d568cd30e578f5310520c0.jpg")

    await ctx.send(embed=embed)

# Events/bot status
@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name="Yunjin - Rise o_ur glass"))
    print('Taengoo is ready to roll')

@bot.event
async def on_message(message):
    if bot.user.mentioned_in(message):
        await message.channel.send('Hello Manusia Bangun dan ratapi kehidupan kalian')
    await bot.process_commands(message)

#auto respond message      
@bot.listen('on_message') 
async def stuff(message):
    if message.content.lower().startswith("absen"):
        msg = await message.channel.send("https://siakad.pradita.ac.id/mahasiswa/daftar_hadir")

@bot.listen('on_message') 
async def stuff(message):

    if message.content.lower().startswith("babi"):
        msg = await message.channel.send("muka kau kayak babi")
        #await asyncio.sleep(10) (auto delete)
        #await msg.delete()

@bot.listen('on message')
async def stuff(message):

    if message.content.lower().startwith("ngi mun ngai"):
        await message.channel.send("ngai mun masa?")

@bot.listen('on message')
async def stuff(message):

    if message.content.lower().startwith("pepepopo"):
        await message.channel.send("pepepopo in action")

#bot token / application token
bot.run('ur bot token')
