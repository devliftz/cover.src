import discord
from discord.ext import commands
import json

class Tools(commands.Cog):
    def __init__(self, Client):
        self.client = Client
    
    @commands.group(name='tool')
    async def tool(self, ctx):
        
        
        if ctx.invoked_subcommand == None:
            list = discord.Embed(title="",
                                 description=f"""**{ctx.author.mention}, provide tool you want to use**""",
                                 color=0xffffff)
            list.add_field(name="Info",
                           value="""```ansi
[1;31m.server[0;0m [1;1m - Get server info```
```ansi
[1;31m.user[0;0m [1;1m - Get user info```""")
            await ctx.reply(embed=list)

    @tool.command()
    async def user(self, ctx, user: discord.Member):
        
        
        if user == None:
            user = ctx.author

        embed = discord.Embed(title="",
                              description=f"""**{user}`s, profile**""",
                              color=0xffffff)
        embed.add_field(name="Account Created",
                        value=f"> `{user.created_at}`",
                        inline=True)
        embed.add_field(name="User ID",
                        value=f"> `{user.id}`",
                        inline=True)
        embed.add_field(name="Status",
                        value=f"> `{user.status}`",
                        inline=False)
        embed.set_image(url=user.banner)
        embed.set_thumbnail(url=user.avatar)
        await ctx.reply(embed=embed)

    @tool.command()
    async def server(self, ctx, id: discord.Guild):
        
        
        embed = discord.Embed(title="",
                              description=f"""> **{id} Info**""",
                              color=0xffffff)
        embed.add_field(name="Guild Created",
                        value=f"`{id.created_at}`",
                        inline=True)
        embed.add_field(name="Members",
                        value=f"`{id.member_count}`",
                        inline=True)
        embed.add_field(name="Guild ID",
                        value=f"`{id.id}`",
                        inline=True)
        embed.add_field(name="Owner",
                        value=f"`{id.owner}`")
        embed.add_field(name="Invite Count",
                        value=f"`{id.invites()}`",
                        inline=True)
        embed.add_field(name="Vanity", 
                        value=f"`{id.vanity_invite()}`",
                        inline=True)
        embed.add_field(name="Channels",
                        value=f"{id.channels.count}")
        embed.add_field(name="Widget",
                        value=f"""```html
{id.widget()}```""", inline=False)
        embed.set_thumbnail(url=id.icon)
        await ctx.reply(embed=embed)

    @tool.command()
    async def platform(self, ctx, member: discord.Member):
        
        
        status_emojis = {
            discord.Status.online: "<:1415online:1088933656854282281>",
            discord.Status.idle: "<:dcidle:1095241881388064858>",
            discord.Status.dnd: "<:9008discorddnd:1088933650105643188>",
            discord.Status.offline: "<:dcoff:1095241885305552916>"
        }

        desktop_status = status_emojis.get(member.desktop_status, "❓")
        mobile_status = status_emojis.get(member.mobile_status, "❓")
        web_status = status_emojis.get(member.web_status, "❓")

        platform_embed = discord.Embed(title=f"{member.display_name}'s Platform Status", color=0xffffff)
        platform_embed.add_field(name="Desktop", value=desktop_status, inline=True)
        platform_embed.add_field(name="Mobile", value=mobile_status, inline=True)
        platform_embed.add_field(name="Web", value=web_status, inline=True)

        await ctx.send(embed=platform_embed)

    @tool.command()
    async def avatar(self, ctx, user: discord.Member):
        
        
        embed = discord.Embed(title="",
                              description=f"[**{user.mention}`s avatar**]({user.avatar})",
                              color=0xffffff)
        embed.set_image(url=user.avatar)
        embed.set_author(icon_url=user.avatar, name=user.name)
        await ctx.reply(embed=embed)

    @commands.command(aliases=['creds', 'c'])
    async def credits(self, ctx):
        
        
        embed = discord.Embed(title="",
                              description=f"**Cover** owned by <@1088473079824523405>",
                              color=0xffffff)
        embed.add_field(name="**Sponsors**",
                        value=f"""[**os#0039**](https://discord.com/users/944142110385377292) `Lead Developer`""")
        await ctx.reply(embed=embed)

async def setup(client):
    await client.add_cog(Tools(client))