PATTERN_PARSER = [
    r".*se trouve l[e|'|a]\s?(.*)?\?",
    r".*trouver ([^\?]*)\?",
    r".*se situe l[e|'|a]\s?(.*)?\?",
    r".*adresse d[e|'|u]\s?(.*)?\?",
    r".*se trouve (.*)?\?",
    r".*ou se trouve ([^\?]*)\?",
    r".*Où se situent ([^\?]*)\?"
]

SENTENCES_ADDRESS = [
    "Mais bien sur ! La voici : ",
    "Si je  me rappelle bien, c'est : ",
    "Il me semblerait bien que ce soit ... : ",
    "Sans nul doute ... : ",
    "Si je ne m'abuse : "]

SENTENCES_WIKI = [
    "T'ai-je déja raconté l'histoire de cette contrée incroyable... ? ",
    "Il fut un temps où je venais flaner dans ce lieu ...   ",
    "l'histoire est la mémoire du monde, et voici celle de ce lieu magique  ",
    "il faut se souvenir des bonnes choses, voici l'histoire de ce lieu bucolique"
]
