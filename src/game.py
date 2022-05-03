import random
import unidecode
from discord import NotFound


def file_to_list(filename):
    res = []
    f = open(filename)
    for line in f:
        res.append(line.lower()[:-1])
        res.append(unidecode.unidecode(line.lower()[:-1]))

    return res


eng_list = file_to_list("src/words/english")
fr_list1 = file_to_list("src/words/french")
fr_list = [word for word in fr_list1 if len(word) == 5]


def word_to_guess(lang):
    if (lang == "en"):
        rand = random.randint(0, len(eng_list))
        return eng_list[rand]
    else:
        rand = random.randint(0, len(fr_list))
        return fr_list[rand]


def correct_placement(guess, ref, found_letters):
    res = ""
    for i in range(5):
        if (guess[i] == ref[i]):
            res += 'g'
            found_letters.remove(guess[i])
        else:
            res += 'r'

    return res


def place(guess, ref):
    res = ""
    found_letters = [i for i in ref]
    green = correct_placement(guess, ref, found_letters)
    for i in range(5):
        if (guess[i] in found_letters and green[i] != 'g'):
            res += 'y'
            found_letters.remove(guess[i])
        else:
            res += green[i]

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
        found = True
        guess = await bot.wait_for('message')
        msg = unidecode.unidecode(guess.content.lower())
        if (len(msg) != 5):
            continue

        if (msg not in eng_list and lang == "en"):
            continue

        if (msg not in fr_list and lang == "fr"):
            continue

        res = place(msg, unidecode.unidecode(word))
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
                await chan.send("Congratulations! You have guessed the word!")
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
            await chan.send("Congratulations! You have guessed the word!")
        else:
            await chan.send("Felicitations ! Vous avez trouve le mot !")


