import sys
import os
from PIL import Image, ImageOps

arg = sys.argv

def main():
    check (arg)
    input = Image.open(arg[1])
    shirt = Image.open("shirt.png")
    input = ImageOps.fit(input,shirt.size)
    input.paste(shirt, shirt)
    input.save(arg[2])

def check(arg):
    ext = [".jpg", ".jpeg", ".png"]
    if len(arg) == 3:
        ext1 = os.path.splitext(arg[1])[1].lower()
        ext2 = os.path.splitext(arg[2])[1].lower()
        try:
            if ext1 not in ext or ext2 not in ext:
                sys.exit("Invalid input")
            elif ext1 != ext2:
                sys.exit("Input and Ouptut have different extensions")
            else:
                with open(arg[1]) as file:
                    return file
        except FileNotFoundError:
            sys.exit("input file does not exist")
        except IndexError:
            sys.exit("Not an image file")
    else:
        if len(arg) < 3:
                sys.exit("Too few command-line arguments")
        else:
                sys.exit("Too many command-line arguments")


if __name__ == "__main__":
    main()