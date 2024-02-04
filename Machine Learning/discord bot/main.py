import discord
from discord.ext import commands
from discord import FFmpegPCMAudio
import requests
import yt_dlp as youtube_dl
import json
from discord import member
from discord.ext.commands import has_permissions, MissingPermissions

intents = discord.Intents.all()
client = commands.Bot(command_prefix= '!', intents=intents)

@client.event
async def on_ready(): # this function will be executed whenever the bot is ready
    print("The bot is now ready for use")
    print("-----------------------------")


@client.command()

async def test(ctx):
    #myid = '<@921723267050524702>'
    await ctx.send('CUET CDI')
    


@client.command()
async def chat(ctx):
    await ctx.send('chat korar manush nai?')

@client.command()
async def on_message(ctx):
    await ctx.send('ok!')

@client.command()
async def off_message(ctx):
    await ctx.send('mara kha')

@client.command(name="নৌকা", aliases=["hi"])
async def gg(ctx):
    await ctx.send("জিতবে আমার নৌকা")
    channel = client.get_channel(1050264893217046559)
    voice = await channel.connect()
    source = FFmpegPCMAudio('E:/song.mp3')
    player = voice.play(source)

@client.event
async def on_member_join(member):
    await member.send('Test')

@client.command(name= "joke", aliases= ["jokes"])
async def joke(ctx):
    url = "https://dad-jokes.p.rapidapi.com/random/joke"
    headers = {
        "X-RapidAPI-Key": "648f4052b9msh10ea555ef62bf7ap154c5ejsn469d80ae4d59",
        "X-RapidAPI-Host": "dad-jokes.p.rapidapi.com"
    }
    response = requests.get(url, headers=headers)

    if response.ok:
        joke = response.json()['body'][0]
        await ctx.send(joke['setup'] + "\n" + joke['punchline'])
    

@client.command(pass_context = True)
async def join_voice(ctx):
    if(ctx.author.voice):
        channel = ctx.message.author.voice.channel
        voice = await channel.connect()
        source = FFmpegPCMAudio('E:/song.mp3')
        player = voice.play(source)
    else:
        await ctx.send("You are not in a voice channel!")

@client.command(pass_context = True)
async def leave(ctx):
    if(ctx.voice_client):
        await ctx.guild.voice_client.disconnect()
    else:
        await ctx.send("You are not in a voice channel!")


@client.command(pass_context = True)
async def pause(ctx):
    voice = discord.utils.get(client.voice_clients, guild = ctx.guild)
    if(voice.is_playing()):
        voice.pause()
        await ctx.send("Song Paused")
    else:
        await ctx.send("No song is currently playing")

        
@client.command(pass_context = True)
async def resume(ctx):
    voice = discord.utils.get(client.voice_clients, guild = ctx.guild)
    if(voice.is_paused()):
        voice.resume()
        await ctx.send("Song Resumed")
    else:
        await ctx.send("Already playing")

@client.command(pass_context = True)
async def stop(ctx):
    voice = discord.utils.get(client.voice_clients, guild = ctx.guild)
    if(voice.is_playing()):
        voice.stop()
        # await ctx.guild.voice_client.disconnect()
        await ctx.send("Song Stopped")
    else:
        await ctx.send("What should I stop? LOL")

@client.command()
@has_permissions(kick_members = True)
async def kick(ctx, member: discord.Member, *, reason = None):
    if(ctx.message.author.id == 735784181145272320):
        await member.kick(reason = reason)
        await ctx.send(f'{member} has been kicked!')
    else:
        await ctx.send("Only Sojib can do it")


client.run('MTE3NjkzODA2ODE2MzQ0ODkyMw.Gg_noR.PKrkEGy9KsbcvVsOPVd11ep7meUYThwZ7sVjkk')

# invite link = https://discord.com/api/oauth2/authorize?client_id=1176938068163448923&permissions=8&scope=bot

# token = MTE3NjkzODA2ODE2MzQ0ODkyMw.G9-8Eh.TZ3YhT4kxRY8Oh0pwHyNxyY0JDddoISt9mJfhM