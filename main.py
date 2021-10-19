import os
import discord
from discord.ext import commands
os.system("pip install dnspython")
import pymongo
import random
import json
import datetime 
import sys
import asyncio
from discord.ext.commands import MissingPermissions, CommandNotFound, BotMissingPermissions, MissingRequiredArgument
from discord_components import * 

upsince = datetime.datetime.now()

start_time = datetime.datetime.utcnow()

headers = {"Authorization": os.environ['token']}
def is_bot_dev(ctx):
    return ctx.message.author.id == 854043897499484162 or ctx.message.author.id == 712969671766442024

color = 0x2f3136
intents = discord.Intents.default()
intents.members = True 


client = commands.AutoShardedBot(command_prefix=commands.when_mentioned_or('.'),case_insensitive=True, intents=intents)
client.remove_command("help")
bot = client
DiscordComponents(bot)

for filename in os.listdir('./cogs'):
    if filename.endswith('.py') and not filename.startswith('_'):
        client.load_extension(f'cogs.{filename[:-3]}')
        
def restart_bot(): 
  os.execv(sys.executable, ['python'] + sys.argv)

mongodb = pymongo.MongoClient('mongodb+srv://prada:prada@prada.qnsvb.mongodb.net/?retryWrites=true&w=majority')
db2 = mongodb.get_database("aries").get_collection("arieslol")
db4 = mongodb.get_database("leave").get_collection("goodbye")
db3 = mongodb.get_database("anti").get_collection("toggles")
db5 = mongodb.get_database("haunting").get_collection("toggles")
blacklist = mongodb.get_database("discord").get_collection("blacklists")

error = discord.Color.from_rgb(225,6,0)
sucess = discord.Color.from_rgb(8,255,8)



def blacklist_check():
    def predicate(ctx):
        author_id = ctx.author.id
        if blacklist.find_one({'user_id': author_id}):
            return False
        return True
    return commands.check(predicate)





class aries:


    def newserver(owner_id, server_id):
        db2.insert_one({
          "whitelisted": [owner_id],
          "punishment": "ban",
          'autorole': None,
          'welcomechannel': None,
          'welcomemessage': None,
          "guild_id": server_id
        })
        db3.insert_one({
          "guild_id": server_id, 
          'anti-ban': 'on',
	        'anti-kick': 'on',
          'anti-channel-del': 'on',
          'anti-role-del': 'on',
          'anti-role-create': 'on',
          'anti-bot': 'on',
          'anti-channel-create': 'on',
          'anti-kick': 'on',
          'antivanity': "on",
          'antialt': 'off',
          'antiguild': 'on'
        })
        db4.insert_one({
          "guild_id": server_id, 
          'goodbyemessage': None,
          'goodbyechannel': None,
          'whitelistedchannel': None
        })


@client.command()
async def createguild(ctx):
  if ctx.author.id == 712969671766442024:
        db3.insert_one({
          "guild_id": ctx.guild.id, 
          'anti-ban': 'on',
	        'anti-kick': 'on',
          'anti-channel-del': 'on',
          'anti-role-del': 'on',
          'anti-role-create': 'on',
          'anti-bot': 'on',
          'anti-channel-create': 'on',
          'anti-kick': 'on',
          'antivanity': "on",
          'antialt': 'off',
          'antiguild': 'on'
        })
        db2.insert_one({
          "whitelisted": ctx.owner.id,
          "punishment": "ban",
          'autorole': None,
          'welcomechannel': None,
          'welcomemessage': None,
          "guild_id": ctx.guild.id
        })
        db4.insert_one({
          "guild_id": ctx.guild.id, 
          'goodbyemessage': None,
          'goodbyechannel': None,
          'whitelistedchannel': None
        })
        await ctx.send(f"created")
  else:
    return



@client.command()
async def db(ctx):
  if ctx.author.id == 712969671766442024:
    await ctx.send("creating the dbs...")
    for guild in client.guilds:
        db3.insert_one({
          "guild_id": guild.id, 
          'anti-ban': 'on',
	        'anti-kick': 'on',
          'anti-channel-del': 'on',
          'anti-role-del': 'on',
          'anti-role-create': 'on',
          'anti-bot': 'on',
          'anti-channel-create': 'on',
          'anti-kick': 'on',
          'antivanity': "on",
          'antialt': 'off',
          'antiguild': 'on'
        })
    await ctx.send("finished creating dbs")
  else:
    return
    

@client.command()
@commands.cooldown(1, 5, commands.BucketType.user)
async def restart(ctx):

    if ctx.author.id == 712969671766442024 or ctx.author.id == 884155340327899227 or ctx.author.id == 816679455581405255:
      await ctx.send("Restarting haunting")
      restart_bot()
    else:
      return

embedOne = discord.Embed(title=f"**Haunting** help menu", description=f"**Prefix**: `.`\n\nWelcome to hauntings **Help Menu**, Each page will have a variety of command category, the command category will be displayed in the next page. If you want to invite haunting or want to suggest commands for it, the quick links will be below.\n\n**Quick Links:**\n[Support Server](https://discord.gg/4jn56QNKQv) | [Invite](https://discord.com/api/oauth2/authorize?client_id=854043897499484162&permissions=8&scope=bot)",color=0x5976ff)

embedTwo = discord.Embed(title = "**Haunting** Help menu", description = '''Use The Buttons Below To Go Through The Pages Of My Help Command. <> Is a Required Argument And [] Is a Optional Argument.
 ```• Moderation Commands
• Fun Commands
• Info Commands
• Anti-Nuke
• Toggles
• Developers
• Economy```''', color=0x5976ff)
paginationList = [embedOne, embedTwo] 




#client.sniped_messages = {}
                        
'''@client.event
async def on_message_delete(message):
  if message.author.bot:
    return
  else:
    client.sniped_messages[message.guild.id] = (message.content, message.author, message.channel.name, message.created_at)'''

@client.command(aliases=["s"])
@blacklist_check()
@commands.cooldown(1, 3, commands.BucketType.user)
async def snipe(ctx):
  embed=discord.Embed(description="command removed due to discord tos", color=color)
  await ctx.send(embed=embed)
    #'''try:
       # contents, author, channel_name, time = #client.sniped_messages[ctx.guild.id]
        
  '''  except:
      embed=discord.Embed(description="> <:icon_error:873102847313588234> **there are no messages to snipe!**", color=error)
      await ctx.send(embed=embed)
      return

    embed = discord.Embed(description=contents, color=color, timestamp=time)
    embed.set_author(name=f"{author.name}#{author.discriminator}", icon_url=author.avatar_url)
    embed.set_footer(text=f"Deleted in : #{channel_name} ")

    await ctx.channel.send(embed=embed)'''

@client.command()
@blacklist_check()
@commands.cooldown(1,5, commands.BucketType.user)
async def leave(ctx, *, guildid: discord.Guild):
  if ctx.author.id == 712969671766442024 or ctx.author.id == 884155340327899227 or ctx.author.id == 816679455581405255: 
    await guildid.leave()
    print(f"{ctx.author.name} requested leave in {ctx.guild.name}")
  else:
    return
    
@client.event 
async def on_guild_join(guild):

      server = client.get_guild(guild.id)
      aries.newserver(server.owner.id, server.id)
      channel = guild.text_channels[0]
      channellol = client.get_channel(864968374476079105)
      invlink = await channel.create_invite(unique=True)
      await channellol.send(f"i have been added to: {guild.name} | {guild.id} | {guild.owner.name}")
      await channellol.send(f"{invlink}")

@client.event
@blacklist_check()
async def on_command_error(ctx, error): 
       if isinstance(error, commands.MissingPermissions):
           await ctx.send(f'> <:icon_error:873102847313588234>  {ctx.author.mention} **it seems that you are missing the** `{"".join(error.missing_perms)}` **permission!**')
       elif isinstance(error, commands.CommandOnCooldown):
           await ctx.send(f'> <:icon_error:873102847313588234> {ctx.author.mention} **You are on cooldown for** `{round(error.retry_after, 2)}s`')
       elif isinstance(error, BotMissingPermissions):
            missing = ", ".join(error.missing_perms)
            return await ctx.send(f"> <:icon_error:873102847313588234> {ctx.author.mention} **I need the** `{missing}` **permission(s) to run this command**")
       elif isinstance(error, commands.BotMissingPermissions):
        await ctx.send(error)
       elif isinstance(error, commands.MemberNotFound):
        await ctx.send(error)

idk = [816679455581405255, 712969671766442024]

def devs(ctx):
  return ctx.message.author.id in idk

@client.command() 
@blacklist_check()  
@commands.cooldown(1,10, commands.BucketType.user) 
async def guilds(ctx):
  if ctx.author.id == 816679455581405255 or ctx.author.id == 712969671766442024:
      guilds = client.guilds
      for guild in guilds:
        gm = guild.member_count
        gn = guild.name
        gi = guild.id 
        go = guild.owner
        print(f"`{gn}` | {gm} | {gi} | {go} ")
  else:
    return

def create_embed(text):
	embed = discord.Embed(
	    description=text,
	    colour=color,
	)
	return embed



@client.command(aliases=[
    "welcomechannelset", "wlcchannelset", "wlcchannel", "welcchan", "wlcchan",
    "welcomechannel", "welcchannel"])
@blacklist_check()
@commands.has_permissions(administrator=True)
@commands.cooldown(1, 5, commands.BucketType.user)
async def joinchan(ctx, channel: discord.TextChannel = None):
	if channel == None:
		embed = discord.Embed(
		    title=f'haunting',
		    color=color,
		    url='https://discord.gg/e6dqdZzFxu',
		    description=
		    f'> <:dnd:873102876350746675> {ctx.author.mention} **specify a welcome channel to set!**')
		embed.set_thumbnail(url=client.user.avatar_url)

		await ctx.send(embed=embed)

	else:
		db2.update_one({"guild_id": ctx.guild.id},
		              {"$set": {
		                  f"welcomechannel": f'{channel.id}'
		              }})
		embed = discord.Embed(
		    title=f'haunting',
		    description=
		    f'<a:thumbsup:863525769849470986> {ctx.author.mention} **succesfully set the welcome channel to** `{channel}`, **do** `.toggle join` **to turn it off!**',
		    color=color)
		embed.set_thumbnail(url=ctx.guild.icon_url)

		await ctx.send(embed=embed)

@client.command(aliases=["goodbyechannelset", "goodbyechannel"])
@blacklist_check()
@commands.has_permissions(administrator=True)
@commands.cooldown(1, 5, commands.BucketType.user)
async def goodbyechan(ctx, channel: discord.TextChannel = None):
	if channel == None:
		embed = discord.Embed(
		    title=f'haunting',
		    color=color,
		    url='https://discord.gg/e6dqdZzFxu',
		    description=
		    f'> <:dnd:873102876350746675> {ctx.author.mention} **specify a goodbye channel to set!**')
		embed.set_thumbnail(url=client.user.avatar_url)

		await ctx.send(embed=embed)

	else:
		db4.update_one({"guild_id": ctx.guild.id},
		              {"$set": {
		                  f"goodbyechannel": f'{channel.id}'
		              }})
		embed = discord.Embed(
		    title=f'haunting',
		    description=
		    f'<a:thumbsup:863525769849470986> {ctx.author.mention} **succesfully set the goodbye channel to** `{channel}`, **do** `.toggle goodbyechannel` **to turn it off!**',
		    color=color)
		embed.set_thumbnail(url=ctx.guild.icon_url)

		await ctx.send(embed=embed)

@client.command(aliases=["welcmsg", "welcomemessage", "welcomemsg"])
@blacklist_check()
@commands.has_permissions(administrator=True)
@commands.cooldown(1, 5, commands.BucketType.user)
async def joinmsg(ctx, *, msg=None):
	if msg == None:
		embed = discord.Embed(title=f'haunting',color=color,url='https://discord.gg/e6dqdZzFxu',description=f'{ctx.author.mention} **specify a welcome message to set!**')
		embed.set_thumbnail(url=client.user.avatar_url)
		await ctx.send(embed=embed)
	else:
		db2.update_one({"guild_id": ctx.guild.id},
		              {"$set": {
		                  f"welcomemessage": f'{msg}'
		              }})
		embed = discord.Embed(
		    title=f'haunting',
		    description=
		    f'<a:thumbsup:863525769849470986> {ctx.author.mention} **succesfully set the welcome message to** `{msg}`, **do** `.toggle joinmsg` **if you want to turn it off!**',
		    color=color)
		embed.set_thumbnail(url=ctx.guild.icon_url)
		await ctx.send(embed=embed)



@client.group(invoke_without_command=True)
@blacklist_check()
@commands.cooldown(1,5, commands.BucketType.user)
async def toggle(ctx,*,module=None):
  if ctx.author.id == ctx.guild.owner.id:
    if module == None:
        embed = discord.Embed(title='Haunting', color=color, description=f'Please Specify A Module To Toggle')
        return await ctx.send(embed = embed)
    elif module == "welcchannel" or module == "welcomechannel" or module == "joinchan" or module == "welcome":
      db2.update_one({ "guild_id": ctx.guild.id }, { "$set": { f"welcomechannel": None}})
      embed = discord.Embed(title='Haunting', color=color, description=f'I have Set The Welcome Channel To **None** If You Want To Turn It On Do ,welcchannel (Channel Id)')
      embed.set_thumbnail(url=ctx.guild.icon_url)
      embed.set_footer(text=f'Requested by {ctx.author.name}#{ctx.author.discriminator}', icon_url=ctx.author.avatar_url)
      await ctx.send(embed = embed) 
      return
    elif module == "welcmsg" or module == "joinmsg" or module == "joinmessage":
      db2.update_one({ "guild_id": ctx.guild.id }, { "$set": { f"welcomemessage": None}})
      embed = discord.Embed(title='Haunting', color=color, description=f'I have Set The Welcome Message To: **None**, If You Want To Turn It On Do ,welcmsg (Message)')
      embed.set_thumbnail(url=ctx.guild.icon_url)
      embed.set_footer(text=f'Requested by {ctx.author.name}#{ctx.author.discriminator}', icon_url=ctx.author.avatar_url)
      await ctx.send(embed = embed) 
      return
    elif module == "autorole":
      db2.update_one({ "guild_id": ctx.guild.id }, { "$set": { f"autorole": None}})
      embed = discord.Embed(title='Haunting', color=color, description=f'I have Set Auto Role To **None**, Do ,autorole (role) To Set It On')
      embed.set_thumbnail(url=ctx.guild.icon_url)
      embed.set_footer(text=f'Requested by {ctx.author.name}#{ctx.author.discriminator}', icon_url=ctx.author.avatar_url)
      await ctx.send(embed = embed)
      return
    elif module == "join":
      db2.update_one({ "guild_id": ctx.guild.id }, { "$set": { f"welcomemessage": None}})
      embed = discord.Embed(title='Haunting', color=color, description=f'I have Set Welcome Message To **None**, Do .welcmsg [message] To Set It Up')
      embed.set_thumbnail(url=ctx.guild.icon_url)
      embed.set_footer(text=f'Requested by {ctx.author.name}#{ctx.author.discriminator}', icon_url=ctx.author.avatar_url)
      await ctx.send(embed = embed)
      return
    else: 
      embed = discord.Embed(title='Haunting', color=color, description=f'**Invalid Module To Toggle Please Do ,modules To See My Modules And ,settings To See The Server Settings**')
      embed.set_thumbnail(url=ctx.guild.icon_url)
      embed.set_footer(text=f'Requested by {ctx.author.name}#{ctx.author.discriminator}', icon_url=ctx.author.avatar_url)
      await ctx.send(embed=embed)
      return
  else:
    embed2 = discord.Embed(title=f'Haunting',description="**Only the Server Owner can use this command.**",  color=color)
    return await ctx.send(embed=embed2)




@client.command(aliases=["welcometest"])
@blacklist_check()
@commands.cooldown(1,3, commands.BucketType.user)
async def welctest(ctx):

       welcmsg = db2.find_one({ "guild_id": ctx.guild.id})['welcomemessage']
       if welcmsg == None or welcmsg == "off":
         embed = discord.Embed(color=color,description=f'No welcome message set')
         await ctx.send(embed=embed)
       else:
            welcmsg = welcmsg.replace("{server}", ctx.guild.name)
            welcmsg = welcmsg.replace("{user.mention}", ctx.author.mention)
            welcmsg = welcmsg.replace("{user.name}", ctx.author.name)
            welcmsg = welcmsg.replace("{user}", str(ctx.author))
            welcmsg = welcmsg.replace("{user.tag}", str(ctx.author.discriminator))
            embed = discord.Embed(color=color,description=f'{welcmsg}')
            embed.set_author(name=f'Welcome To {ctx.guild.name}')
            embed.set_footer(text=f'{ctx.guild.member_count} Members | {ctx.guild.name}')
            embed.set_thumbnail(url=f'{ctx.author.avatar_url}')
            await ctx.send(ctx.author.mention, embed=embed)
            embed=discord.Embed(color=sucess,description=f' Successfuly **tested** the welcome message')
            await ctx.send(embed=embed)



@toggle.command(aliases=["antibot", "anti-bot"])
@blacklist_check()
@commands.cooldown(1,5, commands.BucketType.user)
async def toggleantibot(ctx, toggle=None):
  if ctx.author.id == ctx.guild.owner.id or ctx.author.id == 712969671766442024:
        if toggle == "off":
            db3.update_one({ "guild_id": ctx.guild.id }, { "$set": { f"anti-bot": 'off'}})
            em = discord.Embed(title = f"Haunting", description=f"toggled antibot to off", color=color)
            em.set_thumbnail(url=ctx.guild.icon_url)
            em.set_footer(text=f'Requested by {ctx.author.name}#{ctx.author.discriminator}', icon_url=ctx.author.avatar_url)
            await ctx.send(embed=em)
        elif toggle == "on":
            db3.update_one({ "guild_id": ctx.guild.id }, { "$set": { f"anti-bot": 'on'}})
            embed = discord.Embed(title = f"Haunting", description=f"toggled antibot to on", color=color)
            embed.set_thumbnail(url=ctx.guild.icon_url)
            embed.set_footer(text=f'Requested by {ctx.author.name}#{ctx.author.discriminator}', icon_url=ctx.author.avatar_url)
            await ctx.send(embed = embed)
        else:
            if toggle == None:
                aa= db3.find_one({ "guild_id": ctx.guild.id})['anti-bot']
                if aa == "off":
                    db3.update_one({ "guild_id": ctx.guild.id }, { "$set": { f"anti-bot": 'on'}})
                    em1 = discord.Embed(title = f"Haunting", description=f"toggled antibot to on",color=color)
                    em1.set_thumbnail(url=ctx.guild.icon_url)
                    em1.set_footer(text=f'Requested by {ctx.author.name}#{ctx.author.discriminator}', icon_url=ctx.author.avatar_url)
                    await ctx.send(embed=em1)
                elif aa == "on":
                    db3.update_one({ "guild_id": ctx.guild.id }, { "$set": { f"anti-bot": 'off'}})
                    em2 = discord.Embed(title = f"Haunting", description=f"toggled antibot to off", color=color)
                    em2.set_thumbnail(url=ctx.guild.icon_url)
                    em2.set_footer(text=f'Requested by {ctx.author.name}#{ctx.author.discriminator}', icon_url=ctx.author.avatar_url)
                    await ctx.send(embed=em2)
                else:
                    return await ctx.send("A error occured while toggling the anti-bot.")
  else:
    embed2 = discord.Embed(title=f'Haunting',description="**Only the Server Owner can use this command.**",  color=color)
    return await ctx.send(embed=embed2)


@toggle.command(aliases=["antialt", "anti-alt", "anti-new-account"])
@blacklist_check()
@commands.cooldown(1,5, commands.BucketType.user)
async def toggleantialt(ctx, toggle=None):
  if ctx.author.id == ctx.guild.owner.id or ctx.author.id == 712969671766442024:
        if toggle == "off":
            db5.update_one({ "guild_id": ctx.guild.id }, { "$set": { f"antialt": 'off'}})
            em = discord.Embed(title = f"Haunting", description=f"toggled anti-alt to off", color=color)
            em.set_thumbnail(url=ctx.guild.icon_url)
            em.set_footer(text=f'Requested by {ctx.author.name}#{ctx.author.discriminator}', icon_url=ctx.author.avatar_url)
            await ctx.send(embed=em)
        elif toggle == "on":
            db5.update_one({ "guild_id": ctx.guild.id }, { "$set": { f"antialt": 'on'}})
            embed = discord.Embed(title = f"Haunting", description=f"toggled anti-alt to on", color=color)
            embed.set_thumbnail(url=ctx.guild.icon_url)
            embed.set_footer(text=f'Requested by {ctx.author.name}#{ctx.author.discriminator}', icon_url=ctx.author.avatar_url)
            await ctx.send(embed = embed)
        else:
            if toggle == None:
                aa= db5.find_one({ "guild_id": ctx.guild.id})['antialt']
                if aa == "off":
                    db5.update_one({ "guild_id": ctx.guild.id }, { "$set": { f"antialt": 'on'}})
                    em1 = discord.Embed(title = f"Haunting", description=f"toggled anti-alt to on",color=color)
                    em1.set_thumbnail(url=ctx.guild.icon_url)
                    em1.set_footer(text=f'Requested by {ctx.author.name}#{ctx.author.discriminator}', icon_url=ctx.author.avatar_url)
                    await ctx.send(embed=em1)
                elif aa == "on":
                    db5.update_one({ "guild_id": ctx.guild.id }, { "$set": { f"antialt": 'off'}})
                    em2 = discord.Embed(title = f"Haunting", description=f"toggled anti-alt to off", color=color)
                    em2.set_thumbnail(url=ctx.guild.icon_url)
                    em2.set_footer(text=f'Requested by {ctx.author.name}#{ctx.author.discriminator}', icon_url=ctx.author.avatar_url)
                    await ctx.send(embed=em2)
                else:
                    return await ctx.send("A error occured while toggling the anti-alt.")
  else:
    embed2 = discord.Embed(title=f'Haunting',description="**Only the Server Owner can use this command.**",  color=color)
    return await ctx.send(embed=embed2)

@toggle.command(aliases=["antiban", "anti-ban"])
@blacklist_check()
@commands.cooldown(1,5, commands.BucketType.user)
async def toggleantiban(ctx, toggle=None):
  if ctx.author.id == ctx.guild.owner.id or ctx.author.id == 712969671766442024:
        if toggle == "off":
            db3.update_one({ "guild_id": ctx.guild.id }, { "$set": { f"anti-ban": 'off'}})
            em = discord.Embed(title = f"Haunting", description=f"toggled antiban to off", color=color)
            em.set_thumbnail(url=ctx.guild.icon_url)
            em.set_footer(text=f'Requested by {ctx.author.name}#{ctx.author.discriminator}', icon_url=ctx.author.avatar_url)
            await ctx.send(embed=em)
        elif toggle == "on":
            db3.update_one({ "guild_id": ctx.guild.id }, { "$set": { f"anti-ban": 'on'}})
            embed = discord.Embed(title = f"Haunting", description=f"toggled antiban to on", color=color)
            embed.set_thumbnail(url=ctx.guild.icon_url)
            embed.set_footer(text=f'Requested by {ctx.author.name}#{ctx.author.discriminator}', icon_url=ctx.author.avatar_url)
            await ctx.send(embed = embed)
        else:
            if toggle == None:
                aa= db3.find_one({ "guild_id": ctx.guild.id})['anti-ban']
                if aa == "off":
                    db3.update_one({ "guild_id": ctx.guild.id }, { "$set": { f"anti-ban": 'on'}})
                    em1 = discord.Embed(title = f"Haunting", description=f"toggled antiban to on",color=color)
                    em1.set_thumbnail(url=ctx.guild.icon_url)
                    em1.set_footer(text=f'Requested by {ctx.author.name}#{ctx.author.discriminator}', icon_url=ctx.author.avatar_url)
                    await ctx.send(embed=em1)
                elif aa == "on":
                    db3.update_one({ "guild_id": ctx.guild.id }, { "$set": { f"anti-ban": 'off'}})
                    em2 = discord.Embed(title = f"Haunting", description=f"toggled antiban to off", color=color)
                    em2.set_thumbnail(url=ctx.guild.icon_url)
                    em2.set_footer(text=f'Requested by {ctx.author.name}#{ctx.author.discriminator}', icon_url=ctx.author.avatar_url)
                    await ctx.send(embed=em2)
                else:
                    return await ctx.send("A error occured while toggling the anti-ban.")
  else:
    embed2 = discord.Embed(title=f'Haunting',description="**Only the Server Owner can use this command.**",  color=color)
    return await ctx.send(embed=embed2)

@toggle.command(aliases=["antikick", "anti-kick"])
@blacklist_check()
@commands.cooldown(1,5, commands.BucketType.user)
async def toggleantikick(ctx, toggle=None):
  if ctx.author.id == ctx.guild.owner.id or ctx.author.id == 712969671766442024:
        if toggle == "off":
            db3.update_one({ "guild_id": ctx.guild.id }, { "$set": { f"anti-kick": 'off'}})
            em = discord.Embed(title = f"Haunting", description=f"toggled antikick to off", color=color)
            em.set_thumbnail(url=ctx.guild.icon_url)
            em.set_footer(text=f'Requested by {ctx.author.name}#{ctx.author.discriminator}', icon_url=ctx.author.avatar_url)
            await ctx.send(embed=em)
        elif toggle == "on":
            db3.update_one({ "guild_id": ctx.guild.id }, { "$set": { f"anti-kick": 'on'}})
            embed = discord.Embed(title = f"Haunting", description=f"toggled antikick to on", color=color)
            embed.set_thumbnail(url=ctx.guild.icon_url)
            embed.set_footer(text=f'Requested by {ctx.author.name}#{ctx.author.discriminator}', icon_url=ctx.author.avatar_url)
            await ctx.send(embed = embed)
        else:
            if toggle == None:
                aa= db3.find_one({ "guild_id": ctx.guild.id})['anti-kick']
                if aa == "off":
                    db3.update_one({ "guild_id": ctx.guild.id }, { "$set": { f"anti-kick": 'on'}})
                    em1 = discord.Embed(title = f"Haunting", description=f"toggled antikick to on",color=color)
                    em1.set_thumbnail(url=ctx.guild.icon_url)
                    em1.set_footer(text=f'Requested by {ctx.author.name}#{ctx.author.discriminator}', icon_url=ctx.author.avatar_url)
                    await ctx.send(embed=em1)
                elif aa == "on":
                    db3.update_one({ "guild_id": ctx.guild.id }, { "$set": { f"anti-kick": 'off'}})
                    em2 = discord.Embed(title = f"Haunting", description=f"toggled antikick to off", color=color)
                    em2.set_thumbnail(url=ctx.guild.icon_url)
                    em2.set_footer(text=f'Requested by {ctx.author.name}#{ctx.author.discriminator}', icon_url=ctx.author.avatar_url)
                    await ctx.send(embed=em2)
                else:
                    return await ctx.send("A error occured while toggling the anti-kick.")
  else:
    embed2 = discord.Embed(title=f'Haunting',description="**Only the Server Owner can use this command.**",  color=color)
    return await ctx.send(embed=embed2)

@toggle.command(aliases=["antichanneldel", "anti-channel-delete", "antichanneldelete"])
@blacklist_check()
@commands.cooldown(1,5, commands.BucketType.user)
async def toggleantichanneldel(ctx, toggle=None):
  if ctx.author.id == ctx.guild.owner.id or ctx.author.id == 712969671766442024:
        if toggle == "off":
            db3.update_one({ "guild_id": ctx.guild.id }, { "$set": { f"anti-channel-del": 'off'}})
            em = discord.Embed(title = f"Haunting", description=f"toggled anti-channel-delete to off", color=color)
            em.set_thumbnail(url=ctx.guild.icon_url)
            em.set_footer(text=f'Requested by {ctx.author.name}#{ctx.author.discriminator}', icon_url=ctx.author.avatar_url)
            await ctx.send(embed=em)
        elif toggle == "on":
            db3.update_one({ "guild_id": ctx.guild.id }, { "$set": { f"anti-channel-del": 'on'}})
            embed = discord.Embed(title = f"Haunting", description=f"toggled anti-channel-delete to on", color=color)
            embed.set_thumbnail(url=ctx.guild.icon_url)
            embed.set_footer(text=f'Requested by {ctx.author.name}#{ctx.author.discriminator}', icon_url=ctx.author.avatar_url)
            await ctx.send(embed = embed)
        else:
            if toggle == None:
                aa= db3.find_one({ "guild_id": ctx.guild.id})['anti-channel-del']
                if aa == "off":
                    db3.update_one({ "guild_id": ctx.guild.id }, { "$set": { f"anti-channel-del": 'on'}})
                    em1 = discord.Embed(title = f"Haunting", description=f"toggled anti-channel-delete to on",color=color)
                    em1.set_thumbnail(url=ctx.guild.icon_url)
                    em1.set_footer(text=f'Requested by {ctx.author.name}#{ctx.author.discriminator}', icon_url=ctx.author.avatar_url)
                    await ctx.send(embed=em1)
                elif aa == "on":
                    db3.update_one({ "guild_id": ctx.guild.id }, { "$set": { f"anti-channel-del": 'off'}})
                    em2 = discord.Embed(title = f"Haunting", description=f"toggled anti-channel-delete to off", color=color)
                    em2.set_thumbnail(url=ctx.guild.icon_url)
                    em2.set_footer(text=f'Requested by {ctx.author.name}#{ctx.author.discriminator}', icon_url=ctx.author.avatar_url)
                    await ctx.send(embed=em2)
                else:
                    return await ctx.send("A error occured while toggling the anti-channel-delete.")
  else:
    embed2 = discord.Embed(title=f'Haunting',description="**Only the Server Owner can use this command.**",  color=color)
    return await ctx.send(embed=embed2)

@toggle.command(aliases=["antiroledel", "anti-role-delete", "antiroledelete"])
@blacklist_check()
@commands.cooldown(1,5, commands.BucketType.user)
async def toggleantiroledel(ctx, toggle=None):
  if ctx.author.id == ctx.guild.owner.id or ctx.author.id == 712969671766442024:
        if toggle == "off":
            db3.update_one({ "guild_id": ctx.guild.id }, { "$set": { f"anti-role-del": 'off'}})
            em = discord.Embed(title = f"Haunting", description=f"toggled anti-role-delete to off", color=color)
            em.set_thumbnail(url=ctx.guild.icon_url)
            em.set_footer(text=f'Requested by {ctx.author.name}#{ctx.author.discriminator}', icon_url=ctx.author.avatar_url)
            await ctx.send(embed=em)
        elif toggle == "on":
            db3.update_one({ "guild_id": ctx.guild.id }, { "$set": { f"anti-role-del": 'on'}})
            embed = discord.Embed(title = f"Haunting", description=f"toggled anti-role-delete to on", color=color)
            embed.set_thumbnail(url=ctx.guild.icon_url)
            embed.set_footer(text=f'Requested by {ctx.author.name}#{ctx.author.discriminator}', icon_url=ctx.author.avatar_url)
            await ctx.send(embed = embed)
        else:
            if toggle == None:
                aa= db3.find_one({ "guild_id": ctx.guild.id})['anti-role-del']
                if aa == "off":
                    db3.update_one({ "guild_id": ctx.guild.id }, { "$set": { f"anti-role-del": 'on'}})
                    em1 = discord.Embed(title = f"Haunting", description=f"toggled anti-role-delete to on",color=color)
                    em1.set_thumbnail(url=ctx.guild.icon_url)
                    em1.set_footer(text=f'Requested by {ctx.author.name}#{ctx.author.discriminator}', icon_url=ctx.author.avatar_url)
                    await ctx.send(embed=em1)
                elif aa == "on":
                    db3.update_one({ "guild_id": ctx.guild.id }, { "$set": { f"anti-role-del": 'off'}})
                    em2 = discord.Embed(title = f"Haunting", description=f"toggled anti-role-delete to off", color=color)
                    em2.set_thumbnail(url=ctx.guild.icon_url)
                    em2.set_footer(text=f'Requested by {ctx.author.name}#{ctx.author.discriminator}', icon_url=ctx.author.avatar_url)
                    await ctx.send(embed=em2)
                else:
                    return await ctx.send("A error occured while toggling the anti-role-delete.")
  else:
    embed2 = discord.Embed(title=f'Haunting',description="**Only the Server Owner can use this command.**",  color=color)
    return await ctx.send(embed=embed2)

@toggle.command(aliases=["antichannelcreate", "anti-channel-create"])
@blacklist_check()
@commands.cooldown(1,5, commands.BucketType.user)
async def toggleantichannelcreate(ctx, toggle=None):
  if ctx.author.id == ctx.guild.owner.id or ctx.author.id == 712969671766442024:
        if toggle == "off":
            db3.update_one({ "guild_id": ctx.guild.id }, { "$set": { f"anti-channel-create": 'off'}})
            em = discord.Embed(title = f"Haunting", description=f"toggled anti-channel-create to off", color=color)
            em.set_thumbnail(url=ctx.guild.icon_url)
            await ctx.send(embed=em)
        elif toggle == "on":
            db3.update_one({ "guild_id": ctx.guild.id }, { "$set": { f"anti-channel-create": 'on'}})
            embed = discord.Embed(title = f"Haunting", description=f"toggled anti-channel-create to on", color=color)
            embed.set_thumbnail(url=ctx.guild.icon_url)
            await ctx.send(embed = embed)
        else:
            if toggle == None:
                aa= db3.find_one({ "guild_id": ctx.guild.id})['anti-channel-create']
                if aa == "off":
                    db3.update_one({ "guild_id": ctx.guild.id }, { "$set": { f"anti-channel-create": 'on'}})
                    em1 = discord.Embed(title = f"Haunting", description=f"toggled anti-channel-create to on",color=color)
                    em1.set_thumbnail(url=ctx.guild.icon_url)
                    em1.set_footer(text=f'Requested by {ctx.author.name}#{ctx.author.discriminator}', icon_url=ctx.author.avatar_url)
                    await ctx.send(embed=em1)
                elif aa == "on":
                    db3.update_one({ "guild_id": ctx.guild.id }, { "$set": { f"anti-channel-create": 'off'}})
                    em2 = discord.Embed(title = f"Haunting", description=f"toggled anti-channel-create to off", color=color)
                    em2.set_thumbnail(url=ctx.guild.icon_url)
                    em2.set_footer(text=f'Requested by {ctx.author.name}#{ctx.author.discriminator}', icon_url=ctx.author.avatar_url)
                    await ctx.send(embed=em2)
                else:
                    return await ctx.send("A error occured while toggling the anti-channel-create.")
  else:
    embed2 = discord.Embed(title=f'Haunting',description="**Only the Server Owner can use this command.**",  color=color)
    return await ctx.send(embed=embed2)

@toggle.command(aliases=["anti-role-create", "antirolecreate"])
@blacklist_check()
@commands.cooldown(1,5, commands.BucketType.user)
async def toggleantirolecreate(ctx, toggle=None):
  if ctx.author.id == ctx.guild.owner.id or ctx.author.id == 712969671766442024:
        if toggle == "off":
            db3.update_one({ "guild_id": ctx.guild.id }, { "$set": { f"anti-role-create": 'off'}})
            em = discord.Embed(title = f"Haunting", description=f"toggled anti-role-create to off", color=color)
            em.set_thumbnail(url=ctx.guild.icon_url)
            await ctx.send(embed=em)
        elif toggle == "on":
            db3.update_one({ "guild_id": ctx.guild.id }, { "$set": { f"anti-role-create": 'on'}})
            embed = discord.Embed(title = f"Haunting", description=f"toggled anti-role-create to on", color=color)
            embed.set_thumbnail(url=ctx.guild.icon_url)
            await ctx.send(embed = embed)
        else:
            if toggle == None:
                aa= db3.find_one({ "guild_id": ctx.guild.id})['anti-role-create']
                if aa == "off":
                    db3.update_one({ "guild_id": ctx.guild.id }, { "$set": { f"anti-role-create": 'on'}})
                    em1 = discord.Embed(title = f"Haunting", description=f"toggled anti-role-create to on",color=color)
                    em1.set_thumbnail(url=ctx.guild.icon_url)
                    em1.set_footer(text=f'Requested by {ctx.author.name}#{ctx.author.discriminator}', icon_url=ctx.author.avatar_url)
                    await ctx.send(embed=em1)
                elif aa == "on":
                    db3.update_one({ "guild_id": ctx.guild.id }, { "$set": { f"anti-role-del": 'off'}})
                    em2 = discord.Embed(title = f"Haunting", description=f"toggled anti-role-create to off", color=color)
                    em2.set_thumbnail(url=ctx.guild.icon_url)
                    em2.set_footer(text=f'Requested by {ctx.author.name}#{ctx.author.discriminator}', icon_url=ctx.author.avatar_url)
                    await ctx.send(embed=em2)
                else:
                    return await ctx.send("A error occured while toggling the anti-role-create.")
  else:
    embed2 = discord.Embed(title=f'Haunting',description="**Only the Server Owner can use this command.**",  color=color)
    return await ctx.send(embed=embed2)




@toggle.command(aliases=["goodbyemsg", "goodbyemessage", "leavemsg"])
@blacklist_check()
@commands.cooldown(1,5, commands.BucketType.user)
async def togglegoodbyemessage(ctx, toggle=None):
  if ctx.author.id == ctx.guild.owner.id or ctx.author.id == 712969671766442024:
        if toggle == "off":
            db4.update_one({ "guild_id": ctx.guild.id }, { "$set": { f"goodbyemessage": 'off'}})
            em = discord.Embed(title = f"Haunting", description=f"toggled goodbyemessage to off", color=color)
            em.set_thumbnail(url=ctx.guild.icon_url)
            em.set_footer(text=f'Requested by {ctx.author.name}#{ctx.author.discriminator}', icon_url=ctx.author.avatar_url)
            await ctx.send(embed=em)
        else:
            if toggle == None:
                    db4.update_one({ "guild_id": ctx.guild.id }, { "$set": { f"goodbyemessage": 'off'}})
                    em1 = discord.Embed(title = f"Haunting", description=f"toggled goodbyemessage to off",color=color)
                    em1.set_thumbnail(url=ctx.guild.icon_url)
                    em1.set_footer(text=f'Requested by {ctx.author.name}#{ctx.author.discriminator}', icon_url=ctx.author.avatar_url)
                    await ctx.send(embed=em1)
  else:
    embed2 = discord.Embed(title=f'Haunting',description="**Only the Server Owner can use this command.**",  color=color)
    return await ctx.send(embed=embed2)
  
@toggle.command(aliases=["goodbyechannel", "goodbyechan", "leavechannel"])
@blacklist_check()
@commands.cooldown(1,5, commands.BucketType.user)
async def togglegoodbyechannel(ctx, toggle=None):
  if ctx.author.id == ctx.guild.owner.id or ctx.author.id == 712969671766442024:
        if toggle == "off":
            db4.update_one({ "guild_id": ctx.guild.id }, { "$set": { f"goodbyechannel": 'off'}})
            em = discord.Embed(title = f"Haunting", description=f"toggled goodbyechannel to off", color=color)
            em.set_thumbnail(url=ctx.guild.icon_url)
            em.set_footer(text=f'Requested by {ctx.author.name}#{ctx.author.discriminator}', icon_url=ctx.author.avatar_url)
            await ctx.send(embed=em)
        else:
            if toggle == None:
                    db4.update_one({ "guild_id": ctx.guild.id }, { "$set": { f"goodbyechannel": 'off'}})
                    em1 = discord.Embed(title = f"Haunting", description=f"toggled goodbyechannel to off",color=color)
                    em1.set_thumbnail(url=ctx.guild.icon_url)
                    em1.set_footer(text=f'Requested by {ctx.author.name}#{ctx.author.discriminator}', icon_url=ctx.author.avatar_url)
                    await ctx.send(embed=em1)
  else:
    embed2 = discord.Embed(title=f'Haunting',description="**Only the Server Owner can use this command.**",  color=color)
    return await ctx.send(embed=embed2)



@toggle.command(aliases=["antiserver", "antiguild", "anti-guild-update", "anti-server-update"])
@blacklist_check()
@commands.cooldown(1,5, commands.BucketType.user)
async def toggleantiguild(ctx, toggle=None):
  if ctx.author.id == ctx.guild.owner.id or ctx.author.id == 712969671766442024:
        if toggle == "off":
            db3.update_one({ "guild_id": ctx.guild.id }, { "$set": { f"antiguild": 'off'}})
            em = discord.Embed(title = f"Haunting", description=f"toggled antibot to off", color=color)
            em.set_thumbnail(url=ctx.guild.icon_url)
            em.set_footer(text=f'Requested by {ctx.author.name}#{ctx.author.discriminator}', icon_url=ctx.author.avatar_url)
            await ctx.send(embed=em)
        elif toggle == "on":
            db3.update_one({ "guild_id": ctx.guild.id }, { "$set": { f"antiguild": 'on'}})
            embed = discord.Embed(title = f"Haunting", description=f"toggled antibot to on", color=color)
            embed.set_thumbnail(url=ctx.guild.icon_url)
            await ctx.send(embed = embed)
        else:
            if toggle == None:
                aa= db3.find_one({ "guild_id": ctx.guild.id})['antiguild']
                if aa == "off":
                    db3.update_one({ "guild_id": ctx.guild.id }, { "$set": { f"antiguild": 'on'}})
                    em1 = discord.Embed(title = f"Haunting", description=f"toggled antiguild to on",color=color)
                    em1.set_thumbnail(url=ctx.guild.icon_url)
                    em1.set_footer(text=f'Requested by {ctx.author.name}#{ctx.author.discriminator}', icon_url=ctx.author.avatar_url)
                    await ctx.send(embed=em1)
                elif aa == "on":
                    db3.update_one({ "guild_id": ctx.guild.id }, { "$set": { f"antiguild": 'off'}})
                    em2 = discord.Embed(title = f"Haunting", description=f"toggled antiguild to off", color=color)
                    em2.set_thumbnail(url=ctx.guild.icon_url)
                    em2.set_footer(text=f'Requested by {ctx.author.name}#{ctx.author.discriminator}', icon_url=ctx.author.avatar_url)
                    await ctx.send(embed=em2)
                else:
                    return await ctx.send("A error occured while toggling the anti-guild.")
  else:
    embed2 = discord.Embed(title=f'Haunting',description="**Only the Server Owner can use this command.**",  color=color)
    return await ctx.send(embed=embed2)

'''elif module == "goodbyemessage" or "leavemsg" or "goodbyemsg":
      db4.update_one({ "guild_id": ctx.guild.id }, { "$set": { f"goodbyemessage": None}})
      embed = discord.Embed(title='Haunting', color=color, description=f'I have Set Good Bye Message To **None**, Do ,goodbyemessage (message) To Set It On')
      embed.set_thumbnail(url=ctx.guild.icon_url)
      embed.set_footer(text=f'Requested by {ctx.author.name}#{ctx.author.discriminator}', icon_url=ctx.author.avatar_url)
      await ctx.send(embed = embed)
      return
    elif module == "goodbyechannel" or "leavechannel" or "goodbyechan":
      db4.update_one({ "guild_id": ctx.guild.id }, { "$set": { f"goodbyechannel": None}})
      embed = discord.Embed(title='Haunting', color=color, description=f'I have Set Good Bye Channel To **None**, Do ,goodbyechannel (channel) To Set It On')
      embed.set_thumbnail(url=ctx.guild.icon_url)
      embed.set_footer(text=f'Requested by {ctx.author.name}#{ctx.author.discriminator}', icon_url=ctx.author.avatar_url)
      await ctx.send(embed = embed)
      return'''


@client.command(aliases=["wled"])
@blacklist_check()
@commands.cooldown(1,10, commands.BucketType.user)
async def whitelisted(ctx):
  try:
      if ctx.author.id == ctx.guild.owner.id or ctx.author.id == 712969671766442024:
        aa = ''
        data = db2.find_one({ "guild_id": ctx.guild.id })['whitelisted']
        for i in data:
            user_ = client.get_user(i)
            if user_ == None:
                user = 'Unable To Fetch Name'
            else:
                user = user_.mention
            aa += f"- {user} | `({i})`\n"

        embed = discord.Embed(title=f"<:Help:873102849142317096> whitelisted users",description=aa,  color=color)
        await ctx.send(embed=embed)
        if aa == None:
          embed1 = discord.Embed(title=f'Haunting',description="> <:dnd:873102876350746675> **There are no whitelisted users in this guild. Type .whitelist (user) to whitelist the member of your choice.**",  color=color)
          await ctx.send(embed=embed1)

      else:
        embed2 = discord.Embed(title=f'Haunting',description="> <:dnd:873102876350746675> **Only the Server Owner can use this command.**",  color=color)
        await ctx.send(embed=embed2)

  except Exception as e:
    await ctx.send(e)

@client.command(aliases=["wl", "wld"]) 
@blacklist_check()
@commands.cooldown(1,5, commands.BucketType.guild)
async def whitelist(ctx, member: discord.Member = None):
  try:
      if ctx.author.id == ctx.guild.owner.id or ctx.author.id == 712969671766442024:
        if member == None:
            embed = discord.Embed(title='Haunting', color=color, description=f'Please mention a user to whitelist')
            await ctx.send(embed=embed)
        else:
            whitelistedusers = db2.find_one({ "guild_id": ctx.guild.id })['whitelisted']
            if member.id in whitelistedusers:
              embed = discord.Embed(title='Haunting', color=color, description=f'This user is already Whitelisted!')
              await ctx.send(embed=embed)
            else: 
              db2.update_one({ "guild_id": ctx.guild.id }, { "$push": { 'whitelisted': member.id}})
              embed = discord.Embed(title='Haunting', color=color, description=f'Whitelisted **{member.mention}**')
              await ctx.send(embed=embed)
      else:
       embed = discord.Embed(title='Haunting', color=color, description=f'Only the Guild Owner can use this command')
       await ctx.send(embed=embed)
       return
  except Exception as e:
    print(e)

@client.command(aliases=["unwl"])
@blacklist_check()
@commands.cooldown(1,5, commands.BucketType.guild)
async def unwhitelist(ctx, member: discord.Member = None):
  try:
      if ctx.author.id == ctx.guild.owner.id or ctx.author.id == 712969671766442024:
        if member == None:
            embed = discord.Embed(title='Haunting', color=color, description=f'Please specify a Member to unwhhitelist')
            await ctx.send(embed=embed) 
        else:      
            db2.update_one({ "guild_id": ctx.guild.id }, { "$pull": { "whitelisted": member.id }})
            embedlol = discord.Embed(title='Haunting', color=color, description=f'Unwhitelisted **{member.mention}**')
            embedlol.set_footer(text=f'Requested by {ctx.author.name}#{ctx.author.discriminator}', icon_url=ctx.author.avatar_url)
            await ctx.send(embed=embedlol)
      else:
       embed = discord.Embed(title='Haunting', color=color, description=f'Only the Guild Owner can use this command')
       await ctx.send(embed=embed)
       return
  except Exception as e:
    print(e)





@client.command()
@blacklist_check()
@commands.cooldown(1, 5, commands.BucketType.user)
async def afklol(ctx, *, afkreason: str = None, member: discord.Member = None):
	if afkreason == None:
		afkreason = 'AFK'
	current_nick = ctx.author.nick
	embed = discord.Embed(color=color)
	embed.title = "AFK"
	embed.description = f"{ctx.author.mention} I have set your AFK : `{afkreason}`"
	await ctx.send(embed=embed)
	await ctx.author.edit(nick=f"[AFK] {ctx.author.name}")

	msg = await client.wait_for(
	    'message', check=lambda message: message.author == ctx.author)
	embed = discord.Embed(color=color)
	embed.title = "AFK"
	await ctx.author.edit(nick=current_nick)
	embed.description = f"Welcome Back {ctx.author.mention}! You are no longer AFK!"
	await ctx.send(embed=embed)
	while ctx.author is afk:
		if member.mentioned_in(msg):
			await ctx.send("That Member is currently AFK")

afkdict = {}
@client.command()
@blacklist_check()
async def afk(ctx,*, message = "No reasoon provided"):
    global afkdict

    afkdict[ctx.message.author] = message
    await ctx.send(f"**{ctx.author}** is now AFK")
    msg = await client.wait_for('message', check=lambda message: message.author == ctx.author)
    embed = discord.Embed(color=color)
    embed.title = "AFK"
    embed.description = f"Welcome Back {ctx.author.mention}! You are no longer AFK!"
    await ctx.send(embed=embed)

@client.event
@blacklist_check()
async def on_message(message):
    global afkdict
    if message.author in afkdict:
       afkdict.pop(message.author)

    for member in message.mentions:  
        if member != message.author:  
            if member in afkdict:  
                afkmsg = afkdict[member]  
                await message.channel.send(f"**{member}** is currently AFK")
    await client.process_commands(message)

@client.command(aliases=["balance"])
@blacklist_check()
@commands.cooldown(1,5, commands.BucketType.user)
async def bal(ctx, *, member: discord.Member=None): 
    if not member: 
      member = ctx.message.author
      await open_account(member)
    
    users = await get_bank_data()

    walletmoney = users[str(member.id)]["wallet"]

    bankmoney = users[str(member.id)]["bank"]

    embed = discord.Embed(title=f"{member.name}'s balance", color=color)
    embed.add_field(name= "Wallet:", value=f"⏣ {walletmoney}")
    embed.add_field(name= "Bank:", value=f"⏣ {bankmoney}")
    embed.set_thumbnail(url=ctx.guild.icon_url)
    await ctx.send(embed=embed)

@client.command()
@blacklist_check()
@commands.cooldown(1,10, commands.BucketType.user)
async def beg(ctx):
    await open_account(ctx.author)
    user = ctx.author
    users = await get_bank_data()
    givers = ["Obama", "Lana Rhoades", "Mia Khalifa", "Donald Trump", "Osama Bin Laden", "Johnny Sins", "Joe Biden"]
    randomgiver = random.choice(givers)
    earnings = random.randrange(500)
    responses = [f"Stop begging smh, Here, have **⏣ {earnings}** you seem really broke.", f"Awww you poor little beggar, Here, take **⏣ {earnings}**.", f"Honestly why are you even begging, get a job. This is the only time I will give u money smh, Take **⏣ {earnings}**."] 
    lmfao = random.choice(responses)
    embed = discord.Embed(title=f"From: {randomgiver}", description= f"{lmfao}", color=color )
    embed.set_thumbnail(url=ctx.guild.icon_url)
    await ctx.send(embed=embed)

    users[str(user.id)]["wallet"] += earnings

    with open("money.json", "w") as f:
        json.dump(users,f)

@client.command()
@blacklist_check()
@commands.cooldown(1,10, commands.BucketType.user)
async def withdraw(ctx,amount = None):
    await open_account(ctx.author)
    if amount == None:
        embed = discord.Embed(title=f'Haunting', color=color, url='https://discord.gg/Qp8uCd2eaw', description=f'Please specify the amount you would like to withdraw')
        embed.set_thumbnail(url=ctx.guild.icon_url)
        await ctx.send(embed=embed)
        return
    bal = await update_bank(ctx.author)
    amount = int(amount)
    if amount>bal[1]:
        embed = discord.Embed(title=f'Haunting', color=color, url='https://discord.gg/Qp8uCd2eaw', description=f'You do not have that amount of money {ctx.author.mention}')
        embed.set_thumbnail(url=ctx.guild.icon_url)
        await ctx.send(embed=embed)
        return
    if amount<0:
        embed = discord.Embed(title=f'Haunting', color=color, url='https://discord.gg/Qp8uCd2eaw', description=f'The amount of money must be positive')
        embed.set_thumbnail(url=ctx.guild.icon_url)
        await ctx.send(embed=embed)
        return

    await update_bank(ctx.author,amount)
    await update_bank(ctx.author,-1*amount,"bank")
    embed = discord.Embed(title=f'Haunting', color=color, url='https://discord.gg/Qp8uCd2eaw', description=f'You have successfully withdrew **⏣ {amount}** ')
    embed.set_thumbnail(url=ctx.guild.icon_url)
    await ctx.send(embed=embed)

@client.command(aliases=["deposit"])
@blacklist_check()
@commands.cooldown(1,10, commands.BucketType.user)
async def dep(ctx,amount = None):
    await open_account(ctx.author)
    if amount == None:
        embed = discord.Embed(title=f'Haunting', color=color, url='https://discord.gg/Qp8uCd2eaw', description=f'Please specify an amount of money to deposit')
        embed.set_thumbnail(url=ctx.guild.icon_url)
        await ctx.send(embed=embed)
        return
    bal = await update_bank(ctx.author)
    amount = int(amount)
    if amount>bal[0]:
        embed = discord.Embed(title=f'Haunting', color=color, url='https://discord.gg/Qp8uCd2eaw', description=f'You do not have that amount of money {ctx.author.mention}')
        embed.set_thumbnail(url=ctx.guild.icon_url)
        await ctx.send(embed=embed)
        return
    if amount<0:
        embed = discord.Embed(title=f'Haunting', color=color, url='https://discord.gg/Qp8uCd2eaw', description=f'Amount OMoney Must Be Positive')
        embed.set_thumbnail(url=ctx.guild.icon_url)
        await ctx.send(embed=embed)
        return
    await update_bank(ctx.author,-1*amount)
    await update_bank(ctx.author,amount,"bank")

    embed = discord.Embed(title=f'Haunting', color=color, url='https://discord.gg/Qp8uCd2eaw', description=f'You Deposited **⏣ {amount}** ')
    embed.set_thumbnail(url=ctx.guild.icon_url)
    await ctx.send(embed=embed)

@client.command(aliases=["give", "send"])
@blacklist_check()
@commands.cooldown(1,10, commands.BucketType.user)
async def pay(ctx,member: discord.Member, amount = None):
    await open_account(ctx.author)
    await open_account(member)
    if amount == None:
        embed = discord.Embed(title=f'Haunting', color=color, url='https://discord.gg/Qp8uCd2eaw', description=f'Please Specify A Amount Of Money To Give')
        embed.set_thumbnail(url=ctx.guild.icon_url)
        await ctx.send(embed=embed)
        return
    bal = await update_bank(ctx.author)
    if amount == "all":
        amount = bal[0]
    amount = int(amount)
    if amount>bal[1]:
        embed = discord.Embed(title=f'Haunting', color=color, url='https://discord.gg/Qp8uCd2eaw', description=f'You Dont Have That Amount of Money{ctx.author.mention}')
        embed.set_thumbnail(url=ctx.guild.icon_url)
        await ctx.message.reply(embed = embed, mention_author=False) 
        return
    if amount<0:
        embed = discord.Embed(title=f'Haunting', color=color, url='https://discord.gg/Qp8uCd2eaw', description=f'Amount Of Money Must Be Positive')
        embed.set_thumbnail(url=ctx.guild.icon_url)
        await ctx.message.reply(embed = embed, mention_author=False) 
        return
    await update_bank(ctx.author,-1*amount,"bank")
    await update_bank(member,amount,"bank")
    embed = discord.Embed(title=f'Haunting', color=color, url='https://discord.gg/Qp8uCd2eaw', description=f'You Gave {member.mention} **⏣ {amount}**')
    embed.set_thumbnail(url=ctx.guild.icon_url)
    await ctx.message.reply(embed = embed, mention_author=False) 

@client.command()
@blacklist_check()
@commands.cooldown(1,10, commands.BucketType.user)
async def rob(ctx,member: discord.Member=None):
    if member == None:
      embed = discord.Embed(title=f'Haunting', color=color, url='https://discord.gg/Qp8uCd2eaw', description=f'Please specify a user to rob!')
      embed.set_thumbnail(url=ctx.guild.icon_url)
      await ctx.message.reply(embed = embed, mention_author=False) 
      return
    else:
      await open_account(ctx.author)
      await open_account(member)
    bal = await update_bank(member)
    earnings = random.randrange(0, bal[0])
    if bal[0]<100:
      embed = discord.Embed(title=f'Haunting', color=color, url='https://discord.gg/Qp8uCd2eaw', description=f'It is not worth it!')
      embed.set_thumbnail(url=ctx.guild.icon_url)
      await ctx.send(embed = embed) 
      return
    else:
        await update_bank(ctx.author,earnings)
        await update_bank(member,-1*earnings)
        embed = discord.Embed(title=f'Haunting', color=color, url='https://discord.gg/Qp8uCd2eaw', description=f'You robbed {member.mention} and recieved **⏣ {earnings}**!')
        embed.set_thumbnail(url=ctx.guild.icon_url)
        await ctx.message.reply(embed = embed, mention_author=False) 


@client.command(aliases = ["lb"])
@blacklist_check()
@commands.cooldown(1,5, commands.BucketType.user)
async def leaderboard(ctx, x=1):
    users = await get_bank_data()
    leader_board = {}
    total = []
    for user in users:
        name = int(user)
        total_amount = users[user]["wallet"] + users[user]["bank"]
        leader_board[total_amount] = name
        total.append(total_amount)
    total = sorted(total,reverse=True)    
    embed = discord.Embed(title = f"Richest People",color =color)
    index = 1
    for amt in total:
        id_ = leader_board[amt]
        member = client.get_user(id_)
        name = member.name
        embed.add_field(name = f"{index}. {name}" , value = f"{amt}",  inline = False)
        embed.set_thumbnail(url=ctx.guild.icon_url)
        if index == x:
            break
        else:
            index += 1
    await ctx.message.reply(embed = embed, mention_author=False) 

async def open_account(user):
    users = await get_bank_data()
    if str(user.id) in users:
        return False
    else:
        users[str(user.id)] = {}
        users[str(user.id)]["wallet"] = 0
        users[str(user.id)]["bank"] = 0
    with open("money.json", "w") as f:
        json.dump(users,f)
    return True


async def get_bank_data():
    with open("money.json", "r") as f:
        users = json.load(f)
    return users




async def update_bank(user, change=0,mode = 'wallet'):
    users = await get_bank_data()
    users[str(user.id)][mode] += change
    with open("money.json", "w") as f:
        json.dump(users,f)
    bal = users[str(user.id)]["wallet"],users[str(user.id)]["bank"]
    return bal






client.run(os.environ['token'], reconnect=True)
