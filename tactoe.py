Board = [1,2,3,4,5,6,7,8,9]

def Game():
    win = [(0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6)]

def boards():
    print(Board[0],Board[1],Board[2])
    print(Board[3],Board[4],Board[5])
    print(Board[6],Board[7],Board[8])
    print()

boards()

def player1():
    if Board[n] == 'x' or Board(n) == 'o':
        print("do not go there")
        player1()
    else:
        Board[n] = 'x'

def player2():
    if Board[n] == 'x' or Board(n) == 'o':
        print("do'nt go there")
        player1()
    else:
        Board[n] = 'o'

def position():
    a = input()
    try:
        a = int(a)
        a -= 1
        if a in range(0,9):
            return a
    else:
        print("there is no board")
        print("there is no number")


def board_empty_win():
    count = 0
    for a in win:
        if Board[a[0]] == Board[a[1]] == Board[a[2]] =='x':
            print("player1 win")
            return

        if Board[a[0]] == Board[a[1]] == Board[a[2]] =='o':
            print("player2 win")
            return

        for a in range(9):
            if Board[a] == 'x' or Board[a] == 'o'
                count += 1

            if count == 9:
                print("all space are full and the game end")
                return True
