"""In a file called outdated.py, implement a program that prompts the user for a date, anno Domini,
in month-day-year order, formatted like 9/8/1636 or September 8, 1636,
wherein the month in the latter might be any of the values in the list below:
Then output that same date in YYYY-MM-DD format. If the user’s input is not a valid date in either format,
prompt the user again. Assume that every month has no more than 31 days;
no need to validate whether a month has 28, 29, 30, or 31 days."""

months = [
    "",                 # add a blank entry so the month match to the index
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

def main():

    while True:
        try:
            date = input("Date :")
            date_dash = date.split("/")     # list of the input if like 9/8/1636
            date_word = date.split(" ")     # list of the input if like September 8, 1636

            if len(date_dash) == 3:         # if date like 9/8/1936
                month = int(date_dash[0])
                day = int(date_dash[1])
                year = int(date_dash[2])
                if  month > 12:
                    continue
                elif year > 2100:
                    continue
                elif day > 31:
                    continue
                else:
                    return print(f"{year:02}-{month:02}-{day:02}")

            if len(date_word) == 3:         # if date like September 8, 1636
                m = date_word[0]
                d = int(date_word[1].replace(",",""))
                y = int(date_word[2])

                if m not in months:
                    continue
                elif d > 31:
                    continue
                elif date_word[1].find(",") < 1:
                    continue
                else:
                    return print(f"{y:02}-{months.index(m):02}-{d:02}")


        except EOFError:
            break
        except ValueError:
            continue
main()
