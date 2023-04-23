import hypecord
from hypecord.ext import commands
import pylast

class Lastfm(commands.Cog):
    def __init__(self, Client):
        self.client = Client

    @commands.command(aliases=['lf', 'lfm', 'lastfm', 'fm'])
    async def last(self, ctx, username):
        LASTFM_API_KEY = "c9178512a0aca5aadc905ac2e1490d39"
        LASTFM_API_SECRET = "6efbc95687f87322a160ca36a80972c7"
        avatar = ctx.author.avatar
        user = ctx.author
        network = pylast.LastFMNetwork(api_key=LASTFM_API_KEY, api_secret=LASTFM_API_SECRET)
        user = network.get_user(username)
        current_track = user.get_now_playing()
        if current_track is None:
            notlistening = hypecord.Embed(title="",
                                          description=f"> **{username} is not listening to anything at the moment**",
                                          color=0xffffff)
            notlistening.set_author(icon_url=avatar, name=user)
            await ctx.reply(embed=notlistening)
        else:
            artist = current_track.get_artist().get_name()
            song = current_track.get_title()
            authorurl = current_track.artist.get_url()
            playcount = current_track.get_userplaycount()
            song_url = current_track.get_url()
            track_album = current_track.get_album()
            thumbnail_url = current_track.get_album().get_cover_image()
            embed = hypecord.Embed(title="",
                                color=0xffffff)
            embed.add_field(name="Track:", value=f"[**{song}**]({song_url})", inline=False)
            embed.add_field(name="Artist:", value=f"[**{artist}**]({authorurl})")
            embed.set_author(icon_url=avatar, name=user)
            embed.set_footer(icon_url=thumbnail_url, text=f"Track playcount {playcount} • Album: {track_album}")
            embed.set_thumbnail(url=thumbnail_url)
            await ctx.reply(embed=embed, mention_author=False)

async def setup(client):
    await client.add_cog(Lastfm(client))