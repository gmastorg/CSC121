def generateRandomCharacter():

    import string
    import random

    code = {}

    key = []

    value = []

    key = [i for i in string.printable]

    value = random.sample(key, len(key))

    code = dict(zip(key,value))


