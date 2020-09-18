
numTests = int(input())

for i in range(numTests):
    input() # disgard G
    invitationCodesCount = {}
    guestCodes = input().split()
    for code in guestCodes:
        if code not in invitationCodesCount:
            invitationCodesCount[code] = 1
        else:
            invitationCodesCount[code] += 1
    for code in invitationCodesCount:
        if invitationCodesCount[code] == 1:
            print("Case #" + str(i+1) + ':', code)
            break

