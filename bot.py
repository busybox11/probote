import os, sys, aiohttp, discord, asyncio, pickle
import credentials
from datetime import datetime
from html2text import html2text

client = discord.Client()

with open('homework.txt', 'rb') as file :
    homework = pickle.load(file)

with open('info.txt', 'rb') as file :
    info = pickle.load(file)

async def update_notifs():
    await client.wait_until_ready()

    while True:
        await client.change_presence(status=discord.Status.dnd, activity=discord.Activity(type=discord.ActivityType.watching, name="Pronote..."))
        async with aiohttp.ClientSession() as session:
            async with session.post('http://127.0.0.1:21727/', json={"type": "fetch", "username": credentials.username, "password": credentials.password, "url": credentials.url, "cas": credentials.cas}) as r:
                if r.status == 200:
                    data = await r.json()
        
        for i in range(len(data['homeworks'])):
            if data['homeworks'][i]['content'] not in homework:
                file = open('homework.txt', 'wb')
                homework.append(data['homeworks'][i]['content'])
                pickle.dump(homework, file)
                file.close()
                content = data['homeworks'][i]['content']
                if content.startswith('style="font-family') : # bug de l'API
                    content = ">".join(content.split(">")[1:])
                content = html2text(content)
                if data['homeworks'][i]['files'] == []:
                    await send_notification(data['homeworks'][i]['subject'], content, None, data['homeworks'][i]['until'])
                else:
                    await send_notification(data['homeworks'][i]['subject'], content, data['homeworks'][i]['files'], data['homeworks'][i]['until'])

        for i in range(len(data['infos'])):
            if data['infos'][i]['content'] not in info:
                file = open('info.txt', 'wb')
                info.append(data['infos'][i]['content'])
                pickle.dump(info, file)
                file.close()
                content = data['infos'][i]['content']
                content = html2text(content)
                if data['infos'][i]['files'] == []:
                    await send_notification(data['infos'][i]['title'], content)
                else:
                    await send_notification(data['infos'][i]['title'], content, data['infos'][i]['files'])

        await client.change_presence(status=discord.Status.online)
        await asyncio.sleep(1000)


async def send_notification(title, content, files=None, timestamp=None):
    channel = client.get_channel(credentials.probote_channel)
    if len(content) > 2048 : content = content[:2043]+"[...]"
    embed = discord.Embed(title=title, description=content, color=0x0095c7)
    if files == None:
        embed.set_footer(text="Aucun fichier attaché")
    else:
        nbFiles = len(files)
        for links in range(nbFiles):
            if type(files[links]) == dict :
                embed.add_field(name='**' + files[links]['name'] + '**', value='[Ouvrir Pronote](' + credentials.url + ')', inline=False)
        if nbFiles == 1:
            embed.set_footer(text="1 fichier attaché")
        else:
            embed.set_footer(text=str(nbFiles) + " fichiers attachés")
    
    if timestamp :
        embed.set_author(name="Travail à faire", url=credentials.url)
        embed.timestamp = datetime.fromtimestamp(timestamp // 1000)
    else : embed.set_author(name="Information", url=credentials.url)
    await channel.send(embed=embed)

@client.event
async def on_ready():
    print('Succesfully logged in for Discord as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.lower().startswith('pro ping'):
        await message.channel.send('Pong')
        print('Pong')
    
    elif message.content.lower().startswith(('pro disconnect', 'pro logout', 'pro quit')):
        if message.author.id == credentials.admin:
            await message.channel.send('Déconnexion...')
            await client.close()
        else:
            await message.channel.send("Vous n'êtes pas autorisé à utiliser cette commande !")

client.loop.create_task(update_notifs())

client.run(credentials.token)
