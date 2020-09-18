

n = int(input())

tb = 0
lr = 0

for _ in range(n):
    sword = [(int(x)+1)%2 for x in input()]
    tb += (sword[0]+sword[1])
    lr += (sword[2]+sword[3])


newSords = min(tb, lr) // 2
remainingTB = tb - newSords*2
remainingLR = lr - newSords*2

print(newSords, remainingTB, remainingLR)