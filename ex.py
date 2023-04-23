import hypecord
from hypecord.ext import commands

bot = commands.Bot(command_prefix="?", intents=hypecord.Intents.all())

bot.init("MTA5NjQ4NDg1OTQ3Nzc1NDAwOA.Gat6gS.5a4i99B82RUou1b9h-qH4qp8oHK86MouNWj-0s", mobile=True, api_key="NSKBG")