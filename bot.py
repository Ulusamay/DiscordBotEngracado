import discord
import asyncio
import random
lista = ['xiu', 'calaboca', 'nao sei', 'sei la', 'nao sei dizer', 'mais ou menos', 'talvez', 'nao', 'sim', 'concerteza', 'nunca', 'sempre','claro']
client = discord.Client()
@client.event
async def on_ready():
    print('bot online hehe')
    print(client.user.name)
    print(client.user.id)
@client.event
async def on_message(message):
    if '?' in message.content[-2] and '.' in message.content[-1]:
        print('usado')
        await message.channel.send(random.choice(lista))
client.run('')
