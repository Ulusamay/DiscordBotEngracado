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
        if message.channel.name == 'comandos-bot':
            print(message.author.nick)
            print(message.channel.name, 'é comandos-bot')
            await message.channel.send(random.choice(lista))
        else:
            print(message.author.nick)
            print(message.channel.name, 'não é comandos-bot')
            await message.channel.send('Por favor,só use comandos em #comandos-bot(Leia as #regras)')
client.run('NjE0NjE5NDA2NTEyODE2MTMw.XWMCMw.xwv5Qj42XjpUOmzyRx_bhNSRYQ0')
