
answer = input("What is the Answer to the Great Question of Life, the Universe and everything? ")


def main():

    #cleaning the string (lower case and remove spaces)
    answer_clean = clean(answer)

    #first method with if / else
    """
    if answer_clean == "42" or answer_clean == "forty-two" or answer_clean == "forty two":
        print("yes")
    else:
        print("no")
    """

    #second method with match / case
    match answer_clean:
        case "42" | "forty two" | "forty-two":
            print("yes")
        case _:
            print("no")

def clean(text):
    return text.lower().strip()



main()