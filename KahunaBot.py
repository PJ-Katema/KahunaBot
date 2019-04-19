# Works with Python 3.6
import asyncio
import aiohttp
import aiml
import json
import requests
import os
from discord import Game
from discord.ext.commands import Bot

BOT_PREFIX = "!"# Commands will start with the symbol specified here.
TOKEN = "NTY4NzY1MzUwNTU3MjUzNjMz.XLm4rw.6zdEjt4DySNjqTY5iTDIz7C9_hs" # Get at discordapp.com/developers/applications/me
client = Bot(command_prefix=BOT_PREFIX)
#-------------------------------------------------------------------------------
kernel = aiml.Kernel()

if os.path.isfile("bot_brain.brn"):
    kernel.bootstrap(brainFile = "bot_brain.brn")
else:
    kernel.bootstrap(learnFiles = "std-startup.xml", commands = "load aiml b")
    kernel.saveBrain("bot_brain.brn")

# kernel now ready for use

@client.event
async def on_message(message, context):
    if message.author == client.user:
        return
    if messafe.content.upper().startswith(client.user.mention):
        bot_response = kernel.respond(message)
        await client.say(context.message.author.mention + ", " + bot_response)
#-------------------------------------------------------------------------------

@client.command(name='totube',
                description ="Creates a link to a Together Tube room",
                brief = "Watch Youtube videos together",
                aliases = ['togethertube'],
                pass_context=True)

async def together_tube(context):
    url = requests.get("https://togethertube.com/room/create").url
    await client.say(context.message.author.mention +', your together tube link!\n\n'+ url +'\n\n Happy viewing!')

#-------------------------------------------------------------------------------
#-------------------------------------------------------------------------------
@client.event
async def on_ready():
    await client.change_presence(game=Game(name="with humans"))
    print("Logged in as " + client.user.name)


async def list_servers():
    await client.wait_until_ready()
    while not client.is_closed:
        print("Current servers:")
        for server in client.servers:
            print(server.name)
        print("---------------------")
        await asyncio.sleep(600)


client.loop.create_task(list_servers())
client.run(TOKEN)
