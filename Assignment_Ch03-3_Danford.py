# User inputs required information
p1 = input("Player 1 - Enter [R]ock, [P]aper, or [S]cissors: ")
p2 = input("Player 2 - Enter [R]ock, [P]aper, or [S]cissors: ")

# Force user input into lower case letters to simplify remaining code
player1 = str.lower(p1)
player2 = str.lower(p2)

# Determine which user wins
if player1 == player2:
    print("Nobody wins")
elif player1 == "r":
    if player2 == "s":
        print("Player 1 wins! Rock smashes scissors.")
    else:
        print("Player 2 wins! Scissors cut paper")
elif player1 == "p":
    if player2 == "r":
        print("Player 1 wins! Paper covers rock")
    else:
        print("Player 2 wins! Rock smashes scissors")
elif player1 == "s":
    if player2 == "p":
        print("Player 1 wins! Scissors cut paper")
    else:
        print("Player 2 wins! Paper covers rock")
