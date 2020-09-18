
jars = input().split()
jars = [int(x) for x in jars]
while not (jars[0] == 0 and jars[1] == 0):
    sweet = jars[0]
    sour = jars[1]
    if sweet + sour == 13:
        print("Never speak again.")
    elif sweet > sour:
        print("To the convention.")
    elif sour > sweet:
        print("Left beehind.")
    else:
        print("Undecided.")
    jars = input().split()
    jars = [int(x) for x in jars]