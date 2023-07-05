import random

chk_number = 0

while True:
    try:
        # Prompt for level
        level = int(input("Level: "))
        if level >= 1:
            chk_number = random.randint(1, level)
            break
    except ValueError:
        pass

while True:
    try:
        # Prompt for guess
        guess = int(input("Guess: "))
        if guess >= 0:
            if guess == chk_number:
                print("Just right!")
                break
            elif guess > chk_number:
                print("Too large!")
            else:
                print("Too small!")
    except ValueError:
        pass