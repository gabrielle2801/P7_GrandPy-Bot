import random
from grandpy_bot.constant import SENTENCES_ADDRESS


def sentences_choice():

    choice = random.choice(SENTENCES_ADDRESS)
    print(choice)
    return {"sentences": choice}
    # return random.choice(SENTENCES_ADDRESS)
