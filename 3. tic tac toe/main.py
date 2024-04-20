import random


def check_identical_ver(table):
    for i in range(3):
        new_lst = table[i-1]
        if new_lst[0] == "-" or new_lst[1] == "-" or new_lst[2] == "-":
            pass
        else:
            return new_lst[1:] == new_lst[:-1]


def check_identical_hor(table):
    for i in range(3):
        new_lst = [table[0][i-1], table[1][i-1], table[2][i-1]]
        if new_lst[0] == "-" or new_lst[1] == "-" or new_lst[2] == "-":
            pass
        else:
            return new_lst[1:] == new_lst[:-1]


def check_identical_x(table):
    new_lst_x = [table[0][0], table[1][1], table[2][2]]
    if "-" in new_lst_x:
        pass
    else:
        return new_lst_x[1:] == new_lst_x[:-1]


def check_identical_x2(table):
    new_lst_x2 = [table[0][2], table[1][1], table[2][0]]
    if "-" in new_lst_x2:
        pass
    else:
        return new_lst_x2[1:] == new_lst_x2[:-1]


def table_check(table):
    if "-" in table[0] or "-" in table[1] or "-" in table[2]:
        return True
    else:
        return False


def move(table):
    p_move = input("Where would you like to place your mark? (row column) ")
    try:
        global row
        row = int(p_move[0: 1])
        global column
        column = int(p_move[2: 3])
    except (ValueError) as error:
        print("Incorrect Placement of Character")
        move(table)
    else:
        if row > 3 or column > 3 or row < 1 or column < 1:
            print("Only 1 through 3 please!")
            move(table)
        elif table[row-1][column-1] != "-":
            print("Field already taken")
            move(table)
        else:
            return row, column


game_on = True


class Player():
    def __init__(self):
        self.mark = None
        self.state = None


player_1 = Player()

print("Welcome to my tic tac and toe project!")


def player_role():
    player = input("Do you want to begin? (Y / N) ")
    if player == "Y" or player == "y":
        player_1.state = 0
        player_1.mark = "x"
        print(player_1.state)
    elif player == "N" or player == "n":
        player_1.state = 1
        player_1.mark = "o"
        print(player_1.state)
    else:
        print("Invalid answer!")
        player_role()


def Game():
    player_role()
    global game_on
    global row, column
    table = [["-", "-", "-",], ["-", "-", "-",], ["-", "-", "-"]]
    if player_1.state == 0:
        while game_on:
            move(table)
            # move = input("Where would you like to place your mark? (row column) ")
            # try:
            #    row = int(move[0: 1])
            #    column = int(move[2: 3])
            # except ValueError:
            #    print("Value error")
            table[row-1][column-1] = player_1.mark
            print(*table, sep="\n")
            if check_identical_ver(table) or check_identical_hor(table) or check_identical_x(table) or check_identical_x2(table) == True:
                game_on = False
                print("Someone won")
                break
            if not table_check(table):
                game_on = False
                print("No more space")
                print("It's a draw!")
                break
            input("Press enter to continue the game with the opponent's move ")
            if table_check(table) == True:
                e_row = random.randint(1, 3)
                e_column = random.randint(1, 3)
                while table[e_row-1][e_column-1] != "-":
                    e_row = random.randint(1, 3)
                    e_column = random.randint(1, 3)
                table[e_row-1][e_column-1] = "o"

            print(row, column)
            print(*table, sep="\n")
            if check_identical_ver(table) or check_identical_hor(table) or check_identical_x(table) or check_identical_x2(table) == True:
                print("Someone won")
                game_on = False
                break
            if not table_check(table):
                game_on = False
                print("No more space")
                print("It's a draw!")
                break
    elif player_1.state == 1:
        while game_on:
            input("Press enter to continue the game with the opponent's move ")
            if table_check(table) == True:
                e_row = random.randint(1, 3)
                e_column = random.randint(1, 3)
                while table[e_row-1][e_column-1] != "-":
                    e_row = random.randint(1, 3)
                    e_column = random.randint(1, 3)
                table[e_row-1][e_column-1] = "x"
            print(*table, sep="\n")
            if check_identical_ver(table) or check_identical_hor(table) or check_identical_x(table) or check_identical_x2(table) == True:
                print("Someone won")
                game_on = False
                break
            if not table_check(table):
                game_on = False
                print("No more space")
                print("It's a draw!")
                break
            move(table)
            # move = input("Where would you like to place your mark? (row column) ")
            # try:
            #    row = int(move[0: 1])
            #    column = int(move[2: 3])
            # except ValueError:
            #    print("Value error")
            table[row-1][column-1] = player_1.mark
            print(*table, sep="\n")
            if check_identical_ver(table) or check_identical_hor(table) or check_identical_x(table) or check_identical_x2(table) == True:
                game_on = False
                print("Someone won")
                break
            if not table_check(table):
                game_on = False
                print("No more space")
                print("It's a draw!")
                break

    print(*table, sep="\n")


game = Game()
print("game ended!")
