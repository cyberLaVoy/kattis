
def swap(people, index1, index2):
    people[index1], people[index2] = people[index2], people[index1]

def solve():
    X = int(input())
    people = input()
    people = [l for l in people]

    men = 0
    women = 0
    lostCount = False
    for i in range(len(people)):
        if i+1 < len(people):
            if women > men and  people[i+1] == 'M':
                swap(people, i, i+1)
            if men > women and people[i+1] == 'W':
                swap(people, i, i+1)

        if people[i] == 'W':
            women += 1
        else:
            men += 1

        difference = abs(men - women)
        if difference > X:
            print(men + women - 1)
            lostCount = True
            break

    if not lostCount:
        print(men + women)
solve()