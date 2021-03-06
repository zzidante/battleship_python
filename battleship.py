from random import randint
  
def play_game():
  
  def play_again():
    answer = raw_input("Type Y or YES if you want to play again, type anything else to exit" + "\n")
    if answer.lower() == "y" or answer.lower() == "yes":
      play_game()
    else:
      print "Thanks for playing! See you next time!"
  
  # instantiate board
  
  board = []

  for x in range(5):
    board.append(["O"] * 5)

  def print_board(board):
    for row in board:
      print " ".join(row)

  # Place a ship in random location

  def random_row(board):
    return randint(0, len(board) - 1)

  def random_col(board):
    return randint(0, len(board[0]) - 1)

  # Game Loop, 4 turns.
  for turn in range(4):

    guess_row = ""
    guess_col = ""

    if turn == 0:
      print_board(board)
      ship_row = random_row(board)
      ship_col = random_col(board)

    print "Turn ", turn + 1

    while not guess_row or not guess_col:
      guess_row = raw_input("Guess Row: ").strip()
      guess_col = raw_input("Guess Col: ").strip()

      if not guess_row or not guess_col:
        print "Invalid input, try again"

    guess_row = int(guess_row) - 1
    guess_col = int(guess_col) - 1

    if guess_row == ship_row and guess_col == ship_col:
      board[guess_row][guess_col] = "W"
      print "Congratulations! You sunk my battleship!"
      print_board(board)
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
  
  # game loop exiting on win
  play_again()
          
play_game()
