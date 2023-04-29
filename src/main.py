import discord
from discord.ext import commands
from core.emojis import *
from core.error import on_command_error
import os
import json
import hype
import pylast

def get_server_prefix(client, message):
    with open("config/prefixes.json", "r") as f:
        prefix = json.load(f)

    return prefix[str(message.guild.id)]

bot = commands.AutoShardedBot(command_prefix=get_server_prefix, shard_count=1, intents=discord.Intents.all())
bot.on_command_error = on_command_error
hype.init(mobile=True)

@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name=f".help"))

    for filename in os.listdir('./exts'):
        if filename.endswith('.py'):
            await bot.load_extension(f'exts.{filename[:-3]}')

@bot.command(description="Change Server Prefix", aliases=["prefix", "changeprefix"])
async def setprefix(ctx, *, newprefix: str):

    if len(newprefix) > 2:
        embed_message = discord.Embed(
            color=(0xffffff),
            description=(f"> {warning} **{ctx.author.mention}: Prefix is too large**"),
        )
        await ctx.reply(embed = embed_message, mention_author=False)
    
    else:
        with open("config/prefixes.json", "r") as f:
            prefix = json.load(f)

        prefix[str(ctx.guild.id)] = newprefix

        with open("config/prefixes.json", "w") as f:
            json.dump(prefix, f, indent=4)

        embed_message = discord.Embed(
                color=(0xffffff),
                description=(f"> {check} {ctx.author.mention}: Guild prefix changed to `{newprefix}`"),
            )
        await ctx.reply(embed = embed_message, mention_author=False)

@bot.event
async def on_guild_join(guild):
    with open("config/prefixes.json", "r") as f:
        prefix = json.load(f)

    prefix[str(guild.id)] = "."

    with open("config/prefixes.json", "w") as f:
        json.dump(prefix, f, indent=4)

@bot.event
async def on_guild_remove(guild):
    with open("config/prefixes.json", "r") as f:
        prefix = json.load(f)

    prefix.pop(str(guild.id))

    with open("config/prefixes.json", "w") as f:
        json.dump(prefix, f, indent=4)

bot.run("TOKEN", log_handler=None)