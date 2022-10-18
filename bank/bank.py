# ask for greetings
greetings = input("Greetings: ")

def main():
    # clean the text
    greetings_c = greetings.strip().lower()

    # if it starts with hello -> 0$
    if greetings_c.startswith("hello"):
        print("$0")

    # if it starts with h -> 20*
    elif greetings_c.startswith("h"):
        print("$20")

    # anything else -> 100$
    else:
        print("$100")


main()