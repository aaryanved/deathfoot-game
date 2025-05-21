import random

pp = 0
i = 0
while i < 5:
    try:
        n = int(input("Enter a number: "))
    except ValueError:
        print("Invalid input.")
        continue
    if n < 4:
        m = random.randint(1, 3)
        if n == m:
            print("You Scored!")
            pp += 1
        else:
            print("You didn't score.")
            print("")
        i += 1
    else:
        print("Idiot boy. Game crash because of your foolishness.")
        exit(0)
print("Points Scored:", pp)