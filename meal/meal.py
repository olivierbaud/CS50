# asking for the time: '8:00', '18:00', or '9:00 a.m.' or '6:00 p.m.'
time = input ("What time it is? ")

def main():
    # block for am/pm
    if time.endswith("a.m.") or time.endswith("p.m."):
        time_a, b = time.split(" ")

        if b == "p.m.":
            time_c = convert(time_a) + 12
            print_f(time_c)

        elif b == "a.m.":
            time_c = convert(time_a)
            print_f(time_c)

    # block without am/pm
    else:
        time_c = convert(time)
        print_f(time_c)

# function to print out the result depending of the hours
def print_f(food):
    if 7 <= food <= 8:
        print ("breakfast time")
    elif 12 <= food <= 13:
        print ("lunch time")
    elif 18 <= food <= 19:
        print ("dinner time")

# convert time in base 10 (7:30 -> 7.5)
def convert(time):
    h, m = time.split(":")
    return int(h) + int(m)/60

main()
