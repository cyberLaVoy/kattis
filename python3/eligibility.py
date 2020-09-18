
def isEligible(student):
    studiesBeganYear = int(student[1].split('/')[0])
    birthYear = int(student[2].split('/')[0])
    creditsEarned = int(student[3])
    if studiesBeganYear >= 2010:
        return True
    elif birthYear >= 1991:
        return True
    elif creditsEarned >= 41: 
        return False
    else:
        return None
 

def solve():
    numTests = int(input())

    for i in range(numTests):
        student = input().split()
        name = student[0]
        eligible = isEligible(student)
        if eligible:
            print(name, "eligible")
        elif eligible is None:
            print(name, "coach petitions")
        else:
            print(name, "ineligible")

solve()
   
