import discord
from discord.ext import commands
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from flask import Flask, request
import threading


class Spotify(commands.Cog):
    def __init__(self, client):
        self.client = client
        self.sp = None
        self.authenticate()  # Authenticate and initialize Spotify client when the bot starts

    # Authenticate with Spotify API
    def authenticate(self):
        self.sp = spotipy.Spotify(
            auth_manager=SpotifyOAuth(
                client_id='c4d4d95f4a4e47c196ab0cd03a3bbfa2',
                client_secret='5ca6927d86c04863af13453f4ab61bae',
                redirect_uri='http://localhost:8000/callback', # DOMAIN YOU OWN, or this...
                scope='user-read-playback-state' # WHAT U NEED TO GET INFO
            )
        )

    # Define bot command
    @commands.command(aliases=["spotify", "nowplaying", "currentsong", "sp"])
    async def np(self, ctx):
        author = ctx.author

        try:
            track = self.sp.current_playback()
            if track is not None:
                artist = track['item']['artists'][0]['name']
                song_name = track['item']['name']
                album_cover_url = track['item']['album']['images'][0]['url'] # Get album cover URL
                embed_message = discord.Embed(
                    title="",
                    color=0xffffff
                )
                embed_message.add_field(name="Track:", value=f"**{song_name}**", inline=False)
                embed_message.add_field(name="Artist:", value=f"**{artist}**")
                embed_message.set_author(icon_url="https://api.icey.fr/icons/brands/white/spotify.png", name="Spotify")
                embed_message.set_thumbnail(url=album_cover_url) # Set album cover as thumbnail

                await ctx.reply(embed=embed_message, mention_author=False)
            else:
                await ctx.send("No song is currently playing.")
        except spotipy.SpotifyException as e:  # Catch specific exceptions from spotipy library
            print(f"Error fetching current song: {e}")
            await ctx.send("Failed to fetch current song data.")
        except Exception as e:
            print(f"Error: {e}")
            await ctx.send("An error occurred while processing the command.")

    @commands.command()
    async def skip(self, ctx):
        try:
            self.sp.next_track()
            await ctx.send("Skipping to the next track.")
        except spotipy.SpotifyException as e:
            print(f"Error skipping track: {e}")
            await ctx.send("Failed to skip track.")
        except Exception as e:
            print(f"Error: {e}")
            await ctx.send("An error occurred while processing")

def run_flask():
    app = Flask(__name__)

    @app.route('/callback')
    def callback():
        # Retrieve the authorization code from the query parameters
        authorization_code = request.args.get('code')

        # Complete the authentication process with Spotify using the authorization code
        sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id='c4d4d95f4a4e47c196ab0cd03a3bbfa2',
                                                       client_secret='5ca6927d86c04863af13453f4ab61bae',
                                                       redirect_uri='http://localhost:8000/callback', # same case....
                                                       scope='user-read-playback-state'))
        # You can now use the 'sp' object to make authorized requests to the Spotify Web API
        
        # Return a response indicating success
        return 'Authorization completed successfully'

    app.run(port=5000, )  # Start the web server on port 8000




async def setup(client):
    sp = Spotify(client)
    threading.Thread(target=run_flask).start()  # Start the Flask web server in a separate thread
    await client.add_cog(sp)  # Await the addition of the cog to the bot