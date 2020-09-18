
def intArrToString(arr):
    string = ""
    for n in arr:
        string += chr(n+ord('a')-1)
    return string

def generateSubstring(w, l):
    nums = [x for x in range(1, 27)]
    lowest = w//l
    remainder = w%l
    subNums = [lowest]*l
    for i in range(remainder):
        subNums[i] += 1
    subString = intArrToString(subNums)
    return subString 

def solve():
    params = input().split()
    l = int(params[0])
    w = int(params[1])
    if l*26 < w or w < l:
        print("impossible")
    else:
        subString = generateSubstring(w,l)
        print(subString)
solve()
    
