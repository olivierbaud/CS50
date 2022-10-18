import sys
import csv

arg = sys.argv
input = arg[1]
output = arg[2]

def main():
    check (arg, "csv")
    output_file(clean(input))

#function to create a csv file with header from a list of dict [{},{}]
def output_file(list):
    i=0
    with open(output, "w", newline="\n") as file:
        writer = csv.DictWriter(file, fieldnames=["first", "last", "house"])
        writer.writeheader()
        while i < len(list):
            writer.writerow({"first": list[i]["first"],"last": list[i]["last"],"house": list[i]["house"]})
            i += 1

# create a [{},{},{}] from a csv file and separate the name key ('name': 'Spinnet, Alicia')
# to first and last ('first': 'Alicia', 'last': 'Spinnet')
def clean(f):
    table = []
    name = []
    i = 0
    with open(f) as file:
        reader = csv.DictReader(file)
        for row in reader:
            table.append(row)
    while i < len(table):
        name.append(table[i]["name"].split(","))
        table[i].update({"first": name[i][1].lstrip(), "last": name[i][0]})
        i += 1
    return table

# check if command line is: file.py input.csv output.csv
def check(arg, ext):
    try:
        if len(arg) < 3:
            sys.exit("Too few command-line arguments")
        elif len(arg) > 3:
            sys.exit("Too many command-line arguments")
        elif arg[1].split(".")[1] != ext:
            sys.exit(f"input is not a {ext} file")
        elif arg[2].split(".")[1] != ext:
            sys.exit(f"output is not a {ext} file")
        else:
            with open(arg[1]) as file:
                return file
    except FileNotFoundError:
        sys.exit("input file does not exist")
    except IndexError:
        sys.exit(f"Not a {ext} file")

if __name__ == "__main__":
    main()