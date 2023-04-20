@commands.command(aliases=["bitcoin"])
    async def btc(self, ctx):

        url = "https://api.livecoinwatch.com/coins/single"

        payload = json.dumps({
        "currency": "USD", # GBP works too
        "code": "BTC", # These are codenames for the coins, u can change this to ETH, etc in other commands
        "meta": True
        })
        headers = {
        'content-type': 'application/json',
        'x-api-key': 'YOUR KEY HERE'
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