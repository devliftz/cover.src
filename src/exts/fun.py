import discord
from discord.ext import commands
import random
import json
from core.emojis import *
import io
import contextlib
import json

class Fun(commands.Cog):
    def __init__(self, Client):
        self.client = Client

    @commands.command()
    async def ss(self, ctx, url):
        
        
        embed = discord.Embed(title="",
                              description=f"""**{ctx.author.mention}, here is** `{url}`""",
                              color=0xffffff)
        embed.set_thumbnail(url=url)
        await ctx.reply(embed=embed)

    @commands.command(aliases=['eb', 'eball'])
    async def eightball(self, ctx, *, question):
        
        
        words = ['No', 'Yes', 'Maybe', 'Never', '100% Yes']
        randomize = random.choice(words)
        embed = discord.Embed(title="",
                              description=f"""**{ctx.author.mention} >** `{question}`
                              
                              **8ball >** `{randomize}`""",
                              color=0xffffff)
        await ctx.reply(embed=embed)

    @commands.command()
    async def avatars(self, ctx):
        
        
        urls = ['https://cdn.discordapp.com/embed/avatars/0.png', 'https://cdn.discordapp.com/embed/avatars/1.png',
                'https://cdn.discordapp.com/embed/avatars/2.png', 'https://cdn.discordapp.com/embed/avatars/3.png',
                'https://cdn.discordapp.com/embed/avatars/4.png', 'https://cdn.discordapp.com/attachments/1103358333475356752/1103358878764240906/8569adcbd36c70a7578c017bf5604ea5.png',
                'https://cdn.discordapp.com/attachments/1103358333475356752/1103358879204651018/c82b3fa769ed6e6ffdea579381ed5f5c.png', 'https://cdn.discordapp.com/attachments/1103358333475356752/1103358879682793533/edallthetime.png',
                'https://cdn.discordapp.com/attachments/1103358333475356752/1103358880232259705/f7f2e9361e8a54ce6e72580ac7b967af.png', 'https://cdn.discordapp.com/attachments/1103358333475356752/1103358880953675846/6c5996770c985bcd6e5b68131ff2ba04.png',
                'https://cdn.discordapp.com/attachments/1103358333475356752/1103358881402458123/157e517cdbf371a47aaead44675714a3.png', 'https://cdn.discordapp.com/attachments/1103358333475356752/1103358881905787012/1628fc11e7961d85181295493426b775.png',
                'https://cdn.discordapp.com/attachments/1103358333475356752/1103358882455228498/5445ffd7ffb201a98393cbdf684ea4b1.png']
        randomize = random.choice(urls)
        embed = discord.Embed(title="",
                              description=f"""**{ctx.author.mention}, Here you go**""",
                              color=0xffffff)
        embed.set_image(url=randomize)
        await ctx.reply(embed=embed)

    @commands.group(name="github", aliases=['git', 'gh'])
    async def github(self, ctx):
        
        
        if ctx.invoked_subcommand == None:
            await ctx.reply("Provide an argument")

    @github.command()
    async def user(self, ctx, query: str):
        
        
        from urllib.request import urlopen

        url = f"https://api.github.com/users/{query}"
        response = urlopen(url)
        data_json = json.loads(response.read())

        username = data_json['login']
        user_url = data_json['url']
        folowers = data_json['followers']
        following = data_json['following']
        avatar_url = data_json['avatar_url']
        repos = data_json['public_repos']
        created = data_json['created_at']
        updated = data_json['updated_at']

        embed = discord.Embed(title="",
                              description=f"""{github} **User** [**{username}**]({user_url})""",
                              color=0xffffff)
        embed.add_field(name=f"**Followers: **", value=f"> **{folowers}**")
        embed.add_field(name=f"**Following: **", value=f"> **{following}**")
        embed.add_field(name=f"**Repos: **", value=f"> **{repos}**")
        embed.add_field(name=f"**Created: **", value=f"> **{created}**")
        embed.add_field(name=f"**Updated: **", value=f"> **{updated}**")
        embed.set_thumbnail(url=avatar_url)
    
        await ctx.reply(embed=embed)
        

    @commands.command(aliases=['py', 'pthon'])
    async def python(self, ctx, *, code: str):
        
        
        if code.startswith('```py'):
            code = code[6:-3].strip()
            try:
                with io.StringIO() as buf, contextlib.redirect_stdout(buf):
                    exec(code)
                    output = buf.getvalue().strip()
                    if output:
                        embed = discord.Embed(title="",
                              description=f"""> **Output**
                              ```py
{output}```""",
                              color=0xffffff)
                        embed.set_author(icon_url=f"https://cdn.discordapp.com/avatars/1096484859477754008/9e83d8a91e95366569c5274f1a66d9b3?size=1024", name="cover")
                        await ctx.reply(embed=embed)
                    else:
                        await ctx.send('No output')
            except Exception as e:
                await ctx.send(f'Error: {e}')
        else:
            await ctx.send('Invalid code block format')

    @commands.command()
    async def embedify(self, ctx, *, message):
        
        
        embed = discord.Embed(title="",
                              description=f"""**{message}**""",
                              color=0xffffff)
        await ctx.reply(embed=embed)

async def setup(client):
    await client.add_cog(Fun(client))