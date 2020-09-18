import sys


def functionType(domain, codomain, mappings):
    domain = {v:False for v in domain}
    codomain = {v:[] for v in codomain}
    for mapping in mappings:
        if domain[mapping[0]]:
            return "not a function"
        domain[mapping[0]] = True
        codomain[mapping[1]].append(mapping[0])

    surjective = True
    injective = True
    for v in codomain:
        clength = len(codomain[v])
        if clength == 0:
            surjective = False
        if clength > 1:
            injective = False

    if surjective and injective:
        return "bijective"
    elif surjective:
        return "surjective"
    elif injective:
        return "injective"
    else:
        return "neither injective nor surjective"


def main():
    line = sys.stdin.readline()
    while line != '':
        domain = line.split()[1:]
        codomain = sys.stdin.readline().split()[1:]
        mappingCount = int(input())
        mappings = []
        for i in range(mappingCount):
            mapping = [v.strip() for v in input().split("->")]
            mappings.append(mapping)
        print( functionType(domain, codomain, mappings) )
        line = sys.stdin.readline()
main()