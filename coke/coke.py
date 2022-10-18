
def main():
    amount = 50
    print ("Amount due :", amount)

    while amount >0:
        coin = int(input("Insert Coin: "))
        if coin == 5 or coin == 10 or coin == 25:
            amount = amount - coin
            if amount <= 0:
                print ("Changed owned: ", abs(amount))
            else:
                print ("Amount due: ", amount)
        else:
            print("50 is not accepted")

main()