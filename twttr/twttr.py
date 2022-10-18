text = input("Input: ")
voy = ["a", "e", "i", "o", "u"]

def main():
    print ("Output: ", end="")
    for c in text:
        if c.lower() not in voy:
            print (c, end="")
    print()

main()