# Randomly generates ten (10) math problems formatted as X + Y = , wherein each of X and Y is a non-negative integer with  digits.
# No need to support operations other than addition (+).
# Prompts the user to solve each of those problem. If an answer is not correct (or not even a number), the program should output EEE
# and prompt the user again, allowing the user up to three tries in total.
# If the user has still not answered correctly after three tries, the program should output the correct answer.
# The program should ultimately output the user’s score, a number out of 10.
# Structure your program as follows, wherein get_level prompts (and, if need be, re-prompts)
# the user for a level and returns 1, 2, or 3, and generate_integer returns a randomly generated non-negative integer
# with level digits or raises a ValueError if level is not 1, 2, or 3:

import random

def main():
    i = 0
    score = 0
    level = get_level()
    while i < 10:
        s = 0
        X = generate_integer(level)
        Y = generate_integer(level)
        result = X + Y
        while s < 3:
            try:
                print (f"{X} + {Y} = ", end ="")
                r_input = int(input (""))
                if r_input == result:
                    score += 1
                    break
                elif s == 2: # print result after 3 wrong answers
                    print(f"{X} + {Y} = {result}")
                else:
                    print("EEE")
                s += 1
            except ValueError:
                print("EEE")
                s += 1
                continue
        i += 1
    print(f"Score: {score}")

def get_level():
    ...
    # Prompts the user for a level, . If the user does not input 1, 2, or 3, the program should prompt again.
    while True:
        try:
            level = int(input("Level: "))
            if level in [1,2,3] :
                return level
            else:
                continue
        except ValueError:
            continue

def generate_integer(level):
    ...
    if level == 1:
        return random.randint(0,9)
    else:
        return random.randint(10**(level-1),10**level-1)

if __name__ == "__main__":
    main()