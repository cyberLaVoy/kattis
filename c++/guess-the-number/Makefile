all: build run

build: main.cpp
	g++ -Wall -Werror main.cpp -o program
run:
	./program

clean:
	rm -f program program.o

test: 
	valgrind --leak-check=full ./program
