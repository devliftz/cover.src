import discord
from discord.ext import commands

import json

def get_server_prefix(client, message):
    with open("config/prefixes.json", "r") as f:
        prefix = json.load(f)

    return prefix[str(message.guild.id)]

with open("config/bot.json", "r") as f:
    bcfg = json.load(f)

token = bcfg['TOKEN']

activity=discord.Activity(type=discord.ActivityType.listening, name=";")
bot = commands.AutoShardedBot(command_prefix=get_server_prefix, intents=discord.Intents().all(), shard_count=2, activity=activity)

@bot.event
async def on_ready():
    print("Reays")

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

bot.run(token, log_handler=None)