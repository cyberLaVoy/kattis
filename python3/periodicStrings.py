


def periodicity(string):
    k = 1
    while True:
        if len(string) % k == 0:
            found = True
            for i in range(k, len(string), k):
                #print(k, string[i:i+k], string[i-1]+string[i-k:i-1])
                if string[i:i+k] != string[i-1]+string[i-k:i-1]:
                    found = False
                    break
            if found:
                return k
        k += 1
                

def main():
    string = input()
    print(periodicity(string))
main()