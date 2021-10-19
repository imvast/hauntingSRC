import discord
from discord.ext import commands
import pymongo
import asyncio
from discord_components import * 


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

# EMBED HELPER
def create_embed(text):
    embed = discord.Embed(
        description=text,
        colour=color,
    )
    return embed


color= 0x2f3136
color2=discord.Colour.random()
class Pagination(commands.Cog):
    def __init__(self, client):
        self.client = client
        DiscordComponents(client)
    



    @commands.command()
    async def pages(self, ctx):
      if ctx.author.id == 884155340327899227 or ctx.author.id == 712969671766442024 or ctx.author.id == 816679455581405255:
        current = 0
        embedOne = discord.Embed(title=f"**Haunting** help menu", description=f"**Prefix**: `.`\n\nWelcome to hauntings **Help Menu**, Each page will have a variety of command category, the command category will be displayed in the next page. If you want to invite haunting or want to suggest commands for it, the quick links will be below.\n\n**Quick Links:**\n[Support Server](https://discord.gg/4jn56QNKQv) | [Invite](https://discord.com/api/oauth2/authorize?client_id=854043897499484162&permissions=8&scope=bot)",color=0x5976ff)

        paginationList = [embedOne] 
        mainMessage = await ctx.send(
            embed = paginationList[current],
            components = [ #Use any button style you wish to :)
                [
                    Button(
                        label = "Back",
                        id = "back",
                        style = ButtonStyle.blue
                    ),
                    Button(
                    label = f"Page {int(paginationList.index(paginationList[current])) + 1}/{len(paginationList)}",
                    id = "cur",
                    style = ButtonStyle.grey,
                    disabled = True
                    ),
                    Button(
                        label = "Next",
                        id = "front",
                        style = ButtonStyle.blue
                    )
                ]
            ]
        )
        while True:
            try:
                interaction = await self.bot.wait_for(
                    "button_click",
                    check = lambda i: i.component.id in ["back", "front"],
                    timeout = 15.0
                )
                if interaction.component.id == "back":
                    current -= 1
                elif interaction.component.id == "front":
                    current += 1
                if current == len(paginationList):
                    current = 0
                elif current < 0:
                    current = len(paginationList) - 1

                await interaction.respond(
                    type = 7,
                     embed = paginationList[current],
                     components = [
                        [
                         Button(
                            label = "Back",
                            id = "back",
                            style = ButtonStyle.blue
                        ),
                        Button(
                            label = f"Page {int(paginationList.index(paginationList[current])) + 1}/{len(paginationList)}",
                            id = "cur",
                            style = ButtonStyle.grey,
                            disabled = True
                        ),
                        Button(
                            label = "Next",
                            id = "front",
                            style = ButtonStyle.blue
                        )
                    ]
                ]
            )
            except asyncio.TimeoutError:
              await mainMessage.edit(
                components = [
                    [
                        Button(
                            label = "back",
                            id = "back",
                            style = ButtonStyle.blue,
                            disabled = True
                        ),
                        Button(
                            label = f"Page {int(paginationList.index(paginationList[current])) + 1}/{len(paginationList)}",
                            id = "cur",
                            style = ButtonStyle.grey,
                            disabled = True
                        ),
                        Button(
                            label = "Next",
                            id = "front",
                            style = ButtonStyle.blue,
                            disabled = True
                        )
                    ]
                ]
            )
            break
        else:
          return 


def setup(client):
    client.add_cog(Pagination(client))