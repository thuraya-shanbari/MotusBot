from dotenv import load_dotenv
import os
from discord.ext import commands
import game

load_dotenv(dotenv_path="src/config")


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
        await game.start("fr", ctx.message.channel, bot)

    elif (arg == "en"):
        await ctx.send("English language chosen")
        await game.start("en", ctx.message.channel, bot)

    else:
        await ctx.send("Unknown language")


# @bot.event
# async def on_message(message):
#     if (message.author == bot.user):
#         return
#
#     if (message.content.startswith("ping")):
#         await message.channel.send("pong!")
#
#     if (message.content == "blue"):
#         await message.add_reaction("\U0001F499")


bot.run(os.getenv("TOKEN"))
