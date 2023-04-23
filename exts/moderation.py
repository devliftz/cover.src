import hypecord
from hypecord.ext import commands
from datetime import timedelta
import datetime
import humanfriendly
from core.emojis import *

class Moderation(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.has_permissions(kick_members=True)
    async def kick(self, ctx, member: hypecord.Member, *, reason=None):
        embed = hypecord.Embed(title="",
                               description=f"""> {check} **{member.mention} Has been kicked**""",
                               color=0xffffff)
        embed.set_author(icon_url=f"https://cdn.discordapp.com/avatars/1096484859477754008/9e83d8a91e95366569c5274f1a66d9b3?size=1024", name="cover")
        await member.kick(reason=reason)
        await ctx.reply(embed=embed)

    @commands.command()
    @commands.has_permissions(ban_members=True)
    async def ban(self, ctx, member: hypecord.Member, *, reason=None):
        embed = hypecord.Embed(title="",
                               description=f"""> {check} **Banned {member.mention}**""",
                               color=0xffffff)
        embed.set_author(icon_url=f"https://cdn.discordapp.com/avatars/1096484859477754008/9e83d8a91e95366569c5274f1a66d9b3?size=1024", name="cover")
        await member.ban(reason=reason)
        await ctx.reply(embed=embed)

    @commands.command()
    @commands.has_permissions(manage_messages=True)
    async def purge(self, ctx, amount: int):
        embed = hypecord.Embed(title="",
                               description=f"""> {check} **Purged {amount} messages**""",
                               color=0xffffff)
        embed.set_author(icon_url=f"https://cdn.discordapp.com/avatars/1096484859477754008/9e83d8a91e95366569c5274f1a66d9b3?size=1024", name="cover")
        await ctx.channel.purge(limit=amount)
        await ctx.send(embed=embed)

    @commands.command()
    @commands.has_permissions(manage_messages=True)
    async def slowmode(self, ctx, seconds: int):
        embed = hypecord.Embed(title="",
                            description=f"""> {check} **Slowmode set to** `{seconds}` **by {ctx.author.mention}**""",
                            color=0xffffff)
        embed.set_author(icon_url=f"https://cdn.discordapp.com/avatars/1096484859477754008/9e83d8a91e95366569c5274f1a66d9b3?size=1024", name="cover")
        await ctx.channel.edit(slowmode_delay=seconds)
        await ctx.reply(embed=embed)

        if seconds <= 21601:
            embed = hypecord.Embed(title="",
                            description=f"""> {warning} **{ctx.author.mention} Max value is 21600**""",
                            color=0xffffff)
            embed.set_author(icon_url=f"https://cdn.discordapp.com/avatars/1096484859477754008/9e83d8a91e95366569c5274f1a66d9b3?size=1024", name="cover")
            await ctx.reply(embed=embed)
        elif seconds >= 0:
            embed = hypecord.Embed(title="",
                            description=f"""> {warning} **{ctx.author.mention} Slowmode cannot be negative**""",
                            color=0xffffff)
            embed.set_author(icon_url=f"https://cdn.discordapp.com/avatars/1096484859477754008/9e83d8a91e95366569c5274f1a66d9b3?size=1024", name="cover")
            await ctx.reply(embed=embed)

    @commands.command()
    @commands.has_permissions(manage_messages=True)
    async def unslowmode(self, ctx):
        embed = hypecord.Embed(title="",
                            description=f"""> {check} **Slowmode disabled by {ctx.author.mention}**""",
                            color=0xffffff)
        embed.set_author(icon_url=f"https://cdn.discordapp.com/avatars/1096484859477754008/9e83d8a91e95366569c5274f1a66d9b3?size=1024", name="cover")
        await ctx.channel.edit(slowmode_delay=0)
        await ctx.reply(embed=embed)

    @commands.command()
    @commands.has_permissions(moderate_members=True)
    async def mute(self, ctx, member: commands.MemberConverter, time):
        time = humanfriendly.parse_timespan(time)
        embed = hypecord.Embed(title="",
                               description=f"""> {check} **Muted {member}**""",
                               color=0xffffff)
        embed.set_author(icon_url=f"https://cdn.discordapp.com/avatars/1096484859477754008/9e83d8a91e95366569c5274f1a66d9b3?size=1024", name="cover")
        await member.edit(timed_out_until=hypecord.utils.utcnow()+datetime.timedelta(seconds=time))
        await ctx.reply(embed=embed)

    @commands.command()
    @commands.has_permissions(moderate_members=True)
    async def unmute(self, ctx, member: commands.MemberConverter):
        embed = hypecord.Embed(title="",
                               description=f"""> {check} **Unmuted {member}**""",
                               color=0xffffff)
        embed.set_author(icon_url=f"https://cdn.discordapp.com/avatars/1096484859477754008/9e83d8a91e95366569c5274f1a66d9b3?size=1024", name="cover")
        await member.edit(timed_out_until=hypecord.utils.utcnow()+datetime.timedelta(seconds=0))
        await ctx.reply(embed=embed)

    @commands.has_permissions(manage_messages=True)
    @commands.command(pass_context=True, name="lockdown")
    async def lockdown(self, ctx):
        overwrites_everyone = ctx.message.channel.overwrites_for(self.bot.everyone_role)
        if overwrites_everyone.send_messages == False:
            embed = hypecord.Embed(title="",
                               description=f"""> {locked} **Channel is allready locked down**""",
                               color=0xffffff)
            embed.set_author(icon_url=f"https://cdn.discordapp.com/avatars/1096484859477754008/9e83d8a91e95366569c5274f1a66d9b3?size=1024", name="cover")
            await ctx.reply(embed=embed)
            return
        overwrites_everyone.send_messages = False
        embed = hypecord.Embed(title="",
                           description=f"""> {locked} **Locked {ctx.message.channel.mention}. Only staff members may speak**""",
                           color=0xffffff)
        embed.set_author(icon_url=f"https://cdn.discordapp.com/avatars/1096484859477754008/9e83d8a91e95366569c5274f1a66d9b3?size=1024", name="cover")
        await ctx.reply(embed=embed)
        await self.bot.edit_channel_permissions(ctx.message.channel, self.bot.eve, overwrites_everyone)

async def setup(client):
    await client.add_cog(Moderation(client))