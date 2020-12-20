import discord
client = discord.Client()


@client.event
async def on_ready():
    print(f'{client.user} olarak giriş yaptık...')


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('selam bot'):
        await message.channel.send('Selam, nasılsın. Ben daha yeni yeni konuşmaya başlıyorum.')
    elif "salak" in message.content:

        await message.channel.purge(limit=1)
        await message.channel.send(f'Mesajını sildim.')
        await message.channel.send(f'{message.author} kullandığın kelime hiç hoş değil.')
    elif message.content.startswith('sil bot'):
        # sil bot 10 mesela, 10'a nasıl ulaşırız?
        mesaj_sayisi = int(message.content[7:]) + 1
        await message.channel.purge(limit=mesaj_sayisi)

client.run('NzkwMTYwOTAyNTAyMjE5ODI2.X98krw.qhj0e99m7CPMUL6WkzNwrVSUWuw')
