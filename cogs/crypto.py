import discord
from discord.ext import commands
import requests
import json

class Crypto(commands.Cog, ):
    def __init__(self, Client):
        self.client = Client
        self.description = "Get latest information about crypto"

    @commands.command(description="View BitCoin Info", aliases=["bitcoin"])
    async def btc(self, ctx):

        url = "https://api.livecoinwatch.com/coins/single"

        payload = json.dumps({
        "currency": "USD",
        "code": "BTC",
        "meta": True
        })
        headers = {
        'content-type': 'application/json',
        'x-api-key': '27002a59-1626-42a4-a3e4-c689d3a959fe'
        }

        response = requests.request("POST", url, headers=headers, data=payload)

        data = response.json()

        positive_message = discord.Embed(
            color=(0x758A85),
        ).set_author(
            icon_url='https://imgs.search.brave.com/MTsPAq_Sim0sBrAlHHLon1UZQK5qA-0E6WSIv3-1BCc/rs:fit:1200:1200:1/g:ce/aHR0cHM6Ly9sb2dv/ZG93bmxvYWQub3Jn/L3dwLWNvbnRlbnQv/dXBsb2Fkcy8yMDE3/LzA2L2JpdGNvaW4t/bG9nby0xLTEucG5n',
            name='Bitcoin'
        ).add_field(name='Current Price', value=f'${str(round(data["rate"],2))}', inline=False
        ).add_field(name='Market Change', value=f'+{str(round(data["delta"]["day"],2))}%', inline=False)

        negetive_message = discord.Embed(
            color=(0x758A85),
        ).set_author(
            icon_url='https://imgs.search.brave.com/MTsPAq_Sim0sBrAlHHLon1UZQK5qA-0E6WSIv3-1BCc/rs:fit:1200:1200:1/g:ce/aHR0cHM6Ly9sb2dv/ZG93bmxvYWQub3Jn/L3dwLWNvbnRlbnQv/dXBsb2Fkcy8yMDE3/LzA2L2JpdGNvaW4t/bG9nby0xLTEucG5n',
            name='Bitcoin'
        ).add_field(name='Current Price', value=f'${str(round(data["rate"],2))}', inline=False
        ).add_field(name='Market Change', value=f'-{str(round(data["delta"]["day"],2))}%', inline=False)

        if data["delta"]["day"] > 1:
            await ctx.reply(embed = positive_message, mention_author=False)
        else: 
            await ctx.reply(embed = negetive_message, mention_author=False)

async def setup(client):
    await client.add_cog(Crypto(client))