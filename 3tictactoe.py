board = ["-","-","-",
         "-","-","-",
         "-","-","-"]

#Know if game is still going on by setting it to True
game_on = True

# Initialize our current player to be X
current_player = "X"

#Function to display our game board
def display_board():
    print(board[0] + " | " + board[1] + " | " + board[2] + "      " + "1|2|3")
    print(board[3] + " | " + board[4] + " | " + board[5] + "      " + "4|5|6")
    print(board[6] + " | " + board[7] + " | " + board[8] + "      " + "7|8|9")

# Funtion to define players
def players():
    print("Select Player - X or O")
    p1 = input("Player1: ")
    p2 = ""
    if p1 == "X":
        p2 = "O"
        print("Player2: " + p2)
    elif p1 == "O":
        p2 = "X"
        print("Player2: " + p2)
    elif p1 != "O" or p1 != "X":
        print("Sorry,invalid input. Type X or O")
        play_game()

#Define the player position
def player_position():
    global current_player
    print("Current Player: " + current_player)
    position = input("Choose position from 1 - 9: ")

    # Loop through the program untill there is a win or tie
    valid = False
    while not valid:
        while position not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
          position = input("Choose position from 1 - 9: ")
        position = int(position) - 1

        if board[position] == "-":
            valid = True
        else:
            print("Position already selected, choose another position!")
    board[position] = current_player
    display_board()

#Function to play our tic tac game 
def play_game():
    print("My Tic Tac Toe Game")
    display_board()
    players()
    
  #loop  to flip players untill there is a win
    while game_on:
        player_position()
        
        #Check winner
        def check_winner():
            global game_on
            #Check rows if there is a win 
            if board[0] == board[1] == board[2] != "-":
                game_on = False
                print("Congratulations " + board[0]+" you WON!")
            elif board[3] == board[4] == board[5] != "-":
                game_on = False
                print("Congratulations " + board[3]+" you WON!")
            elif board[6] == board[7] == board[8] != "-":
                game_on = False
                print("Congratulations " + board[6]+" you WON!")
             #Check columns if there is a win
            elif board[0] == board[3] == board[6] != "-":
                game_on = False
                print("Congratulations " + board[0]+" you WON!")
            elif board[1] == board[4] == board[7] != "-":
                game_on = False
                print("Congratulations " + board[1]+" you WON!")
            elif board[2] == board[5] == board[8] != "-":
                game_on = False
                print("Congratulations " + board[2]+" you WON!")
             #Check diagonals if there is a win
            elif board[0] == board[4] == board[8] != "-":
                game_on = False
                print("Congratulations " + board[0]+" you WON!")
            elif board[2] == board[4] == board[6] != "-":
                game_on = False
                print("Congratulations "+ board[6]+" you WON!")
             #If none of the above, then, it's a tie
            elif "-" not in board:
                game_on = False
                print("It's a Tie")
                exit()

        #Function to flip player
        def flip_player():
            global current_player
            if current_player == "X":
                current_player = "O"
            else:
                current_player = "X"
        flip_player()
        check_winner()
#Play our tic tac game
play_game()