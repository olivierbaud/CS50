
camel = input("camelCase: ")

print("snake_case: ", end="")
# loop in the string
for s in camel:
    # check if upper caracter
    if s.isupper():
        s = s.lower()
        print ("_", end="")
    print(s, end="")
# new line
print()
