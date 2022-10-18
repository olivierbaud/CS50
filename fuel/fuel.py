"""
In a file called fuel.py, implement a program that prompts the user for a fraction,
formatted as X/Y, wherein each of X and Y is an integer, and then outputs, as a percentage rounded to the nearest integer,
how much fuel is in the tank.
If, though, 1% or less remains, output E instead to indicate that the tank is essentially empty.
And if 99% or more remains, output F instead to indicate that the tank is essentially full.

If, though, X or Y is not an integer, X is greater than Y, or Y is 0, instead prompt the user again.
(It is not necessary for Y to be 4.)
Be sure to catch any exceptions like ValueError or ZeroDivisionError.
"""
"""
def main():
    print (get_fraction("Fraction: "))

def get_fraction(prompt):
    while True:
        try:
            fraction = input(prompt)
            op = int(fraction.find("/"))
            X = int(fraction[0:op])
            Y = int(fraction[op+1:len(fraction)])
            if X/Y >1:
                continue
            elif X/Y >= 0.99:
                return "F"
            elif X/Y <= 0.01:
                return "E"
            else:
                return f"{int(round((X/Y * 100)))}%"
        except ValueError:
            continue
        except ZeroDivisionError:
            continue
main()"""

def main():
    percentage = convert(input("Fraction: "))
    print(gauge(percentage))

def convert(fraction):
    while True:
        try:
            op = int(fraction.find("/"))
            X = int(fraction[0:op])
            Y = int(fraction[op+1:len(fraction)])
            if X > Y:
                raise ValueError

            else:
                return int(round(X/Y * 100))
        except ValueError:
            raise ValueError
        except ZeroDivisionError:
            raise ZeroDivisionError

def gauge(percentage):
    if percentage <= 1:
        return "E"
    elif percentage >= 99:
        return "F"
    else:
        return percentage


if __name__ == "__main__":
    main()