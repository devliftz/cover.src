import discord
from discord.ext import commands
import json
import requests
from modules.formatter import Colorate, Colors
import os
from modules import handler
from discord- import Dashboard
from modules import mobile

from modules.help_formatter import AppMenu, PrettyHelp

def get_server_prefix(client, message):
    with open("config/prefixes.json", "r") as f:
        prefix = json.load(f)

    return prefix[str(message.guild.id)]

with open("config/bot.json", "r") as f:
    bcfg = json.load(f)

token = bcfg['TOKEN']

menu = AppMenu(ephemeral=True)
ending_note = " "
bot = commands.AutoShardedBot(command_prefix=get_server_prefix, intents=discord.Intents().all(), shard_count=2, help_command=PrettyHelp(menu=menu, ending_note=ending_note), description="Commands For bot owner to manage its components")
bot_dashboard = Dashboard(bot,
	"secret_key", 
	"https://your-bot-website.com/dashboard"
)

shardusg = bot.shard_id

@bot.event
async def on_ready():
    handler.log(f"Logging in using static token")
    await bot.change_presence(status=discord.Status.online, activity=discord.Game(name="?"))

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

@bot.command(description="Change Server Prefix", aliases=["prefix", "changeprefix"])
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

@bot.command(description="Allows bot owner to reload all commands", aliases=["rs", "rb"])
async def restart(ctx):
    embed = discord.Embed(title="",
                          description=f"""> **Restarting**""",
                          color=0xffffff)
    await ctx.reply(embed=embed)
    for filename in os.listdir('./cogs'):
        if filename.endswith('.py'):
            await bot.reload_extension(f'cogs.{filename[:-3]}')

bot.run(token)