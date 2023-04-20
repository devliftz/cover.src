import discord
from discord.ext import commands
import requests
import json

class Moderating(commands.Cog):
    def __init__(self, Client):
        self.client = Client
        self.description = "Server moderating commands"

    @commands.command(description="Clear chat messages")
    @commands.has_permissions(manage_messages=True)
    async def clear(ctx, amount=5):
        await ctx.channel.purge(limit=amount+1)

async def setup(client):
    await client.add_cog(Moderating(client))