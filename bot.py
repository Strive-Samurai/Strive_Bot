import discord
import os
import random

from discord.ext import commands


client = commands.Bot(command_prefix="!")
filtered_words = ["fuck"]
bro = ["bro","bruh","brother","sis","sister"]

@client.event
async def on_ready():
    print("The bot is ready")

@client.event
async def on_message(msg):
    for word in filtered_words:
        if word.lower() in msg.content.lower() :
            print(msg.author,"cursed")
            await msg.channel.send("You have been reported to the Leader of the server")
            await msg.delete()
    await client.process_commands(msg)



@client.command()
async def hi(ctx):
    await ctx.send("Hi")

@client.command(aliases=['d'])
@commands.has_permissions(manage_messages = True)
async def clear(ctx,amount=2):
    await ctx.channel.purge(limit = amount)

@client.command(aliases=['s'])
@commands.has_permissions(kick_members = True)
async def send(ctx,member : discord.Member):
    await member.send("Congrats you are officially a part of the Strive Clan")




client.run(os.environ['NzI0NjQyNDcwODkzMTkxMjYw.XxjJ4w.IwShBOZsJ3uRjWOOvhnjK7_SztE'])