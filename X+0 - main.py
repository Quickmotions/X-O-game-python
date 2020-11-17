#imports
import random
import time

#modules
def playerChoice():
   boxChoice = 0
   Choice = ""
   if gameRunning == True:
      time.sleep(0.5)
      print("make first move")
      Choice = str(input("Enter a number between 1 and 9: "))
      while boxChoice == 0:
         if Choice == "1" or Choice == "2" or Choice == "3" or Choice == "4" or Choice == "5" or Choice == "6" or Choice == "7" or Choice == "8" or  Choice == "9":
            boxChoice = int(Choice)
            if bo[boxChoice] == "-":
               bo[int(boxChoice)]  = "X"
               return
            else:
               boxChoice = 0
               
               Choice = str(input("Position already taken, Re-enter a number: "))
         else:
            Choice = str(input("Incorrect Value, Re-enter a number between 1 and 9: "))
      
      


def aiChoice():
   if gameRunning == True:
      time.sleep(0.5)
      print("ai Selecting")

          

      if (bo[1] == "X" and bo[2] == "X" and bo[3] == "-"): # top row
          boxChoice = 3
          bo[boxChoice]  = "O"
      elif (bo[2] == "X" and bo[3] == "X" and bo[1] == "-"):
          boxChoice = 1
          bo[boxChoice]  = "O"
      elif (bo[1] == "X" and bo[3] == "X" and bo[2] == "-"):
          boxChoice = 2
          bo[boxChoice]  = "O"

      elif (bo[4] == "X" and bo[5] == "X" and bo[6] == "-"): # middle row
          boxChoice = 6
          bo[boxChoice]  = "O"
      elif (bo[5] == "X" and bo[6] == "X" and bo[4] == "-"):
          boxChoice = 4
          bo[boxChoice]  = "O"
      elif (bo[4] == "X" and bo[6] == "X" and bo[5] == "-"):
          boxChoice = 5
          bo[boxChoice]  = "O"

      elif (bo[7] == "X" and bo[8] == "X" and bo[9] == "-"): #bottom row
          boxChoice = 9
          bo[boxChoice]  = "O"
      elif (bo[7] == "X" and bo[9] == "X" and bo[7] == "-"):
          boxChoice = 8
          bo[boxChoice]  = "O"
      elif (bo[4] == "X" and bo[8] == "X" and bo[9] == "-"):
          boxChoice = 7
          bo[boxChoice]  = "O"

      elif (bo[6] == "X" and bo[9] == "X" and bo[3] == "-"): #right column
          boxChoice = 3
          bo[boxChoice]  = "O"
      elif (bo[3] == "X" and bo[9] == "X" and bo[6] == "-"):
          boxChoice = 6
          bo[boxChoice]  = "O"
      elif (bo[3] == "X" and bo[6] == "X" and bo[9] == "-"):
          boxChoice = 9
          bo[boxChoice]  = "O"

      elif (bo[5] == "X" and bo[8] == "X" and bo[2] == "-"): #middle column
          boxChoice = 2
          bo[boxChoice]  = "O"
      elif (bo[2] == "X" and bo[8] == "X" and bo[5] == "-"):
          boxChoice = 5
          bo[boxChoice]  = "O"
      elif (bo[2] == "X" and bo[5] == "X" and bo[8] == "-"):
          boxChoice = 8
          bo[boxChoice]  = "O"

      elif (bo[4] == "X" and bo[7] == "X" and bo[1] == "-"): #left column
          boxChoice = 1
          bo[boxChoice]  = "O"
      elif (bo[1] == "X" and bo[7] == "X" and bo[4] == "-"):
          boxChoice = 4
          bo[boxChoice]  = "O"
      elif (bo[1] == "X" and bo[4] == "X" and bo[7] == "-"):
          boxChoice = 7
          bo[boxChoice]  = "O"

      elif (bo[5] == "X" and bo[9] == "X" and bo[1] == "-"): #diagonal
          boxChoice = 1
          bo[boxChoice]  = "O"
      elif (bo[1] == "X" and bo[9] == "X" and bo[5] == "-"):
          boxChoice = 5
          bo[boxChoice]  = "O"
      elif (bo[1] == "X" and bo[5] == "X" and bo[9] == "-"):
          boxChoice = 9
          bo[boxChoice]  = "O"
          
      elif (bo[5] == "X" and bo[7] == "X" and bo[3] == "-"): #diagonal
          boxChoice = 3
          bo[boxChoice]  = "O"
      elif (bo[3] == "X" and bo[7] == "X" and bo[5] == "-"):
          boxChoice = 5
          bo[boxChoice]  = "O"
      elif (bo[3] == "X" and bo[5] == "X" and bo[7] == "-"):
          boxChoice = 7
          bo[boxChoice]  = "O"
      else:



            #ai try to win
         if (bo[1] == "O" and bo[2] == "O" and bo[3] == "-"): # top row
             boxChoice = 3
             bo[boxChoice]  = "O"
         elif (bo[2] == "O" and bo[3] == "O" and bo[1] == "-"):
             boxChoice = 1
             bo[boxChoice]  = "O"
         elif (bo[1] == "O" and bo[3] == "O" and bo[2] == "-"):
             boxChoice = 2
             bo[boxChoice]  = "O"

         elif (bo[4] == "O" and bo[5] == "O" and bo[6] == "-"): # middle row
             boxChoice = 6
             bo[boxChoice]  = "O"
         elif (bo[5] == "O" and bo[6] == "O" and bo[4] == "-"):
             boxChoice = 4
             bo[boxChoice]  = "O"
         elif (bo[4] == "O" and bo[6] == "O" and bo[5] == "-"):
             boxChoice = 5
             bo[boxChoice]  = "O"

         elif (bo[7] == "O" and bo[8] == "O" and bo[9] == "-"): #bottom row
             boxChoice = 9
             bo[boxChoice]  = "O"
         elif (bo[7] == "O" and bo[9] == "O" and bo[7] == "-"):
             boxChoice = 8
             bo[boxChoice]  = "O"
         elif (bo[4] == "O" and bo[8] == "O" and bo[9] == "-"):
             boxChoice = 7
             bo[boxChoice]  = "O"

         elif (bo[6] == "O" and bo[9] == "O" and bo[3] == "-"): #right column
             boxChoice = 3
             bo[boxChoice]  = "O"
         elif (bo[3] == "O" and bo[9] == "O" and bo[6] == "-"):
             boxChoice = 6
             bo[boxChoice]  = "O"
         elif (bo[3] == "O" and bo[6] == "O" and bo[9] == "-"):
             boxChoice = 9
             bo[boxChoice]  = "O"

         elif (bo[5] == "O" and bo[8] == "O" and bo[2] == "-"): #middle column
             boxChoice = 2
             bo[boxChoice]  = "O"
         elif (bo[2] == "O" and bo[8] == "O" and bo[5] == "-"):
             boxChoice = 5
             bo[boxChoice]  = "O"
         elif (bo[2] == "O" and bo[5] == "O" and bo[8] == "-"):
             boxChoice = 8
             bo[boxChoice]  = "O"

         elif (bo[4] == "O" and bo[7] == "O" and bo[1] == "-"): #left column
             boxChoice = 1
             bo[boxChoice]  = "O"
         elif (bo[1] == "O" and bo[7] == "O" and bo[4] == "-"):
             boxChoice = 4
             bo[boxChoice]  = "O"
         elif (bo[1] == "O" and bo[4] == "O" and bo[7] == "-"):
             boxChoice = 7
             bo[boxChoice]  = "O"

         elif (bo[5] == "O" and bo[9] == "O" and bo[1] == "-"): #diagonal
             boxChoice = 1
             bo[boxChoice]  = "O"
         elif (bo[1] == "O" and bo[9] == "O" and bo[5] == "-"):
             boxChoice = 5
             bo[boxChoice]  = "O"
         elif (bo[1] == "O" and bo[5] == "O" and bo[9] == "-"):
             boxChoice = 9
             bo[boxChoice]  = "O"
             
         elif (bo[5] == "O" and bo[7] == "O" and bo[3] == "-"): #diagonal
             boxChoice = 3
             bo[boxChoice]  = "O"
         elif (bo[3] == "O" and bo[7] == "O" and bo[5] == "-"):
             boxChoice = 5
             bo[boxChoice]  = "O"
         elif (bo[3] == "O" and bo[5] == "O" and bo[7] == "-"):
             boxChoice = 7
             bo[boxChoice]  = "O"
         else:
            #check for middle
            
            if (bo[5] == "-"):
               boxChoice = 5
               bo[boxChoice]  = "O"
            else:
               #pick random 1-9
               boxChoice = random.randint(1, 9)
               while boxChoice <1 or boxChoice >9 or bo[boxChoice]  != "-":
                  boxChoice = random.randint(1, 9)
                  if bo[boxChoice]  != "-":
                     bo[boxChoice]  = "O"
               
               bo[boxChoice]  = "O"


def showUI():
   print(bo[1] ,  bo[2], bo[3])
   print(bo[4],  bo[5], bo[6])
   print(bo[7], bo[8],bo[9])

def winCheckP():
   if ((bo[7] == "X" and bo[8] == "X" and bo[9] == "X") or # across the top
      (bo[4] == "X" and bo[5] == "X" and bo[6] == "X") or # across the middle
      (bo[1] == "X" and bo[2] == "X" and bo[3] == "X") or # across the bottom
      (bo[7] == "X" and bo[4] == "X" and bo[1] == "X") or # down the left side
      (bo[8] == "X" and bo[5] == "X" and bo[2] == "X") or # down the middle
      (bo[9] == "X" and bo[6] == "X" and bo[3] == "X") or # down the right side
      (bo[7] == "X" and bo[5] == "X" and bo[3] == "X") or # diagonal
      (bo[9] == "X" and bo[5] == "X" and bo[1] == "X")):
         return True
   else:
         return False

def winCheckA():
   if ((bo[7] == "O" and bo[8] == "O" and bo[9] == "O") or # across the top
      (bo[4] == "O" and bo[5] == "O" and bo[6] == "O") or # across the middle
      (bo[1] == "O" and bo[2] == "O" and bo[3] == "O") or # across the bottom
      (bo[7] == "O" and bo[4] == "O" and bo[1] == "O") or # down the left side
      (bo[8] == "O" and bo[5] == "O" and bo[2] == "O") or # down the middle
      (bo[9] == "O" and bo[6] == "O" and bo[3] == "O") or # down the right side
      (bo[7] == "O" and bo[5] == "O" and bo[3] == "O") or # diagonal
      (bo[9] == "O" and bo[5] == "O" and bo[1] == "O")):
         return True
   else:
         return False
      


def isBoardFull():
   if "-" in bo:
      return False
   else:
      return True
    

#vars
bo = ["-", "-", "-", "-", "-", "-", "-", "-", "-", "-"]
gameRunning = True

#game running
while gameRunning == True:
   playerChoice()
   showUI()
   if winCheckP() == True:
         showUI()
         print("Player Wins")
         exit()
   if winCheckA() == True:
         showUI()
         print("AI Wins")
         exit()
   if isBoardFull() == True:
         showUI()
         print('The game is a tie!')
         exit()
               
   if gameRunning == True:
      aiChoice()
      showUI()
   if winCheckP() == True:
         showUI()
         print("Player Wins")
         exit()
   if winCheckA() == True:
         showUI()
         print("AI Wins")
         exit()
         showUI()
     
   if isBoardFull() == True:
         showUI()
         print('The game is a tie!')
         exit()
               



