positions=["   " for i in range(9)]

def print_board():
    print(f'|{positions[0]}|{positions[1]}|{positions[2]}|')
    print(f'|{positions[3]}|{positions[4]}|{positions[5]}|')
    print(f'|{positions[6]}|{positions[7]}|{positions[8]}|')

def player_move(icon):
    if icon==" X ":
        print("Your turn player 1")
    elif icon==" O ":
        print("Your turn player 2")
    choice=int(input("Enter position(1-9):"))
    if positions[choice-1]=="   ":
        positions[choice-1]=icon
    else:
        print("Position is taken\n")

def victory(icon):
    if positions[0]==icon and positions[1]==icon and positions[2]==icon or\
    positions[3]==icon and positions[4]==icon and positions[5]==icon or\
    positions[6]==icon and positions[7]==icon and positions[8]==icon or\
    positions[0]==icon and positions[4]==icon and positions[8]==icon or\
    positions[2]==icon and positions[4]==icon and positions[6]==icon or\
    positions[0]==icon and positions[3]==icon and positions[6]==icon or\
    positions[1]==icon and positions[4]==icon and positions[7]==icon or\
    positions[2]==icon and positions[5]==icon and positions[8]==icon:
        return True
    return False

def draw():
    if "   " not in positions:
        return True
    else:
        return False


while True:
    print_board()
    player_move(" X ")
    print_board()
    if victory(" X "):
        print("Congrats X you Won")
        break
    elif draw():
        print("Its a draw")
        break
    player_move(" O ")
    if victory(" O "):
        print("Congrats O you Won")
        break
    

    
    

