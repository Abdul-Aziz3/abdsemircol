import random

def getRandomNumber():
    random_tall = random.randint(1,200)
    random_tall2 = random.randint(1,200)

    return random_tall, random_tall2

print(getRandomNumber())
