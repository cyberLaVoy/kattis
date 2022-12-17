
params = input().split()
numCompanies = int(params[0])
numRequests = int(params[1])

companies = {}

company = 1
for location in input().split():
    companies[str(company)] = int(location)
    company += 1

for i in range(numRequests):
    request = input().split()
    if request[0] == '1':
        companies[request[1]] = int(request[2])
    else:
        print(abs(companies[request[1]] - companies[request[2]]))