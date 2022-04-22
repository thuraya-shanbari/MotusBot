from dotenv import load_dotenv
import os
from discord.ext import commands

load_dotenv(dotenv_path="config")

class MotusBot(commands.Bot):
    def __init__(self):
        super().__init__(command_prefix="!")

    async def on_ready(self):
        print("MotusBot is ready to play!")

bot = MotusBot()


@bot.command()
async def ping(ctx):
    await ctx.send("pong!")


@bot.command()
async def play(ctx, arg=""):
    if (arg == ""):
        await ctx.send("Please specify a language")

    elif (arg == "fr"):
        await ctx.send("Langue francaise choisi")

    elif (arg == "en"):
        await ctx.send("English language chosen")

    else:
        await ctx.send("Unknown language")


bot.run(os.getenv("TOKEN"))
