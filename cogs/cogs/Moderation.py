import discord
from discord.ext import commands
import pymongo
import os
import requests
import asyncio
def blacklist_check():
    def predicate(ctx):
        author_id = ctx.author.id
        if blacklist.find_one({'user_id': author_id}):
            return False
        return True
    return commands.check(predicate)
error = discord.Color.from_rgb(225,6,0)
sucess = discord.Color.from_rgb(8,255,8)
# Database Setup
headers = {"Authorization": os.environ['token']}
os.system("pip install dnspython")
mongodb = pymongo.MongoClient('mongodb+srv://prada:prada@prada.qnsvb.mongodb.net/?retryWrites=true&w=majority')
db2 = mongodb.get_database("aries").get_collection("arieslol")
db4 = mongodb.get_database("leave").get_collection("goodbye")
db3 = mongodb.get_database("anti").get_collection("toggles")
db5 = mongodb.get_database("haunting").get_collection("toggles")
blacklist = mongodb.get_database("discord").get_collection("blacklists")

# EMBED HELPER
def create_embed(text):
    embed = discord.Embed(
        description=text,
        colour=color,
    )
    return embed

color= 0x2f3136
color2=discord.Colour.random()
class Moderation(commands.Cog):
    def __init__(self, client):
        self.client = client


    @commands.command()
    @blacklist_check()
    @commands.has_permissions(manage_channels=True)
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def unlock(self, ctx, channel: discord.TextChannel = None):
      if not channel:
            channel = ctx.channel
      overwrite = ctx.channel.overwrites_for(ctx.guild.default_role)
      overwrite.send_messages = True
      await ctx.channel.set_permissions(ctx.guild.default_role, overwrite=overwrite)
      embed = discord.Embed(description=f'**{channel}** is now unlocked', color=sucess)
      await ctx.send(embed=embed)

    @commands.command()
    @blacklist_check()
    @commands.has_permissions(manage_channels=True)
    async def lock(self, ctx, *, channel: discord.TextChannel=None):
        if not channel:
            channel = ctx.channel
        try:
            if channel.overwrites_for(ctx.guild.default_role).send_messages == True or channel.overwrites_for(ctx.guild.default_role).send_messages == None:
                overwrite = ctx.channel.overwrites_for(ctx.guild.default_role)
                overwrite.send_messages = False
                await channel.set_permissions(ctx.guild.default_role, overwrite=overwrite)
                return await ctx.send(embed = discord.Embed(title='', description=f"**{channel.name}** is now locked", color=sucess))
            else:
                overwrite = ctx.channel.overwrites_for(ctx.guild.default_role)
                overwrite.send_messages = None
                await channel.set_permissions(ctx.guild.default_role, overwrite=overwrite)
                return await ctx.send(embed = discord.Embed(title='', description=f"**{channel.name}** is now unlocked", color=sucess))
        except:
            await ctx.send(embed = discord.Embed(title='', description=f"failed to lock **{channel.name}**/n check if i have the correct permissions", color=error))



    @commands.command(aliases=['sm', "slowmode"])
    @blacklist_check()
    @commands.cooldown(1, 5, commands.BucketType.user)
    @commands.has_permissions(manage_channels=True)
    async def setslowmode(self, ctx, seconds: int):
      await ctx.channel.edit(slowmode_delay=seconds)
      embed = discord.Embed(title='', description=f'Set slow mode to **{seconds}**', color=sucess)
      await ctx.send(embed=embed)

    @commands.command(aliases=['offsm'])
    @blacklist_check()
    @commands.cooldown(1, 5, commands.BucketType.user)
    @commands.has_permissions(manage_channels=True)
    async def offslowmode(self, ctx):
      await ctx.channel.edit(slowmode_delay=0)
      embed = discord.Embed(title='', description=f'Slowmode is now set to **0**', color=sucess)
      await ctx.send(embed=embed)

    @commands.command()
    @blacklist_check()
    @commands.has_permissions(manage_channels=True)
    @commands.cooldown(1, 15, commands.BucketType.guild)
    async def nuke(self, ctx):
     channel_info = [ctx.channel.category, ctx.channel.position]
     await ctx.channel.clone()
     await ctx.channel.delete()
     embed=discord.Embed(description=f'channel nuked by **{ctx.author}**',color=sucess)
     embed.set_image(url="https://cdn.discordapp.com/attachments/854048083511607356/858751017776709632/tenor.gif")
     new_channel = channel_info[0].text_channels[-1]
     await new_channel.edit(position=channel_info[1])
     await new_channel.send(embed=embed)

    @commands.has_permissions(ban_members=True)
    @blacklist_check()
    @commands.command()
    @commands.cooldown(1, 3, commands.BucketType.channel)
    async def unban(self, ctx, userid):
      user = discord.Object(id=userid)
      await ctx.guild.unban(user)
      em = discord.Embed(description=f'**{user.id}** is now unbanned', color=sucess)
      await ctx.send(embed=em)
      

    @commands.command(aliases=['emojiadd', 'addemoji'])
    @blacklist_check()
    @commands.cooldown(1, 3, commands.BucketType.channel)
    @commands.has_permissions(manage_emojis=True)
    async def steal(self, ctx, emote=None):
        try:
          if emote == None:
            return await ctx.send(embed=discord.Embed(description="input a emoji", color=error))
          else:
            if emote[0] == '<':
                name = emote.split(':')[1]
                emojiname = emote.split(':')[2][:-1]
                a = emote.split(':')[0]
                if a == '<a':
                    url = f'https://cdn.discordapp.com/emojis/{emojiname}.gif'
                else:
                    url = f'https://cdn.discordapp.com/emojis/{emojiname}.png'
                try:
                    response = requests.get(url) 
                    img = response.content
                    emote = await ctx.guild.create_custom_emoji(name=name, image=img) 
                    return await ctx.send(embed=discord.Embed(description=f"added {emote}", color=sucess))
                except Exception:
                    return await ctx.send(embed=discord.Embed(description=f"failed to add emoji", color=error))
            else:
                return await ctx.send(embed=discord.Embed(description=f"invalid emoji", color=error))
        except Exception:
            return await ctx.send(embed=discord.Embed(description=f"A error occured while adding the emoji", color=error))

    

    @commands.command()
    @blacklist_check()
    @commands.cooldown(1, 5, commands.BucketType.channel)
    @commands.has_permissions(administrator=True)
    async def jail(self, ctx, member: discord.Member=None):
      if member == None:
       await ctx.send(embed=discord.Embed(description=f"input a user to jail", color=error))
      else:
        await ctx.send(embed=discord.Embed( description=f"**{member}** is being jailed...", color=sucess))
        role = discord.utils.get(ctx.guild.roles, name="jailed")
        if not role:
            await ctx.guild.create_role(name="jailed")

        jail = discord.utils.get(ctx.guild.text_channels, name="jail")
        if not jail:
            try:
                overwrites = {
                    ctx.guild.default_role: discord.PermissionOverwrite(read_messages=False, send_messages=False),
                    ctx.guild.me: discord.PermissionOverwrite(read_messages=True)
                }            
                jail = await ctx.guild.create_text_channel("jail", overwrites=overwrites)
            except discord.Forbidden:
                return await ctx.send(embed=discord.Embed(description=f" i dont the the required permissions", color=error))

        for channel in ctx.guild.channels:
            if channel.name == "jail":
                perms = channel.overwrites_for(role)
                perms.send_messages = True
                perms.read_messages = True
                await channel.set_permissions(role, overwrite=perms)
            else:
                perms = channel.overwrites_for(role)
                perms.send_messages = False
                perms.read_messages = False
                perms.view_channel = False
                await channel.set_permissions(role, overwrite=perms)

        role = discord.utils.get(ctx.guild.roles, name="jailed")
        await member.add_roles(role)

        await jail.send(content=member.mention, embed=discord.Embed(description="You are now jailed, dm one of the staff to unjail you.", color=color))
        await ctx.send(embed=discord.Embed( description=f"**{member}** is now jailed", color=sucess))
        

    @commands.command()
    @blacklist_check()
    @commands.cooldown(1, 5, commands.BucketType.channel)
    @commands.has_permissions(administrator=True)
    async def unjail(self, ctx, member: discord.Member=None):
      if member == None:
            await ctx.send(embed=discord.Embed( description=f"input a user to unjail", color=error))
      else: 
        role = discord.utils.get(ctx.guild.roles, name="jailed")
        await member.remove_roles(role)
        await ctx.send(embed=discord.Embed(description=f"**{member}** is now unjailed", color=sucess))

    @commands.command()
    @blacklist_check()
    @commands.has_guild_permissions(kick_members=True)
    @commands.cooldown(1, 3, commands.BucketType.channel)
    async def kick(self, ctx, member: discord.Member=None, *, reason=None):
      try:
           if member == None:
                await ctx.send(embed=discord.Embed(description=f"input a user", color=error)) 
           elif ctx.author == member:
             await ctx.send(embed=discord.Embed(description=f"You can not kick your self", color=error))
           elif ctx.author.top_role < member.top_role:
             await ctx.send(embed=discord.Embed(description=f"You can not kick a member above you", color=error))
           elif ctx.guild.owner == member:
               if ctx.author.id == ctx.guild.owner:
                    return
               else:
                  await ctx.send(embed=discord.Embed(description=f"you can not kick the server owner", color=error))
           else:
            if reason == None:
                try:
                    try:
                        await member.kick(reason = f"\nKick command used by {ctx.author.name}#{ctx.author.discriminator}\n")
                        reasonEmbed = discord.Embed(description = f'**{member}** is now kicked\nReason: {reason}\n \n ',color = sucess)
                        reasonEmbed.set_author(name=f"{member.name}" + "#"+ f"{member.discriminator}", icon_url=f'{member.avatar_url}')
                        reasonEmbed.set_footer(text=f"kicked by {ctx.author.name}", icon_url = '{}'.format(ctx.author.avatar_url))
                        await ctx.send(embed=reasonEmbed)
                    except:
                        await member.kick(reason = f"\nKick command used by {ctx.author.name}#{ctx.author.discriminator}\n")
                        reasonEmbed2 = discord.Embed(description = f'**{member}** is now kicked\nReason: {reason}\n \n ',color = sucess)
                        reasonEmbed2.set_author(name=f"{member.name}" + "#"+ f"{member.discriminator}", icon_url='{}'.format(member.avatar_url))
                        reasonEmbed2.set_footer(text=f"kicked by {ctx.author.name}", icon_url = '{}'.format(ctx.author.avatar_url))
                        await ctx.send(embed=reasonEmbed2)
                except:
                    await ctx.send(embed=discord.Embed(description=f"Could not kick {member}", color=error))
            else:
                try:
                    await member.kick(reason = f"\nKick command used by {ctx.author.name}#{ctx.author.discriminator}\n")
                    reasonEmbed3 = discord.Embed(description = f'**{member}** is now kicked\nReason: {reason}\n \n ',color = sucess)
                    reasonEmbed3.set_author(name=f"{member.name}" + "#"+ f"{member.discriminator}", icon_url='{}'.format(member.avatar_url))
                    reasonEmbed3.set_footer(text=f"kicked by {ctx.author.name}", icon_url = '{}'.format(ctx.author.avatar_url))
                    await ctx.send(embed=discord.Embed(description=f"Could not kick {member}", color=error))
                except:
                    await ctx.send(embed=discord.Embed(description=f"Could not kick **{member}**", color=error))
      except Exception as e:
          await ctx.send(e)

    @commands.command()
    @blacklist_check()
    @commands.has_guild_permissions(ban_members=True)
    @commands.cooldown(1, 3, commands.BucketType.channel)
    async def ban(self, ctx, member: discord.Member=None, *, reason=None):
      try:
               if member == None:
                await ctx.send(embed=discord.Embed(description=f"input a user", color=error)) 
               elif ctx.author == member:
                 await ctx.send(embed=discord.Embed( description=f"You can not ban your self", color=error))
               elif ctx.author.top_role < member.top_role:
                 await ctx.send(embed=discord.Embed(description=f"You can not ban a member above you", color=error))
               elif ctx.guild.owner == member:
                   if ctx.author.id == ctx.guild.owner:
                       return
                   else:
                     await ctx.send(embed=discord.Embed(description=f"you can not ban the server owner", color=error))
        
               else:
                if reason == None:
                    try:
                        try:
                               await member.ban(reason=f"Ban command used by {ctx.author.name}#{ctx.author.discriminator}\nreason: {reason}")
                               reasonEmbed = discord.Embed(description = f'**{member}** is now banned\nReason: {reason}\n \n ',color = sucess)
                               reasonEmbed.set_author(name=f"{member.name}" + "#"+ f"{member.discriminator}", icon_url='{}'.format(member.avatar_url))
                               reasonEmbed.set_footer(text=f"Banned by {ctx.author.name}", icon_url = '{}'.format(ctx.author.avatar_url))
                               await ctx.send(embed=reasonEmbed)
                        except:
                             await member.ban(reason=f"Ban command used by {ctx.author.name}#{ctx.author.discriminator}\nreason: {reason}")
                             reasonEmbed2 = discord.Embed(description = f'**{member}** is now banned\nReason: {reason}\n \n ',color = sucess)
                             reasonEmbed2.set_author(name=f"{member.name}" + "#"+ f"{member.discriminator}", icon_url='{}'.format(member.avatar_url))
                             reasonEmbed2.set_footer(text=f"banned by {ctx.author.name}", icon_url = '{}'.format(ctx.author.avatar_url))
                             await ctx.send(embed=reasonEmbed2)
                    except:
                        await ctx.send(embed=discord.Embed(description=f"**{member}** could not be banned", color=error))
                else:
                    try:
                        try:
                              await member.ban(reason=f"Ban command used by {ctx.author.name}#{ctx.author.discriminator}\nreason: {reason}")
                              reasonEmbed2 = discord.Embed(description = f'**{member}** is now banned\nReason: {reason}\n \n ',color = sucess)
                              reasonEmbed2.set_author(name=f"{member.name}" + "#"+ f"{member.discriminator}", icon_url='{}'.format(member.avatar_url))
                              reasonEmbed2.set_footer(text=f"banned by {ctx.author.name}", icon_url = '{}'.format(ctx.author.avatar_url))
                              await ctx.send(embed=reasonEmbed2)
                        except:
                              await member.ban(reason=f"Ban command used by {ctx.author.name}#{ctx.author.discriminator}\nreason: {reason}")
                              reasonEmbed2 = discord.Embed(description = f'**{member}** is now banned\nReason: {reason}\n \n ',color = sucess)
                              reasonEmbed2.set_author(name=f"{member.name}" + "#"+ f"{member.discriminator}", icon_url='{}'.format(member.avatar_url))
                              reasonEmbed2.set_footer(text=f"banned by {ctx.author.name}", icon_url = '{}'.format(ctx.author.avatar_url))
                              await ctx.send(embed=reasonEmbed2)
                    except:
                        await ctx.send(embed=discord.Embed( description=f"**{member}** could not be banned", color=error))
      except Exception as e:
          await ctx.send(e)



    @commands.command(aliases=['r'])
    @blacklist_check()
    @commands.cooldown(1, 5, commands.BucketType.user)
    @commands.has_permissions(manage_roles=True)
    async def role(self, ctx, member : discord.Member=None, *, role : discord.Role):
      if member is None:
        embed0 = discord.Embed(title = "Missing Argument", description=f"Missing Argument, Correct Use Is ,role (user) (role)", color=color)
        await ctx.message.reply(embed = embed0, mention_author=False) 
        return
      else:
        if role.position >= ctx.guild.me.top_role.position:
          embedidk= discord.Embed(description=f"My role is under {role.name}. Please pull my role up to be able to use this command.", color=error)
          await ctx.message.reply(embed = embedidk, mention_author=False) 
          return 
        if ctx.author.id == ctx.guild.owner.id:
          if role in member.roles:
              await member.remove_roles(role, reason=f"Role Command Used By {ctx.author.name}#{ctx.author.discriminator}") 
              embed = discord.Embed(description=f"Removed the role {role.name} from {member.name}", color=sucess) 
              await ctx.send(embed=embed)
              return
          else:
              await member.add_roles(role, reason=f"Role Command Used By {ctx.author.name}#{ctx.author.discriminator}") 
              embed1 = discord.Embed(description=f"Gave the role {role.name} to {member.name}", color=sucess)
              await ctx.send(embed=embed1)
              return  
        else:
          if role.position > ctx.author.top_role.position:
              embedbored = discord.Embed(description=f"That role is above you!!", color=error) 
              await ctx.send(embed=embedbored)
              return
          if role == ctx.author.top_role.position:
              embedbored1 = discord.Embed(description=f"That role is the same position as your top role!!", color=error) 
              await ctx.send(embed=embedbored1)
              return   
          else:
              if role in member.roles:
                  await member.remove_roles(role, reason=f"Role command used by {ctx.author.name}#{ctx.author.discriminator}") 
                  embed1 = discord.Embed(description=f"Removed the role {role.name} from {member.name}", color=sucess) 
                  await ctx.send(embed=embed1)
                  return
              else:
                  await member.add_roles(role, reason=f"Role command used by {ctx.author.name}#{ctx.author.discriminator}") 
                  embed2 = discord.Embed(description=f"Gave the role {role.name} to {member.name}", color=sucess)
                  await ctx.send(embed=embed2) 
                  return


    @commands.command()
    @blacklist_check()
    @commands.cooldown(1, 5, commands.BucketType.channel)
    @commands.has_permissions(ban_members=True)
    async def idban(self, ctx, userid, *, reason="None"):
     if not userid:
       await ctx.send(embed=discord.Embed(description="input a user id", color=error))
       return 
     else:  
            try:
                userid = int(userid)
            except:
                await ctx.send(embed=discord.Embed(description='User ID not found', color=error))
        
            try:
                await ctx.guild.ban(discord.Object(userid), reason=reason)
                idbanembed = discord.Embed(description=f'**{userid}** has been banned', colour=sucess)
                idbanembed.set_footer(text=f"Responsible Mod: {ctx.author}")
                await ctx.send(embed=idbanembed)
            except:
                await ctx.send(embed=discord.Embed(description=f"Failed to ban **{userid}**", color=error))


    @commands.command()
    @blacklist_check()
    @commands.has_permissions(manage_roles=True)
    async def mute(self, ctx, member: discord.Member=None, *, reason=None):

       guild = ctx.guild
       mutedRole = discord.utils.get(guild.roles, name="Muted")
       if member == None:
          return await ctx.send(embed=discord.Embed(description=f"input a member", color=error))
       if not mutedRole:
        mutedRole = await guild.create_role(name="Muted")

       for channel in ctx.guild.channels:
           await channel.set_permissions(mutedRole, speak=False, send_messages=False, read_message_history=True, read_messages=True)

       await member.add_roles(mutedRole, reason=reason)
       embed=discord.Embed(description=f"Muted **{member}**", color=sucess)
       await ctx.message.reply(embed = embed, mention_author=False) 

              
    @commands.command()
    @blacklist_check()
    @commands.has_permissions(manage_roles=True)
    @commands.cooldown(1, 3, commands.BucketType.channel)
    async def unmute(self, ctx, member: discord.Member=None, *, reason: str = None):
            if member == None:
              return await ctx.send(embed=discord.Embed(description=f"input a member", color=error))
            guild = ctx.guild
            muted_role = discord.utils.get(guild.roles, name="Muted")
            if not muted_role:
                return await ctx.send(embed=discord.Embed(description=f"**{member}** is not muted", color=error))
            else:
                try:
                    try:
                        await member.remove_roles(muted_role)
                        unmuteembed = discord.Embed(description=f'Unmuted **{member}**', color=sucess)
                        await ctx.send(embed=unmuteembed)
                    except:
                        await member.remove_roles(muted_role)
                        unmute2embed = discord.Embed(description=f'Unmuted **{member}**', color=sucess)
                        await ctx.send(embed=unmute2embed)
                except:
                    await ctx.send(embed=discord.Embed(description=f"Coulnt unmute **{member}**", color=error))

    @commands.command()
    @blacklist_check()
    @commands.has_permissions(administrator=True)
    @commands.cooldown(1,15, commands.BucketType.user)
    async def setup(self, ctx):
      try:
         channel2 = discord.utils.get(ctx.guild.channels, name=f'haunting-logs')
         embed = discord.Embed(title = f"Welcome To Hauntings Setup! Starting Setup in 2 seconds...",color =color)
         msg = await ctx.send(embed=embed)
         embed6 = discord.Embed(title = f"<a:loading1:863106653682925622> Checking For Logging Channel...",color =color)
         await msg.edit(embed=embed6)
      
         if not channel2:
            embed7 = discord.Embed(title = f"<a:loading1:863106653682925622> Checking For Logging Channel...",color =color)
            await msg.edit(embed=embed7)
            embed22 = discord.Embed(title = f"<a:loading1:863106653682925622> Could Not Find A Logging Channel. Creating A Logging Channel..", color=color)
            await msg.edit(embed=embed22)
            channel = await ctx.guild.create_text_channel(name='haunting-logs')
            overwrite = channel.overwrites_for(ctx.guild.default_role)
            overwrite.send_messages = False
            overwrite.view_channel = False
            await channel.set_permissions(ctx.guild.default_role, overwrite=overwrite)
            embed8 = discord.Embed(title = f"<a:loading1:863106653682925622> Checking For Logging Channel...",color =color)
            embed8.add_field(name = f"<a:loading1:863106653682925622> Could not find a Logging Channel. Creating A Logging Channel..", value='‏‏‎‎', inline=False)
            embed8.add_field(name =f"<a:success:863095257654493195> Created Logging Channel", value='‏‏‎', inline=False)
            await msg.edit(embed=embed8)
            embed11 = discord.Embed(title = f"<a:success:863095257654493195> Checking For Logging Channel...",color =color)
            embed11.add_field(name = f"<a:success:863095257654493195> Could Not Find A Logging Channel. Creating A Logging Channel..", value='‏‏‎', inline=False)
            embed11.add_field(name =f"<a:success:863095257654493195> Created Logging Channel", value='‏‏‎', inline=False)
            embed11.add_field(name = f"```Finished Hauntings Setup, To Completly Finish Hauntings setup you could set a welcome channel by doing ,welcchannel (channel) and to set a welcome message do welcmsg (welcome message).```",value='‏‏‎', inline=False)
            await msg.edit(embed=embed11)
         else:
            embed9 = discord.Embed(title = f"<a:loading1:863106653682925622> Checking For Logging Channel...",color =color,inline=False)
            embed9.add_field(name = f"<a:success:863095257654493195> Found Logging Channel",value='‏‏‎', inline=False)
            await msg.edit(embed=embed9)
            embed10 = discord.Embed(title = f"<a:success:863095257654493195> Checking For Logging Channel...",color =color, inline=False)
            embed10.add_field(name = f"<a:success:863095257654493195> Found Channel",value='‏‏‎', inline=False)
            embed10.add_field(name = f"```Successfully Completed Setup! To completly finish Hauntings setup, you could set a welcome channel by doing .joinchan (channel) and to set a welcome message do .joinmsg (welcome message).```",value='‏‏‎',inline=False)
            await msg.edit(embed=embed10)
            print(f"{ctx.author.name} send a cmd in {ctx.guild.name}")
      except Exception as e:
       print(e)


    @commands.command(aliases = ["config"])
    @blacklist_check()
    @commands.cooldown(1,5, commands.BucketType.user)
    @commands.has_permissions(administrator=True)
    async def settings(self, ctx):
      try:
       embed = discord.Embed(description='Haunting', color=color)
       enabled = "<:enabled:878656838697107506>"
       disabled = "<:disabled:890163769332871210>"
       antiban = db3.find_one({'guild_id': ctx.guild.id})['anti-ban']
       antibot = db3.find_one({'guild_id': ctx.guild.id})['anti-bot']
       antikick = db3.find_one({'guild_id': ctx.guild.id})['anti-kick']
       antichannel = db3.find_one({'guild_id': ctx.guild.id})['anti-channel-create']
       antirole = db3.find_one({'guild_id': ctx.guild.id})['anti-role-create']
       antiban = db3.find_one({'guild_id': ctx.guild.id})['anti-ban']
       antichanneldel = db3.find_one({'guild_id': ctx.guild.id})['anti-channel-del']
       antiroledel = db3.find_one({'guild_id': ctx.guild.id})['anti-role-del']
       log = discord.utils.get(ctx.guild.channels, name=f'haunting-logs')
       if log == None: logcheck = disabled
       else: logcheck = enabled
       if antiban == "on": bancheck = enabled
       elif antiban == "off": bancheck = disabled
       if antikick == "on": kickcheck = enabled
       elif antikick == "off": kickcheck = disabled
       if antichannel == "on": channelcreatecheck = enabled
       elif antichannel == "off": channelcreatecheck = disabled
       if antibot == "on": botcheck = enabled
       elif antibot == "off": botcheck = disabled
       if antirole == "on": rolecheck = enabled
       elif antirole == "off": rolecheck = disabled
       if antiroledel == "on": roledelcheck = enabled
       elif antiroledel == "off": roledelcheck = disabled
       if antichanneldel == "on": channeldelcheck = enabled
       elif antichanneldel == "off": channeldelcheck = disabled


       if channeldelcheck == disabled:
               channeldel = f"{channeldelcheck}"
       if channeldelcheck == enabled:
          channeldel = f"{channeldelcheck}"
       if roledelcheck == disabled:
          roledel = f"{roledelcheck}"
       if roledelcheck == enabled:
          roledel = f"{roledelcheck}"
       if bancheck == disabled:
         ban = f"{bancheck}"
       if bancheck == enabled:
           ban = f"{bancheck}"
       if kickcheck == disabled:
         kick = f"{kickcheck}"
       if kickcheck == enabled:
          kick = f"{kickcheck}"
       if channelcreatecheck == disabled:
        channel = f"{channelcreatecheck}"
       if channelcreatecheck == enabled:
          channel = f"{channelcreatecheck}"
       if rolecheck == disabled:
        role = f"{rolecheck}"
       if rolecheck == enabled:
        role = f"{rolecheck}"
       if botcheck == enabled:
        bot = f"{botcheck}"
       if botcheck == disabled:
        bot = f"{botcheck}"
       if logcheck == enabled:
        log = f"{logcheck}"
       if logcheck == disabled:
        log = f"{logcheck}"
       punishment = db2.find_one({ "guild_id": ctx.guild.id })['punishment']
       if punishment == None:
          punishment = "No Punishment has been set yet"
       welcchannel= db2.find_one({ "guild_id": ctx.guild.id })['welcomechannel']
       if welcchannel == None:
         welcchannel = f"{disabled}"
       else:
         welcchannel = f"<#{welcchannel}>"
       welcmsg= db2.find_one({ "guild_id": ctx.guild.id })['welcomemessage']
       if welcmsg == None: 
        welcmsg = f"{disabled}"

       goodbyechannel= db4.find_one({ "guild_id": ctx.guild.id })['goodbyechannel']
       if goodbyechannel == "off" or goodbyechannel == None:
         goodbyechannel = f"{disabled}"
       else:
         goodbyechannel = f"<#{goodbyechannel}>"
       goodbyemsg= db4.find_one({ "guild_id": ctx.guild.id })['goodbyemessage']
       if goodbyemsg == "off" or goodbyemsg == None: 
         goodbyemsg = f"{disabled}"
       else:
         goodbyemsg = f"{goodbyemsg}"
       autoroleid = db2.find_one({ "guild_id": ctx.guild.id })['autorole']
       if autoroleid == None:
          autoroleid = f"{disabled}"
       else:
          autoroleid = f"<@{autoroleid}>"
       embed.add_field(name='Punishment:', value=f'{punishment}')
       embed.add_field(name='Welcome Channel', value=f'{welcchannel}')
       embed.add_field(name='Welcome Message', value=f'{welcmsg}')
       embed.add_field(name='Goodbye Channel', value=f'{goodbyechannel}')
       embed.add_field(name='Goodbye Message', value=f'{goodbyemsg}')
       embed.add_field(name='Autorole', value=f'{autoroleid}')
       embed.add_field(name='Logging Channel', value=f'{log}')
       embed.add_field(name='Anti-Ban', value=f'{ban}')    
       embed.add_field(name='Anti-Kick', value=f'{kick}')     
       embed.add_field(name='Anti-Bot', value=f'{bot}')     
       embed.add_field(name='Anti-Channel-Create', value=f'{channelcreatecheck}')
       embed.add_field(name='Anti-Role-Create', value=f'{rolecheck}')    
       embed.add_field(name='Anti-Channel-Delete', value=f'{channeldel}')      
       embed.add_field(name='Anti-Role-Delete', value=f'{roledel}')                                    
       await ctx.send(embed = embed)
      except Exception as e:
        await ctx.send(f"there was an error\n```{e}```")

    @commands.command(aliases=["massunban"])
    @blacklist_check()
    @commands.has_permissions(ban_members=True)
    @commands.cooldown(1,15, commands.BucketType.guild)
    async def unbanall(self, ctx):
     try:
        unbanned = 0
        banlist = await ctx.guild.bans()
        idktbh = len(banlist)  
        if idktbh == 0:
          embed =discord.Embed(color=error, description=f'There is no banned users')
          await ctx.send(embed=embed)
          return
        else:
         embed = discord.Embed(color=sucess, description=f'**{len(banlist)}** users are being unbanned')
         msg = await ctx.send(embed=embed)
         for users in banlist:
               await ctx.guild.unban(user=users.user)
               unbanned += 1
         embed1 = discord.Embed( color=sucess, description=f'**{unbanned}** users have been unbanned')
         await msg.edit(embed=embed1)
     except Exception as e:
       print(e)


    @commands.has_permissions(manage_messages=True)
    @commands.command()
    @blacklist_check()
    @commands.cooldown(1,5, commands.BucketType.user)
    async def purge(self, ctx, amount=0):
        if amount == 0:
          embed = discord.Embed(description=f"input a amount", color=error)
          idklol = await ctx.send(embed=embed)
        else:
          await ctx.channel.purge(limit=amount + 1)
          embed = discord.Embed(title='Purged', description=f"Purged {amount} Message(s)",color=sucess, delete_after=3)
          idk = await ctx.send(embed=embed)
          await asyncio.sleep(3)
          await idk.delete()


    @commands.command()
    @blacklist_check()
    @commands.has_permissions(administrator=True)
    @commands.cooldown(1,3, commands.BucketType.guild)
    async def punishment(self, ctx, punishment= None):
       if punishment == None:
           embed = discord.Embed(color=error, description=f'input a punishment')
           await ctx.send(embed=embed)
       if punishment.lower() == 'ban':
           db2.update_one({ "guild_id": ctx.guild.id }, { "$set": { "punishment": "ban"}})
           embed = discord.Embed(color=sucess, description=f'Punishment Is Now Set To **Ban**')
           await ctx.send(embed=embed)
       elif punishment.lower() == 'kick':
        db2.update_one({ "guild_id": ctx.guild.id }, { "$set": { "punishment": "kick"}})
        embed = discord.Embed(color=sucess, description=f'The punishment is now set to Kick!')
        await ctx.send(embed=embed)
       else:
        embed = discord.Embed(color=error, description=f'Invalid Form Of Punishment')
        await ctx.send(embed=embed)

def setup(client):
    client.add_cog(Moderation(client))