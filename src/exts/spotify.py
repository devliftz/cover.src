from typing import Optional
import discord
from discord.ext import commands
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from flask import Flask, request, render_template
import threading
from core.emojis import *
import json

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
                scope='user-read-playback-state user-modify-playback-state' # WHAT U NEED TO GET INFO
            )
        )

    # Define bot command
    @commands.command(aliases=["spotify", "nowplaying", "currentsong", "sp", "track"])
    async def np(self, ctx):
        
        
        author = ctx.author

        try:
            track = self.sp.current_playback()

            if track is not None:
                artist = track['item']['artists'][0]['name']
                song_name = track['item']['name']
                album_cover_url = track['item']['album']['images'][0]['url']
                embed_message = discord.Embed(
                    title="",
                    color=0xffffff
                )
                embed_message.add_field(name="Track:", value=f"**{song_name}**", inline=False)
                embed_message.add_field(name="Artist:", value=f"**{artist}**")
                embed_message.set_author(icon_url="https://www.iconsdb.com/icons/preview/white/spotify-xxl.png", name="Spotify")
                embed_message.set_thumbnail(url=album_cover_url)

                await ctx.reply(embed=embed_message, mention_author=False)
            else:
                await ctx.send("No song is currently playing.")
        except spotipy.SpotifyException as e:
            print(f"Error fetching current song: {e}")
            await ctx.send("Failed to fetch current song data.")
        except Exception as e:
            print(f"Error: {e}")
            await ctx.send("An error occurred while processing the command.")

    @commands.command()
    async def album(self, ctx):
        

        author = ctx.author

        try:
            track = self.sp.current_playback()
            if track is not None:
                album_cover_url = track['item']['album']['images'][0]['url']
                album_name = track['item']['album']['name']

                embed = discord.Embed(title="",
                                      color=0xffffff,
                                      description=f"**{album_name}`s Icon**")
                embed.set_image(url=album_cover_url)
                await ctx.reply(embed=embed)
        except spotipy.SpotifyException as e:
            print(f"Error fetching current album: {e}")
            await ctx.send("Failed to fetch current album data.")
        except Exception as e:
            print(f"Error: {e}")
            await ctx.send("An error occurred while processing the command.")

    @commands.command(aliases=['next'])
    async def skip(self, ctx):
        
        
        try:
            self.sp.next_track()
            embed = discord.Embed(title="",
                                  description=f"> **Skipping to the next track**",
                                  color=0xffffff)
            embed.set_author(icon_url="https://www.iconsdb.com/icons/preview/white/spotify-xxl.png", name="Spotify")
            await ctx.reply(embed=embed)
        except spotipy.SpotifyException as e:
            print(f"Error skipping track: {e}")
            await ctx.send("Failed to skip track.")
        except Exception as e:
            print(f"Error: {e}")
            await ctx.send("An error occurred while processing")

    @commands.command()
    async def previous(self, ctx):
        
        
        try:
            self.sp.previous_track()
            embed = discord.Embed(title="",
                                  description=f"> **Skipping to the previous track**",
                                  color=0xffffff)
            embed.set_author(icon_url="https://www.iconsdb.com/icons/preview/white/spotify-xxl.png", name="Spotify")
            await ctx.reply(embed=embed)
        except spotipy.SpotifyException as e:
            print(f"Error changing track: {e}")
            await ctx.send("Failed to change track.")
        except Exception as e:
            print(f"Error: {e}")
            await ctx.send("An error occurred while processing")

    @commands.command()
    async def pause(self, ctx):
        
        
        try:
            self.sp.pause_playback()
            embed = discord.Embed(title="",
                                  description=f"> {check} **Pausing current track**",
                                  color=0xffffff)
            embed.set_author(icon_url="https://www.iconsdb.com/icons/preview/white/spotify-xxl.png", name="Spotify")
            await ctx.reply(embed=embed)
        except spotipy.SpotifyException as e:
            print(f"Error while pausing track: {e}")
            await ctx.send("Failed to pause track.")
        except Exception as e:
            print(f"Error: {e}")
            await ctx.send("An error occurred while processing")

    @commands.command()
    async def play(self, ctx):
        
        
        try:
            self.sp.start_playback()
            embed = discord.Embed(title="",
                                  description=f"> {check} **Unpaused**",
                                  color=0xffffff)
            embed.set_author(icon_url="https://www.iconsdb.com/icons/preview/white/spotify-xxl.png", name="Spotify")
            await ctx.reply(embed=embed)
        except spotipy.SpotifyException as e:
            print(f"Error while playing track: {e}")
            await ctx.send("Failed to play track.")
        except Exception as e:
            print(f"Error: {e}")
            await ctx.send("An error occurred while processing")

    @commands.command()
    async def playlists(self, ctx):
        
        
        try:
            playlists = self.sp.user_playlists(limit=4, user=self.sp._get_id)
            embed = discord.Embed(title="",
                                  description=f"""**User Playlists** ```
{playlists}""",
                                  color=0xffffff)
            embed.set_author(icon_url="https://www.iconsdb.com/icons/preview/white/spotify-xxl.png", name="Spotify")
            await ctx.reply(embed=embed)
        except spotipy.SpotifyException as e:
            print(f"Failed fetcing user playlists: {e}")
            await ctx.send("Failed fetcing user playlists")
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
                                                       scope='user-read-playback-state user-modify-playback-state'))
        # You can now use the 'sp' object to make authorized requests to the Spotify Web API

        return "Auth"

    app.run(port=5000)  # Start the web server on port 8000

async def setup(client):
    sp = Spotify(client)
    threading.Thread(target=run_flask).start()  # Start the Flask web server in a separate thread
    await client.add_cog(sp)  # Await the addition of the cog to the bot