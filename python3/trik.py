
steps = input()

setup = [1,0,0]
for step in steps:
    if step == 'A':
        setup[0], setup[1] = setup[1], setup[0]
    elif step == 'B':
        setup[1], setup[2] = setup[2], setup[1]
    elif step == 'C':
        setup[0], setup[2] = setup[2], setup[0]

for i in range(len(setup)):
    if setup[i] == 1:
        print(i+1)
        break
