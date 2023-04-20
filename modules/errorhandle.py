import discord
from discord.ext import commands

class DiscordErrorHandler(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    async def send_error_message(self, ctx, error):
        embed = discord.Embed(title="Error", description=str(error), color=discord.Color.red())
        await ctx.send(embed=embed)

        print(f"Error: {error}")

    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        if isinstance(error, commands.CommandNotFound):
            return
        elif isinstance(error, commands.MissingPermissions):
            embed = discord.Embed(title="Error", description="You do not have permission to execute this command", color=discord.Color.red())
            await ctx.send(embed=embed)
            print(f"Error: {error}")
        else:
            await self.send_error_message(ctx, error)
