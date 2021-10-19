import discord
from discord.ext import commands
import pymongo

def blacklist_check():
    def predicate(ctx):
        author_id = ctx.author.id
        if blacklist.find_one({'user_id': author_id}):
            return False
        return True
    return commands.check(predicate)
error = discord.Color.from_rgb(225,6,0)
sucess = discord.Color.from_rgb(8,255,8)

mongodb = pymongo.MongoClient('mongodb+srv://prada:prada@prada.qnsvb.mongodb.net/?retryWrites=true&w=majority')
db2 = mongodb.get_database("aries").get_collection("arieslol")
db4 = mongodb.get_database("leave").get_collection("goodbye")
db3 = mongodb.get_database("anti").get_collection("toggles")
db5 = mongodb.get_database("haunting").get_collection("toggles")
blacklist = mongodb.get_database("discord").get_collection("blacklists")


def create_embed(text):
    embed = discord.Embed(
        description=text,
        colour=color,
    )
    return embed


color= 0x2f3136
color2=discord.Colour.random()
class Welcome(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.group(invoke_without_command=True, aliases=["welc"])
    @blacklist_check()
    @commands.cooldown(1, 3, commands.BucketType.user)
    async def welcome(self,ctx):
        embed = discord.Embed(title="welcome | Help", color=color)
        embed.add_field(name="usage", value="welcome message {message}\nwelcome channel {channel}\nwelcome test\nwelcome variables", inline=False)
        embed.add_field(name="What they do", value="welcome message - Sets the welcome message\nwelcome channel - Sets the welcome channel\nwelcome test - Shows you what the welcome message would look like\nwelcome variables - Shows the goodbye variables", inline=False)
        embed.add_field(name="variables", value="{user.name} - Sends the users name\n{user.mention} - Mentions the user\n{user} - Sends the users name and tag\n{user.tag} - Sends the users tag\discriminator\n{server} - Sends the servers name", inline=False)
        await ctx.send(embed=embed)

    @welcome.command(aliases=["channel"])
    @blacklist_check()
    @commands.has_permissions(administrator=True)
    @commands.cooldown(1, 3, commands.BucketType.user)
    async def chan(self, ctx, channel: discord.TextChannel = None):
      if channel == None:
        embed = discord.Embed(color=error,description=f'input a channel')
        await ctx.send(embed=embed)
      else:
        db2.update_one({"guild_id": ctx.guild.id},{"$set": {f"welcomechannel": f'{channel.id}'}})
        embed = discord.Embed(description=f'succesfully **set** the welcome channel',color=sucess)
        await ctx.send(embed=embed)

    @welcome.command(aliases=["message"])
    @blacklist_check()
    @commands.has_permissions(administrator=True)
    @commands.cooldown(1, 3, commands.BucketType.user)
    async def msg(self, ctx, *, msg=None):
      if msg == None:
        embed = discord.Embed(color=error,description=f'input a message')
        await ctx.send(embed=embed)
      else:
        db2.update_one({"guild_id": ctx.guild.id},{"$set": {f"welcomemessage": f'{msg}'}})
        embed = discord.Embed(description=
		    f'Succesfully **set** the welcome message',color=sucess)
        await ctx.send(embed=embed)
        
    @welcome.command()
    @blacklist_check()
    @commands.cooldown(1,5, commands.BucketType.user)
    async def test(self, ctx):

       welcmsg = db2.find_one({ "guild_id": ctx.guild.id})['welcomemessage']
       if welcmsg == None or welcmsg == "off":
         embed = discord.Embed(color=error,description=f'No welcome message set')
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
            
    @welcome.command()
    @blacklist_check()
    @commands.cooldown(1, 3, commands.BucketType.channel)
    async def variables(self, ctx):
       embed = discord.Embed(title = "Haunting", description="{user.name} - Sends the users name\n{user.mention} - Mentions the user\n{user} - Sends the users name and tag\n{user.tag} - Sends the users tag\discriminator\n{server} - Sends the servers name", color=color)
       await ctx.send(embed=embed)


def setup(client):
    client.add_cog(Welcome(client))