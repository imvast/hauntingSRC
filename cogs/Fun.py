import discord
from discord.ext import commands
import random
import requests
import pymongo
import os
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


class Fun(commands.Cog):
    def __init__(self, client):
        self.client = client
    
    @commands.command()
    @blacklist_check()
    @commands.cooldown(1, 4, commands.BucketType.user)
    async def hug(self, ctx, member: discord.Member):
      if member is None:
        embed=discord.Embed(description="**input a `user` to hug.", color=color)
        await ctx.send(embed=embed)
      hugg = requests.get("https://nekos.life/api/v2/img/hug")
      res = hugg.json()
      embed=discord.Embed(description=f"`{ctx.author.name}` **hugged** `{member.name}`", color=color)
      embed.set_image(url=res["url"])
      await ctx.send(embed=embed)
    @commands.command()
    @commands.cooldown(1, 3, commands.BucketType.user)
    @blacklist_check()
    async def dadjoke(self, ctx):
          url = "https://dad-jokes.p.rapidapi.com/random/joke"
          example = requests.get(url, headers={
           'x-rapidapi-host': "dad-jokes.p.rapidapi.com",
            'x-rapidapi-key': "b427ebd9b7mshdec22c93a021bb2p1f73f2jsn931eaddd67c4"})

          get_json = example.json()
          await ctx.send(get_json['body'][0]['setup'])
          await ctx.send(get_json['body'][0]['punchline'])
  
    @commands.command()
    @blacklist_check()
    @commands.cooldown(1, 4, commands.BucketType.user)
    async def slap(self, ctx, member: discord.Member=None):
      if member is None:
        embed=discord.Embed(description="input a **user**", color=color)
        await ctx.send(embed=embed)
      else:
        slapp = requests.get("https://nekos.life/api/v2/img/slap")
        res = slapp.json()
        embed=discord.Embed(description=f"`{ctx.author.name}` **slapped** `{member.name}`",color=color)
        embed.set_image(url=res["url"])
        await ctx.send(embed=embed)

    @commands.command()
    @blacklist_check()
    @commands.cooldown(1, 4, commands.BucketType.user)
    async def hack(self, ctx, *, member: discord.Member):
      responses = [
        f"{member.name}@fatgmail.com", f"{member.name}@hotmom.com",
        f"{member.name}@gaylord.com", f"{member.name}@gaymail.com"
        f"{member.name}@hentaimaster.com"
    ]

      password = [
        f"gaymailxoxo", f"{member.name}isgayxo", f"imabitch",
        f"bigdick{member.name}"
      ]
      websites = [
        f"fatbitchesfightingoverfood.com",
        f"ilovehentai.com",
        f"vorqzisdaddy.com",
    f"stopchangingyournameproxyorsinful.com",
        f"https://www.pornhub.com/home/search/gay", f"bigfreecocks.com",         f"howtomakeyourpplarger.com"
      ]
      ipad = [f"135.791.113", f"123.456.789", f"987.654.321", f"696.969.690"]
      msgs = [
        f"Why is my dick so little?", f"How do I tell my friends I'm gay",
        f"I'm stuck inside the washing machine", f"vorqz is so sexy bro", f"Send nudes", "I'm gay"
      ]
      messags = [
        f"Gay", f"Cock", f"Fuck", f"ilydaddy", f"vorqz",
f"fatbitchesfightingoverfood", "Fap", "OOP"
      ]
      if member == ctx.message.author:
        emb = discord.Embed(color=color,
                            description="You cannot hack yourself.")
        emb.set_author(
            name='Error : Author',
            icon_url='https://www.freeiconspng.com/uploads/error-icon-4.png')
        await ctx.send(embed=emb)
        return

      if member == member.id:
        member = member
      message = await ctx.send(f"Hacking {member.name}")
      await asyncio.sleep(3)
      await message.edit(content=f"Finding {member.name}'s Discord Info..")
      asyncio.sleep(3)
      await message.edit(content=f"Cracking {member.name}'s Login Info..")
      await asyncio.sleep(2)
      await message.edit(content=f"Information now leaking..")
      await asyncio.sleep(2)
      await message.edit(
        content=
        f"Email:`{random.choice(responses)}`\n Password: `{random.choice(password)}`"
    )
      await asyncio.sleep(2)
      await message.edit(
          content=f"Finding {member.name}'s Most Recent Websites..")
      await asyncio.sleep(2)
      await message.edit(content=f"{random.choice(websites)}")
      await asyncio.sleep(2)
      await message.edit(content=f"Searching for {member.name}'s IP Address..")
      await asyncio.sleep(2)
      await message.edit(content=f"Found {member.name}'s IP Address")
      await asyncio.sleep(2)
      await message.edit(content=f"IP Address: `{random.choice(ipad)}`")
      await asyncio.sleep(3)
      await message.edit(content="Finding most used word..")
      await asyncio.sleep(2)
      await message.edit(content=f"Found {member.name}'s Most Common Word")
      await asyncio.sleep(2)
      await message.edit(content=f"Most common words: `{random.choice(msgs)}`")
      await asyncio.sleep(3)
      await message.edit(content="Finding most recent word..")
      await asyncio.sleep(2)
      await message.edit(content=f"Found {member.name}'s Most Recent Word")
      await asyncio.sleep(2)
      await message.edit(content=f"Most recent word: `{random.choice(messags)}`")
      await asyncio.sleep(2)
      await message.edit(content=f"Selling {member.name}'s Fortnite Account in the Dark Web")
      await asyncio.sleep(2)
      await message.edit(content=f"Hacked {member.mention}")

    @commands.command()
    @blacklist_check()
    @commands.cooldown(1, 4, commands.BucketType.user)
    async def kiss(self, ctx, member: discord.Member=None):
      if member is None:
        embed=discord.Embed(description="**input a `user` to kiss.**")
        await ctx.send(embed=embed)
      else:
        kisss = requests.get("https://nekos.life/api/v2/img/kiss")
        res = kisss.json()
        embed=discord.Embed(description=f"`{ctx.author.name}` **kissed** `{member.name}`",color=color)
        embed.set_image(url=res["url"])
        await ctx.send(embed=embed)


    @commands.command(aliases=['simp', 'simprate'])
    @blacklist_check()
    @commands.cooldown(1, 4, commands.BucketType.user)
    async def _simp(self, ctx, *, member: discord.Member=None):
      member = ctx.author if not member else member
      responses = ["Your 75% a simp.",
                "Your 100% a simp.",
                "You’re 5% simp.",
                "You’re 15% simp.",
                "You’re 25% simp.",
                "You're 85% simp.",
                "You’re 95% a simp.",
                "MF UR MAD SIMP 💀.",
                "You’re 100% simp.",
                "Your 90% simp.",
                "You’re 80% simp.",
                "You’re 70% simp.",
                "You’re 69% simp.",
                "You’re 60% simp.",
                "You’re 50% simp.",
                "You’re 40% simp..",
                "You’re 30% simp.",
                "You’re 20% simp.",
                "You’re 10% simp.",
                "You’re not a simp."]
      embed = discord.Embed(title=f"{member.name}'s simprate:", description=f"{random.choice(responses)}", color=color)
      await ctx.send(embed=embed)
    @commands.command()
    @blacklist_check()
    @commands.cooldown(1, 4, commands.BucketType.user)
    async def feed(self, ctx, member: discord.Member=None):
      if member is None:
        embed=discord.Embed(description="**input a `user` to feed.**",color = color)
        await ctx.send(embed=embed)
      else:
        feedd = requests.get("https://nekos.life/api/v2/img/feed")
        res = feedd.json()
        embed=discord.Embed(description=f"`{ctx.author.name}` **fed** `{member.name}`",color=color)
        embed.set_image(url=res["url"])
        await ctx.send(embed=embed)

    @commands.command(aliases=["ppsize"])
    @blacklist_check()
    @commands.cooldown(1, 4, commands.BucketType.user)
    async def pp(self, ctx,*, user: discord.Member = None):
       if user is None:
           user = ctx.author
           size = random.randint(1,50)
           ppsize = ""
           for _i in range(size):
               ppsize += "="
               embed = discord.Embed(title=f"{user}'s pp size", description=f"8{ppsize}D", colour=color)
           await ctx.send(embed=embed)

    @commands.command()
    @blacklist_check()
    @commands.cooldown(1, 4, commands.BucketType.user)
    async def pat(self, ctx, member: discord.Member=None):
      if member is None:
        embed=discord.Embed(description="  **input a `user` to pat.**")
        await ctx.send(embed=embed)
      else:
        patt = requests.get("https://nekos.life/api/v2/img/pat")
        res = patt.json()
        embed=discord.Embed(description=f"`{ctx.author.name}` **patted** `{member.name}`", color=color)
        embed.set_image(url=res["url"])
        await ctx.send(embed=embed)


    @commands.command(aliases=["8ball", "magicball", "hauntingball", "is", "question"])
    @blacklist_check()
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def _8ball(self, ctx, *, question):
      if question == None:
        embed=discord.Embed(description="**Specify a question**",color = color)
        await ctx.send(embed=embed)
      else:
        responses = ["it is certain", "Yes", "No", "Ask again later.", "As I see it, yes", "Signs point to yes", "Hell naw", "You may rely on it,", "Most likely", "better not tell you now", "Of course not", "Is that even a question?", "Negative", "Definetly not"]
        embed = discord.Embed(title=f'',description=f':8ball: | {random.choice(responses)}, `{ctx.author.name}`', color=color)
        await ctx.send(embed=embed)
        
    @commands.command()
    @blacklist_check()
    @commands.cooldown(1, 4, commands.BucketType.user)
    async def tickle(self, ctx, member: discord.Member=None):
      if member is None:
        embed=discord.Embed(description="**input a `user` to slap.**")
        await ctx.send(embed=embed)
      else:
        slapp = requests.get("https://nekos.life/api/v2/img/tickle")
        res = slapp.json()
        embed=discord.Embed(description=f"`{ctx.author.name}` **tickled** `{member.name}`",color=color)
        embed.set_image(url=res["url"])
        await ctx.send(embed=embed)



    @commands.command(aliases=['coin'])
    @blacklist_check()
    @commands.cooldown(1,5, commands.BucketType.user)
    async def coinflip(self, ctx):
       choices = ["heads", "tails"]
       embed = discord.Embed(title='Coinflip',description = f'{random.choice(choices)}', color=color)
       await ctx.send(embed=embed)
       print(f"{ctx.author.name} send a cmd in {ctx.guild.name}")



    @commands.command()
    @blacklist_check()
    @commands.cooldown(1,5, commands.BucketType.channel)
    async def teddy(self, ctx):
      await ctx.send("teddyW")

    @commands.command()
    @blacklist_check()  
    @commands.cooldown(1,5, commands.BucketType.channel)
    async def vorqz(self, ctx):
      await ctx.send("vorqzW ong")

    @commands.command()
    @blacklist_check()
    @commands.cooldown(1,5, commands.BucketType.channel)
    async def vert(self, ctx):
      await ctx.send("Beneekak")

    @commands.command()
    @blacklist_check()
    @commands.cooldown(1,5, commands.BucketType.channel)
    async def eclipze(self, ctx):
       await ctx.send("Eclipze is a dad")

    @commands.command()
    @blacklist_check()
    @commands.cooldown(1,5, commands.BucketType.channel)
    async def dark(self, ctx):
     await ctx.send("VorqzK")

    @commands.command()
    @blacklist_check()
    @commands.cooldown(1,5, commands.BucketType.channel)
    async def krzx(self, ctx):
      await ctx.send("krzx is better than vert")

    @commands.command()
    @blacklist_check()
    @commands.cooldown(1,5, commands.BucketType.channel)
    async def veltz(self, ctx):
      await ctx.send("idk")

    @commands.command()
    @blacklist_check()
    @commands.cooldown(1,5, commands.BucketType.channel)
    async def jaal(self, ctx):
        await ctx.send("ily jaal")



    @commands.command()
    @blacklist_check()
    @commands.cooldown(1,5, commands.BucketType.channel)
    async def vincx(self, ctx):
      await ctx.send("a kid")

    @commands.command()
    @blacklist_check()
    @commands.cooldown(1,5, commands.BucketType.channel)
    async def mason(self, ctx):
      await ctx.send("mason is a kool kid")

    @commands.command()
    @blacklist_check()
    @commands.cooldown(1,5, commands.BucketType.channel)
    async def bana(self, ctx):
     await ctx.send("banaWdiscordK")

    @commands.command()
    @blacklist_check()
    @commands.cooldown(1,5, commands.BucketType.channel)
    async def geb(self, ctx):
       await ctx.send("geb W")


    @commands.command()
    @blacklist_check()
    @commands.cooldown(1, 3, commands.BucketType.user)
    async def randomnumber(self, ctx):
    	embed = discord.Embed(title="Random Number",description=(random.randint(1, 101)),color=(color))
    	await ctx.send(embed=embed)



def setup(client):
    client.add_cog(Fun(client))