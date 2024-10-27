print("Welcome to the biggest Tic Tac Toe contest in the world.")
print()
Symbol_for_PLAYER1 = input("PLAYER-1, ascertain your symbol: ")
print()
Symbol_for_PLAYER2 = input("PLAYER-2, ascertain your symbol: ")

if Symbol_for_PLAYER1 >= Symbol_for_PLAYER2:
    Larger_symbol = Symbol_for_PLAYER1
else:
    Larger_symbol = Symbol_for_PLAYER2

Space_for_symbols = " "
Underline_for_symbols = "_"

Board = ["  " + Space_for_symbols + "  |  " + Space_for_symbols + "  |  " + Space_for_symbols + "  ",
        "  " + Space_for_symbols + "  |  " + Space_for_symbols + "  |  " + Space_for_symbols + "  ",
        "__" + Underline_for_symbols + "__|__" + Underline_for_symbols + "__|__" + Underline_for_symbols + "__",
        "  " + Space_for_symbols + "  |  " + Space_for_symbols + "  |  " + Space_for_symbols + "  ",
        "  " + Space_for_symbols + "  |  " + Space_for_symbols + "  |  " + Space_for_symbols + "  ",
        "__" + Underline_for_symbols + "__|__" + Underline_for_symbols + "__|__" + Underline_for_symbols + "__",
        "  " + Space_for_symbols + "  |  " + Space_for_symbols + "  |  " + Space_for_symbols + "  ",
        "  " + Space_for_symbols + "  |  " + Space_for_symbols + "  |  " + Space_for_symbols + "  ",
        "  " + Space_for_symbols + "  |  " + Space_for_symbols + "  |  " + Space_for_symbols + "  "]


#The function helps us do our job.
def Placing_the_shape( Symbol ):
    Row = int(input("Which row do you want to place your symbol? < 1 - 3 > "))
    while Row not in range(1, 4):
        Row = int(input("Which row do you want to place your symbol? < 1 - 3 > "))
    Column = int(input("Which column do you want to place your symbol? < 1 - 3 > "))
    while Column not in range(1, 4):
        Column = int(input("Which column do you want to place your symbol? < 1 - 3 > "))
    while " " not in Board[ ( Row - 1 ) * 3 + 1 ][ ( Column - 1 ) * 6 + 2 ]:
        Row = int(input("Which row do you want to place your symbol? < 1 - 3 > "))
        while Row not in range(1, 4):
            Row = int(input("Which row do you want to place your symbol? < 1 - 3 > "))
        Column = int(input("Which column do you want to place your symbol? < 1 - 3 > "))
        while Column not in range(1, 4):
            Column = int(input("Which column do you want to place your symbol? < 1 - 3 > "))
    Board[ ( Row - 1 ) * 3 + 1 ] = Board[ ( Row - 1 ) * 3 + 1 ][: ( Column - 1 ) * 6 + 2 ] + Symbol + Board[ ( Row - 1 ) * 3 + 1 ][ ( Column - 1 ) * 6 + 3 :]


#The function which starts the game.
def Start():
    soul=0
    print()
    for Element in Board:
        print(Element)
    Equality = 0
    Breaker = False
    while True:
        #Player one's turn.
        print()
        print("PLAYER-1, your turn.")
        Placing_the_shape( Symbol_for_PLAYER1 )
        for Element in Board:
            print(Element)

        #Winning conditions for PLAYER1.
        for Row in range(1, 4):
            if all( Board[ ( Row - 1 ) * 3 + 1 ][ ( Column - 1 ) * 6 + 2 ] == Symbol_for_PLAYER1 for Column in range(1, 4) ):
                Breaker = True
                break
        for Column in range(1, 4):
            if all( Board[ ( Row - 1 ) * 3 + 1 ][ ( Column - 1 ) * 6 + 2 ] == Symbol_for_PLAYER1 for Row in range(1, 4) ):
                Breaker = True
                break
        if all( Board[ ( Place - 1 ) * 3 + 1 ][ ( Place - 1 ) * 6 + 2 ] == Symbol_for_PLAYER1 for Place in range(1, 4) ) or all( Board[ ( Place - 1 ) * 3 + 1 ][ ( 1 - Place ) * 6 + 14 ] == Symbol_for_PLAYER2 for Place in range(1, 4) ):
            Breaker = True

        if Breaker:
            print("PLAYER-1 wins!")
            break
        
        #If none of the conditions is satisfied, the game will be continued...
        Equality += 1
        
        #Equality condition.
        if Equality == 9:
            soul += 1
            print("Perfectly Balanced!")
            break

        #Player two's turn.
        print()
        print("PLAYER-2, your turn.")
        Placing_the_shape( Symbol_for_PLAYER2 )
        for Element in Board:
            print(Element)

        #Winning conditions for PLAYER2.
        for Row in range(1, 4):
            if all( Board[ ( Row - 1 ) * 3 + 1 ][ ( Column - 1 ) * 6 + 2 ] == Symbol_for_PLAYER2 for Column in range(1, 4) ):
                Breaker = True
                break
        for Column in range(1, 4):
            if all( Board[ ( Row - 1 ) * 3 + 1 ][ ( Column - 1 ) * 6 + 2 ] == Symbol_for_PLAYER2 for Row in range(1, 4) ):
                Breaker = True
                break
        if all( Board[ ( Place - 1 ) * 3 + 1 ][ ( Place - 1 ) * 6 + 2 ] == Symbol_for_PLAYER2 for Place in range(1, 4) ) or all( Board[ ( Place - 1 ) * 3 + 1 ][ ( 1 - Place ) * 6 + 14 ] == Symbol_for_PLAYER2 for Place in range(1, 4) ):
            Breaker = True
        
        if Breaker:
            print("PLAYER-2 wins!")
            break
        
        #If none of the conditions is satisfied, the game will be continued...
        Equality += 1

#Startig the game for the first time.     
Start()

while soul == 1:
    Board = ["  " + Space_for_symbols + "  |  " + Space_for_symbols + "  |  " + Space_for_symbols + "  ",
    "  " + Space_for_symbols + "  |  " + Space_for_symbols + "  |  " + Space_for_symbols + "  ",
    "__" + Underline_for_symbols + "__|__" + Underline_for_symbols + "__|__" + Underline_for_symbols + "__",
    "  " + Space_for_symbols + "  |  " + Space_for_symbols + "  |  " + Space_for_symbols + "  ",
    "  " + Space_for_symbols + "  |  " + Space_for_symbols + "  |  " + Space_for_symbols + "  ",
    "__" + Underline_for_symbols + "__|__" + Underline_for_symbols + "__|__" + Underline_for_symbols + "__",
    "  " + Space_for_symbols + "  |  " + Space_for_symbols + "  |  " + Space_for_symbols + "  ",
    "  " + Space_for_symbols + "  |  " + Space_for_symbols + "  |  " + Space_for_symbols + "  ",
    "  " + Space_for_symbols + "  |  " + Space_for_symbols + "  |  " + Space_for_symbols + "  "]
    Start()
#Being able to start a new game.

while True:
    print("----------------------------------------")
    Try = input("Do you want to try again? < Y or N > ")
    while Try not in ["Y", "N"]:
        Try = input("Do you want to try again? < Y or N > ")
    if Try == "Y":
        Board = ["  " + Space_for_symbols + "  |  " + Space_for_symbols + "  |  " + Space_for_symbols + "  ",
        "  " + Space_for_symbols + "  |  " + Space_for_symbols + "  |  " + Space_for_symbols + "  ",
        "__" + Underline_for_symbols + "__|__" + Underline_for_symbols + "__|__" + Underline_for_symbols + "__",
        "  " + Space_for_symbols + "  |  " + Space_for_symbols + "  |  " + Space_for_symbols + "  ",
        "  " + Space_for_symbols + "  |  " + Space_for_symbols + "  |  " + Space_for_symbols + "  ",
        "__" + Underline_for_symbols + "__|__" + Underline_for_symbols + "__|__" + Underline_for_symbols + "__",
        "  " + Space_for_symbols + "  |  " + Space_for_symbols + "  |  " + Space_for_symbols + "  ",
        "  " + Space_for_symbols + "  |  " + Space_for_symbols + "  |  " + Space_for_symbols + "  ",
        "  " + Space_for_symbols + "  |  " + Space_for_symbols + "  |  " + Space_for_symbols + "  "]
        Start()
    else:
        break
#THE-END
