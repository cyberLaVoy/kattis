
def isPalindrome(v):
    if len(v) == 1 or len(v) == 0:
        return True
    if v[0] == v[-1]:
        return isPalindrome(v[1:-1])
    else:
        return False

palindromes = []
count = 0
i = 1
while count < 50000:
    if isPalindrome( "{0:b}".format(i) ):
        palindromes.append(i)
        print(i, "{0:b}".format(i), count)
        count += 1
    i += 2

print(palindromes)
