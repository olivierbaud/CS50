def main():
    greets = input("Greetings: ")
    print(f"${value(greets)}")


def value(greeting):
    if greeting.strip().lower().startswith("hello"):
        return 0

    elif greeting.strip().lower().startswith("h"):
        return 20

    # anything else -> 100$
    else:
        return 100

if __name__ == "__main__":
    main()