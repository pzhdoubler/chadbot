import discord
import os

from keepAlive import keep_alive

client = discord.Client()

images = {
  "yes" : "yes.jpg" ,
  "no" : "no.jpg" ,
  "sue" : "sue.jpg" ,
  "psps" : "ps.jpg" ,
  "lents" : "lenny-lents.jpg",
  "expert" : "theexpert.jpeg",
  "lookaway" : "lookingaway.jpg",
  "lookdirect" : "lookingdirectly.jpg",
  "manifest" : "manifest.jpg",
  "donotsee" : "pretendidonot.jpg",
  "reality" : "reality.jpg",
  "lookrespect" : "respectfully.png",
  "limit" : "limit.png",
  "stress" : "stress.jpg"
}

breakout = "-"

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith(breakout):
        command = message.content.lstrip(breakout)
        if command in images:
            await message.channel.send(file=discord.File(images[command]))

        if command == "chadhelp":
            command_list = "Chadman Commands:\n"
            for i in images.keys():
              command_list += breakout + i + "\n"
            await message.channel.send(command_list)


    # if message.content.startswith('-yes'):
    #     await message.channel.send(file=discord.File('yes.jpg'))

    # if message.content.startswith('-no'):
    #     await message.channel.send(file=discord.File('no.jpg'))

    # if message.content.startswith('-sue'):
    #     await message.channel.send(file=discord.File('sue.jpg'))

    # if message.content.startswith('-psps'):
    #     await message.channel.send(file=discord.File('ps.jpg'))

    # if message.content.startswith('-lents'):
    #     await message.channel.send(file=discord.File('lenny-lents.jpg'))

    # if message.content.startswith('-expert'):
    #     await message.channel.send(file=discord.File('theexpert.jpeg'))

    # if message.content.startswith('-lookaway'):
    #     await message.channel.send(file=discord.File('lookingaway.jpg'))

    # if message.content.startswith('-lookdirect'):
    #     await message.channel.send(file=discord.File('lookingdirectly.jpg'))

    # if message.content.startswith('-manifest'):
    #     await message.channel.send(file=discord.File('manifest.jpg'))

    # if message.content.startswith('-donotsee'):
    #     await message.channel.send(file=discord.File('pretendidonot.jpg'))

    # if message.content.startswith('-reality'):
    #     await message.channel.send(file=discord.File('reality.jpg'))

    # if message.content.startswith('-lookrespect'):
    #     await message.channel.send(file=discord.File('respectfully.png'))

    # if message.content.startswith('-limit'):
    #     await message.channel.send(file=discord.File('limit.png'))

    # if message.content.startswith('-stress'):
    #     await message.channel.send(file=discord.File('stress.jpg'))

#    if message.content.startswith('-drop'):
#        await message.channel.send("kd")
#
#    if message.content.startswith('-verify'):
#        await message.channel.send("kverify")

keep_alive()
client.run(os.getenv('TOKEN'))
