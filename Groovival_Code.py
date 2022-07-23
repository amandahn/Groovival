"""
Groovival

Author: Amanda Ngo
Description: Responds to commands given in a discord server to play music
Created: June 14, 2022
Last Modified: July 23, 2022
Inspired by: https://youtu.be/ml-5tXRmmFk and https://youtu.be/jHZlvRr9KxM

"""

import discord
from discord.ext import commands
import youtube_dl

class music(commands.Cog):
    def __init__(self, client):
        self.client = client
    
    # Description: Bot joins the user's current voice channel
    # Precondition: User must be in a voice channel
    @commands.command()
    async def join(self,ctx):
       await ctx.author.voice.channel.connect()
    
    # Description: Bot leaves the user's current voice channel
    # Precondition: User must be in a voice channel
    @commands.command()
    async def leave(self, ctx):
        await ctx.voice_client.disconnect()
    
    # Description: Bot streams the given youtube link into the voice channel
    # Precondition: User must be in a voice channel; must be a valid youtube link
    @commands.command()
    async def play(self, ctx, url):
        FFMPEG_OPTIONS = {"before_options": "-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5", "options": "-vn"}
        YDL_OPTIONS = {"format":"bestaudio"}
        vc = ctx.voice_client

        with youtube_dl.YoutubeDL(YDL_OPTIONS) as ydl:
            info = ydl.extract_info(url, download=False)
            url_ydl = info["formats"][0]["url"]
            source = await discord.FFmpegOpusAudio.from_probe(url_ydl, **FFMPEG_OPTIONS)
        vc.play(source)
    
    # Description: Bot sends a description of its commands into a message channel
    @commands.command()
    async def info(self, ctx):
        await ctx.send("**REQUIREMENTS: user must be in a voice channel to use the following commands**\n**!join** ➞ Groovival joins the channel\n\
                        **!disconnect** ➞ Groovival leaves the channel\n**!play** some url ➞ Streams the given url into the server (MUST BE A YOUTUBE URL)\n\
                        **!pause** ➞ Pauses a given song, if not currently paused\n**!unpause** ➞ Unpauses a given song, if currently paused\n\
                        **!stop** ➞ Stops a current playing song, if music is currently playing\n")

    # Description: Bot pauses the current song being played
    # Precondition: Audio must be currently plaiyng
    @commands.command()
    async def pause(self, ctx):
        await ctx.voice_client.pause()
        await ctx.send("Music paused")
    
    # Description: Bot unpauses the current song
    # Precondition: Audio must be currently paused
    @commands.command()
    async def unpause(self, ctx):
        await ctx.voice_client.resume()
        await ctx.send("Music unpaused")
    
    # Description: Bot stops the current song
    # Precondition: Audio must be currently plaiyng
    @commands.command()
    async def stop(self, ctx):
        await ctx.voice_client.stop()
        await ctx.send("Music stopped")

def setup(client):
    client.add_cog(music(client))
