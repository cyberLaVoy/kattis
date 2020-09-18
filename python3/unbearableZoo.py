

numAnimals = int(input())

listNum = 1
while numAnimals != 0:
    print("List " + str(listNum) + ':')
    animalCount = {}
    for i in range(numAnimals):
        animal = input().split()
        animal = animal[len(animal)-1].lower()
        if animal not in animalCount: 
            animalCount[animal] = 1
        else:
            animalCount[animal] += 1
    for animal in sorted(animalCount.keys()):
        print(animal, '|', animalCount[animal])
    listNum += 1
    numAnimals = int(input())
