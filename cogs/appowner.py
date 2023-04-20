import discord
from discord.ext import commands
import requests
import json

class AppOwner(commands.Cog):
    def __init__(self, Client):
        self.client = Client
        self.description = """Owner commands only etc. ?prefixes"""
    
    @commands.command(description="Get list of every bot prefix")
    async def prefixes(self, ctx):
        with open("./config/prefixes.json", "r") as f:
            pr = f.read()

        embed = discord.Embed(title="",
                              description=f"""```json
                              {pr}```""",
                              color=0xffffff)
        embed.set_author(icon_url=f"https://cdn.discordapp.com/avatars/1096484859477754008/c912fe6323c3885f5d42302b7caa0812?size=1024", name="Cover")
        await ctx.reply(embed=embed)

async def setup(client):
    await client.add_cog(AppOwner(client))