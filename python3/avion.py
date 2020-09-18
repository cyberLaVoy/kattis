
found = False
for i in range(1, 6):
    line = input()
    if "FBI" in line:
        found = True
        print(i)

if not found:
    print("HE GOT AWAY!")