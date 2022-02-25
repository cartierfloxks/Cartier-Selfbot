import discord
from discord.ext import commands
from discord.ext.commands import *
from colorama import Fore, Style
from gtts import gTTS
import random
import datetime
import string
import asyncio
import json
import requests
import urllib
import os

def cls():
    os.system('cls')

class SELFBOT():
    __version__ = 1

with open("config.json") as f:
    j = json.load(f)
    token = j["token"]
    prefix = j["prefix"]
    deltimer = j["delete_timer"]

client = commands.Bot(command_prefix=prefix,self_bot=True)
client.remove_command("help")
pre = j["prefix"]

def logo():
    print(f"""{Fore.GREEN}
   ______           __  _          
  / ____/___ ______/ /_(_)__  _____
 / /   / __ `/ ___/ __/ / _ \/ ___/
/ /___/ /_/ / /  / /_/ /  __/ /    
\____/\__,_/_/   \__/_/\___/_/  
Dont skid or nigger

{Fore.GREEN}Logged In As: {Fore.RED}[{Fore.BLUE}{client.user.name}#{client.user.discriminator}{Fore.RED}]
{Fore.GREEN}Your ID is: {Fore.RED}[{Fore.BLUE}{client.user.id}{Fore.RED}]

{Fore.RED}----------CREDITS----------{Fore.BLUE}

{Fore.RED}{Fore.GREEN}Cartier SelfBot V{SELFBOT.__version__}, 50+ Commands
Made By Cartier{Fore.RED}

---------------------------{Fore.RESET}""")


# Events

@client.event
async def on_ready():
    cls()
    logo() 

@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        await ctx.send("`Missing Permissions, You're Missing The Permissions Necessary To Use This Command`")
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("`Missing Required Argument, Try Again?`")

# Other Shit

languages = {
    'hu': 'Hungarian, Hungary',
    'nl': 'Dutch, Netherlands',
    'no': 'Norwegian, Norway',
    'pl': 'Polish, Poland',
    'pt-BR': 'Portuguese, Brazilian, Brazil',
    'ro': 'Romanian, Romania',
    'fi': 'Finnish, Finland',
    'sv-SE': 'Swedish, Sweden',
    'vi': 'Vietnamese, Vietnam',
    'tr': 'Turkish, Turkey',
    'cs': 'Czech, Czechia, Czech Republic',
    'el': 'Greek, Greece',
    'bg': 'Bulgarian, Bulgaria',
    'ru': 'Russian, Russia',
    'uk': 'Ukranian, Ukraine',
    'th': 'Thai, Thailand',
    'zh-CN': 'Chinese, China',
    'ja': 'Japanese',
    'zh-TW': 'Chinese, Taiwan',
    'ko': 'Korean, Korea'
}

locales = [
    "da", "de",
    "en-GB", "en-US",
    "es-ES", "fr",
    "hr", "it",
    "lt", "hu",
    "nl", "no",
    "pl", "pt-BR",
    "ro", "fi",
    "sv-SE", "vi",
    "tr", "cs",
    "el", "bg",
    "ru", "uk",
    "th", "zh-CN",
    "ja", "zh-TW",
    "ko"
]

# Help Commands

@client.command()
async def help(ctx):
  await ctx.message.delete()
  await ctx.send(f"""```
Cartier Selfbot

{pre}mod - Shows moderation commands
{pre}misc - Shows miscellaneous commands
{pre}utility - Shows utility commands
{pre}status - Shows status commands
{pre}nuke - Shows nuke commands
{pre}personal - Shows personal commands
{pre}math - Shows math commands
{pre}server - Shows server commands
{pre}nsfw - Shows nsfw commands

Created by Cartier```""", delete_after=deltimer)

@client.command(aliases=["mod"])
async def moderation(ctx):
  await ctx.message.delete()
  await ctx.send(f"""```
Moderator Commands

{pre}ban - Bans the specified member
{pre}kick - Kicks the specified member
{pre}addrole - Adds a role to the specified member
{pre}takerole - Takes a role from the specified member
{pre}mute - Mutes the specified member
{pre}purge - Purges specified amount of messages

Created by Cartier```""", delete_after=deltimer)

@client.command()
async def status(ctx):
  await ctx.message.delete()
  await ctx.send(f"""```
Status Commands

{pre}game - Changes your status to a playing
{pre}stream - Changes your status to a streaming
{pre}listen - Changes your status to listening
{pre}watch - Changes your status to watching
{pre}clear - Resets your custom status

Created by Cartier```""", delete_after=deltimer)

@client.command(aliases=["util"])
async def utility(ctx):
  await ctx.message.delete()
  await ctx.send(f"""```
Utility Commands

{pre}avatar - Shows the specified members avatar
{pre}creator - Sends the tag of the creator
{pre}ping - Shows the clients latency
{pre}info - Shows some info on yourself
{pre}tts - Sends a message in text to speech
{pre}dumpemojis - Dumps all the emojis in a server

Created by Cartier```""", delete_after=deltimer)

@client.command(aliases=["misc"])
async def miscellaneous(ctx):
  await ctx.message.delete()
  await ctx.send(f"""```
Misc Commands

{pre}hug - Sends a gif of hugging the mentioned members/member
{pre}kiss - Sends a gif of kissing the mentioned members/member
{pre}spam - Spams the specified text
{pre}ascii - Sends the specified text in ascii
{pre}wizz - Fake wizzes a server
{pre}dmlist - Dms everyone on your DMs list a message
{pre}dmfriends - Dms all your friends a message

Created by Cartier```""", delete_after=deltimer)
  
@client.command()
async def nsfw(ctx):
  await ctx.message.delete()
  await ctx.send(f"""```
Nsfw Commands

{pre}hentai - Sends a hentai image
{pre}sex - Sends a sex image
{pre}tits - Sends a tit image
{pre}pussy - Sends a pussy image
{pre}dick - Sends a dick image

Created by Cartier```""", delete_after=deltimer)

@client.command()
async def nuke(ctx):
  await ctx.message.delete()
  await ctx.send(f"""```
Nuke Commands

{pre}ball - Bans all server members
{pre}kall - Kicks all server members
{pre}schan - Spams channels with desired name
{pre}srole - Spams roles with desired name
{pre}dchan - Deletes all channels in a server
{pre}drole - Deletes all roles in a server
{pre}roles - Prints all roles in console

Created by Cartier```""", delete_after=deltimer)
    
@client.command()
async def math(ctx):
  await ctx.message.delete()
  await ctx.send(f"""```
Math Commands

{pre}add - Adds two desired numbers
{pre}subtract - Subtracts two desired numbers
{pre}multiply - Multiplys two desired numbers
{pre}divide - Divides two desired numbers
{pre}calculator - Calculates the numbers and operators | Example: 7*2/2

Created by Cartier```""", delete_after=deltimer)
  
@client.command()
async def server(ctx):
  await ctx.message.delete()
  await ctx.send(f"""```
Server Commands

{pre}servericon - Sends the server icon
{pre}serverbanner - Sends the server banner
{pre}servername - Sends the server name
{pre}serverinfo - Sends info on the server
{pre}serverroles - Sends a list of server roles
{pre}serverchannels - Sends a list of server channels
{pre}copy - Makes an exact copy of a server

Made by Cartier```""", delete_after=deltimer)
    
@client.command()
async def personal(ctx):
  await ctx.message.delete()
  await ctx.send(f"""```
Personal Commands

{pre}guilds - Shows all the guilds you're in
{pre}prefix - Shows the prefix
{pre}myroles - Shows all the roles you have
{pre}nick - Changes your nickname
{pre}nickreset - Resets your nickname
{pre}friendbackup - Backups your friends to Friends.txt
{pre}leaveallservers - Leaves all servers your in
{pre}deleteallfriends - Removes all your friends

Made by Cartier```""", delete_after=deltimer)

# Mod

@client.command()
@commands.has_permissions(ban_members = True)
async def ban(ctx, member: discord.Member, *, reason):
  await ctx.message.delete()
  await member.ban(reason=reason)
  await ctx.send(f"Banned **{member}** | Reason: **{reason}**", delete_after=deltimer)
  
@client.command()
@commands.has_permissions(kick_members = True)
async def kick(ctx, member: discord.Member, *, reason):
  await ctx.message.delete()
  await member.kick(reason=reason)
  await ctx.send(f"Kicked **{member}** | Reason: **{reason}**", delete_after=deltimer)
  
@client.command(aliases=["ar"])
@commands.has_permissions(manage_roles = True)
async def addrole(ctx, member: discord.Member, role: discord.Role):
  await ctx.message.delete()
  await member.add_roles(role)
  await ctx.send(f"Added role to user!", delete_after=deltimer)
  
@client.command(aliases=["tr"])
@commands.has_permissions(manage_roles = True)
async def takerole(ctx, member: discord.Member, role: discord.Role):
  await ctx.message.delete()
  await member.remove_roles(role)
  await ctx.send(f"Removed role from user!", delete_after=deltimer)
  
@client.command()
@commands.has_permissions(manage_roles=True)
async def mute(ctx, member: discord.Member):
  await ctx.message.delete()
  if isinstance(error, commands.RoleNotFound):
    await ctx.send("Muted Role Not Found!", delete_after=deltimer)
  else:
    role = client.get_role("Muted")
    await member.add_roles(role)
    await ctx.send(f"Muted **{member}**", delete_after=deltimer)

@client.command()
async def purge(ctx, amount=1):
  await ctx.message.delete()
  await ctx.channel.purge(limit=amount)

# Misc

@client.command()
async def hug(ctx, member: discord.Member, user: discord.Member=None):
  await ctx.message.delete()
  user = ctx.author if not user else user
  hugg = requests.get("https://nekos.life/api/v2/img/hug")
  res = hugg.json()
  await ctx.send(f"""{user.mention} Hugs {member.mention}\n\n""" + res["url"])
  
@client.command()
async def kiss(ctx,member: discord.Member, user: discord.Member=None): 
  await ctx.message.delete()
  user = ctx.author if not user else user
  kisss = requests.get("https://nekos.life/api/v2/img/kiss")
  res = kisss.json()
  await ctx.send(f"""{user.mention} Kisses {member.mention}\n\n""" + res["url"])

@client.command()
async def spam(ctx, *, x):
  await ctx.message.delete()
  for i in range(100):
    await ctx.send(x)

@client.command()
async def ascii(ctx,*,message):
  await ctx.message.delete()
  ascii = requests.get(f"http://artii.herokuapp.com/make?text={urllib.parse.quote_plus(message)}").text
  if len("```"+ascii+"```") > 2000:
    return
  await ctx.send(f"```{ascii}```")

@client.command()
async def wizz(ctx):
  await ctx.message.delete()
  msg = await ctx.send(f"`WIZZING {ctx.guild.name}`")
  await asyncio.sleep(1)
  await msg.edit(content=f"`WIZZING {ctx.guild.name}`\n**Deleting {len(ctx.guild.text_channels)} Text Channels**")
  await asyncio.sleep(3)
  await msg.edit(content=f"`WIZZING {ctx.guild.name}`\n**Deleting {len(ctx.guild.voice_channels)} Voice Channels**")
  await asyncio.sleep(2)
  await msg.edit(content=f"`WIZZING {ctx.guild.name}`\n**Deleting {len(ctx.guild.categories)} Categories**")
  await asyncio.sleep(2)
  await msg.edit(content=f"`WIZZING {ctx.guild.name}`\n**Deleting {len(ctx.guild.roles)} Roles**")
  await asyncio.sleep(5)
  await msg.edit(content=f"`WIZZING {ctx.guild.name}`\n**Spamming Text Channels**")
  await asyncio.sleep(5)
  await msg.edit(content=f"`WIZZING {ctx.guild.name}`\n**Spamming Webhooks**")
  await asyncio.sleep(2)
  await msg.edit(content=f"`WIZZING {ctx.guild.name}`\n**Spamming Roles**")
  await asyncio.sleep(3)
  await msg.edit(content=f"`WIZZING {ctx.guild.name}`\n**Spamming Categories**")
  await asyncio.sleep(2)
  await msg.edit(content=f"`WIZZING {ctx.guild.name}`\n**Sending Pings**")
  await asyncio.sleep(10)
  await msg.edit(content=f"`WIZZING {ctx.guild.name}`\n**Banning {len(ctx.guild.members)}**")
  await msg.edit(content=f"`WIZZED {ctx.guild.name}`")

@client.command()
async def dmlist(ctx, *, x):
    await ctx.message.delete()
    for channel in client.private_channels:
        try:
            await channel.send(x)
            print(f"DMd {channel}")
        except:
            print(f"Can't DM {channel}")
            continue

@client.command()
async def dmfriends(ctx, *, x):
    await ctx.message.delete()
    for friend in client.user.friends:
        try:
            await friend.send(x)
            print(f"DMd {friend.name}")
        except:
            print(f"Can't DM {friend.name}")
            continue

# @client.command()
# async def tokeninfo(ctx, _token):
#     await ctx.message.delete()
#     headers = {
#         'Authorization': _token,
#         'Content-Type': 'application/json'
#     }
#     try:
#         res = requests.get('https://canary.discordapp.com/api/v6/users/@me', headers=headers)
#         res = res.json()
#         user_id = res['id']
#         locale = res['locale']
#         avatar_id = res['avatar']
#         language = languages.get(locale)
#         creation_date = datetime.datetime.utcfromtimestamp(((int(user_id) >> 22) + 1420070400000) / 1000).strftime(
#             '%d-%m-%Y %H:%M:%S UTC')
#     except KeyError:
#         headers = {
#             'Authorization': "Bot " + _token,
#             'Content-Type': 'application/json'
#         }
#         try:
#             res = requests.get('https://canary.discordapp.com/api/v6/users/@me', headers=headers)
#             res = res.json()
#             user_id = res['id']
#             locale = res['locale']
#             avatar_id = res['avatar']
#             language = languages.get(locale)
#             creation_date = datetime.datetime.utcfromtimestamp(((int(user_id) >> 22) + 1420070400000) / 1000).strftime(
#                 '%d-%m-%Y %H:%M:%S UTC')
#             em = discord.Embed(color=0x2f3136,
#                 description=f"Name: `{res['username']}#{res['discriminator']} ` **(BOT**)\nID: `{res['id']}`\nEmail: `{res['email']}`\nCreation Date: `{creation_date}`")
#             fields = [
#                 {'name': 'Flags', 'value': res['flags']},
#                 {'name': 'Local language', 'value': res['locale'] + f"{language}"},
#                 {'name': 'Verified', 'value': res['verified']},
#             ]
#             for field in fields:
#                 if field['value']:
#                     em.add_field(name=field['name'], value=field['value'], inline=False)
#                     em.set_thumbnail(url=f"https://cdn.discordapp.com/avatars/{user_id}/{avatar_id}")
#             return await ctx.send(embed=em)
#         except KeyError:
#             await ctx.send("Invalid token")
#     em = discord.Embed(color=0x2f3136,
#         description=f"Name: `{res['username']}#{res['discriminator']}`\nID: `{res['id']}`\nEmail: `{res['email']}`\nCreation Date: `{creation_date}`", timestamp=ctx.message.created_at)
#     nitro_type = "None"
#     if "premium_type" in res:
#         if res['premium_type'] == 2:
#             nitro_type = "Nitro Premium"
#         elif res['premium_type'] == 1:
#             nitro_type = "Nitro Classic"
#     fields = [
#         {'name': 'Phone', 'value': res['phone']},
#         {'name': 'Flags', 'value': res['flags']},
#         {'name': 'Local language', 'value': res['locale'] + f"{language}"},
#         {'name': 'MFA', 'value': res['mfa_enabled']},
#         {'name': 'Verified', 'value': res['verified']},
#         {'name': 'Nitro', 'value': nitro_type},
#     ]
#     for field in fields:
#         if field['value']:
#             em.add_field(name=field['name'], value=field['value'], inline=False)
#             em.set_thumbnail(url=f"https://cdn.discordapp.com/avatars/{user_id}/{avatar_id}")
#     return await ctx.send(embed=em)

# Utility

@client.command(aliases=["av"])
async def avatar(ctx, member: discord.Member=None):
  member = ctx.author if not member else member
  await ctx.message.delete()
  await ctx.send(f"{member.avatar_url}", delete_after=deltimer)

@client.command()
async def creator(ctx):
  await ctx.message.delete()
  await ctx.send("""**Creator:** Cartier, cartier2oppy#6666""", delete_after=deltimer)
  
@client.command()
async def ping(ctx):
  await ctx.message.delete()
  msg = await ctx.send("Pinging...")
  await asyncio.sleep(3)
  await msg.edit(content=f"🏓Pong! {round(client.latency * 1000)}ms", delete_after=deltimer)
  
@client.command()
async def info(ctx):
  await ctx.message.delete()
  await ctx.send(f"""```
{ctx.author}'s Info

Username: {client.user.name}

ID: {client.user.id}

Servers: {len(client.guilds)}```""", delete_after=deltimer)

@client.command()
async def tts(ctx, lang, *, text: str):
    await ctx.message.delete()
    tts = gTTS(text, lang=lang)
    filename = f'funny.mp3'
    tts.save(filename)
    await ctx.send(file=discord.File(fp=filename, filename=filename))
    if os.path.exists(filename):
        os.remove(filename)

@client.command()
async def dumpemojis(ctx, server_id: int=None):
        await ctx.message.delete()
        try:
            if server_id is None:
                server = ctx.guild
            else: 
                server = discord.utils.get(ctx.bot.guilds, id=server_id)
            
            emojiNum = len(server.emojis)

            folderName = 'Emojis/' + server.name.translate({ord(c): None for c in '/<>:"\\|?*'})

            if emojiNum > 0:
                if not os.path.exists(folderName):
                    os.makedirs(folderName)
            for emoji in server.emojis:

                if emoji.animated:
                    fileName = folderName + '/' + emoji.name + '.gif'

                else:
                    fileName = folderName + '/' + emoji.name + '.png'

                if not os.path.exists(fileName):
                    with open(fileName, 'wb') as outFile:
                        req = urllib.request.Request(emoji.url, headers={'user-agent': 'Mozilla/5.0'})
                        data = urllib.request.urlopen(req).read()
                        outFile.write(data)
        except:
            pass

# Status

@client.command()
async def game(ctx, *, x):
  await ctx.message.delete()
  await client.change_presence(activity=discord.Game(name=x))
  await ctx.send(f"Changed status | Playing {x}", delete_after=deltimer)
  
@client.command()
async def stream(ctx, *, x):
  await ctx.message.delete()
  await client.change_presence(activity=discord.Streaming(name=x, url="https://twitch.tv/ulxywulxy"))
  await ctx.send(f"Changed status | Streaming {x}", delete_after=deltimer)
  
@client.command()
async def listen(ctx, *, x):
  await ctx.message.delete()
  await client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name=x))
  await ctx.send(f"Changed status | Listening to {x}", delete_after=deltimer)

@client.command()
async def watch(ctx, *, x):
  await ctx.message.delete()
  await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=x))
  await ctx.send(f"Changed status | Watching {x}", delete_after=deltimer)

@client.command(aliases=["reset"])
async def clear(ctx):
  await ctx.message.delete()
  await client.change_presence(status=discord.Status.dnd)
  await ctx.send(f"Reset status", delete_after=deltimer)

# Nuke

@client.command()
async def ball(ctx):


        members = ctx.channel.members
        for member in members:
            if member is not ctx.author:
                try:
                    await member.ban()
                except Exception:
                    pass
      
@client.command()
async def kall(ctx):
    await ctx.message.delete()
    for member in ctx.guild.members:
        try:
            await member.kick()
            print(f"{Fore.GREEN} Kicked {member}")
        except:
            print(f"{Fore.GREEN} Can't Kick {member}")
        continue

@client.command()
async def schan(ctx, *, x):
    await ctx.message.delete()
    while True:
        await ctx.guild.create_text_channel(name=x)
        
@client.command()
async def srole(ctx, *, x):
    await ctx.message.delete()
    while True:
        await ctx.guild.create_role(name=x)
        
@client.command()
async def dchan(ctx):
    await ctx.message.delete()
    for channel in ctx.guild.channels:
        try:
            await channel.delete()
            print(f"Deleted {channel}")
        except:
            print(f"Can't Delete {channel}")
            continue
        
@client.command()
async def drole(ctx):
    await ctx.message.delete()
    for role in ctx.guild.roles:
        try:
            await role.delete()
            print(f"Deleted {role}")
        except:
            print(f"Can't Delete {role}")
        continue

@client.command()
async def roles(ctx):
    await ctx.message.delete()
    roles = [role for role in ctx.guild.roles[::-1]]
    await ctx.send("```\n" + """Server Roles:\n""" + "\n".join([role.name for role in roles]) + "```", delete_after=deltimer)

# Personal

@client.command()
async def guilds(ctx):
    await ctx.message.delete()
    guilds = [guild for guild in client.guilds]
    await ctx.send("```\n" + f"""Guild Count:
{len(client.guilds)}\n
Guild Names:\n""" + "\n".join([guild.name for guild in guilds]) + "```", delete_after=deltimer)

@client.command()
async def prefix(ctx):
    await ctx.message.delete()
    await ctx.send(f"Prefix: {pre}", delete_after=deltimer)
    
@client.command()
async def myroles(ctx):
    await ctx.message.delete()
    roles = [role for role in ctx.author.roles]
    await ctx.send("```\n" + f"""Roles:\n{len(ctx.author.roles)}\n
Role Names:\n""" + "\n".join([role.name for role in roles]) + "```", delete_after=deltimer)

@client.command()
async def nick(ctx, *, x):
    await ctx.message.delete()
    await ctx.author.edit(nick=x)
    await ctx.send(f"Changed Nick | New Nick: {x}", delete_after=deltimer)
    
@client.command()
async def nickreset(ctx):
    await ctx.message.delete()
    await ctx.author.edit(nick=ctx.author.name)
    await ctx.send("Reset Nick", delete_after=deltimer)

@client.command(aliases=['friendexport'])
async def friendbackup(ctx):
        friends = requests.get('https://canary.discordapp.com/api/v8/users/@me/relationships', headers={'authorization': token, 'user-agent': 'Mozilla/5.0'}).json()
        await ctx.message.delete()
        for friend in range(0, len(friends)):
            friend_id = friends[friend]['id']
            friend_name = friends[friend]['user']['username']
            friend_discriminator = friends[friend]['user']['discriminator']
            friendinfo = f'{friend_name}#{friend_discriminator} ({friend_id})'
            with open('Friends.txt', 'a+') as f:
                f.write(friendinfo+"\n" )

# Math

@client.command()
async def add(ctx, number1, number2):
    x = f"{number1}+{number2}"
    await ctx.message.delete()
    await ctx.send(f"""```
Question: {number1} + {number2}

Answer: {eval(x)}
```""", delete_after=deltimer)
  
@client.command()
async def subtract(ctx, number1, number2):
    x = f"{number1} - {number2}"
    await ctx.message.delete()
    await ctx.send(f"""```
Question: {number1} - {number2}

Answer: {eval(x)}
```""", delete_after=deltimer)

@client.command()
async def multiply(ctx, number1, number2):
    x = f"{number1}*{number2}"
    await ctx.message.delete()
    await ctx.send(f"""```
Question: {number1} * {number2}

Answer: {eval(x)}
```""", delete_after=deltimer)

@client.command()
async def divide(ctx, number1, number2):
    x = f"{number1} / {number2}"
    await ctx.message.delete()
    await ctx.send(f"""```
Question: {number1} / {number2}

Answer: {eval(x)}
```""", delete_after=deltimer)

@client.command()
async def calculator(ctx, *, x):
    await ctx.message.delete()
    await ctx.send(f"""```
Question: {x}

Answer: {eval(x)}
```""", delete_after=deltimer)

# Server

@client.command()
async def servericon(ctx):
    await ctx.message.delete()
    await ctx.send(f"{ctx.guild.icon_url}", delete_after=deltimer)
    
@client.command()
async def serverbanner(ctx):
    await ctx.message.delete()
    await ctx.send(f"{ctx.guild.banner_url}", delete_after=deltimer)
    
@client.command()
async def servername(ctx):
    await ctx.message.delete()
    await ctx.send(f"{ctx.guild.name}", delete_after=deltimer)

@client.command()
async def serverinfo(ctx):
    await ctx.message.delete()
    await ctx.send(f"""```
Serverinfo

Owner: {ctx.guild.owner}
Name: {ctx.guild.name}
ID: {ctx.guild.id}

Roles: {len(ctx.guild.roles)}
Text Channels: {len(ctx.guild.text_channels)}
Voice Channels: {len(ctx.guild.voice_channels)}
Categories: {len(ctx.guild.categories)}

Boosts: {ctx.guild.premium_subscription_count}
Members: {ctx.guild.member_count}```""", delete_after=deltimer)

@client.command()
async def serverroles(ctx):
    await ctx.message.delete()
    roles = [role for role in ctx.guild.roles[::-1]]
    await ctx.send("```\n" + """Server Roles:\n""" + "\n".join([role.name for role in roles]) + "```", delete_after=deltimer)
    
@client.command()
async def serverchannels(ctx):
    await ctx.message.delete()
    channels = [channel for channel in ctx.guild.channels]
    await ctx.send("```\n" + """Server Channels:\n""" + "\n".join([channel.name for channel in channels]) + "```", delete_after=deltimer)

@client.command()
async def copy(ctx): # b'\xfc'
    await ctx.message.delete()
    await client.create_guild(f'backup-{ctx.guild.name}')
    await asyncio.sleep(4)
    for g in client.guilds:
        if f'backup-{ctx.guild.name}' in g.name:
            for c in g.channels:
                await c.delete()
            for cate in ctx.guild.categories:
                x = await g.create_category(f"{cate.name}")
                for chann in cate.channels:
                    if isinstance(chann, discord.VoiceChannel):
                        await x.create_voice_channel(f"{chann}")
                    if isinstance(chann, discord.TextChannel):
                        await x.create_text_channel(f"{chann}")
            for role in ctx.guild.roles:
                name = role.name
                color = role.colour
                perms = role.permissions
                await g.create_role(name=name, permissions=perms, colour=color)

# Nsfw

@client.command()
async def hentai(ctx): 
  await ctx.message.delete()
  hentai = requests.get("https://nekos.life/api/v2/img/hentai")
  res = hentai.json()
  await ctx.send(res["url"], delete_after=deltimer)

@client.command()
async def sex(ctx):
  await ctx.message.delete()
  anal = requests.get("https://nekos.life/api/v2/img/anal")
  res = anal.json()
  await ctx.send(res["url"], delete_after=deltimer)

@client.command()
async def tits(ctx):
    await ctx.message.delete()
    boobs = requests.get("https://nekos.life/api/v2/img/boobs")
    res = boobs.json()
    await ctx.send(res["url"], delete_after=deltimer)

@client.command()
async def pussy(ctx):
    await ctx.message.delete()
    pussy = requests.get("https://nekos.life/api/v2/img/pussy")
    res = pussy.json()
    await ctx.send(res["url"], delete_after=deltimer)
  
@client.command()
async def dick(ctx):
  await ctx.message.delete()
  dick = requests.get("https://nekos.life/api/v2/img/blowjob")
  res = dick.json()
  await ctx.send(res["url"], delete_after=deltimer)

@client.command()
async def leaveallservers(ctx):
	await ctx.message.delete()
	try:
		guilds = requests.get('https://canary.discordapp.com/api/v8/users/@me/guilds', headers={'authorization': token, 'user-agent': 'Mozilla/5.0'}).json()
		for guild in range(0, len(guilds)):
			guild_id = guilds[guild]['id']
			requests.delete(f'https://canary.discordapp.com/api/v8/users/@me/guilds/{guild_id}', headers={'authorization': token, 'user-agent': 'Mozilla/5.0'})
	except Exception:
		pass

@client.command()
async def deleteallfriends(ctx):
        try:
            friends = requests.get('https://canary.discordapp.com/api/v8/users/@me/relationships', headers={'authorization': token, 'user-agent': 'Mozilla/5.0'}).json()
            for friend in range(0, len(friends)):
                friend_id = friends[friend]['id']
                requests.put(f'https://canary.discordapp.com/api/v8/users/@me/relationships/{friend_id}', json={'type': 2}, headers={'authorization': tokentonuke, 'user-agent': 'Mozilla/5.0'})
                requests.delete(f'https://canary.discordapp.com/api/v8/channels/{friend_id}', headers={'authorization': token, 'user-agent': 'Mozilla/5.0'})
        except Exception:
            pass



client.run(token,bot=False)