# test
    # test

def main():
    percentage = convert(input("Fraction: "))
    print(gauge(percentage))


def gauge(percentage):
    if percentage <= 1:
        return "E"
    elif percentage >= 99:
        return "F"
    else:
        return str(percentage)+"%"
test
pour voir