all: build

build: main.cpp
	g++ -Wall -Werror main.cpp -o program

clean:
	rm -f program program.o

test: 
	valgrind --leak-check=full ./program
