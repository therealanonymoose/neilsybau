import discord
from dotenv import load_dotenv
import os
import asyncio
import random
import json

load_dotenv()
token = os.getenv('DISCORD_TOKEN')
target_id = int(os.getenv('TARGET_USER_ID'))

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

with open('triggers.json', 'r') as f:
    data = json.load(f)

@client.event
async def on_ready():
    print(f'Bot ready')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.author.id == target_id and random.random() <= 0.1:
            emojis = ['🇸', '🇾', '🇧', '🇦', '🇺']
            
            #run everything at once
            await asyncio.gather(
                *(message.add_reaction(emoji) for emoji in emojis),
                message.channel.send('neil sybau')
            )

    lowered = message.content.lower()
    for category in data.values():  #every json category
        triggers = category.get('triggers', [])
        responses = category.get('responses', [])
        if any(trigger in lowered for trigger in triggers):
            await message.channel.send(random.choice(responses))
            return

client.run(token)