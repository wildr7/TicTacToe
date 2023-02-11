def makeboard():
  board = []
  for i in range(9):
    board.append(" ")
  return board
def printboard(board):
  print("  0  1  2")
  print("0 {}|{} | {}".format(board[0], board[1], board[2]))
  print(" _________ ")
  print("1 {}|{} | {}".format(board[3], board[4], board[5]))
  print(" _________ ")
  print("2 {}|{} | {}".format(board[6], board[7], board[8]))

def get_user_input(board, player):
  print("Player {}".format(player))
  row = int(input("Enter Row: "))
  row = int(row)
  while (0 > row or row > 2):
    print("Try again with numbers on the board")
    row = int(input("Enter row: "))
  col = int(input("Enter Column: "))
  while(0 > col or col > 2):
    print("Try again with numbers on the board")
    col = input("Enter Column: ")


  index = row * 3 + col
  if(board[index] != " "):
   print("That's not gonna work out! This space is taken")
   get_user_input(board, player)
  else:
    if(player == 1):
      board[index] = "x"
    else:
      board[index] = "o"
    
def check3(board, i1, i2, i3):
#check3 on the board and give 3 coordinates on the board  
  if board[i1] != " " and board[i2]  == board[i1] and board[i3] == board[i1]: 
    return True
  else:  
    return False
    
def checkwin(board, player):
  if check3(board,0,1,2) or check3(board,3,4,5) or check3(board,6,7,8) or check3(board,0,3,6) or check3(board,1,4,7) or check3(board,2,5,8) or check3(board,0,4,8) or check3(board,2,4,6):
    printboard(board)
    print("Player {} Wins!".format(player))
    return False
  else:
    return True

def main():
  board = makeboard()
  player = 1 
  count = 0
  playgame = True
  while(playgame):
    printboard(board)
    get_user_input(board,player)
    playgame = checkwin(board,player)
    count += 1
    if count > 8:
      printboard(board)
      print("Tie Game")
      playgame = False
    if player == 1:
      player = 2 
    else:
      player = 1




main()

