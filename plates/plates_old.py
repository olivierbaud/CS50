import string

def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    plate_list = []
    num = []

    for c in s:
        plate_list.append(c)

    for i in range(len(s)):
        if plate_list[i].isnumeric():
            num.append(plate_list[i])

    # check if between 2 and 6 caracters
    if 1 < len(s) < 7:

        # check if 2 first caracters are letters
        if (plate_list[0].isalpha() and plate_list[1].isalpha()):

            # check if numbers at the end when there are numbers
            if not checknumber(num):

                # check if first number != 0
                if len(num) > 0 and int(num[0]) != 0:

                    # Check if punctuation
                    if not punct(s):
                        return True

    else:
        return False

def punct(t):
    for c in t:
        if c in string.punctuation:
            return True

def checknumber(l):
    print(l)
    for n in l:
        if not n.isnumeric():
            return True


main()