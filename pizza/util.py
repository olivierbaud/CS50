import sys
# function check if one argument in the command line, and the file extension
# need command line argument(sys.argv) and the extension in string format ("py" or "csv")
def check(arg, ext):
    try:
        if len(arg) == 1:
            sys.exit("Too few command-line arguments")
        elif len(arg) > 2:
            sys.exit("Too many command-line arguments")
        elif arg[1].split(".")[1] != ext:
            sys.exit(f"Not a {ext} file")
        else:
            with open(arg[1]) as file:
                return file
    except FileNotFoundError:
        sys.exit("File does not exist")
    except IndexError:
        sys.exit(f"Not a {ext} file")