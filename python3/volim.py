
player = int(input())
numPlayers = 8
numQuestions = int(input())
time = 210

for i in range(numQuestions):
    question = input().split()
    taken = int(question[0])
    answer = question[1]
    time -= taken
    if time <= 0:
        print(player)
        break
    if answer == "T":
        player = player%numPlayers+1