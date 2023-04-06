import openai_secret_manager
import openai
import discord
from discord.ext import commands

# Fetching OpenAI API Key from the Secrets Manager
assert "openai" in openai_secret_manager.get_services()
secrets = openai_secret_manager.get_secret("openai")

# Authenticating with the OpenAI API
openai.api_key = secrets["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"]

# Setting up the Discord Bot
bot = commands.Bot(command_prefix='!')

# Defining the chatgpt command
@bot.command(name='chatgpt')
async def chatgpt(ctx, *, message):
    # Generating a response from the OpenAI GPT-3 model
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=message,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.5,
    )

    # Sending the generated response to the Discord channel
    await ctx.send(response.choices[0].text)

# Running the Discord Bot
bot.run("MTA5MzM0OTg0ODA1NDUxMzY4NA.GHSEjJ.Ob8A089BJoajToD4T1taUyD4Y2yZBO5S-nF1Lo")