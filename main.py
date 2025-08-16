import discord
from dotenv import load_dotenv
import os
import asyncio
import random

load_dotenv()
token = os.getenv('DISCORD_TOKEN')
target_id = int(os.getenv('TARGET_USER_ID'))

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'Bot ready')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    lowered = message.content.lower()
    responses = [
        'im lowk hungry rn',
        'i could go for some food',
        'ima go grab sm to eat',
        'food?',
        'food is my middle name brochacho',
        'bro im so hungry rn',
        'ima eat you',
        'ima have a snack',
        'yo my doordash driver is fucking late bro'
    ]
    if 'food' in lowered or 'eat' in lowered:
        await message.channel.send(random.choice(responses))
        return

    if message.author.id == target_id:
        if random.random() > 0.05:
            return

        emojis = ['🇸', '🇾', '🇧', '🇦', '🇺']
        
        #run everything at once
        await asyncio.gather(
            *(message.add_reaction(emoji) for emoji in emojis),
            message.channel.send('neil sybau')
        )

client.run(token)