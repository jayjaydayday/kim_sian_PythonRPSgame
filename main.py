from random import randint
from gameComponents import winLose, gameVars, gameRules
choices = ["rock", "paper", "scissors"]

print("\n\033[1;36m////////Welcome to Rock, Paper, Scissors Game////////\n")
print("\033[0;0mRock beats Scissors")
print("Scissors beats Paper")
print("Paper beats Rock")
print("\n\033[1;36m/////////////////////////////////////////////////////\n")

while gameVars.player is False:

    print("\033[1;36mPlayer Lives" + str(gameVars.playerLives))
    print("\033[1;35mComputer Lives" + str(gameVars.computerLives))
    print("\n\033[0;0m--------------------------------------------------\n")
    print("Choose rock, paper, or scissors. Or type quit to exit\n")
    gameVars.player = input("choose rock, paper or scissors:")

    if gameVars.player not in choices:
        if gameVars.player == "quit":
            exit()
            break
        print("\033[0;31mWe do not have this option\033[0;0m")

    else:
        gameVars.computer = gameVars.choices[randint(0, 2)]
        print("\n---------------------------------------------------\n")
        print("\033[1;36mplayer chose:" + gameVars.player)
        print("\033[1;35mcomputer chose:" + gameVars.computer)
        print("\n\033[0;0m---------------------------------------------\n")

        gameRules.result(gameVars.computer)

        print("\033[1;35mcomputer lives count:" + str(gameVars.computerLives))
        print("\033[1;36mplayer lives count:" + str(gameVars.playerLives))
        print("\n\033[0;0m---------------------------------------------\n")

        if gameVars.playerLives == 0:
            winLose.winorlose("lost :(")

        if gameVars.computerLives == 0:
            winLose.winorlose("won :)")

    gameVars.player = False