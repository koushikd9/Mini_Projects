import random

def guess():
    range=int(input("What is the range"))
    num=random.randint(1,range)

    while True:
        guess=int(input("Guess the number:"))
        if guess==num:
            print("You are correct")
            break
        elif guess>=num:
            print("Number is high")
        else:
            print("Number is low")

guess()