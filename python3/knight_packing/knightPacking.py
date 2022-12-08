# Read the input
n = int(input())

# If the board size is odd, the first player wins, otherwise the second player wins
if n % 2 == 1:
  print("first")
else:
  print("second")