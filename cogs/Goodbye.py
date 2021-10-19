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
class Goodbye(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.group(invoke_without_command=True)
    @commands.cooldown(1, 3, commands.BucketType.user)
    async def goodbye(self, ctx):
        embed = discord.Embed(title="Goodbye | Help", color=color)
        embed.add_field(name="usage", value="goodbye message {message}\ngoodbye channel {channel}\ngoodbye test, goodbye variables", inline=False)
        embed.add_field(name="What they do", value="goodbye message - Sets the goodbye message\ngoodbye channel - Sets the goodbye channel\ngoodbye test - Shows you what the goodbye message would look like\ngoodbye variables - Shows the goodbye variables", inline=False)
        embed.add_field(name="variables", value="{user.name} - Sends the users name\n{user.mention} - Mentions the user\n{user} - Sends the users name and tag\n{user.tag} - Sends the users tag\discriminator\n{server} - Sends the servers name", inline=False)
        await ctx.send(embed=embed)

    @goodbye.command()
    @blacklist_check()
    @commands.cooldown(1, 3, commands.BucketType.channel)
    async def variables(self, ctx):
        embed = discord.Embed(title = "Haunting", description="{user.name} - Sends the users name\n{user.mention} - Mentions the user\n{user} - Sends the users name and tag\n{user.tag} - Sends the users tag\discriminator\n{server} - Sends the servers name", color=color)
        await ctx.send(embed=embed)

    @goodbye.command(aliases=["msg","message"])
    @blacklist_check()
    @commands.has_permissions(administrator=True)
    @commands.cooldown(1, 3, commands.BucketType.user)
    async def goodbyemessagelol(self, ctx, *, msg=None):
      if msg == None:
        embed = discord.Embed(color=error,description=f"input a message")
        await ctx.send(embed=embed)
      else:
        db4.update_one({"guild_id": ctx.guild.id},{"$set": {f"goodbyemessage": f'{msg}'}})
        embed = discord.Embed(description=f'Succesfully **set** the goodbye message',color=sucess)
        await ctx.send(embed=embed)
    
    @goodbye.command(aliases=["channelset", "channel", "chan"])
    @blacklist_check()
    @commands.has_permissions(administrator=True)
    @commands.cooldown(1, 3, commands.BucketType.user)
    async def goodbyechanlol(self, ctx, channel: discord.TextChannel = None):
      if channel == None:
        embed = discord.Embed(color=error,description=f'input a message')
        await ctx.send(embed=embed)
      else:
        db4.update_one({"guild_id": ctx.guild.id},{"$set": {f"goodbyechannel": f'{channel.id}'}})
        embed = discord.Embed(description=f'Succesfully **set** the goodbye channel', color=sucess)
        await ctx.send(embed=embed)
    @goodbye.command()
    @blacklist_check()
    @commands.cooldown(1,3, commands.BucketType.user)
    async def test(self, ctx):
       goodbyemessage = db4.find_one({ "guild_id": ctx.guild.id})['goodbyemessage']
       if goodbyemessage == None or goodbyemessage == "off":
         embed = discord.Embed(color=color,description='No goodbye message set')
         await ctx.send(embed=embed)
         return
       else:
                     goodbyemessage = goodbyemessage.replace("{server}", ctx.guild.name)
                     goodbyemessage = goodbyemessage.replace("{user.mention}", ctx.author.mention)
                     goodbyemessage = goodbyemessage.replace("{user.name}", ctx.author.name)
                     goodbyemessage = goodbyemessage.replace("{user}", str(ctx.author))
                     goodbyemessage = goodbyemessage.replace("{user.tag}", str(ctx.author.discriminator))
                     await ctx.send(goodbyemessage)
                     embed=discord.Embed(color=sucess,description=f' Successfuly **tested** the goodbye message')
                     await ctx.send(embed=embed)


def setup(client):
    client.add_cog(Goodbye(client))