import discord
from discord.ext import commands
import random
import requests
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

color = 0x2f3136
os.system("pip install dnspython")
# Database Setup
mongodb = pymongo.MongoClient('mongodb+srv://prada:prada@prada.qnsvb.mongodb.net/?retryWrites=true&w=majority')
db = mongodb.get_database("discord").get_collection("welcoming")
blacklist = mongodb.get_database("discord").get_collection("blacklists")
class Help(commands.Cog):
    def __init__(self, client):
        self.client = client
    


    @commands.command(aliases=['h'])
    @commands.cooldown(1, 3, commands.BucketType.user)
    @blacklist_check()
    async def help(self, ctx):
        embed = discord.Embed(title=f"Haunting", description=f"""
        **Invite**: [Click here](https://discord.com/api/oauth2/authorize?client_id=854043897499484162&permissions=8&scope=bot%20applications.commands)
**Support**: Server [Click here](https://discord.gg/e6dqdZzFxu)""",color=color)
        embed.add_field(name="**Moderation**",value="""
`Ban`, `Kick`, `unbanall`, `purge`, `nuke`, `slowmode`, `offslowmode`, `botinvite`, `lock`, `unlock`, `idban`, `mute`, `unmute`, `setup`, `nick`, `unban`, `steal`, `jail`, `unjail`, `welcomechannel`, `welcomemessage`, `goodbye`, `goodbye message`, `autorole`, `punishment` """,inline=False)
        embed.add_field(name="**Fun**",value="""
`yomama`, `kiss`, `hug`, `tickle`, `slap`, `hack`, `simp`, `8ball`, `feed`, `pp`, `pat`, `coinflip`, `rob`, `bal`, `give`, `leaderboard`, `deposit`, `withdraw`, `randomnumber`, `poll`, `dadjoke`
""",inline=False)
        embed.add_field(name="**Utility**",value="""
`botinfo`,`Invite`, `settings`, `poll`,`Upvote`, `Avatar`, `userbanner`, `Uptime`, `Banner`, `servericon`, `Ping`, `Serverinfo`, `Userinfo`, `membercount`, `bug`, `getbotinvite`, `firstmessage`, `goodbye test`, `welcometest`, `invites`, `afk`, `userid`, `serverid`, `boosts`, `modules`, `perms`, `roleinfo`
""",inline=False)
        embed.add_field(name="**Anti-Nuke**",value="""
`Whitelist`, `Unwhitelist`, `Whitelisted`, `Settings`, `Toggle`, `punishment`
""",inline=False)
        embed.add_field(name="**Toggles**",value="""
`anti-ban`, `anti-kick`, `anti-channel-create`, `anti-role-create`, `anti-bot`, `anti-channel-delete`, `anti-role-delete`, `welcomemessage`, `welcomechannel`, `goodbyechannel`, `goodbyemessage`, `autorole`
""",inline=False)
        embed.add_field(name="**Developer**",value="""
`jsk`, `restart`, `shutdown`, `blacklist`, `unblacklist`, `showblacklist`, `load`, `unload`, `leave`, `sync`, `reload`, `botclean`, `guilds`
""",inline=False)
        await ctx.send(embed=embed)
  


def setup(client):
    client.add_cog(Help(client))