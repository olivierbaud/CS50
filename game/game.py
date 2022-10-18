import random
#Prompts the user for a level, . If the user does not input a positive integer, the program should prompt again.
#Randomly generates an integer between 1 and , inclusive, using the random module.
#Prompts the user to guess that integer. If the guess is not a positive integer, the program should prompt the user again.
#If the guess is smaller than that integer, the program should output Too small! and prompt the user again.
#If the guess is larger than that integer, the program should output Too large! and prompt the user again.
#If the guess is the same as that integer, the program should output Just right! and exit.

while True:
    try:
        level = int(input("Level: "))
        if int(level) > 0:
            break
        else:
            continue
    except ValueError:
        continue

result = random.randint(1,level)

while True:
    try:
        guess = int(input("Guess: "))
    except ValueError:
        continue
    match guess:
        case guess if guess <1:
            continue
        case guess if guess < result:
            print("Too small!")
            continue
        case guess if guess > result:
            print("Too large!")
            continue
        case guess if guess == result:
            print("Just right!")
            break
