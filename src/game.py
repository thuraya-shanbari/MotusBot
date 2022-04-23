import random
from discord import NotFound


def file_to_list(filename):
    res = []
    f = open(filename)
    for line in f:
        res.append(line.lower()[:-1])

    return res


eng_list = file_to_list("src/words/english")
fr_list = file_to_list("src/words/french")


def word_to_guess(lang):
    if (lang == "en"):
        rand = random.randint(0, 1376)
        return eng_list[rand]
    else:
        rand = random.randint(0, 1530)
        return fr_list[rand]


def place(guess, ref):
    res = ""
    for i in range(5):
        if (guess[i] == ref[i]):
            res += 'g'
        elif (guess[i] in ref):
            res += 'y'
        else:
            res += 'r'
    return res


async def start(lang, channel, bot):
    chan = bot.get_channel(int(channel.id))
    word = word_to_guess(lang)
    blank = ""
    for i in range(5):
        blank += '\U000026AA'
    await chan.send(blank)
    tries = 0
    found = True

    while (tries < 5):
        guess = await bot.wait_for('message')
        msg = guess.content
        if (len(msg) != 5):
            continue

        if (msg not in eng_list and lang == "en"):
            continue

        if (msg not in fr_list and lang == "fr"):
            continue

        res = place(msg, word)
        to_send = ""
        for letter in res:
            if (letter == 'g'):
                to_send += '\U0001F7E2'

            if (letter == 'y'):
                to_send += '\U0001F7E1'

            if (letter == 'r'):
                to_send += '\U0001F534'

            if (letter != 'g'):
                found = False

        await chan.send(to_send)
        if (found == True):
            if (lang == "en"):
                await chan.send("Congratulations! You have guess the word!")
            else:
                await chan.send("Felicitations ! Vous avez trouve le mot !")
            return

        tries += 1

    if (tries == 5 and found == False):
        if (lang == "en"):
            await chan.send("Oh no! You lost! The word was: " + word)
        else:
            await chan.send("Oh non ! Vous avez perdu ! Le mot etait : " + word)

    if (found == True):
        if (lang == "en"):
            await chan.send("Congratulations! You have guess the word!")
        else:
            await chan.send("Felicitations ! Vous avez trouve le mot !")
