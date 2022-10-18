import re

def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    if matches := re.search(r"^([0-9]?[0-9]?[0-9])\.([0-9]?[0-9]?[0-9])\.([0-9]?[0-9]?[0-9])\.([0-9]?[0-9]?[0-9])$", ip):
        A,B,C,D = matches.groups()
        if int(A) <= 255 and int(B) <= 255 and int(C) <= 255 and int(D) <= 255:
            return True
        else:
            return False
    else:
        return False

if __name__ == "__main__":
    main()