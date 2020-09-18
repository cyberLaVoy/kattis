
name = input()

shortName = ""
for i in range(len(name)-1):
    if name[i] != name[i+1]:
        shortName += name[i]
shortName += name[len(name)-1]
print(shortName)