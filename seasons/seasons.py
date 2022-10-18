from datetime import date
import inflect
p = inflect.engine()
import sys


def main():
    print(date_gap(input("Date of birth?: ")))

def date_gap(birth):
    try:
        birthday = date(int(birth.split("-")[0]),int(birth.split("-")[1]),int(birth.split("-")[2]))
    except ValueError:
        sys.exit("Invalid date")
    result = date.today() - birthday
    return f"{p.number_to_words(result.days * 24 * 60, andword='').capitalize()} minutes"

if __name__ == "__main__":
    main()