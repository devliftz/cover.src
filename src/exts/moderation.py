import discord
from discord.ext import commands
from core.emojis import *
import json

class Moderation(commands.Cog):
    def __init__(self, Client):
        self.client = Client

    @commands.command()
    @commands.has_permissions(kick_members=True)
    async def kick(self, ctx, member: discord.Member, *, reason=None):
        
        
        embed = discord.Embed(title="",
                               description=f"""> {check} **{member.mention} Has been kicked**""",
                               color=0xffffff)
        embed.set_author(icon_url=f"https://cdn.discordapp.com/avatars/1096484859477754008/9e83d8a91e95366569c5274f1a66d9b3?size=1024", name="cover")
        await member.kick(reason=reason)
        await ctx.reply(embed=embed)

    @commands.command()
    @commands.has_permissions(ban_members=True)
    async def ban(self, ctx, member: discord.Member, *, reason=None):
        
        
        embed = discord.Embed(title="",
                               description=f"""> {check} **Banned {member.mention}**""",
                               color=0xffffff)
        embed.set_author(icon_url=f"https://cdn.discordapp.com/avatars/1096484859477754008/9e83d8a91e95366569c5274f1a66d9b3?size=1024", name="cover")
        await member.ban(reason=reason)
        await ctx.reply(embed=embed)

    @commands.command()
    @commands.has_permissions(manage_messages=True)
    async def purge(self, ctx, amount: int):
        
        
        embed = discord.Embed(title="",
                               description=f"""> {check} **Purged {amount} messages**""",
                               color=0xffffff)
        embed.set_author(icon_url=f"https://cdn.discordapp.com/avatars/1096484859477754008/9e83d8a91e95366569c5274f1a66d9b3?size=1024", name="cover")
        await ctx.channel.purge(limit=amount)
        await ctx.send(embed=embed)

    @commands.command()
    @commands.has_permissions(manage_messages=True)
    async def slowmode(self, ctx, seconds: int):
        
        
        embed = discord.Embed(title="",
                            description=f"""> {check} **Slowmode set to** `{seconds}` **by {ctx.author.mention}**""",
                            color=0xffffff)
        embed.set_author(icon_url=f"https://cdn.discordapp.com/avatars/1096484859477754008/9e83d8a91e95366569c5274f1a66d9b3?size=1024", name="cover")
        await ctx.channel.edit(slowmode_delay=seconds)
        await ctx.reply(embed=embed)    

    @commands.command()
    @commands.has_permissions(manage_messages=True)
    async def unslowmode(self, ctx):
        
        
        embed = discord.Embed(title="",
                            description=f"""> {check} **Slowmode disabled by {ctx.author.mention}**""",
                            color=0xffffff)
        embed.set_author(icon_url=f"https://cdn.discordapp.com/avatars/1096484859477754008/9e83d8a91e95366569c5274f1a66d9b3?size=1024", name="cover")
        await ctx.channel.edit(slowmode_delay=0)
        await ctx.reply(embed=embed)

    @commands.command()
    @commands.has_permissions(moderate_members=True)
    async def mute(self, ctx, member: commands.MemberConverter, time):
        
        
        time = humanfriendly.parse_timespan(time)
        embed = discord.Embed(title="",
                               description=f"""> {check} **Muted {member}**""",
                               color=0xffffff)
        embed.set_author(icon_url=f"https://cdn.discordapp.com/avatars/1096484859477754008/9e83d8a91e95366569c5274f1a66d9b3?size=1024", name="cover")
        await member.edit(timed_out_until=discord.utils.utcnow()+datetime.timedelta(seconds=time))
        await ctx.reply(embed=embed)

    @commands.command()
    @commands.has_permissions(moderate_members=True)
    async def unmute(self, ctx, member: commands.MemberConverter):
        
        
        embed = discord.Embed(title="",
                               description=f"""> {check} **Unmuted {member}**""",
                               color=0xffffff)
        embed.set_author(icon_url=f"https://cdn.discordapp.com/avatars/1096484859477754008/9e83d8a91e95366569c5274f1a66d9b3?size=1024", name="cover")
        await member.edit(timed_out_until=discord.utils.utcnow()+datetime.timedelta(seconds=0))
        await ctx.reply(embed=embed)
    
async def setup(client):
    await client.add_cog(Moderation(client))