import string
def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    i = 0
    numindex = 0

    #All vanity plates must start with at least two letters.”
    if not s[0].isalpha() and s[1].isalpha():
        #print("no 2 letter first")
        return False

    #“… vanity plates may contain a maximum of 6 characters (letters or numbers) and a minimum of 2 characters.”
    if len(s) < 2 or len(s) > 6:
        #print("wrong length")
        return False

    # The first number used cannot be a ‘0’.”
    while i < len(s):
        if s[i].isnumeric():
            if s[i] == "0":
                #print("first number can't be 0")
                return False
            else:
                numindex = i
                break
        i += 1

    #“Numbers cannot be used in the middle of a plate; they must come at the end.
    # For example, AAA222 would be an acceptable; AAA22A would not be acceptable.
    if numindex > 0:
        while numindex < len(s):
            if s[numindex].isalpha():
                #print("numbers can't be in the middle")
                return False
            else:
                numindex += 1

    #“No periods, spaces, or punctuation marks are allowed.”
    for c in s:
        if c in string.punctuation or c == " ":
            #print("no punctuation")
            return False

    return True

main()