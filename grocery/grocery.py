""""In a file called grocery.py, implement a program that prompts the user for items, one per line,
until the user inputs control-d (which is a common way of ending one’s input to a program).
Then output the user’s grocery list in all uppercase, sorted alphabetically by item,
prefixing each line with the number of times the user inputted that item.
No need to pluralize the items. Treat the user’s input case-insensitively."""

grocery = {}

def main():
    while True:
        try:
    # input item
            item = input().upper()
    # check if item in in the grocery: add one to the value
            if item in grocery:
                grocery[item] += 1
    # otherwise add the item to the grocery
            else:
                grocery.update({item: 1})
    # if CTRLD print the list
        except EOFError:
            grocery_print(grocery)
            break
        except KeyError:
            continue


def grocery_print(list):
    for i in sorted(list):
        print (list[i], i)

main()