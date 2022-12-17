
numCommands = int(input())

for i in range(numCommands):
    command = input().split()
    if len(command) > 2:
        do = ""
        if command[0].lower() == "simon" and command[1] == "says":
            for i in range(2, len(command)):
                do += command[i] + ' '
            print(do[:len(do)-1])
        else: # added for other problem version
            print()
