
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
        return str(percentage)+"%"

if __name__ == "__main__":
    main()