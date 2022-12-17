
def count(obj):
    return obj[1]
def name(obj):
    return obj[0]

def main():
    numTests = int(input())
    for _ in range(numTests):
        numShipments = int(input())
        itemCounts = {}
        for _ in range(numShipments):
            shipment = input().split()
            itemName = shipment[0]
            itemCount = int(shipment[1])
            if itemName not in itemCounts:
                itemCounts[itemName] = 0
            itemCounts[itemName] += itemCount
        itemCounts = [(k, v) for k,v in itemCounts.items()]
        itemCounts.sort(key=name)
        itemCounts.sort(key=count, reverse=True)
        print(len(itemCounts))
        for n, c in itemCounts:
            print(n, c)


if __name__ == "__main__":
    main()