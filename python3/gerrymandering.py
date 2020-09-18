


numPrecincts, numDistricts = input().split()

districts = []
for i in range(int(numDistricts)):
    districts.append({'A':0, 'B':0})

for i in range(int(numPrecincts)):
    results = input().split()
    district = int(results[0])-1
    districts[district]['A'] += int(results[1])
    districts[district]['B'] += int(results[2])

totalWastedA = 0
totalWastedB = 0
totalVotes = 0

for d in districts:
    Avotes = d['A'] 
    Bvotes = d['B'] 
    totalDistrictVotes = Avotes+Bvotes
    if Avotes > Bvotes:
        wastedB = Bvotes
        wastedA = Avotes - ( totalDistrictVotes//2 + 1 ) 
        print('A', wastedA, wastedB)
    else:
        wastedA = Avotes
        wastedB = Bvotes - ( totalDistrictVotes//2 + 1 ) 
        print('B', wastedA, wastedB)
    totalVotes += totalDistrictVotes
    totalWastedB += wastedB
    totalWastedA += wastedA

print( abs(totalWastedA-totalWastedB)/totalVotes )