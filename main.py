import discord
import os
from discord.ext import commands
from webserver import keepalive

client = commands.Bot(description = "OSTS Bot", command_prefix = "!")
client.remove_command('help')

@client.event
async def on_ready():
    await client.change_presence(activity=discord.Game(name='Open Sourcing Corporate Clash'))
    print("#################\n# Bot is online #\n#################")
    print("Running as: " + client.user.name)
    print("Discord.py: " + discord.__version__)
    print("Created by Cranky Supertoon#7376")

@client.command()
async def ping(ctx):
    await ctx.send('Pong!')

@client.command()
async def breathe(ctx):
  await ctx.send('https://tenor.com/view/spongebob-roast-boy-gif-5259347')

@client.command()
async def fellowship(ctx):
  await ctx.send('https://i.ibb.co/6ssChhj/unknown.png')

@client.command(aliases=['frizzy'])
async def ponyboy(ctx):
  await ctx.send('https://i.ibb.co/VLvF7ZM/unknown.png')

@client.command()
async def help(ctx):
  author = ctx.message.author
  
  embed = discord.Embed(
  color = discord.Color.orange()
  )

  embed.set_author(name="Commands:")
  embed.add_field(name="General", value="!help - Shows This Message\n!ping - Says Pong Back To You", inline=False)
  embed.add_field(name="Fun", value="!breathe - Shows a Breathing Meme\n!fellowship - Shows a Fellowship Meme\n!frizzy - Shows a Frizzy Meme")

  await ctx.send(author, embed=embed)

@client.event
async def on_message(message):
  if message.channel.id == 690334345344712817 or message.channel.id == 690334300830564548:
    await message.add_reaction('👍')
    await message.add_reaction('👎')
  await client.process_commands(message)

keepalive()
TOKEN = os.environ.get("DISCORD_BOT_SECRET")
client.run(TOKEN)
