from gameComponents import gameVars


def result(status):
    if gameVars.computer == gameVars.player:
        print("\n\033[0;33mtie! try again\033[0;0m\n")

    elif gameVars.player == "rock":
        if gameVars.computer == "paper":
            print("\n\033[0;31mYOU LOSE!\033[0;0m\n")
            gameVars.playerLives = gameVars.playerLives - 1
        else:
            print("\n\033[0;32mYOU WIN!!!\033[0;0m\n")
            gameVars.computerLives = gameVars.computerLives - 1

    elif gameVars.player == "paper":
        if gameVars.computer == "scissors":
            print("\n\033[0;31mYOU LOSE!\033[0;0m\n")
            gameVars.playerLives = gameVars.playerLives - 1
        else:
            print("\n\033[0;32mYOU WIN!!!\033[0;0m\n")
            gameVars.computerLives = gameVars.computerLives - 1

    elif gameVars.player == "scissors":
        if gameVars.computer == "rock":
            print("\n\033[0;31mYOU LOSE!\033[0;0m\n")
            gameVars.playerLives = gameVars.playerLives - 1
        else:
            print("\033[0;32mYOU WIN!!!\033[0;0m\n")
            gameVars.computerLives = gameVars.computerLives - 1