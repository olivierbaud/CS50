def main():
    print("Output:",shorten (input("Input: ")))


def shorten(s):
    voy =["a", "e", "i", "o", "u"]
    result = ""
    for _ in s:
        if _.lower() not in voy:
            result = result + _
    return result

if __name__ == "__main__":
    main()
