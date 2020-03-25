import os, sys, aiohttp, discord, asyncio, pickle, validators
import credentials
from datetime import datetime
from html2text import html2text
from urllib.request import urlretrieve
from urllib.parse import unquote

client = discord.Client()

async def update_notifs():
    await client.wait_until_ready()

    with open('homework.txt', 'rb') as file :
        homework = pickle.load(file)

    with open('info.txt', 'rb') as file :
        info = pickle.load(file)

    while True:
        await client.change_presence(status=discord.Status.dnd, activity=discord.Activity(type=discord.ActivityType.watching, name="Pronote..."))
        async with aiohttp.ClientSession() as session:
            async with session.post('http://127.0.0.1:21727/', json={"type": "fetch", "username": credentials.username, "password": credentials.password, "url": credentials.url, "cas": credentials.cas}) as r:
                if r.status == 200:
                    data = await r.json()

        for i in range(len(data['homeworks'])):
            if data['homeworks'][i]['content'] not in homework:
                homework.append(data['homeworks'][i]['content'])
                with open('homework.txt', 'wb') as file :
                    pickle.dump(homework, file)
                await send_notification(data['homeworks'][i]['subject'], data['homeworks'][i]['content'], data['homeworks'][i]['files'], data['homeworks'][i]['until'])

        for i in range(len(data['infos'])):
            if data['infos'][i]['content'] not in info:
                info.append(data['infos'][i]['content'])
                with open('info.txt', 'wb') as file :
                    pickle.dump(info, file)
                try:
                    data['infos'][i]['title']
                except KeyError:
                    data['infos'][i]['title'] = "Aucun titre"
                await send_notification(data['infos'][i]['title'], data['infos'][i]['content'], data['infos'][i]['files'])

        await client.change_presence(status=discord.Status.online)
        await asyncio.sleep(1000)


async def send_notification(title, content, files=None, timestamp=None):
    channel = client.get_channel(credentials.probote_channel)

    if content.startswith('style="font-family') : # bug de l'API
        content = ">".join(content.split(">")[1:])
    content = html2text(content)

    if len(content) > 2048 : content = content[:2043]+"[...]"
    embed = discord.Embed(title=title, description=content, color=0x0095c7)

    if timestamp :
        embed.set_author(name="Travail à faire")
        embed.timestamp = datetime.fromtimestamp(timestamp // 1000)
    else : embed.set_author(name="Information")

    nbFiles = len(files) if files else 0
    if nbFiles == 0 : embed.set_footer(text="Aucun fichier attaché")
    elif nbFiles == 1: embed.set_footer(text="1 fichier attaché")
    else: embed.set_footer(text=str(nbFiles) + " fichiers attachés")
    
    await channel.send(embed=embed)

    if files :
        for file in files :
            if type(file) == dict :
                if not validators.url(file['name']):
                    path, _ = urlretrieve(file['url'])
                    name = file['name']
                    await channel.send(file=discord.File(path, unquote(name)))
                else:
                    await channel.send(file['name'])
            else :
                if not validators.url(file):
                    print(file)
                    path, _ = urlretrieve(file)
                    name = file.split("/")[-1]
                    name = name.split("?")[0]
                    await channel.send(file=discord.File(path, unquote(name)))
                else:
                    await channel.send(file)


@client.event
async def on_ready():
    print('Succesfully logged in for Discord as {0.user}'.format(client))


@client.event
async def on_message(message):
    if message.author != credentials.admin :
        return

    if message.content.startswith('pro ping'):
        await message.channel.send('Pong')
        print('Pong')
    
    elif message.content.startswith('pro quit'):
        await message.channel.send('Déconnexion...')
        await client.close()


client.loop.create_task(update_notifs())

client.run(credentials.token)
