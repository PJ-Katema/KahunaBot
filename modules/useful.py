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
