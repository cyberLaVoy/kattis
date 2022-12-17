
numTests = int(input())

for i in range(numTests):
    tests = input().split()
    numDays = int(tests[1])
    totalCandles = int(numDays*((2+(numDays+1))/2))
    print(i+1,totalCandles)