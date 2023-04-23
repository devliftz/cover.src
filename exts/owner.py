import hypecord
from hypecord.ext import commands
import requests
import json
from urllib.request import urlopen
from core.emojis import *
from urllib.error import HTTPError
import time

class AppOwner(commands.Cog):
    def __init__(self, Client):
        self.client = Client
        self.description = """Owner commands only etc. ?prefixes"""

    @commands.command(description="Get list of every bot prefix")
    async def prefixes(self, ctx):
        with open("./config/prefixes.json", "r") as f:
            pr = f.read()

        embed = hypecord.Embed(title="",
                              description=f"""```json
{pr}```""",
                              color=0xffffff)
        embed.set_author(icon_url=f"https://cdn.discordapp.com/avatars/1096484859477754008/9e83d8a91e95366569c5274f1a66d9b3?size=1024", name="cover")
        await ctx.reply(embed=embed)

    @commands.command(aliases=['bl'])
    async def blacklist(self, ctx, user: hypecord.Member = None):
        with open("./config/blacklist.json", "r") as f:
            blc = f.read()

        embed = hypecord.Embed(title="",
                              description=f"""```json
{blc}```""",
                              color=0xffffff)
        embed.set_author(icon_url=f"https://cdn.discordapp.com/avatars/1096484859477754008/9e83d8a91e95366569c5274f1a66d9b3?size=1024", name="cover")
        await ctx.reply(embed=embed)

    @commands.command(aliases=['aif'])
    @commands.is_owner()
    async def api(self, ctx, api):
        url = f"http://api.icey.fr/{api}.json"
        load = hypecord.Embed(title="",
                              description=f"""> **Loading..**""",
                              color=0xffffff)
        load.set_author(icon_url=f"https://cdn.discordapp.com/avatars/1096484859477754008/9e83d8a91e95366569c5274f1a66d9b3?size=1024", name="cover")
        loadem = await ctx.reply(embed=load)
        time.sleep(.5)
        try:
            response = urlopen(url)
        except HTTPError as e:
            if e.code == 404:
                errorembed = hypecord.Embed(title="",
                            description=f"""> **Error 404. This resource doesnt exist** ```json
{
    "error": "not_found"
}```""",
                                    color=0xffffff)
                errorembed.set_author(icon_url=f"https://cdn.discordapp.com/avatars/1096484859477754008/9e83d8a91e95366569c5274f1a66d9b3?size=1024", name="cover")
                await loadem.edit(embed=errorembed)
                return
            else:
                raise

        data_json = json.loads(response.read())
        formatted_json = json.dumps(data_json, indent=2)
        foundembed = hypecord.Embed(title="",
                            description=f"""```json
{formatted_json}```""",
                            color=0xffffff)
        foundembed.set_author(icon_url=f"https://cdn.discordapp.com/avatars/1096484859477754008/9e83d8a91e95366569c5274f1a66d9b3?size=1024", name="cover")
        await loadem.edit(embed=foundembed)

    @commands.command()
    @commands.is_owner()
    async def reload(self, ctx):
        embed = hypecord.Embed(title="", description="> **Reloading cogs**\n\n", color=0xffffff)
        embed.set_author(icon_url=f"https://cdn.discordapp.com/avatars/1096484859477754008/9e83d8a91e95366569c5274f1a66d9b3?size=1024", name="cover")

        cog_list = ""
        for cog in self.client.cogs:
            await self.client.reload_extension(f"cogs.{cog.lower()}")
            cog_list += f"- **{cog}**\n"
        embed.description += cog_list

        msg = await ctx.send(embed=embed)
        for cog in self.client.cogs:
            embed.description = embed.description.replace(f"- **{cog}**\n", f"**{cog}** {check}\n")
            await msg.edit(embed=embed)

        await msg.edit(embed=embed)

async def setup(client):
    await client.add_cog(AppOwner(client))