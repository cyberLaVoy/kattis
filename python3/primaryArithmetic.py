

def countNumberOfCarries(arr1, arr2):
    arr1.reverse()
    arr2.reverse()
    carryCount = 0
    carry = 0
    for i in range(min(len(arr1), len(arr2))):
        if arr1[i] + arr2[i] + carry >= 10:
            carryCount += 1
            carry = 1
        else:
            carry = 0
    longest = None
    if len(arr1) > len(arr2):
        longest = arr1
    if len(arr2) > len(arr1):
        longest = arr2
    
    if longest is not None and carry == 1:
        for j in range(i+1, len(longest)):
            if longest[j] + carry >= 10:
                carryCount += 1
            else:
                break

    return carryCount

def main():
    params = input().split()
    while not (params[0] == '0' and params[1] == '0'):
        numCarries = countNumberOfCarries([int(x) for x in params[0]], [int(x) for x in params[1]])
        if numCarries in [0,1]:
            if numCarries == 0:
                numCarries = "No"
            print(numCarries, "carry operation.")
        else:
            print(numCarries, "carry operations.")
        params = input().split()
main()

