
params = input().split()

price = int(params[0])
power = int(params[1])

price /= 10**power
price = round(price)
price = int(price*10**power)
print(price)

