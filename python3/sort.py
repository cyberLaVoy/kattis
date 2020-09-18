

def count(tup):
    return tup[1]

def main():
    params = input().split()

    nums = [ int(x) for x in input().split() ]

    counts = {}

    for v in nums:
        if v not in counts:
            counts[v] = 0
        counts[v] += 1

    counts = [(key, counts[key]) for key in counts.keys()]
    counts.sort(key=count, reverse=True)
    
    for p in counts:
        for _ in range(count(p)):
            print(p[0], end=' ')
    print()

main()