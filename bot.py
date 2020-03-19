import os
import sys
import aiohttp
import discord
import asyncio
import pickle
import credentials
from datetime import datetime

client = discord.Client()

file = open('homework.txt', 'rb')

data = ""
homework = pickle.load(file)

file.close()

async def update_info_task():
    await client.wait_until_ready()
    while True:
        await client.change_presence(status=discord.Status.dnd, activity=discord.Activity(type=discord.ActivityType.watching, name="Pronote..."))
        async with aiohttp.ClientSession() as session:
            async with session.post('http://127.0.0.1:21727/', json={"type": "fetch", "username": credentials.username, "password": credentials.password, "url": credentials.url, "cas": credentials.cas}) as r:
                if r.status == 200:
                    global data
                    data = await r.json()
        for i in range(len(data['homeworks'])):
            if data['homeworks'][i]['content'] not in homework:
                file = open('homework.txt', 'wb')
                homework.append(data['homeworks'][i]['content'])
                pickle.dump(homework, file)
                file.close()
                if data['homeworks'][i]['files'] == []:
                    await send_notification(data['homeworks'][i]['subject'], data['homeworks'][i]['content'], None, data['homeworks'][i]['until'])
                else:
                    await send_notification(data['homeworks'][i]['subject'], data['homeworks'][i]['content'], data['homeworks'][i]['files'], data['homeworks'][i]['until'])
        await client.change_presence(status=discord.Status.online, activity=discord.Game(name="pro help"))
        await asyncio.sleep(1000)

async def send_notification(subject, content, files, timestamp):
    channel = client.get_channel(credentials.probote_channel)
    embed = discord.Embed(title=subject, description=content.replace('<br>', '\n'), color=0x0095c7)
    if files == None:
        embed.set_footer(text="Aucun fichier attaché")
    else:
        nbFiles = len(files)
        for links in range(nbFiles):
            embed.add_field(name='**' + files[links]['name'] + '**', value='[Ouvrir Pronote](' + credentials.url + ')', inline=False)
        if nbFiles == 1:
            embed.set_footer(text="1 fichier attaché")
        else:
            embed.set_footer(text=str(nbFiles) + " fichiers attachés")
    embed.set_author(name="Nouveau devoir", url=credentials.url)
    embed.timestamp = datetime.fromtimestamp(timestamp // 1000)
    await channel.send(embed=embed)

@client.event
async def on_ready():
    print('Succesfully logged in for Discord as {0.user}'.format(client))
    await client.change_presence(activity=discord.Game(name="pro help"))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.lower().startswith('pro ping'):
        await message.channel.send('Pong')
        print('Pong')

    elif message.content.lower().startswith(("pro moy", "pro moyenne")):
        trimestre = len(data['marks'])
        moyenne = str(data['marks'][trimestre]['averages']['studentClass'])
        embed = discord.Embed(title="Moyenne de la classe", color=0x00ff00)
        embed.add_field(name="Trimestre " + str(trimestre), value=moyenne, inline=False)
        await message.channel.send(embed=embed)
    
    elif message.content.lower().startswith('pro help'):
        embed = discord.Embed(title="Aide de Probote", description="Liste des commandes de Probote", color=0x00ff00)
        embed.add_field(name="Affiche la moyenne de la classe pour le trimestre en cours", value="`pro moyenne` ou `pro moy`", inline=False)
        embed.add_field(name="Pong !", value="`pro ping`", inline=False)
        embed.add_field(name="Affiche la liste des commandes de Probote", value="`pro help`", inline=False)
        await message.channel.send(embed=embed)

    elif message.content.lower().startswith('pro debug embed homework'):
        embed = discord.Embed(title="Nouveau devoir", description="Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vivamus imperdiet sed elit id hendrerit. Curabitur nec purus nisi. Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis.", color=0x0095c7)
        embed.set_author(name="Français - Mme MICHEL", url=credentials.url)
        if "nofile" in message.content.lower():
            embed.set_footer(text="Aucun fichier attaché")
        else:
            embed.add_field(name="2 fichiers attachés", value="Fichier 1.pdf\nFichier 2.pdf", inline=False)
        await message.channel.send(embed=embed)
    
    elif message.content.lower().startswith('pro debug notification'):
        channel = client.get_channel(credentials.probote_channel)
        embed = discord.Embed(title="FRANÇAIS", description="Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vivamus imperdiet sed elit id hendrerit. Curabitur nec purus nisi. Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis.", color=0x0095c7)
        if "nofile" in message.content.lower():
            embed.set_footer(text="Aucun fichier attaché")
        else:
            embed.add_field(name="2 files attached", value="[Fichier_1.pdf](http://test.fr/1)\n[Fichier_2.pdf](http://test.fr/2)\n", inline=False)
        embed.set_author(name="Nouveau devoir", url=credentials.url)
        embed.timestamp = datetime.datetime.utcnow()
        await channel.send(embed=embed)
    
    elif message.content.lower().startswith(('pro disconnect', 'pro logout', 'pro quit')):
        if message.author.id == credentials.admin:
            await message.channel.send('Logging out.')
            await client.close()
        else:
            await message.channel.send("You're not allowed to do this !")

client.loop.create_task(update_info_task())

client.run(credentials.token)
