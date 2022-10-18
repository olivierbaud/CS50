names = []

def main():
    while True:
        try:
            names.append(input(""))
        except EOFError:
            printlist(names)
            break


def printlist(n):
    if len(n) == 1:
        print(f"Adieu, adieu, to {n[0]}" )
    elif len(n) == 2:
        print(f"Adieu, adieu, to {n[0]} and {n[1]}")
    else:
        i = 0
        print("Adieu, adieu, to ", end="")
        while i < (len(n)-1):
            print (n[i], end=", ")
            i+=1
        print (f"and {n[i]}")

main()
