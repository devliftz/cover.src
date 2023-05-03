import discord
from discord.ext import commands
from core.emojis import *
from core.error import on_command_error
import os
import json
import hype
import pylast
from datetime import datetime
from discord_webhook import DiscordWebhook, DiscordEmbed

webhook = DiscordWebhook(url='https://discord.com/api/webhooks/1103360596893782028/ET9z_ahytBSbOIJHq1oRF6G3xAchxUmERLt8zvPpzapebFF7f9RPMvDC7r4pdaUhjqKG')

def get_server_prefix(client, message):
    with open("./src/config/prefixes.json", "r") as f:
        prefix = json.load(f)

    return prefix[str(message.guild.id)]

bot = commands.Bot(command_prefix=get_server_prefix, intents=discord.Intents.all(), help_command=None)
bot.on_command_error = on_command_error
hype.init(mobile=True)

@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name=f".help"))

    for filename in os.listdir('./src/exts'):
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
        with open("./src/config/prefixes.json", "r") as f:
            prefix = json.load(f)

        prefix[str(ctx.guild.id)] = newprefix

        with open("./src/config/prefixes.json", "w") as f:
            json.dump(prefix, f, indent=4)

        embed_message = discord.Embed(
                color=(0xffffff),
                description=(f"> {check} {ctx.author.mention}: Guild prefix changed to `{newprefix}`"),
            )
        await ctx.reply(embed = embed_message, mention_author=False)

@bot.event
async def on_guild_join(guild):
    discord_server_id = str(guild.id)
    server_name = guild.name
    server_icon = guild.icon
    server_owner = str(guild.owner)
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    join_log = bot.get_channel(1103344598333526066)

    embed = discord.Embed(title="",
                          description=f"> **I just joined** `{server_name}`",
                          color=0xffffff)
    embed.add_field(name="**ID**",
                    value=f"||`{discord_server_id}`||")
    embed.set_thumbnail(url=server_icon)
    embed.set_footer(text=":)")
    await join_log.send(embed=embed)

    with open("./src/config/prefixes.json", "r") as f:
        prefix = json.load(f)

    with open("./src/config/servers.json", "r") as f:
        servers = json.load(f)

    prefix[str(guild.id)] = "."

    servers[discord_server_id] = {
        "server_name": server_name,
        "server_owner": server_owner,
        "date_added": current_time
    }

    with open("./src/config/prefixes.json", "w") as f:
        json.dump(prefix, f, indent=4)

    with open("./src/config/servers.json", "w") as f:
        json.dump(servers, f, indent=4)

@bot.event
async def on_guild_remove(guild):
    with open("./src/config/prefixes.json", "r") as f:
        prefix = json.load(f)

    prefix.pop(str(guild.id))

    with open("./src/config/prefixes.json", "w") as f:
        json.dump(prefix, f, indent=4)

@bot.command()
async def prefixes(ctx):
    with open("./src/config/prefixes.json", "r") as f:
        prf = f.read()

    embed = discord.Embed(title="",
                          description=f"""```json
{prf}```""",
color=0xffffff)
    await ctx.reply(embed=embed)
    
@bot.command()
async def servers(ctx):
    with open("./src/config/servers.json", "r") as f:
        jso = f.read()

    embed = discord.Embed(title="",
                          description=f"""```json
{jso}```""",
color=0xffffff)
    await ctx.reply(embed=embed)

@bot.command()
@commands.is_owner()
async def reload(ctx):
    embed = discord.Embed(title="",
                          description=f"Reloading cogs",
                          color=0xffffff)
    
    for filename in os.listdir('./src/exts'):
        if filename.endswith('.py'):
            await bot.reload_extension(f'exts.{filename[:-3]}')

    await ctx.reply(embed=embed)

bot.run("MTA5NjQ4NDg1OTQ3Nzc1NDAwOA.G7k0iZ.nY3m7P9L-TlxaV1O_gc2Nbx2Lf-SC_0A12JAh0", log_handler=None)