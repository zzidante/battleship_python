from random import randint
  
def play_game():
  
  def play_again():
    answer = raw_input("Type Y or YES if you want to play again, type anything else to exit" + "\n")
    if answer.lower() == "y" or answer.lower() == "yes":
      play_game()
    else:
      print "Thanks for playing! See you next time!"
  
  # instantiate board, print it pretty before a turn
  
  board = []

  for x in range(5):
    board.append(["O"] * 5)

  def print_board(board):
    for row in board:
      print " ".join(row)

  print_board(board)

  # Place a ship in random location on board

  def random_row(board):
    return randint(0, len(board) - 1)

  def random_col(board):
    return randint(0, len(board[0]) - 1)

  ship_row = random_row(board)
  ship_col = random_col(board)

  # Game Loop, 4 turns.

  for turn in range(4):
    print "Turn ", turn + 1
		# TODO: sterilize user input, no answer breaks program
    guess_row = raw_input("Guess Row: ")
    guess_col = raw_input("Guess Col: ")
    
    guess_row = int(guess_row) - 1
    guess_col = int(guess_col) - 1

    if guess_row == ship_row and guess_col == ship_col:
      print "Congratulations! You sunk my battleship!"
      break
    else:
      if (guess_row < 0 or guess_row > 4) or (guess_col < 0 or guess_col > 4):
        print "Oops, that's not even in the ocean."
      elif(board[guess_row][guess_col] == "X"):
        print "You guessed that one already."
      else:
        print "You missed my battleship!"
        board[guess_row][guess_col] = "X"

      print_board(board)
      if turn == 3:
        print "Game Over"
        play_again()
          
play_game()
