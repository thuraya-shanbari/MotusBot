from discord.ext import commands

bot = commands.Bot(command_prefix="!")

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

bot.run('OTY2OTk2NTE1ODE2MDc5NDMw.YmJ3rw.ucwzVoE0mYLKQesNIvJ2UeAgZgA')