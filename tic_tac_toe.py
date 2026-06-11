from random import randrange

board = []
size = 3
square = 0 #casilla que se juega
available_squares = []
occupied_squares = []
player1 = "0"
CPU = "X"

def display_board(board):
    # The function accepts one parameter containing the board's current status
    # and prints it out to the console.
    line1 = "+-------+"
    line2 = "|       |"
    line3 = ""
    board_list = []
    row = ""

    for i in range(size):
      l1, l2, l3, l4, l5 = "", "", "", "", ""
      for j in range(size):
        if j == (size-1):
          l1 += line1[:]
        else:
          l1 += line1[:-1]

      for k in range(size):
        if k == (size-1):
          l2 += line2[:]
        else:
            l2 += line2[:-1]
      for l in range(size):
        val = board[i][l]
        line3 = "|   "+str(val) + "   |"
        if l == (size-1):
          l3 += line3[:]
        else:
          l3 += line3[:-1]
      l4 = l2
      l5 = l1
      row = l1+"\n"+l2+"\n"+l3+"\n"+l4
      print(row)
    print(l1) # additional bottom line

def enter_move(board):
    # The function accepts the board's current status, asks the user about their move,
    # checks the input, and updates the board according to the user's decision.
    pass_test = False
    while pass_test == False:

      try:
        number_square = eval(input("Enter your move: "))
        # dummy test: number
        number_square += 0
        int_number_square = int(number_square)
        # detect float number
        if number_square - int_number_square != 0:
          print("Not an integer. Enter a valid number")
        # detect integer number
        else:
          # detect invalid number out of range
          if not (number_square>0 and number_square<10):
            print("Not valid number. Out of range")
          # detect not available square
          elif number_square not in available_squares:
            print("Not valid number. Unavailable number")
          else:
            # test pass!
            pass_test = True

      except ValueError:
        print("Not a number")
      except:
        print("Not valid number...")
    #print("Number chosen is ", number_square)

    update_board(board, number_square, player1)
    display_board(board)


def make_list_of_free_fields(board):
    # The function browses the board and builds a list of all the free squares;
    # the list consists of tuples, while each tuple is a pair of row and column numbers.
    None

def victory_for(board, sign):
    # The function analyzes the board's status in order to check if
    # the player using 'O's or 'X's has won the game
    victory = False
    player = ("You", "CPU")
    winner = player[0]
    count = 0

    if sign == CPU:
      winner = player[1]

    for i in range(size):
      # count horizontal moves -, must have 3 in a row
      count = 0
      count = board[i].count(sign)
      if count == size:
        ##print(player, " won", "horizontal")
        victory = True
        return victory

    # count vertical moves |, must have 3 in a column
    # get column index containing value
    temp_col_index = []
    for i in range(len(board[0])):
      if board[0][i] == sign:
        temp_col_index.append(i)

    for col in temp_col_index:
      count = 0
      for row in range(size):
        if board[row][col] == sign:
          count+=1
        if count == size:
          ##print(player, " won", "vertical" )
          victory = True
          return victory

    # count diagonal moves, hard-coded
    # ascending diagonal /
    col = 0
    count = 0
    for row in range(size):
      col -= 1
      if board[row][col] == sign:
        count += 1
    if count == size:
      ##print(player, " won", "ascending diagonal")
      victory = True
      return victory
    # descending diagonal \
    col = 0
    count = 0
    for row in range(size):
      col = row
      if board[row][col] == sign:
        count += 1
    if count == size:
      ##print(player, " won", "descending diagonal")
      victory = True
      return victory

    # default: false, no victory for player or CPU
    ##print(player, " didn't win")
    return victory

def draw_move(board):
    # The function draws the computer's move and updates the board.
    square = 0
    square_index = 0
    # Detect first CPU move, middle square "5"
    if len(available_squares) == size**2:
      square = 5
      #print("--firts CPU move---")
    else:
      square_index = randrange(len(available_squares))
      square = available_squares[square_index]
      #print("--random CPU move--")

    update_board(board, square, CPU)
    display_board(board)


def update_board(board, number_square, player):
   for row in range(size):
    for col in range(size):
      my_eval = board[row][col]
      # find square
      if my_eval == number_square:
        board[row][col] = player
        # update available squares
        available_squares.remove(number_square)
        occupied_squares.append(number_square)
        return


# create board
for i in range(size):
    row = []
    col = []
    for j in range(size):
        square+=1
        col.append(square)
        available_squares.append(square)
    row = col[:]
    board.append(row[:])

# for information
#print(board)
display_board(board)

finish_game = False
while finish_game == False:
  # CPU move
  draw_move(board)
  # Check CPU victory
  finish_game = victory_for(board, CPU)
  if finish_game:
    print("CPU won !")
    break
  if len(available_squares) == 0:
    print("Draw !") # Draw (empate)
    finish_game = True
    break

  # Player move
  enter_move(board)
  # Check player victory
  finish_game = victory_for(board, player1)
  if finish_game:
    print("You won !")
    break

  if len(available_squares) == 0:
    print("Draw !") # Draw (empate)
    finish_game = True
    break
