import random

def game(my_choice,computer_choice):

    if my_choice==computer_choice:
        print("Its a Tie\n")

    elif (my_choice==1 and computer_choice==3 or my_choice==2 and computer_choice==1 or my_choice==3 and computer_choice==2):
        print("You Won\n")

    elif (my_choice==1 and computer_choice==2 or my_choice==2 and computer_choice==3 or my_choice==3 and computer_choice==1):
        print("Computer has won\n")

def display_fun(number):
    if number==1:
        value="Rock"
    elif number==2:
        value="Paper"
    elif number==3:
        value="Scissor"
    return value

while(True):
    my_choice=int(input("Enter your choice: \n1.Rock \n2.Paper \n3.Scissor\n"))
    computer_choice=random.randint(1,3)
    print(f" Your choice:{display_fun(my_choice)}\n Computer choice:{display_fun(computer_choice)}\n")
    game(my_choice,computer_choice)


