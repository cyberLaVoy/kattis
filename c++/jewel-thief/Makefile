all: build run

build: main.cpp
	g++ -Wall -Werror main.cpp -o program
run:
	./program < ../testInput.txt

clean:
	rm -f program program.o

test: 
	valgrind --track-origins=yes --leak-check=full ./program < ../testInput.txt
