def convert(text):
    text = text.replace(":)", "🙂")
    text = text.replace(":(", "🙁")
    return texts


def main():
    text_mod = convert(input("type your text: "))
    print (text_mod)

main()