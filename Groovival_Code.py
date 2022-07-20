"""
Groovival

Author: Amanda Ngo
Description: Responds to commands given in a discord server to play music
Created: June 14, 2022
Last Modified: July 20, 2022
Inspired by: https://youtu.be/ml-5tXRmmFk and https://youtu.be/jHZlvRr9KxM

"""

import discord
from discord.ext import commands
import youtube_dl

class music(commands.Cog):
    def __init__(self, client):
        self.client = client
     
    @commands.command()
    async def info(self, ctx):
        commands_list = ["REQUIREMENTS: user must be in a voice channel to use the following commands", "!join -> Groovival joins the channel",
                        "!disconnect -> Groovival leaves the channel", "!play url -> Streams the given url into the server (MUST BE A YOUTUBE URL)"]
        for i in range(len(commands_list)):
            await ctx.send(commands_list[i] + "\n")
 
    @commands.command()
    async def join(self,ctx):

       await ctx.author.voice.channel.connect()

    @commands.command()
    async def disconnect(self, ctx):
        await ctx.voice_client.disconnect()

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


def setup(client):
    client.add_cog(music(client))
