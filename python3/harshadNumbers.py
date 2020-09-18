
start = int(input())

for i in range(start, 1000000001):
    digitSum = 0 
    digitString = str(i)
    for j in range(len(digitString)):
        digitSum += int(digitString[j])
    if i % digitSum == 0:
        print(i)
        break


