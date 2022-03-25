from gameComponents import gameVars


def winorlose(status):
    print("you " + status)

    choice = input("Do you want to play again? y/n: ")

    if choice == "n":
        print("====== see ya! =======")
        exit()
    elif choice == "y":
        gameVars.playerLives = 3
        gameVars.computerLives = 3
        gameVars.player = False