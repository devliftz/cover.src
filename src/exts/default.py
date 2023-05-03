import discord
from discord.ext import commands
import os
import random
import json

class Default(commands.Cog):
    def __init__(self, Client):
        self.client = Client
    
    @commands.command(aliases=['p', 'test'])
    async def ping(self, ctx):
        
        
        latency = self.client.latency
        words = ['e-girls', '9yo kids 🤡', 'ur mom', 'milk',
                 'discord', 'doxxed!', 'potato servers']
        random_word = random.choice(words)
        embed = discord.Embed(title="",
                              description=f"> **It took** `{latency}` to ping **{random_word}**",
                              color=0xffffff)
        await ctx.reply(embed=embed)

    @commands.group(name="help", aliases=['h', 'cmds'])
    async def help(self, ctx):
        
        
        if ctx.invoked_subcommand == None:
            list = discord.Embed(title="",
                                 description=f"""Made by [**nap.#4677**](https://discord.com/users/1088473079824523405) | Sponsored by [**os#0039**](https://discord.com/users/944142110385377292) ```ansi
[1;31m[][0;0m = Required Arguments
.help [1;31m[[0;0mcommand [1;31m|[0;0m subcommand[1;31m][0;0m```""",
color=0xffffff)
            list.add_field(name="**Default**",
                           value="`help`, `links`",
                           inline=False)
            list.add_field(name="**Tools**",
                           value="`tool`, `user [id]`, `server`, `credits`, `platform [user]`, `avatar`",
                           inline=False)
            list.add_field(name="**Fun**",
                           value="""`ss`, `eightball [question]`, `avatars`, `github user [username]`, `python [code]`, `embedify [text]`""",
                           inline=False)
            list.add_field(name="**Spotify**",
                           value="`spotify`, `album`, `skip`, `player`",
                           inline=False)
            list.add_field(name="**Moderation**",
                           value="`kick [user]`, `ban [user]`, `purge [ammount]`, `slowmode [time]`, `unslowmode`, `mute [user] [time]`, `unmute [user]`",
                           inline=False)
            list.add_field(name="**Owner Stuff**",
                           value="`prefix`, `leave`, `reload`",
                           inline=False)
            list.set_author(icon_url="https://cdn.discordapp.com/avatars/1096484859477754008/9e83d8a91e95366569c5274f1a66d9b3.png?size=1024", name="cover`s Help")
            await ctx.reply(embed=list)

    @help.command()
    async def cogs(self, ctx):
        
        
        files = os.listdir("./src/exts")
        file_names = [f for f in os.listdir("./src/exts") if os.path.isfile(os.path.join("./src/exts", f)) and f.endswith('.py')]

        embed = discord.Embed(title="",
                              description=f"""**Cogs List** ```
{file_names}```""",
                              color=0xffffff)
        await ctx.reply(embed=embed)

    @help.command()
    async def source(self, ctx):
        
        
        embed = discord.Embed(title="",
                              description=f"""cover`s Source code""",
                              color=0xffffff)
        embed.add_field(name="**Github**",
                        value="[**Repository**](https://github.com/devliftz/cover.src)")
        embed.add_field(name="**Join Our team**",
                        value="[**Forms**](https://jobs.icey.fr/cover-team)")
        await ctx.reply(embed=embed)

async def setup(client):
    await client.add_cog(Default(client))