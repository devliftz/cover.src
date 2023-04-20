import discord
from discord.ext import commands
import json
import requests
from modules.formatter import Colorate, Colors
import os
from modules import handler
from modules import mobile

def get_server_prefix(client, message):
    with open("config/prefixes.json", "r") as f:
        prefix = json.load(f)

    return prefix[str(message.guild.id)]

with open("config/bot.json", "r") as f:
    bcfg = json.load(f)

token = bcfg['TOKEN']

bot = commands.AutoShardedBot(command_prefix=get_server_prefix, intents=discord.Intents().all(), shard_count=2)

shardusg = bot.shard_id

@bot.event
async def on_ready():
    handler.log(f"Logging in using static token")
    for filename in os.listdir('./cogs'):
        if filename.endswith('.py'):
            await bot.load_extension(f'cogs.{filename[:-3]}')

@bot.event
async def on_shard_ready(shard_id):
    handler.log(f"Shard ID: {shard_id} is ready!")

@bot.event
async def on_guild_join(guild):
    with open("config/prefixes.json", "r") as f:
        prefix = json.load(f)

    prefix[str(guild.id)] = ";"

    with open("config/prefixes.json", "w") as f:
        json.dump(prefix, f, indent=4)

@bot.event
async def on_guild_remove(guild):
    with open("config/prefixes.json", "r") as f:
        prefix = json.load(f)

    prefix.pop(str(guild.id))

    with open("config/prefixes.json", "w") as f:
        json.dump(prefix, f, indent=4)

@bot.command(aliases=["prefix", "changeprefix"])
async def setprefix(ctx, *, newprefix: str):

    if len(newprefix) > 2:
        embed_message = discord.Embed(
            color=(0x758A85),
            description=(f"> <:caution:1096425475590598836>  {ctx.author.mention}: Prefix is too large"),
        )
        await ctx.reply(embed = embed_message, mention_author=False)
    
    else:
        with open("config/prefixes.json", "r") as f:
            prefix = json.load(f)

        prefix[str(ctx.guild.id)] = newprefix

        with open("config/prefixes.json", "w") as f:
            json.dump(prefix, f, indent=4)

        embed_message = discord.Embed(
                color=(0x758A85),
                description=(f"> <:check:1096543207837421648> {ctx.author.mention}: Guild prefix changed to `{newprefix}`"),
            )
        await ctx.reply(embed = embed_message, mention_author=False)

bot.run(token)