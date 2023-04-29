import discord
from discord.ext import commands
import traceback
from .emojis import *

async def on_command_error(ctx, error):
        if isinstance(error, commands.CommandNotFound):
            # Ignore command not found errors
            return

        if isinstance(error, commands.MissingPermissions):
            missingprem = discord.Embed(title="",
                           description=f"""> {warning} **{ctx.author.mention}, This command is admin only**""",
                           color=0x4e5058)
            missingprem.set_author(icon_url="https://cdn.discordapp.com/avatars/1096484859477754008/9e83d8a91e95366569c5274f1a66d9b3?size=1024", name="cover")
            await ctx.reply(embed=missingprem)
        elif isinstance(error, commands.BadArgument):
            badarg = discord.Embed(title="",
                           description=f"""> {warning} **{ctx.author.mention}, you provided an invalid argument**""",
                           color=0x4e5058)
            badarg.set_author(icon_url="https://cdn.discordapp.com/avatars/1096484859477754008/9e83d8a91e95366569c5274f1a66d9b3?size=1024", name="cover")
            await ctx.reply(embed=badarg)
        elif isinstance(error, commands.MissingRequiredArgument):
            if error.param.name == 'channel':
                embed = discord.Embed(title="",
                                    description=f"""> {channel} **{ctx.author.mention}, Please specify a channel**""",
                                    color=0x4e5058)
                embed.set_author(icon_url="https://cdn.discordapp.com/avatars/1096484859477754008/9e83d8a91e95366569c5274f1a66d9b3?size=1024", name="cover")
                await ctx.reply(embed=embed)
            
            else:
                bmissadarg = discord.Embed(title="",
                            description=f"""> {warning} **{ctx.author.mention}, please provide an argument**""",
                            color=0x4e5058)
                bmissadarg.set_author(icon_url="https://cdn.discordapp.com/avatars/1096484859477754008/9e83d8a91e95366569c5274f1a66d9b3?size=1024", name="cover")
                await ctx.reply(embed=bmissadarg)
        elif isinstance(error, commands.NotOwner):
            nowembed = discord.Embed(title="",
                                   description=f"""> {locked} **{ctx.author.mention}, this command is locked to bot owner**""",
                                   color=0x4e5058)
            nowembed.set_author(icon_url="https://cdn.discordapp.com/avatars/1096484859477754008/9e83d8a91e95366569c5274f1a66d9b3?size=1024", name="cover")
            await ctx.reply(embed=nowembed)
        elif isinstance(error, commands.CommandOnCooldown):
            coold = discord.Embed(title="",
                           description=f"""> {warning} **{ctx.author.mention}, This command is on cooldown**""",
                           color=0x4e5058)
            coold.set_author(icon_url="https://cdn.discordapp.com/avatars/1096484859477754008/9e83d8a91e95366569c5274f1a66d9b3?size=1024", name="cover")
            await ctx.reply(embed=coold)
        else:
            print(f"Ignoring exception in command {ctx.command}:")
            traceback.print_exception(type(error), error, error.__traceback__)