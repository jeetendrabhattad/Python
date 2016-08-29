#!/usr/bin/python

def PrintDeckOfCards():
    #    cards = input("Enter list of cards to be categorized:")
    cards = list(eval(raw_input("Enter list of cards to be categorized:")))
    print cards
    for x in cards:
        if x in range(1,14):
            print("{} is heart".format(x))
        elif x in range(14,27):
            print("{} is spade".format(x))
        elif x in range(27,40):
            print("{} is diamond".format(x))
        elif x in range(40,53):
            print("{} is club".format(x))
        else:
            print("{} is not from Deck of cards".format(x))

if __name__=="__main__":
    PrintDeckOfCards()
