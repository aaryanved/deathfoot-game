import random
pp = 0
n = int(input("Enter a number: "))
if n < 4:
    m = random.randint(1, 3)
    if n == m:
        print("You Scored!")
        print("")
        pp += 1
    else:
        print("You didn't score.")
        print("")
else:
    print("Idiot boy. Game crash because of your foolishness.")
    exit(0)