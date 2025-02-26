
#TOKEN = "MTM0Mzg3MTgyODU1NjUxMzI5MA.GeN_tv.n8a8hrTVepLu9TTFy7QiepoPfMajyYg6SWVKZA"  # test bot 
# test bot 

import discord
import os
from discord.ext import commands
from discord import app_commands

# โหลด Token จาก .env
TOKEN = ("MTM0Mzg3MTgyODU1NjUxMzI5MA.GeN_tv.n8a8hrTVepLu9TTFy7QiepoPfMajyYg6SWVKZA")

# ตั้งค่าบอทและเปิดใช้ Intents
intents = discord.Intents.default()
intents.typing = True
intents.presences = False
intents.message_content = True  # เปิดให้บอทอ่านข้อความได้
intents.members = True  # เปิดให้บอทเข้าถึงข้อมูลสมาชิก

bot = commands.Bot(command_prefix='-', intents=intents)

@bot.event
async def on_ready():
    print(f"✅ บอททำงานแล้ว! ชื่อ: {bot.user}")
    synced = await bot.tree.sync()
    print(f"{len(synced)} command(s)")

@bot.command()
async def hi(ctx):
    await ctx.send("hallo!")

@bot.event
async def on_member_join(member):
    channel = bot.get_channel(1343919465623982201)
    text=f"welcome to sever test bot, {member.mention}!"

    emmbed = discord.Embed(title = 'welcome to the sever!', description = text, color = 0x66FFFF)
    await channel.send(text)
    await channel.send(embed= emmbed)

@bot.event
async def on_member_remove(member):
    channel = bot.get_channel(1343919484066599006)
    text=f"we will remember , {member.mention}!"
    await channel.send(text)

@bot.event
async def on_message(message):
    message_sever = message.content
    if message_sever == 'hallo':
        await message.channel.send("hi i'm Peter how do I help?")
    
    elif message_sever == 'hi' :
        await message.channel.send("hello sir "+str(message.author.name))
    
    await bot.process_commands(message)

@bot.command()
async def setup(ctx):
    await ctx.send(f"not now {ctx.author.name}!")

@bot.tree.command(name='setup', description= 'all setup in this bot' )
async def start(interaction):
    await interaction.response.send_message('hallo is me bot discord')

@bot.tree.command(name='name')
@app_commands.describe(name = "what you name?")
async def namecommand(interaction, name : str):
    await interaction.response.send_message(f"hi sir {name}!")




bot.run(TOKEN)  # ใช้ Tok:en อย่างปลอดภัย
