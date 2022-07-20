"""
Groovival

Author: Amanda Ngo
Description: Responds to commands given in a discord server to play music
Last Modified: June 22, 2022
Addition URL: https://discord.com/api/oauth2/authorize?client_id=989267518944346192&permissions=8&redirect_uri=https%3A%2F%2Fdiscord.com%2Foauth2%2Fauthorize%3Fclient_id%3D989267518944346192%26scope%3Dbot&response_type=code&scope=identify%20email%20guilds%20connections%20guilds.join%20guilds.members.read%20gdm.join%20rpc%20rpc.notifications.read%20applications.builds.read%20applications.builds.upload%20messages.read%20webhook.incoming%20bot%20rpc.activities.write%20rpc.voice.write%20rpc.voice.read%20applications.commands%20applications.store.update%20applications.entitlements%20activities.read%20activities.write%20relationships.read%20voice%20dm_channels.read
Inspired and modified from: https://youtu.be/ml-5tXRmmFk
"""

import discord
from discord.ext import commands
import Groovival_Code

cogs = [Groovival_Code]

client = commands.Bot(command_prefix="!", intents = discord.Intents.all())

for i in range(len(cogs)):
    cogs[i].setup(client)


client.run('OTg5MjY3NTE4OTQ0MzQ2MTky.GHyAMf.Ww3HxlVXXI-veofk1NKuLvPHy0OGHw9Hj0fIrU')
