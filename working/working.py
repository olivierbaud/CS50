import re

def main():
    print(convert(input("Hours: ")))

def convert(s):
    if matches := re.search(r"([0-9]+):?([0-9]+)? ([APM ]+) to ([0-9]+):?([0-9]+)? ([APM]+)", s):
        h1, m1, ampm1, h2, m2, ampm2 = matches.groups()
        if m1 and int(m1) > 59 or m2 and int(m2) > 59 or int(h1) > 12 or int(h2) > 12:
            raise ValueError
        else:
            if ampm1 == "PM":
                h1 = int(h1) + 12
            if ampm2 == "PM":
                h2 = int(h2) + 12
            if int(h1) == 12 or int(h1) == 24:
                h1 = int(h1)-12
            if int(h2) == 12 or int(h2) == 24:
                h2 = int(h2)-12
            if m1 and m2:
                return f"{int(h1):02d}:{int(m1):02d} to {int(h2):02d}:{int(m2):02d}"
            elif m1 == None and m2 == None:
                return f"{int(h1):02d}:00 to {int(h2):02d}:00"
            else:
                raise ValueError
    else:
        raise ValueError

if __name__ == "__main__":
    main()