import sys
from ..pizza.util import check

arg = sys.argv

def main():
    check(arg)
    print(count(arg[1]))

def count(f):
    lines = 0
    with open(f) as file:
        for row in file:
            if row.lstrip().startswith("#"):
                lines += 0
                #print(lines, row, end ="")
            elif row.isspace():
                lines += 0
                #print(lines, row, end ="")
            else:
                lines += 1
                #print(lines, row, end ="")
    return lines

"""def check(arg):
    try:
        if len(arg) == 1:
            sys.exit("Too few command-line arguments")
        elif len(arg) > 2:
            sys.exit("Too many command-line arguments")
        elif arg[1].split(".")[1] != "py":
            sys.exit("Not a python file")
        else:
            with open(arg[1]) as file:
                return file
    except FileNotFoundError:
        sys.exit("File does not exist")
"""

if __name__ == "__main__":
    main()