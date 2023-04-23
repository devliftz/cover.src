import hypecord
from hypecord.ext import commands
from core.emojis import *
from core.error import on_command_error
import os
import json
import pylast

def get_server_prefix(client, message):
    with open("config/prefixes.json", "r") as f:
        prefix = json.load(f)

    return prefix[str(message.guild.id)]

bot = commands.AutoShardedBot(command_prefix=get_server_prefix, shard_count=1, intents=hypecord.Intents.all())
bot.on_command_error = on_command_error

@bot.event
async def on_ready():
    await bot.change_presence(activity=hypecord.Activity(type=hypecord.ActivityType.listening, name=f"Hi"))

    for filename in os.listdir('./exts'):
        if filename.endswith('.py'):
            await bot.load_extension(f'exts.{filename[:-3]}')

@bot.command(description="Change Server Prefix", aliases=["prefix", "changeprefix"])
async def setprefix(ctx, *, newprefix: str):

    if len(newprefix) > 2:
        embed_message = hypecord.Embed(
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

        embed_message = hypecord.Embed(
                color=(0xffffff),
                description=(f"> {check} {ctx.author.mention}: Guild prefix changed to `{newprefix}`"),
            )
        await ctx.reply(embed = embed_message, mention_author=False)

@bot.event
async def on_guild_join(guild):
    with open("config/prefixes.json", "r") as f:
        prefix = json.load(f)

    prefix[str(guild.id)] = "?"

    with open("config/prefixes.json", "w") as f:
        json.dump(prefix, f, indent=4)

@bot.event
async def on_guild_remove(guild):
    with open("config/prefixes.json", "r") as f:
        prefix = json.load(f)

    prefix.pop(str(guild.id))

    with open("config/prefixes.json", "w") as f:
        json.dump(prefix, f, indent=4)

bot.init("MTA5NjQ4NDg1OTQ3Nzc1NDAwOA.Gat6gS.5a4i99B82RUou1b9h-qH4qp8oHK86MouNWj-0s", mobile=True, api_key="NSKBG")