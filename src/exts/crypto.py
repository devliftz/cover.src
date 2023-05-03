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
            color=(0xffffff),
        ).set_author(
            icon_url='http://api.icey.fr/icons/crypto/white/btc.png',
            name='Bitcoin'
        ).add_field(name='Current Price', value=f'${str(round(data["rate"],2))}', inline=False
        ).add_field(name='Market Change', value=f'+{str(round(data["delta"]["day"],2))}%', inline=False)

        negetive_message = discord.Embed(
            color=(0xffffff),
        ).set_author(
            icon_url='http://api.icey.fr/icons/crypto/white/btc.png',
            name='Bitcoin'
        ).add_field(name='Current Price', value=f'${str(round(data["rate"],2))}', inline=False
        ).add_field(name='Market Change', value=f'-{str(round(data["delta"]["day"],2))}%', inline=False)

        if data["delta"]["day"] > 1:
            await ctx.reply(embed = positive_message, mention_author=False)
        else: 
            await ctx.reply(embed = negetive_message, mention_author=False)
        
    @commands.command(description="Get etherium info", aliases=["etherium"])
    async def eth(self, ctx):

        url = "https://api.livecoinwatch.com/coins/single"

        payload = json.dumps({
        "currency": "USD",
        "code": "ETH",
        "meta": True
        })
        headers = {
        'content-type': 'application/json',
        'x-api-key': '27002a59-1626-42a4-a3e4-c689d3a959fe'
        }

        response = requests.request("POST", url, headers=headers, data=payload)

        data = response.json()

        positive_message = discord.Embed(
            color=(0xffffff),
        ).set_author(
            icon_url='http://api.icey.fr/icons/crypto/white/eth.png',
            name='Etherium'
        ).add_field(name='Current Price', value=f'${str(round(data["rate"],2))}', inline=False
        ).add_field(name='Market Change', value=f'+{str(round(data["delta"]["day"],2))}%', inline=False)

        negetive_message = discord.Embed(
            color=(0xffffff),
        ).set_author(
            icon_url='http://api.icey.fr/icons/crypto/white/eth.png',
            name='Etherium'
        ).add_field(name='Current Price', value=f'${str(round(data["rate"],2))}', inline=False
        ).add_field(name='Market Change', value=f'-{str(round(data["delta"]["day"],2))}%', inline=False)

        if data["delta"]["day"] > 1:
            await ctx.reply(embed = positive_message, mention_author=False)
        else: 
            await ctx.reply(embed = negetive_message, mention_author=False)

    @commands.command(description="Get dogecoin info", aliases=["dc"])
    async def dodgecoin(self, ctx):

        url = "https://api.livecoinwatch.com/coins/single"

        payload = json.dumps({
        "currency": "USD",
        "code": "DOGE",
        "meta": True
        })
        headers = {
        'content-type': 'application/json',
        'x-api-key': '27002a59-1626-42a4-a3e4-c689d3a959fe'
        }

        response = requests.request("POST", url, headers=headers, data=payload)

        data = response.json()

        positive_message = discord.Embed(
            color=(0xffffff),
        ).set_author(
            icon_url='http://api.icey.fr/icons/crypto/white/doge.png',
            name='Dogecoin'
        ).add_field(name='Current Price', value=f'${str(round(data["rate"],2))}', inline=False
        ).add_field(name='Market Change', value=f'+{str(round(data["delta"]["day"],2))}%', inline=False)

        negetive_message = discord.Embed(
            color=(0xffffff),
        ).set_author(
            icon_url='http://api.icey.fr/icons/crypto/white/doge.png',
            name='Dogecoin'
        ).add_field(name='Current Price', value=f'${str(round(data["rate"],2))}', inline=False
        ).add_field(name='Market Change', value=f'-{str(round(data["delta"]["day"],2))}%', inline=False)

        if data["delta"]["day"] > 1:
            await ctx.reply(embed = positive_message, mention_author=False)
        else: 
            await ctx.reply(embed = negetive_message, mention_author=False)

    @commands.command()
    async def crypto(self, ctx, crypt):
        
        cryptupper = crypt.upper()
            
        url = "https://api.livecoinwatch.com/coins/single"

        payload = json.dumps({
        "currency": "USD",
        "code": cryptupper,
        "meta": True
        })
        headers = {
        'content-type': 'application/json',
        'x-api-key': '27002a59-1626-42a4-a3e4-c689d3a959fe'
        }

        response = requests.request("POST", url, headers=headers, data=payload)

        data = response.json()

        positive_message = discord.Embed(
            color=(0xffffff),
        ).set_author(
            icon_url=f'http://api.icey.fr/icons/crypto/white/{crypt}.png',
            name=f'{cryptupper}'
        ).add_field(name='Current Price', value=f'${str(round(data["rate"],2))}', inline=False
        ).add_field(name='Market Change', value=f'+{str(round(data["delta"]["day"],2))}%', inline=False)

        negetive_message = discord.Embed(
            color=(0xffffff),
        ).set_author(
            icon_url=f'http://api.icey.fr/icons/crypto/white/{crypt}.png',
            name=f'{cryptupper}'
        ).add_field(name='Current Price', value=f'${str(round(data["rate"],2))}', inline=False
        ).add_field(name='Market Change', value=f'-{str(round(data["delta"]["day"],2))}%', inline=False)

        if data["delta"]["day"] > 1:
            await ctx.reply(embed = positive_message, mention_author=False)
        else: 
            await ctx.reply(embed = negetive_message, mention_author=False)

async def setup(client):
    await client.add_cog(Crypto(client))