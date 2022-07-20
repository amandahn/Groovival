"""
Groovival

Author: Amanda Ngo
Description: Responds to commands given in a discord server to play music
Last Modified: June 22, 2022
Inspired and modified from: https://youtu.be/ml-5tXRmmFk
"""

import discord
from discord.ext import commands
import Groovival_Code

cogs = [Groovival_Code]

client = commands.Bot(command_prefix="!", intents = discord.Intents.all())

for i in range(len(cogs)):
    cogs[i].setup(client)
    
client.run('token')
