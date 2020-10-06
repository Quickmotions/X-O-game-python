import time
import random
singlePlayerType = ""
singlePlayerRowSelect = ""
singlePlayerColumnSelect = ""
singlePlayerRedoTurn = False
row1A = " "
row1B = " "
row1C = " "
row2A = " "
row2B = " "
row2C = " "
row3A = " "
row3B = " "
row3C = " "

gameType = ""
gameRunning = False




while True:
    print("-------------------")
    print("Knots and Crosses")
    print("-------------------")
    print("press enter to begin")

    gameType = int(input())

    print("\n do you want to play singleplayer or multiplayer \n s = singleplayer \n m = multiplayer")
    gameType = ""
    while gameType != "s" and gameType != "m":
        gameType = str(input())
        if gameType != "s" and gameType != "m":
            print("Error, enter s or m")

    if gameType == "s":
        print("Starting singleplayer game")
        gameRunning = True
        time.sleep(2)
        print("\n \n \n \n \n \n \n \n \n \n \n \n \n \n")
        print("do you want to play x or o \n x goes first \n (type x or o)")
        singlePlayerType = str(input())

        if singlePlayerType != "x" and singlePlayerType != "o":
            singlePlayerType = "x"
        while gameRunning == True:
            #player turn
            #figure out n number
            if singlePlayerType == "x":
                singlePlayerRedoTurn = True
                while singlePlayerRedoTurn == True:
                    singlePlayerRedoTurn = False
                    singlePlayerColumnSelect = ""
                    singlePlayerRowSelect = ""
                    singlePlayerRedoTurn = True
                    print(row1A, " | ",row1B, " | ", row1C)
                    print(row2A, " | ", row2B, " | ", row2C)
                    print(row3A, " | ", row3B, " | ", row3C)

                    print("\n what row do you want?\n 1 = row1 \n 2 = row2 \n 3 = row3")
                    while singlePlayerRowSelect != 1 and singlePlayerRowSelect != 2 and singlePlayerRowSelect != 3:
                        singlePlayerRowSelect = int(input())
                        if singlePlayerRowSelect != 1 and singlePlayerRowSelect != 2 and singlePlayerRowSelect != 3:
                            print("Error, expected 1, 2, or 3 \n please re-enter number")
                        elif singlePlayerRowSelect == 1 or singlePlayerRowSelect == 2 or singlePlayerRowSelect == 3:
                            break
                    print("\n what column do you want? \n  1, 2 or 3")
                    while singlePlayerColumnSelect != 1 and singlePlayerColumnSelect != 2 and singlePlayerColumnSelect != 3:
                        singlePlayerColumnSelect = int(input())
                        if singlePlayerColumnSelect != 1 and singlePlayerColumnSelect != 2 and singlePlayerColumnSelect != 3:
                            print("Error, expected 1, 2, or 3 \n please re-enter number")
                        elif singlePlayerColumnSelect == 1 or singlePlayerColumnSelect == 2 or singlePlayerColumnSelect == 3:
                            break
                            
                    if singlePlayerRowSelect == 1 and singlePlayerColumnSelect == 1:
                        if row1A == "X" or row1A == "O":
                            singlePlayerRedoTurn = True
                            print("Error Space already taken redo turn")
                        elif row1A != "X" and row1A != "O":
                            row1A = "X"
                            singlePlayerRedoTurn = False

                    if singlePlayerRowSelect == 1 and singlePlayerColumnSelect == 2:
                        if row1B == "X" or row1B == "O":
                            singlePlayerRedoTurn = True
                            print("Error Space already taken redo turn")
                        elif row1B != "X" and row1B != "O":
                            row1B = "X"
                            singlePlayerRedoTurn = False

                    if singlePlayerRowSelect == 1 and singlePlayerColumnSelect == 3:
                        if row1C == "X" or row1C == "O":
                            singlePlayerRedoTurn = True
                            print("Error Space already taken redo turn")
                        elif row1C != "X" and row1C != "O":
                            row1C = "X"
                            singlePlayerRedoTurn = False

                    if singlePlayerRowSelect == 2 and singlePlayerColumnSelect == 1:
                        if row2A == "X" or row2A == "O":
                            singlePlayerRedoTurn = True
                            print("Error Space already taken redo turn")
                        elif row2A != "X" and row2A != "O":
                            row2A = "X"
                            singlePlayerRedoTurn = False

                    if singlePlayerRowSelect == 2 and singlePlayerColumnSelect == 2:
                        if row2B == "X" or row2B == "O":
                            singlePlayerRedoTurn = True
                            print("Error Space already taken redo turn")
                        elif row2B != "X" and row2B != "O":
                            row2B = "X"
                            singlePlayerRedoTurn = False

                    if singlePlayerRowSelect == 2 and singlePlayerColumnSelect == 3:
                        if row2C == "X" or row2C == "O":
                            singlePlayerRedoTurn = True
                            print("Error Space already taken redo turn")
                        elif row2C != "X" and row2C != "O":
                            row2C = "X"
                            singlePlayerRedoTurn = False

                    if singlePlayerRowSelect == 3 and singlePlayerColumnSelect == 1:
                        if row3A == "X" or row3A == "O":
                            singlePlayerRedoTurn = True
                            print("Error Space already taken redo turn")
                        elif row3A != "X" and row3A != "O":
                            row3A = "X"
                            singlePlayerRedoTurn = False

                    if singlePlayerRowSelect == 3 and singlePlayerColumnSelect == 2:
                        if row3B == "X" or row3B == "O":
                            singlePlayerRedoTurn = True
                            print("Error Space already taken redo turn")
                        elif row3B != "X" and row3B != "O":
                            row3B = "X"
                            singlePlayerRedoTurn = False

                    if singlePlayerRowSelect == 3 and singlePlayerColumnSelect == 3:
                        if row3C == "X" or row3C == "O":
                            singlePlayerRedoTurn = True
                            print("Error Space already taken redo turn")
                        elif row3C != "X" and row3C != "O":
                            row3C = "X"
                            singlePlayerRedoTurn = False
                            
                            
            #test for player win
            
            print("checking win conditions")
            if row1A == "X" and row1B == "X" and row1C == "X":
                print("player won")
                #end
            if row2A == "X" and row2B == "X" and row2C == "X":
                print("player won")
                #end
            if row3A == "X" and row3B == "X" and row3C == "X":
                print("player won")
                #end
            if row1A == "X" and row2A == "X" and row3A == "X":
                print("player won")
                #end
            if row1B == "X" and row2B == "X" and row3B == "X":
                print("player won")
                #end
            if row1C == "X" and row2C == "X" and row3C == "X":
                print("player won")
                #end
             if row1A == "X" and row2B == "X" and row3C == "X":
                print("player won")
                #end
            if row3A == "X" and row2B == "X" and row1C == "X":
                print("player won")
                #end
          
              


            #Computer Turn
            time.sleep(2)
            print("computer turn here")
            if row1A == "X" and row1B == "X" and row1C != "X":
                row1C = "O"
            if row1B == "X" and row1C == "X" and row1A != "X":
                row1A = "O"
            if row1C == "X" and row1A == "X" and row1B != "X":
                row1B = "O"
                
            if row2A == "X" and row2B == "X" and row2C != "X":
                row2C = "O"
            if row2B == "X" and row2C == "X" and row2A != "X":
                row2A = "O"
            if row2C == "X" and row2A == "X" and row2B != "X":
                row2B = "O"
               
            if row3A == "X" and row3B == "X" and row3C != "X":
                row3C = "O"
            if row3B == "X" and row3C == "X" and row3A != "X":
                row2A = "O"
            if row3C == "X" and row3A == "X" and row3B != "X":
                row3B = "O"
                
            
                














    if gameType == "m":
        print("Starting multiplayer game")
        gameRunning = True
        time.sleep(2)
        print("\n \n \n \n \n \n \n \n \n \n \n \n \n \n")






#Fergus H
