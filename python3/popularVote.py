
def determineWinner():
    numCandidates = int(input())
    voteCounts = []
    totalVotes = 0
    maxVoteCount = 0
    for i in range(numCandidates):
        voteCount = int(input())
        voteCounts.append(voteCount)
        totalVotes += voteCount
        if voteCount > maxVoteCount:
            maxVoteCount = voteCount
    winners = []
    for i in range(len(voteCounts)):
        if voteCounts[i] == maxVoteCount:
            winners.append(i+1)
    if len(winners) > 1:
        print("no winner")
    else:
        if maxVoteCount > totalVotes/2:
            print("majority winner", winners[0])
        else:
            print("minority winner", winners[0])

def solve():
    numTests = int(input())
    for i in range(numTests):
        determineWinner()
solve()