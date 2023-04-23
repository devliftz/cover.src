import hypecord
import time

async def loadingembed(ctx, text):
    loading = hypecord.Embed(title="",
                           description=f"""> **Loading..**""",
                           color=0xffffff)
    loading.set_author(icon_url=f"https://cdn.discordapp.com/avatars/1096484859477754008/9e83d8a91e95366569c5274f1a66d9b3?size=1024", name="cover")
    final = hypecord.Embed(title="",
                           description=f"""> **{text}**""",
                           color=0xffffff)
    final.set_author(icon_url=f"https://cdn.discordapp.com/avatars/1096484859477754008/9e83d8a91e95366569c5274f1a66d9b3?size=1024", name="cover")
    msg = await ctx.reply(embed=loading)
    time.sleep(.7)
    await msg.edit(embed=final)