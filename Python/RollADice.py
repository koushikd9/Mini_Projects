import random

while True:
    choice=input("Do you want to Roll Dice or exit:Y/N").capitalize()
    if choice=="Y":
        print(random.randint(1,6))
    elif choice=="N":
        print("Bye")
        break

