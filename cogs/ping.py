import discord
from discord.ext import commands
import requests
import json

class Ping(commands.Cog):
    def __init__(self, Client):
        self.client = Client
        self.shards = self.client.shards
        self.description = "Check bot`s latency"
    
    @commands.command(description="Check shard latency")
    async def shard(self, ctx, shard_id: int):
        shard = self.client.get_shard(shard_id)
        if shard is None:
            await ctx.send("Invalid shard ID")
            return

        shard_info = await self.client.shard_at(shard_id) # Use the correct method name
        guild_count = shard_info["guild_count"]
        user_count = shard_info["user_count"]
        await ctx.send(f"Shard {shard_id} has {guild_count} guilds and {user_count} users")

async def setup(client):
    await client.add_cog(Ping(client))