import discord
import asyncio
import random
import os

#import module
from discord.ext import commands
from datetime import datetime, timedelta
from discord.utils import get #edit
from discord import FFmpegPCMAudio
from youtube_dl import YoutubeDL
from song import songAPI

from dotenv import load_dotenv #add
load_dotenv()
token = os.getenv('TOKEN')

message_lastseen = datetime.now()
message2_lastseen = datetime.now()

bot = commands.Bot(command_prefix='+', help_command=None)


aboutSong = songAPI()

#bot online
@bot.event 
async def on_ready():
    print(f"Logged in as {bot.user}")

@bot.command()
async def test(ctx, *, par):
    await ctx.channel.send("You typed {0}".format(par))

@bot.command()
async def help(ctx):
    emBed = discord.Embed(title="ลุงพล bot help", description =" All available bot command", color=0x42f5a7)
    emBed.add_field(name="+help", value = "Get help command", inline=True)
    emBed.add_field(name="+play", value = "Play a music with Youtube link", inline=True)
    emBed.add_field(name="+poll", value = "Get a poll for voting", inline=True)
    emBed.set_thumbnail(url='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSRkqVrVWhIcZ4ahKLDtziqL1zt84oZsho70MhzHMtNM8nZ8jq3fkauHbBoK6Co9ebH43A&usqp=CAU')
    emBed.set_image(url='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTbksTx4PKiVXVsGpJlzwNQl2s2WrX0R-MHcg&usqp=CAU')
    emBed.set_author(name="Dome", icon_url="https://www.freeiconspng.com/thumbs/human-icon-png/human-icon-png-png-20.png")
    emBed.set_footer(text ="ลุงพล บอท")

    await ctx.channel.send(embed=emBed)

@bot.command()
async def schedule(ctx):
    emBed = discord.Embed(title="Class schedule", color=0xf0ffff)
    emBed.set_image(url='https://cdn-icons-png.flaticon.com/512/470/470326.png')
    await ctx.channel.send(embed=emBed)

#reminder
@bot.command()
async def remind(ctx, time, *, task):
    #+remind 1m Play games
    def convert(time):
        pos = ['s', 'm', 'h', 'd']
        #set time to list
        time_dict = {"s": 1, "m": 60, "h": 3600, "d": 3600*24}
        #match unit and sec
        unit = time[-1]

        if unit not in pos:
            return -1
        try:
            val = int(time[:-1])
        except:
            return -2
        
        return val * time_dict[unit]
    
    convert_time = convert(time)
    times = convert_time
    half_time = convert_time/2
    quater_time = half_time/2

    #quater
    qday = quater_time // (24 * 3600)
 
    quater_time = quater_time % (24 * 3600)
    qhour = quater_time // 3600
 
    quater_time %= 3600
    qminutes = quater_time // 60
 
    quater_time %= 60
    qseconds = quater_time

    #half
    hday = half_time // (24 * 3600)
 
    half_time = half_time % (24 * 3600)
    hhour = half_time // 3600
 
    half_time %= 3600
    hminutes = half_time // 60
 
    half_time %= 60
    hseconds = half_time

    #full
    day = convert_time // (24 * 3600)

    convert_time = convert_time % (24 * 3600)
    hour = convert_time // 3600
 
    convert_time %= 3600
    minutes = convert_time // 60
 
    convert_time %= 60
    seconds = convert_time

    # return "%d:%02d:%02d" % (hour, minutes, seconds)


    if convert_time == -1:
        await ctx.send("You didn't answer time correctly")
        return

    if convert_time == -2:
        await ctx.send("The time must be an integer")
        return

    #reminder start
    emBed = discord.Embed(title="Lung Pol's Reminder Start", color=0x42f5a7)
    emBed.add_field(name="Reminder", value = task, inline=False)
    emBed.add_field(name="From", value = ctx.author.mention, inline=False)
    emBed.add_field(name="Time Left", value = f"{day} days {hour} hours {minutes} minutes {seconds} seconds", inline=False)  
    msg = await ctx.channel.send(embed=emBed)
    await msg.add_reaction('✅')

    #reminder idle
    await asyncio.sleep(times/2)
    emBed = discord.Embed(title="Lung Pol's Reminder", color=0x42f5a7)
    emBed.add_field(name="Reminder", value = task, inline=False)
    emBed.add_field(name="From", value = ctx.author.mention, inline=False)
    if hday ==0.0:
        hday = int(hday)
    if hhour ==0.0:
        hhour = int(hhour)
    if hminutes ==0.0:
        hminutes = int(hminutes)
    if hseconds ==0.0:
        hseconds = int(hseconds)
    emBed.add_field(name="Time Left", value = f"{hday} days {hhour} hours {hminutes} minutes {hseconds} seconds", inline=False)  
    msg = await ctx.channel.send(embed=emBed)
    await msg.add_reaction('✅')
    
    await asyncio.sleep(times/4)
    emBed = discord.Embed(title="Lung Pol's Reminder", color=0x42f5a7)
    emBed.add_field(name="Reminder", value = task, inline=False)
    emBed.add_field(name="From", value = ctx.author.mention, inline=False)
    if qday ==0.0:
        qday = int(qday)
    if qhour ==0.0:
        qhour = int(qhour)
    if qminutes ==0.0:
        qminutes = int(qminutes)
    if qseconds ==0.0:
        qseconds = int(qseconds)
    emBed.add_field(name="Time Left", value = f"{qday} days {qhour} hours {qminutes} minutes {qseconds} seconds", inline=False)  
    msg = await ctx.channel.send(embed=emBed)
    await msg.add_reaction('✅')
    
    #reminder finish
    await asyncio.sleep(times/4)
    emBed = discord.Embed(title="Lung Pol's Reminder Finish !", color=0x42f5a7)
    emBed.add_field(name="Reminder", value = task, inline=False)
    emBed.add_field(name="From", value = ctx.author.mention, inline=False)
    emBed.add_field(name="Time Left", value = f"0 days 0 hours 0 minutes 0 seconds", inline=False)  
    msg = await ctx.channel.send(embed=emBed)
    await msg.add_reaction('✅')

# polling
@bot.command()
async def poll(ctx, *, message):
    emBed = discord.Embed(title="Poll of the day", description=f"{message}", color=0x42f5a7)
    msg = await ctx.channel.send(embed=emBed)
    await msg.add_reaction('👍')
    await msg.add_reaction('👎')

#bot interact message
@bot.event
async def on_message(message):
    global message_lastseen, message2_lastseen
    if message.content == '!Hello':
        print(message.channel)
        await message.channel.send('Hello ' + str(message.author.name))
    
    elif message.content == '!bye':
        print(message.channel)
        await message.channel.send('Good bye')

    #introduce bot
    elif message.content == '!bot' and datetime.now() >= message_lastseen:
        message_lastseen = datetime.now() + timedelta(seconds=5)
        print(message.channel)
        await message.channel.send('I am '+ str(bot.user.name))
        print('{0} calling user when {1} and you can use {2}'. format(message.author.name, datetime.now(), message_lastseen))

    #introduce user
    elif message.content == '!user' and datetime.now() >= message2_lastseen:
        message2_lastseen = datetime.now() + timedelta(seconds=5)
        await message.channel.send('You are '+ str(message.author.name))

    elif message.content == '!logout':
        await bot.logout()

    await bot.process_commands(message)


@bot.command()
async def play(ctx, *, search: str):
    await aboutSong.play(ctx, search)

@bot.command()
async def stop(ctx):
    await aboutSong.stop(ctx)

@bot.command()
async def pause(ctx):
    await aboutSong.pause(ctx)

@bot.command()
async def resume(ctx):
    await aboutSong.resume(ctx)

@bot.command()
async def leave(ctx):
    await aboutSong.leave(ctx) #edit

@bot.command()
async def skip(ctx):
    await aboutSong.skip(ctx) #edit

@bot.command()
async def queueList(ctx):
    await aboutSong.queueList(ctx) #edit


bot.run(token)   



