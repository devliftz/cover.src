import hypecord
from hypecord.ext import commands
from core.embed import loadingembed
import requests

class Fun(commands.Cog):
    def __init__(self, Client):
        self.client = Client
        self.base_url = 'https://api.popcat.xyz/github'

    @commands.command()
    async def github(self, ctx, *, query: str):
        """
        Searches for a user, organization, or repository on GitHub.
        """
        url = f"https://api.github.com/search/users?q={query}"
        response = requests.get(url)

        if response.ok:
            data = response.json()
            result = data['items'][0]
            if result['type'] == 'User':
                embed = hypecord.Embed(title="",
                                       description=f"""> [****](https://github.com/{query})""")
                message = f"Found user: {result['login']}"
            elif result['type'] == 'Organization':
                message = f"Found organization: {result['login']}"
            else:
                message = f"Found repository: {result['full_name']}"
        else:
            message = "An error occurred while searching for the query."

        await ctx.send(message)

    @commands.command()
    async def test(self, ctx):
        loadingembed("test")

async def setup(client):
    await client.add_cog(Fun(client))