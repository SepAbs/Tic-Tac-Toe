from random import *

print("Welcome to the biggest Tic Tac Toe contest in the world.")
print()
Your_symbol = input("Ascertain your symbol: ")
print()
Symbol_for_your_opponent = input("Your opponent just let you to appoint a symbol for it. Do it now! ")

if Your_symbol >= Symbol_for_your_opponent:
    Larger_symbol = Your_symbol
else:
    Larger_symbol = Symbol_for_your_opponent

Space_for_symbols = " " * len( Larger_symbol )
Underline_for_symbols = "_" * len( Larger_symbol )

Board = ["  " + Space_for_symbols + "  |  " + Space_for_symbols + "  |  " + Space_for_symbols + "  ",
        "  " + Space_for_symbols + "  |  " + Space_for_symbols + "  |  " + Space_for_symbols + "  ",
        "__" + Underline_for_symbols + "__|__" + Underline_for_symbols + "__|__" + Underline_for_symbols + "__",
        "  " + Space_for_symbols + "  |  " + Space_for_symbols + "  |  " + Space_for_symbols + "  ",
        "  " + Space_for_symbols + "  |  " + Space_for_symbols + "  |  " + Space_for_symbols + "  ",
        "__" + Underline_for_symbols + "__|__" + Underline_for_symbols + "__|__" + Underline_for_symbols + "__",
        "  " + Space_for_symbols + "  |  " + Space_for_symbols + "  |  " + Space_for_symbols + "  ",
        "  " + Space_for_symbols + "  |  " + Space_for_symbols + "  |  " + Space_for_symbols + "  ",
        "  " + Space_for_symbols + "  |  " + Space_for_symbols + "  |  " + Space_for_symbols + "  "]

#This function helps you do your job.
def Placing_the_shape1( Symbol ):
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

def Placing_the_shape2( Symbol ):
    Row = randint(1, 3)
    Column = randint(1, 3)
    while " " not in Board[ ( Row - 1 ) * 3 + 1 ][ ( Column - 1 ) * 6 + 2 ]:
        Row = randint(1, 3)
        Column = randint(1, 3)
    Board[ ( Row - 1 ) * 3 + 1 ] = Board[ ( Row - 1 ) * 3 + 1 ][: ( Column - 1 ) * 6 + 2 ] + Symbol + Board[ ( Row - 1 ) * 3 + 1 ][ ( Column - 1 ) * 6 + 3 :]

#The function which starts the game.
def Start():
    print()
    for Element in Board:
        print(Element)
    Equality = 0
    Breaker = False
    while True:
        #Player one's turn.
        print()
        print("Your turn.")
        Placing_the_shape1( Your_symbol )

        #Winning conditions for you.
        for Row in range(1, 4):
            if all( Board[ ( Row - 1 ) * 3 + 1 ][ ( Column - 1 ) * 6 + 2 ] == Your_symbol for Column in range(1, 4) ):
                Breaker = True
                break
        for Column in range(1, 4):
            if all( Board[ ( Row - 1 ) * 3 + 1 ][ ( Column - 1 ) * 6 + 2 ] == Your_symbol for Row in range(1, 4) ):
                Breaker = True
                break
        if all( Board[ ( Place - 1 ) * 3 + 1 ][ ( Place - 1 ) * 6 + 2 ] == Your_symbol for Place in range(1, 4) ) or all( Board[ ( Place - 1 ) * 3 + 1 ][ ( 1 - Place ) * 6 + 14 ] == Your_symbol for Place in range(1, 4) ):
            Breaker = True
        
        if Breaker:
            for Element in Board:
                print(Element)
            print("YOU WIN!")
            break
        
        #If none of the conditions is satisfied, the game will be continued...
        Equality += 1
        
        #Equality condition.
        if Equality == 9:
            print("Perfectly Balanced!")
            break

        #Opponent's turn.
        Placing_the_shape2( Symbol_for_your_opponent )
        for Element in Board:
            print(Element)

        #Winning conditions for your opponent.
        for Row in range(1, 4):
            if all( Board[ ( Row - 1 ) * 3 + 1 ][ ( Column - 1 ) * 6 + 2 ] == Symbol_for_your_opponent for Column in range(1, 4) ):
                Breaker = True
                break
        for Column in range(1, 4):
            if all( Board[ ( Row - 1 ) * 3 + 1 ][ ( Column - 1 ) * 6 + 2 ] == Symbol_for_your_opponent for Row in range(1, 4) ):
                Breaker = True
                break
        if all( Board[ ( Place - 1 ) * 3 + 1 ][ ( Place - 1 ) * 6 + 2 ] == Symbol_for_your_opponent for Place in range(1, 4) ) or all( Board[ ( Place - 1 ) * 3 + 1 ][ ( 1 - Place ) * 6 + 14 ] == Symbol_for_your_opponent for Place in range(1, 4) ):
            Breaker = True

        if Breaker:
            print("The opponent wins!")
            break
        
        #If none of the conditions is satisfied, the game will be continued...
        Equality += 1

#Startig the game for the first time.     
Start()

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
print("Have fun ;)")
#THE-END
