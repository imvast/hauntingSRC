import discord
from discord.ext import commands
import pymongo
import os
import datetime
import time
import json
import discord.utils
import psutil
import random
import typing
import aiohttp
color = 0x2f3136

headers = {"Authorization": f"Bot ODU0MDQzODk3NDk5NDg0MTYy.YMeMXA.NQTh8fQiwkQNkSVp2tYylTGcR8w"}
with open('jokes.json') as f:
    jokes = json.load(f)
    yomamajokes = jokes.get("fat") 

def blacklist_check():

    def predicate(ctx):
        author_id = ctx.author.id
        if blacklist.find_one({'user_id': author_id}):
            return False
        return True
    return commands.check(predicate)
start_time = datetime.datetime.utcnow()
# Database Setup
error = discord.Color.from_rgb(225,6,0)
sucess = discord.Color.from_rgb(8,255,8)
os.system("pip install dnspython")
mongodb = pymongo.MongoClient('mongodb+srv://prada:prada@prada.qnsvb.mongodb.net/?retryWrites=true&w=majority')
db2 = mongodb.get_database("aries").get_collection("arieslol")
db4 = mongodb.get_database("leave").get_collection("goodbye")
db3 = mongodb.get_database("anti").get_collection("toggles")
db5 = mongodb.get_database("haunting").get_collection("toggles")
blacklist = mongodb.get_database("discord").get_collection("blacklists")

class Utility(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(aliases=['av'])
    @blacklist_check()
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def avatar(self, ctx, member: typing.Union[discord.Member, discord.User] = None):
     member = ctx.author if not member else member
     embed = discord.Embed(title=f'**{member}**\'s avatar', color=color)
     embed.set_image(url=member.avatar_url)
     await ctx.send(embed=embed)

    @commands.command()
    @blacklist_check()
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def servericon(self, ctx, member: discord.Member = None):
      if not ctx.guild.icon_url:
        embed = discord.Embed(description=f'no banner set for this server', color=error)
        await ctx.send(embed=embed)
      else:
        embed = discord.Embed(description=f'{ctx.guild.name}\'s icon', color=color)
        embed.set_image(url=ctx.guild.icon_url)
        await ctx.send(embed=embed)
      
    @commands.command(aliases=['mc', 'membercount'])
    @blacklist_check()
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def members(self, ctx):
      total = ctx.guild.member_count
      humans = len(list(filter(lambda m: not m.bot, ctx.guild.members)))
      bots = len(list(filter(lambda m: m.bot, ctx.guild.members)))
      embed=discord.Embed(title = f"{ctx.guild.name} Member Count:", description=f"""
      ```asciidoc\ntotal    :: {total}\nhumans   :: {humans}\nbots     :: {bots}```
      """, color=color)
      await ctx.send(embed = embed) 


    @commands.command(aliases=['stats2', 'bi2', 'info2'])
    @blacklist_check()
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def botinfo2(self, ctx):
      try: 
          allmembers = 0
          for guild in self.client.guilds:
              allmembers += guild.member_count
          CPU_Usage = round(psutil.cpu_percent(), 1)
          used_MemoryGB = round(round(psutil.virtual_memory().used) / 102400000) / 10
          total_Ram = round(round(psutil.virtual_memory().total) / 102400000) / 10  
          before = time.monotonic()
          database = round(time.monotonic() - before) * 1000
          embed=discord.Embed(title = "Haunting", url = "https://discord.gg/Ff4mtDqXUR", description=f"""
      ```asciidoc\nGuilds    :: {len(self.client.guilds)}\nUsers     :: {allmembers}\nLibrary   :: Dpy\nDevs      :: Veltz#0001, vorqz#0001, vert#0009 ```\n\n \n\n```asciidoc\nPrefix   :: .\nStatus   :: Online\nDpy      :: 1.7.3\nCmds     :: {len(self.client.commands)}```\n\n \n\n```asciidoc\nPing     :: {int(self.client.latency * 1000)}Ms\nDb Ping  :: {database}Ms```\n\n \n\n```asciidoc\nCpu Usage :: {CPU_Usage}\nTotal Ram :: {total_Ram}\nRam Usage :: {used_MemoryGB}```
      """,color=color)
          await ctx.send(embed=embed)
          print(f"{ctx.author.name} executed botinfo command")
      except Exception as e:
        print(e)   

    @commands.command(aliases=['stats', 'bi', 'info'])
    @blacklist_check()
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def botinfo(self, ctx):
      try: 
          allmembers = 0
          for guild in self.client.guilds:
              allmembers += guild.member_count
          CPU_Usage = round(psutil.cpu_percent(), 1)
          used_MemoryGB = round(round(psutil.virtual_memory().used) / 102400000) / 10
          total_Ram = round(round(psutil.virtual_memory().total) / 102400000) / 10  
          before = time.monotonic()
          database = round(time.monotonic() - before) * 1000
          embed=discord.Embed(title = "Haunting", url = "https://discord.gg/Ff4mtDqXUR", description=f"""
      ```yaml\nGuilds    : {len(self.client.guilds)}\nUsers     : {allmembers}\nLibrary   : Dpy\nDevs      : Veltz#0001, vorqz#0001, vert#0009 ```\n\n \n\n```yaml\nPrefix   : .\nStatus   : Online\nDpy      : 1.7.3\nCmds     : {len(self.client.commands)}```\n\n \n\n```yaml\nPing     : {int(self.client.latency * 1000)}Ms\nDb Ping  : {database}Ms```\n\n \n\n```yaml\nCpu Usage : {CPU_Usage}\nTotal Ram : {total_Ram}\nRam Usage : {used_MemoryGB}```
      """,color=color)
          await ctx.send(embed=embed)
          print(f"{ctx.author.name} executed botinfo command")
      except Exception as e:
        print(e)  
    @commands.command(aliases=["botinvite", "getbotinv", "botinv"])  
    @blacklist_check()
    @commands.cooldown(1, 3, commands.BucketType.user)
    async def getbotinvite(self, ctx, member: typing.Union[discord.Member, discord.User] = None):
        if member == None:
          embed=discord.Embed(description="Please mention a bot for me to get its invite", color=color)
          await ctx.send(embed=embed)
          return
        if not member.bot:
          embed=discord.Embed(description="You must mention a bot not a user", color=color)
          await ctx.send(embed=embed)
          return
        else:
          embed=discord.Embed(description=f"Bot invite: https://discord.com/api/oauth2/authorize?client_id={member.id}&permissions=8&scope=bot", color=color)
          await ctx.send(embed=embed)

    @commands.command()
    @blacklist_check()
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def serverbanner(self, ctx):
      try:
        banner = ctx.guild.banner
        if not banner:
          embed = discord.Embed(description=f'**{ctx.guild}** has no banner', color=error)
          await ctx.send(embed=embed)
        else:
          embed = discord.Embed(description=f'**{ctx.guild}**\'s banner', color=color)
          embed.set_image(url=ctx.guild.banner_url)
          await ctx.send(embed=embed)     
      except Exception as e:
        print(e)
    @commands.command()
    @blacklist_check()
    @commands.cooldown(1, 3, commands.BucketType.user)
    async def serverid(self, ctx):
      await ctx.send(f"`server id`: {ctx.guild.id}")

    @commands.command(aliases=["memberid"])
    @blacklist_check()
    @commands.cooldown(1, 3, commands.BucketType.user)
    async def userid(self, ctx, member:discord.Member=None):
      member = ctx.author if not member else member
      await ctx.send(f"`{member.name}'s id`: {member.id}")


        
    @commands.command()
    async def boosts(self, ctx):
        await ctx.send(embed=discord.Embed(title="boosts", description=ctx.guild.premium_subscription_count, color=color))

    @commands.command(aliases=['ui2', 'userinfo2'])
    @blacklist_check()
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def whois2(self, ctx, *, user: str=None):
      if user is None:
        user = ctx.author  
        date_format = "%a, %d %b %Y %I:%M %p"
        embed = discord.Embed(color=color, description=user.mention)
        embed.set_author(name=str(user), icon_url=user.avatar_url)
        embed.set_thumbnail(url=user.avatar_url)
        embed.add_field(name="Joined", value=user.joined_at.strftime(date_format))
        embed.add_field(name="User ID", value=f'{user.id}')
        embed.add_field(name="Registered", value=user.created_at.strftime(date_format))
        if len(user.roles) > 1:
            role_string = ' '.join([r.mention for r in user.roles][1:])
            embed.add_field(name="Roles [{}]".format(len(user.roles)-1), value=role_string, inline=False)
        perm_string = ', '.join([str(p[0]).replace("_", " ").title() for p in user.guild_permissions if p[1]])
        embed.add_field(name="Guild permissions", value=perm_string, inline=False)
        embed.set_footer(text=f'Requested by {ctx.author.name}#{ctx.author.discriminator}', icon_url=ctx.author.avatar_url)
        return await ctx.send(embed = embed) 


    @commands.command(aliases=['ui', 'userinfo'])
    @blacklist_check()
    @commands.cooldown(1, 3, commands.BucketType.user)
    async def whois(self, ctx, *, user:typing.Union[discord.Member, discord.User]=None):
      try:
        user = user or ctx.author
        async with aiohttp.ClientSession(headers=headers) as session:
          async with session.get(f"https://discord.com/api/v9/users/{user.id}") as res:
            r = await res.json()
            if not r:
                return await ctx.send("Invalid user")
            if user not in ctx.guild.members:
              if user.bot:
                bot = "Yes"
              else:
                bot = "No"
              joined_discord = user.created_at.strftime("%d %b %Y %H:%M")
              embed= discord.Embed(color=color, description=user.mention)
              embed.set_author(name=str(user), icon_url=user.avatar_url)
              embed.set_thumbnail(url=user.avatar_url)
              embed.add_field(name="User ID", value=user.id)
              embed.add_field(name="Name", value=user.name)
              embed.add_field(name="Discriminator/Tag", value=user.discriminator)
              embed.add_field(name="Joined Discord", value=joined_discord)
              embed.add_field(name="Bot", value=bot)
              await ctx.send(embed=embed)
              return
            joined_server = user.joined_at.strftime("%d %b %Y %H:%M")
            joined_discord = user.created_at.strftime("%d %b %Y %H:%M")
            embed1= discord.Embed(color=color, description=user.mention)
            embed1.set_author(name=str(user), icon_url=user.avatar_url)
            embed1.set_thumbnail(url=user.avatar_url)
            embed1.add_field(name="Joined Discord", value=joined_discord)
            embed1.add_field(name="Joined Server", value=joined_server)
            embed1.add_field(name="Name", value=user.name)
            embed1.add_field(name="Nickname", value=user.nick)
            embed1.add_field(name="Discriminator", value=user.discriminator)
            embed1.add_field(name="User's ID", value=user.id)
            perm_string = ', '.join([str(p[0]).replace("_", " ").title() for p in user.guild_permissions if p[1]])
            if perm_string == 0:
              perm_string = "None"
            embed1.add_field(name="Guild permissions", value=perm_string, inline=False)
            await ctx.send(embed=embed1)
      except Exception as e:
            await ctx.send(e)

    @commands.command()
    @blacklist_check()
    @commands.cooldown(1, 3, commands.BucketType.user)
    async def yomama(self, ctx):
      try:
        jsonlol =random.choice(yomamajokes)
        await ctx.send(jsonlol)
      except Exception as e:
        print(e)

    @commands.cooldown(1, 5, commands.BucketType.channel)
    @blacklist_check()
    @commands.command(aliases=["si"])
    async def serverinfo(self, ctx):
        guild = ctx.message.guild
        total_users = ctx.guild.member_count
        total_bots = len([member for member in guild.members if member.bot == True])
        total_humans = total_users - total_bots
        text_channels = len(ctx.guild.text_channels)
        voice_channels = len(ctx.guild.voice_channels)
        passed = (ctx.message.created_at - guild.created_at).days
        created_at = ("Created on {}.".format(guild.created_at.strftime("`%d %b %Y` at `%H:%M`"), passed))
        embed = discord.Embed(description=created_at, colour=color)
        embed.add_field(name="**Owner**", value=f"{guild.owner}", inline=False)
        embed.add_field(name="**Region**", value=str(guild.region), inline=False)
        embed.add_field(name="**Boosts**", value=guild.premium_subscription_count, inline=False)
        embed.add_field(name="**Roles**", value=len(guild.roles), inline=False)
        embed.add_field(name="**Members**", value=total_users, inline=False)
        embed.add_field(name="**Humans**", value=total_humans, inline=False)
        embed.add_field(name="**Bots**", value=total_bots, inline=False)
        embed.add_field(name="**Text Channels**", value=text_channels, inline=False)
        embed.add_field(name="**Voice Channels**", value=voice_channels, inline=False)
        embed.set_footer(text=f"Server ID: {str(guild.id)}")
        
        if guild.icon_url:
            embed.set_author(name=guild.name, url=guild.icon_url)
            embed.set_thumbnail(url=guild.icon_url)
            await ctx.send(embed=embed)
        else:
            embed.set_author(name=guild.name)
            await ctx.send(embed=embed)

    @commands.command()
    @blacklist_check()
    @commands.has_permissions(manage_nicknames=True)
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def nick(self, ctx, member: discord.Member,*, nick):
      await member.edit(nick=nick)
      embed = discord.Embed(title='', description=f'updated **{member}** nickname', color=color)
      await ctx.send(embed=embed)



    @commands.command(aliases=["vote"])
    @blacklist_check()
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def upvote(self, ctx):
      embed = discord.Embed(title='Upvote', description='[top.gg](https://top.gg/bot/854043897499484162/vote)\n[discordbots](https://discord.ly/safe)', color=color)
      await ctx.send(embed=embed)



    @commands.command()
    @blacklist_check()
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def uptime(self, ctx):
	    uptime = datetime.datetime.utcnow() - start_time
	    uptime = str(uptime).split('.')[0]
	    embed = discord.Embed(description=f"**Uptime** : " + '' + uptime + '',color=color)
	    await ctx.send(embed=embed)
  

    @commands.command(aliases=["firstmessage"])
    @commands.cooldown(1, 5, commands.BucketType.user)
    @blacklist_check()
    async def firstmsg(self, ctx, channel: discord.TextChannel = None):
        if channel is None:
            channel = ctx.channel
        first_message = (await channel.history(limit=1, oldest_first=True).flatten())[0]
        embed = discord.Embed(color=color)
        embed.set_author(name="First message", url=first_message.jump_url)
        await ctx.send(embed=embed)


    @commands.command(aliases=['latency', 'p'])
    @commands.cooldown(1, 3, commands.BucketType.user)  
    @blacklist_check()
    async def ping(self, ctx):
        before = time.monotonic()
        database = round(time.monotonic() - before) * 1000
        embed = discord.Embed(description=f'<:Help:869867582403014676>  Latency : `{int(self.client.latency * 1000)}ms`\n<:Help:869867582403014676>  Database : `{database}Ms`', color=color)
        await ctx.send(embed=embed)

    @commands.command()
    @blacklist_check()
    @commands.cooldown(1,5, commands.BucketType.user)
    async def bug(self, ctx, *, message=None):
      if message == None:
         embed = discord.Embed(title="",description="input a bug", color=error)
         await ctx.send(embed=embed)
      else:
        embed = discord.Embed(title="",description="The bug has been sent to the devs", color=sucess) 
        await ctx.send(embed=embed)

        channel = self.client.get_channel(864968374476079105)
        embed2 = discord.Embed(title=f"New Bug reported by {ctx.author.name}#{ctx.author.discriminator}",description=f"Bug = **{message}**\n Server = **{ctx.guild.name}**",color=color)
        await channel.send(embed=embed2)


    @commands.command(aliases=['ub', 'userbanner'])
    @blacklist_check()
    @commands.cooldown(1,3, commands.BucketType.user)
    async def banner(self, ctx, user:typing.Union[discord.Member, discord.User]=None):
     user = user or ctx.author
     async with aiohttp.ClientSession(headers=headers) as session:
       async with session.get(f"https://discord.com/api/v9/users/{user.id}") as res:
         try:
            r = await res.json()
            if not str(r['banner']) == "None":
              embed=discord.Embed(color=color)
              if str(r['banner']).startswith("a_"): 
                embed.set_image(url=f"https://images.discordapp.net/banners/{user.id}/{str(r['banner'])}.gif?size=512")
              else:
               embed.set_image(url=f"https://images.discordapp.net/banners/{user.id}/{str(r['banner'])}?size=512")
              embed.set_author(name=user.name, icon_url=user.avatar_url)
              await ctx.send(embed=embed)            
            else:
              embed=discord.Embed(color=error, description=f'**{user.name}** does not have a banner set')
              await ctx.send(embed=embed)
         except:
           pass


    @commands.command()
    @blacklist_check()
    @commands.cooldown(1,5, commands.BucketType.channel)
    async def invites(self, ctx, member: discord.Member = None):
       if member == None:
           member = ctx.message.author
       totalInvites = 0
       for i in await ctx.guild.invites():
           if i.inviter == member:
                totalInvites += i.uses
       embed = discord.Embed(color=color,description=f"**{ctx.author}** has **{str(totalInvites)}** invites")
       await ctx.send(embed=embed)
    @commands.command(aliases=["leavevariables"])
    @blacklist_check()
    @commands.cooldown(1, 5, commands.BucketType.channel)
    async def goodbyevariables(self, ctx):
     embed = discord.Embed(title = "Haunting", description="{user.name} - Sends the users name\n{user.mention} - Mentions the user\n{user} - Sends the users name and tag\n{user.tag} - Sends the users tag\discriminator\n{server} - Sends the servers name", color=color)
     await ctx.send(embed=embed)

    @commands.command(aliases=["welcvariables"])
    @blacklist_check()
    @commands.cooldown(1, 5, commands.BucketType.channel)
    async def welcomevariables(self, ctx):
     embed = discord.Embed(title = "Haunting", description="{user.name} - Sends the users name\n{user.mention} - Mentions the user\n{user} - Sends the users name and tag\n{user.tag} - Sends the users tag\discriminator\n{server} - Sends the servers name", color=color)
     await ctx.send(embed=embed)

    @commands.command(aliases=["m", "module"])
    @blacklist_check()
    @commands.cooldown(1,10, commands.BucketType.user) 
    @commands.has_permissions(administrator=True)
    async def modules(self, ctx):
        embed = discord.Embed(title='**Hauntings Modules **', description=   f'''welcchannel
welcmsg
autorole
goodbyemessage
goodbyechannel
antiban
antikick
antiroledel
antichanneldel
antibot
antichannelcreate
antirolecreate''',color=color)

        embed.set_thumbnail(url=ctx.guild.icon_url)
        await ctx.send(embed = embed) 


    @commands.command(aliases=['supportserver'])
    @blacklist_check()
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def support(self, ctx):
      embed = discord.Embed(title='Support server', description='[Support Server](https://discord.gg/jWxrxw6qRs)', color=color)
      await ctx.send(embed=embed)

    @commands.command(aliases=["perms"])
    @blacklist_check()
    @commands.cooldown(1, 3, commands.BucketType.user)
    async def permissions(self, ctx, *, user: discord.Member=None):
        author = ctx.message.author
        if not user:
            user = author
        perms = "\n".join([x[0].replace("_", " ").title() for x in filter(lambda p: p[1] == True, user.guild_permissions)])
        embed=discord.Embed(description=perms, color=color)
        embed.set_author(name="{}'s permissions".format(user.name), icon_url=user.avatar_url)
        await ctx.send(embed=embed)

    @commands.command(aliases=["inv"])
    @blacklist_check()
    @commands.cooldown(1,3, commands.BucketType.user)
    async def invite(self, ctx):
        embed = discord.Embed(title='**Haunting**', color=color, description= f'''Invite Me [__here__](https://discord.com/api/oauth2/authorize?client_id=854043897499484162&permissions=8&scope=bot%20applications.commands)
Join My Support Server [__here__](https://discord.gg/e6dqdZzFxu)
Upvote Me [__here__](https://discord.ly/safe) And [__here__](https://top.gg/bot/854043897499484162/vote)''')

        await ctx.send(embed = embed) 

    @commands.command(aliases=["ri"]) 
    @blacklist_check()
    @commands.cooldown(1, 3, commands.BucketType.user)
    async def roleinfo(self, ctx, *, role: discord.Role=None):
        if role == None:
          embed=discord.Embed(description="input a role", color=error)
          await ctx.send(embed=embed)
        perms = role.permissions
        members = len([x for x in ctx.guild.members if role in x.roles])
        if perms.value == 0: 
            msg = f"{role.name} has no permissions"
        else:
            msg = " ".join([x[0].replace("_", " ").title() for x in filter(lambda p: p[1] == True, perms)])
        if role.hoist:
            hoist = "Yes"
        else:
            hoist = "No"
        if role.mentionable:
            mention = "Yes"
        else:
            mention = "No"
        embed=discord.Embed(color=color)
        embed.set_author(name=f"{role.name} Role Info", icon_url=ctx.guild.icon_url)
        embed.add_field(name="Mentionable", value=mention)
        embed.add_field(name="Role Color", value=role.colour)
        embed.add_field(name="Amount of users in role", value=members)
        embed.add_field(name="Hoisted", value=hoist)
        embed.add_field(name="Role ID", value=role.id)
        embed.add_field(name="Role Permissions", value=msg, inline=False)
        await ctx.send(embed=embed)
        
    @commands.command()
    @blacklist_check()
    @commands.has_permissions(manage_messages=True)
    @commands.cooldown(1, 3, commands.BucketType.user)
    async def poll(self, ctx, *, message):
      embed = discord.Embed(title=f"{ctx.author.name}#{ctx.author.discriminator} asked: {message}?",
	    description="yes => <a:gud:873102788727541822> \nno => <a:versace_thumbsdown:873102786911420416>\n ")
      msg = await ctx.send(embed=embed)
      await msg.add_reaction("<a:gud:873102788727541822>")
      await msg.add_reaction("<a:versace_thumbsdown:873102786911420416>")

def setup(client):
    client.add_cog(Utility(client))