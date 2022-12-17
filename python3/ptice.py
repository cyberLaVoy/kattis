

def numCorrect(guessPattern, answer):
    numCorrect = 0
    for i in range(len(answer)):
        if guessPattern[i%len(guessPattern)] == answer[i]:
            numCorrect += 1
    return numCorrect

def solve():
    people = [["Adrian", {"guess":"ABC", "correct": 0}],["Bruno", {"guess":"BABC", "correct": 0}],["Goran", {"guess":"CCAABB", "correct": 0}]]
    input() # toss out first line
    answer = input()
    record = []
    for person in people:
        record.append(numCorrect(person[1]["guess"], answer))
        person[1]["correct"] = numCorrect(person[1]["guess"], answer)
    best = max(record)
    print(best)
    for person in people:
        if person[1]["correct"] == best:
            print(person[0])
solve()



