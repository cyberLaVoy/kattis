all: build run

build:
	kotlinc main.kt -include-runtime -d program.jar
run: 
	java -jar program.jar < ../testInput.txt

clean:
	rm program.jar