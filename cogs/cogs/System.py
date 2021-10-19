import discord, os, math, pymongo, asyncio
from discord.ext.commands.cooldowns import BucketType
from discord.ext import commands
import sys
def create_embed(text):
    embed = discord.Embed(
        description=text,
        colour=color,
    )
    return embed
def blacklist_check():
    def predicate(ctx):
        author_id = ctx.author.id
        if blacklist.find_one({'user_id': author_id}):
            return False
        return True
    return commands.check(predicate)



def is_owner(ctx):
    return ctx.message.author.id == 712969671766442024 or ctx.message.author.id == 884155340327899227 or ctx.message.author.id == 816679455581405255
os.system("pip install dnspython")
mongodb = pymongo.MongoClient('mongodb+srv://prada:prada@prada.qnsvb.mongodb.net/?retryWrites=true&w=majority')
db = mongodb.get_database("discord").get_collection("welcoming")
blacklist = mongodb.get_database("discord").get_collection("blacklists")

color = 0x2f3136
class System(commands.Cog):
    def __init__(self, client):
        self.client = client
        self.blacklist = blacklist

        @commands.command()
        @commands.cooldown(1,3, commands.BucketType.channel)
        async def appeal(self, ctx):
         if blacklist.find_one({ 'user_id' : ctx.author.id }):
          if ctx.guild is None:
           await ctx.send(f"{ctx.author.mention}\nDM vorqz#6666 your appeal request!")
          channel = client.get_channel(864968374476079105)
          await channel.send(f"New Appeal Request From: {ctx.author.id}")
         else:
           await ctx.send("This command can only be used in DMs.")

    @commands.command()
    @commands.is_owner()
    @commands.cooldown(1, 2, commands.BucketType.channel)
    async def accept_appeal(self, ctx, *, member: discord.Member):
      try:
        await member.send("You request has been accepted! Thanks for using Haunting.")
        await ctx.send("Sent!")
      except:
        await ctx.send("Failed to send.")

    @commands.command()
    @commands.is_owner()
    async def blacklist(self, ctx, userid: int, reason=None):
        if blacklist.find_one({'user_id': userid}):
            await ctx.send(
                embed=create_embed(
                    'That Member has already been blacklisted.'
                )
            )
        else:
            if self.client.get_user(userid) != None:
                blacklist.insert_one({'user_id': userid})
                await ctx.send(
                    embed=create_embed(
                        f'<@{userid}> is now **blacklisted** from using Haunting.'
                    )
                )
               # user = self.client.get_user(userid)
               # await user.send(embed=create_embed(f'You have been **__blacklisted__** from using Haunting.\nReason: `{reason}`'))
            else:
                await ctx.send(
                    embed=create_embed(
                        'Unknown Member. Please make sure that the member you have mentioned is in a server that I am in!'
                    ),
                    delete_after=30
                )

    @commands.command()
    @commands.is_owner()
    async def showblacklist(self, ctx, page: int = 1):
        output = ''
        blacklisted = blacklist.find()
        pages = math.ceil(blacklisted.count()/10)
        if 1 <= page <= pages:
            counter = 1+(page-1)*10
            for user in blacklisted[(page-1)*10:page*10]:
                user = self.client.get_user(user['user_id'])
                output += f'**{counter}.** `{user.name}` | `{user.id}`\n'
                output += f'**{counter}.** `{user}` | `{user}`\n'
                counter += 1
            embed = discord.Embed(
                colour=discord.Colour.from_rgb(136,3,252),
                title='**__Blacklisted Users__**',
                description=output,
                timestamp=ctx.message.created_at
            )
            embed.set_footer(
                text=f'Page {page} of {pages}'
            )
            await ctx.send(
                embed=embed
            )
        else:
            await ctx.send(
                embed=create_embed(
                    'The specified page does not exist'
                ),
                delete_after=10
            )
            

    @commands.command()
    @commands.is_owner()
    async def unblacklist(self, ctx, userid: int):
        if blacklist.find_one({'user_id': userid}):
            blacklist.delete_one({'user_id': userid})
            await ctx.send(
                embed=create_embed(
                    f'The member <@{userid}> has been unblacklisted.'
                ),
                delete_after=30
            )
        else:
            await ctx.send(
                embed=create_embed(
                    f'The member <@{userid}> is not blacklisted.'
                ),
                delete_after=10
            )


    @commands.command()
    @commands.is_owner()
    async def load(self, ctx, extension):
      try:
        self.client.load_extension(f'cogs.{extension}')
        await ctx.send(f"Loaded {extension}")
      except Exception as e:
          print(f"error: {e}")
    @commands.command()
    @commands.is_owner()
    async def unload(self, ctx, extension):
      try:
        self.client.unload_extension(f'cogs.{extension}')
        await ctx.send(f"Unloaded {extension}")
      except Exception as e:
          await ctx.send(f"error: {e}")



    @commands.command()
    @commands.is_owner()
    async def sync(self, ctx):
        msg = await ctx.send(f"snycing...")
        cogs=0
        try:
          for filename in os.listdir('./cogs'):
            if filename.endswith('.py') and not filename.startswith('System'):
              self.client.reload_extension(f'cogs.{filename[:-3]}')
              cogs += 1
          await msg.edit(f"synced {cogs} cog(s)")
        except:
            await msg.edit(f"got a error while sycning cogs")




    @commands.command()
    async def botclean(self, ctx, amount: int):
     if ctx.message.author.id == 712969671766442024 or ctx.message.author.id == 884155340327899227:
        await ctx.message.delete()
        async for message in ctx.message.channel.history(limit=amount).filter(lambda m: m.author == self.client.user).map(lambda m: m):
            try:
                    await message.delete()
            except:
                pass
     else:
       return

    @commands.command()
    @blacklist_check()
    @commands.cooldown(1,5, commands.BucketType.user)
    async def shutdown(self, ctx):
        if ctx.author.id == 712969671766442024:
           await ctx.send("Shuting down....")
           await self.client.logout()
        else:
           return

def setup(client):
    client.add_cog(System(client))