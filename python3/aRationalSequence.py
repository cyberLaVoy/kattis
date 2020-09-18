import queue, math

MAX_Q = 300
MAX_N = 15

def isMaxQ(node, maxQ=MAX_Q):
    q = node[1]
    if q >= maxQ:
        return True
    return False

def parent(node):
    p = node[0]
    q = node[1]
    jump = None
    if p == q:
        return None, jump
    elif p < q:
        jump = "L"
        return [p, q-p], jump
    else:
        jump = "R"
        return [p-q, q], jump
def leftChild(node):
    p = node[0]
    q = node[1]
    left = [p, p+q]
    return left
def rightChild(node):
    p = node[0]
    q = node[1]
    right = [p+q, q]
    return right

def generateSequence(maxN=MAX_N, maxQ=MAX_Q):
    sequence = "{"
    Q = queue.Queue()
    Q.put([1,1])
    place = 1
    node = Q.get()
    while place <= maxN and not isMaxQ(node, maxQ):
        sequence += str(place) + ':' + str(node) + ','
        Q.put(leftChild(node))
        Q.put(rightChild(node))
        node = Q.get()
        place += 1
    sequence = sequence[:-1]
    sequence += '}'
    return sequence


def nodeNumber(node):
    level = 1
    jumpSequence = []
    top, jump = parent(node)
    while top is not None:
        jumpSequence.append(jump)
        top, jump = parent(top)
        level += 1
    shift = 0 
    while len(jumpSequence) != 0:
        jump = jumpSequence.pop()
        if jump == "R":
            shift = shift*2+1 
        else:
            shift = shift*2 
    return 2**(level-1) + shift

def version2():
    numTests = int(input())
    for i in range(numTests):
        params = input().split()
        node = params[1].split('/')
        node = [int(x) for x in node]
        print(i+1, nodeNumber(node))


def F(n):
    whichLevel = 0
    temp = n
    while temp != 0:
        temp = temp >> 1
        whichLevel += 1
    shift = n - 2**(whichLevel-1)
    jumpSequence = []
    while n != 1:
        if shift & 1 == 1:
            jumpSequence.append("R")
        else:
            jumpSequence.append("L")
        n = n >> 1 # parent node number
        whichLevel -= 1
        shift = n - 2**(whichLevel-1)

    node = [1,1]
    while len(jumpSequence) != 0:
        jump = jumpSequence.pop()
        if jump == "R": 
            node = rightChild(node)
        else:
            node = leftChild(node)
    return node

def version3():
    numTests = int(input())
    for i in range(numTests):
        params = input().split()
        n = int(params[1])
        answer = F(n)
        print( i+1, str(answer[0]) + '/' + str(answer[1]) )


def nextNode(node):
    if node == [1,1]:
        return leftChild(node)
    p = node[0]
    q = node[1]
    tempParent, jump = parent(node)
    if q > p:
        return rightChild(tempParent)
    elif q == 1:
        return [q, p+1]
    else:
        count = int(p/q) # distance from common sibling (sibling from commmon ancestor)
        node = [p%q,q] # find common sibling 
        tempParent,jump = parent(node)
        node = rightChild(tempParent) # find sibling, ancestor of next
        node[1] = node[1]+node[0]*count # find next
        return node


def version1():
    numTests = int(input())
    for i in range(numTests):
        params = input().split()
        node = params[1].split('/')
        node = [int(x) for x in node]
        tempNext = nextNode(node)
        print(i+1, str(tempNext[0]) + '/' + str(tempNext[1]))


def main():
    #sequence = generateSequence(MAX_N, MAX_Q)
    #print(sequence)
    version1()
    #version2()
    #version3()

if __name__ == "__main__":
    main()