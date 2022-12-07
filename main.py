import os
import openai
import discord
from discord.ext import commands

# <summary>
#
#   Python Discord Bot answering messages with AI generated text
#   using OpenAI's GPT-3 API
#   using discord.py
#
#   tr3x © 2022
#
# </summary>


# OpenAI API Key
openai.api_key = os.getenv("OPENAI_API_KEY")

# Discord Bot Token
discord_token = os.getenv("DISCORD_TOKEN")

# declaring Discord Bot
client = commands.Bot(command_prefix="", intents=discord.Intents.all())


# on msg event bot will check if author is not itself, if channel is private chat and will send a message which will
# be edited when answer is ready
@client.event
async def on_message(message):
    if message.author == bot.user:
        return
    if isinstance(message.channel, discord.DMChannel):
        await message.channel.typing()
        message = await message.channel.send("Ich denke nach...")
        await message.edit(content=answer(message.content))


# requesting and returning answer from openai via davinci-003
def answer(message):
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=message,
        temperature=0.7,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    return response.get("choices")[0].get("text")


# running bot
client.run(discord_token)
