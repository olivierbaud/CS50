import sys
import random
import pyfiglet
from pyfiglet import Figlet

figlet = Figlet()
fonts = figlet.getFonts()


def main():

    if len(sys.argv) == 1:
        text = input("Input :")
        font = random.choice(fonts)
        output(text, font)
    elif len(sys.argv) == 3:
        tagv = sys.argv[1] == "-f" or sys.argv[1] == "--font"
        fontv = sys.argv[2] in fonts
        if check2(tagv,fontv):
            text = input("Input :")
            output(text,sys.argv[2])
    else:
        sys.exit("Invalid usage1")

def output(t, f):
    figlet.setFont(font=f)
    print(figlet.renderText(t))

def check2(t,f):
    if t and f:
        return True
    else:
        sys.exit("Invalid usage4")

main()