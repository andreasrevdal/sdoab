import discord
from discord.ext import commands
import openai

print(discord.__version__) 

intents = discord.Intents.default()
intents.messages = True
intents.message_content = True
bot = commands.Bot(command_prefix='!', intents=intents)

openai_api_key = 'API_KEY'

@bot.event
async def on_ready():
    print(f'{bot.user.name} came online!')
    await bot.change_presence(activity=discord.Game(name="@ me to talk!"))

@bot.event
async def on_message(message):
    if bot.user.mentioned_in(message) and message.mention_everyone is False:
        if message.author == bot.user:
            return

        content = message.content.replace(f'<@!{bot.user.id}>', '').strip()

        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo-16k",
            messages=[
                {"role": "system", "content": "You are NAME a smart and fun bot that serves as the mascot of the Discord server called NAME. You live to help others."},
                {"role": "user", "content": content}
            ],
            api_key=openai_api_key
        )

        await message.channel.send(response['choices'][0]['message']['content'])

    await bot.process_commands(message)

# Run the bot
bot.run('discord bot token')
