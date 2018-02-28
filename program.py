import random

def printBoard():
    boardStr = """|--------------------|\n|01|02|03|04|05|06|07|\n|--------------------|\n|08|09|10|11|12|13|14|\n|--------------------|\n|15|16|17|18|19|20|21|\n|--------------------|\n|22|23|24|25|26|27|28|\n|--------------------|\n|29|30|31|32|33|34|35|\n|--------------------|\n|36|37|38|39|40|41|42|\n|--------------------|\n|43|44|45|46|47|48|49|\n|--------------------|"""

    #If they're on the same square
    if p1Pos == p2Pos:
        
        if p1Pos < 10:
            boardStr = boardStr.replace("0" + str(p1Pos), "@$")
        else:
            boardStr = boardStr.replace(str(p1Pos), "@$")
            
    else:
        
        #If they're on different squares
        if p1Pos < 10:
            boardStr = boardStr.replace("0" + str(p1Pos), "@@")
        else:
            boardStr = boardStr.replace(str(p1Pos), "@@")

        if p2Pos < 10:
            boardStr = boardStr.replace("0" + str(p2Pos), "$$")
        else:
            boardStr = boardStr.replace(str(p2Pos), "$$")
    
    print(boardStr)



#Load Messages
messagesFile = open("messages.txt")
messages = messagesFile.readlines()

startGameMsg = messages[0].strip()
doubleMsg = messages[1].strip()
finishGameMsg = messages[2].strip()




#Load Obstacles - Format: position (1-49), direction (f/b), amount
#For example: 24,f,5
#(Obstacle position is 24, player will move forward 5 spaces)
obstaclesFile = open("obstacles.txt")
obstaclesLines = obstaclesFile.readlines()
obstacles = {}

for lines in obstaclesLines:
    lines = lines.split(",")
    obstacles[int(lines[0])] = [lines[1], int(lines[2].strip())]


#Basic variables
p1Pos = 1
p2Pos = 1
inputVal = ""
print(startGameMsg, "\n")


#Game loop
while True:

    #Player 1
    inputVal = input("Player 1: Please enter 'R' to roll your dice!\n> ")

    if inputVal.lower() != "r":
        print("")
        continue
    
    if inputVal.lower() == "r":
        dice1 = random.randint(1, 6)
        dice2 = random.randint(1, 6)

        if dice1 == dice2:
            
            #Move backwards
            print("\n" + doubleMsg)
            p1Pos -= dice1 + dice2
            
            if p1Pos < 1:
                p1Pos = 1
                
                
            print("Player 1 has rolled a double ", dice1, ". Moving backward ", dice1 * 2, " spaces. Now at position ", p1Pos, ".", sep="")
                
        else:
            
            #Move forwards
            print("")
            p1Pos += dice1 + dice2

            if p1Pos > 49:
                p1Pos = 49
            
            print("Player 1 has rolled a ", dice1, " and a ", dice2, ". Moving forward ", dice1 + dice2, " spaces. Now at position ", p1Pos, ".", sep="")

        #Check obstacles
        if p1Pos in obstacles:
                if obstacles[p1Pos][0] == "f":
                    print("Player 1 has hit an obstacle! Moving forward ", obstacles[p1Pos][1], " spaces! Now at position ", p1Pos + obstacles[p1Pos][1], ".", sep="")
                    p1Pos += obstacles[p1Pos][1]

                elif obstacles[p1Pos][0] == "b":
                    print("Player 1 has hit an obstacle! Moving backward ", obstacles[p1Pos][1], " spaces! Now at position ", p1Pos - obstacles[p1Pos][1], ".", sep="")
                    p1Pos -= obstacles[p1Pos][1]

        print("")
        printBoard()
        print("")

        if p1Pos >= 49:
            print("Congratulations! Player 1 wins the game! They have passed 49!")
            break

        print("")

    #Player 2 takes their turn
    while True:
        inputVal = input("Player 2: Please enter 'R' to roll your dice!\n> ")
        if inputVal.lower() == "r":
            break
        print("")
    
    dice1 = random.randint(1, 6)
    dice2 = random.randint(1, 6)

    if dice1 == dice2:
        
        #Move backwards
        print("\n" + doubleMsg)
        p2Pos -= dice1 + dice2
            
        if p2Pos < 1:
           p2Pos = 1
            
        print("Player 2 has rolled a double ", dice1, ". Moving backward ", dice1 * 2, " spaces. Now at position ", p2Pos, ".", sep="")
                
    else:
        
        #Move forwards
        print("")
        p2Pos += dice1 + dice2

        if p2Pos > 49:
            p2Pos = 49
            
        print("Player 2 has rolled a ", dice1, " and a ", dice2, ". Moving forward ", dice1 + dice2, " spaces. Now at position ", p2Pos, ".", sep="")

        #Check obstacles
        if p2Pos in obstacles:
            if obstacles[p2Pos][0] == "f":
                print("Player 2 has hit an obstacle! Moving forward ", obstacles[p2Pos][1], " spaces! Now at position ", p2Pos + obstacles[p2Pos][1], ".", sep="")
                p2Pos += obstacles[p2Pos][1]

            elif obstacles[p2Pos][0] == "b":
                print("Player 2 has hit an obstacle! Moving backward ", obstacles[p2Pos][1], " spaces! Now at position ", p2Pos - obstacles[p2Pos][1], ".", sep="")
                p2Pos -= obstacles[p2Pos][1]

    print("")
    printBoard()
    print("")

    if p2Pos >= 49:
        print("Congratulations! Player 2 wins the game! They have passed 49!")
        break

    print("")

print(finishGameMsg)
