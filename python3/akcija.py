
numBooks = int(input())

books = []
for i in range(numBooks):
    books.append(int(input()))
books.sort(reverse=True)
cost = 0
if len(books) % 3 == 1:
    cost += books.pop()
elif len(books) % 3 == 2:
    cost += books.pop()
    cost += books.pop()
while len(books) != 0:
    books.pop()
    cost += books.pop()
    cost += books.pop()

print(cost)