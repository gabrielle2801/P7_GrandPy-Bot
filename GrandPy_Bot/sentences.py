import random
from grandpy_bot.constant import SENTENCES_ADDRESS, SENTENCES_WIKI


def sentences_address():

    choice_address = random.choice(SENTENCES_ADDRESS)
    print(choice_address)
    return {"sentences": choice_address}


def sentences_wiki():
    choice_wiki = random.choice(SENTENCES_WIKI)
    return {"sentences_wiki": choice_wiki}
