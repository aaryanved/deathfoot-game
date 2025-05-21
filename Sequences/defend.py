import random

def defend(bp):
    n = int(input("Enter a number: "))
    if n < 4:
        m = random.randint(1, 3)
        if n == m:
            print("You Lost!")
            print("")
            bp += 1
        else:
            print("Bot didn't score.")
            print("")
    else:
        print("Idiot boy. Game crash because of your foolishness.")
        exit(0)
    return bp