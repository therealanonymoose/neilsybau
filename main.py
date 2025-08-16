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

    if message.author.id == target_id:
        if random.random() > 0.1:
            return

        emojis = ['🇸', '🇾', '🇧', '🇦', '🇺']
        
        #run everything at once
        await asyncio.gather(
            *(message.add_reaction(emoji) for emoji in emojis),
            message.channel.send('neil sybau')
        )

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
    triggers = [
        'food', 'eat', 'hungry', 'snack', 'dinner', 'lunch', 'breakfast', 'starving', 'meal', 'feast',
        'drink', 'doordash', 'ubereats', 'grubhub', 'restaurant', 'cafe', 'bistro', 'diner', 'buffet',
        'cuisine', 'dish', 'gourmet', 'tasty', 'yummy', 'delicious', 'craving', 'nourish', 'savor',
        'bite', 'munch', 'chew', 'pizza', 'burger', 'fries', 'tacos', 'ramen', 'ice cream', 'cookies',
        'cake', 'pastry', 'sandwich', 'salad', 'soup', 'noodles', 'pasta', 'steak', 'seafood', 'sushi',
        'dim sum', 'boba', 'smoothie', 'milkshake', 'coffee', 'tea', 'juice', 'cocktail', 'beer',
        'wine', 'soda', 'chips', 'popcorn', 'pretzel', 'candy', 'chocolate', 'donut', 'bagel', 'waffle',
        'pancake', 'omelette', 'quiche', 'lasagna', 'curry', 'bbq', 'kebab', 'falafel', 'nachos',
        'hotdog', 'sub', 'wrap', 'dumpling', 'pierogi', 'paella', 'fondue', 'mac and cheese',
        'granola', 'yogurt', 'poke', 'ceviche', 'brunch', 'comfort food',
        'cook', 'bake', 'boil', 'fry', 'grill', 'roast', 'simmer', 'sauté', 'blend',
        'mix', 'chop', 'dice', 'whisk', 'season', 'marinate', 'stir', 'knead', 'poach', 'broil',
        'spicy', 'sweet', 'salty', 'sour', 'bitter', 'tangy', 'creamy', 'crunchy', 'savory',
        'fresh', 'hot', 'cold', 'juicy', 'zesty', 'flavorful', 'rich', 'buttery', 'crispy',
        'gulp', 'sip', 'chow down', 'feast', 'devour', 'nom', 'nosh', 'wolf down', 'dig in',
        'hungrily', 'supper', 'happy hour', 'picnic', 'potluck', 'banquet',
        'mcdonalds', 'kfc', 'subway', 'starbucks', 'dominos', 'chipotle', 'wendys', 'panera', 'panda express',
        'dunkin', 'five guys', 'brownie', 'pudding', 'mousse', 'cupcake', 'tart', 'macaron', 'gelato', 'fudge',
        'cinnamon roll', 'mocha', 'matcha', 'latte', 'espresso', 'mocktail',
        'pho', 'gnocchi', 'biryani', 'shawarma', 'samosa', 'bruschetta', 'tortilla', 'risotto', 'tagine'
    ]
    if any(trigger in lowered for trigger in triggers):
        await message.channel.send(random.choice(responses))
        return

client.run(token)