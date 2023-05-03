import json
import discord
from discord.ext import commands
from discord import ActionRow, Button
import asyncio

class Developer(commands.Cog, ):
    def __init__(self, Client):
        self.client = Client
    
    @commands.command(aliases=["bl"])
    async def blacklist(self, ctx, member: discord.Member = None): # type: ignore
        try:
            with open("./src/config/blacklist.json", "r") as f:
                blacklist_data = json.load(f)

            if str(member.id) in blacklist_data:
                del blacklist_data[str(member.id)]
                with open("./src/config/blacklist.json", "w") as f:
                    json.dump(blacklist_data, f, indent=4)
                await ctx.send("User has been unblacklisted.")
            else:
                blacklist_data[str(member.id)] = True
                with open("./src/config/blacklist.json", "w") as f:
                    json.dump(blacklist_data, f, indent=4)
                    await ctx.send("User has been blacklisted.")  
        except Exception as e:
            print(f"An error occurred: {e}")

    @commands.command()
    @commands.is_owner()
    async def leave(self, ctx, server: discord.Guild):
        await self.client.leave(server=server)
        embed = discord.Embed(title="",
                              description=f"**Leaving** `{server.name}`",
                              color=0xffffff)
        await ctx.reply(embed=embed)

    @commands.command()
    @commands.is_owner()
    async def guilds(self, ctx):
        guilds = self.client.guilds
        await ctx.reply(f"{guilds}")

async def setup(client):
    await client.add_cog(Developer(client))