CC= gcc
target = hanoi
objects = hanoi.h main.o move.o get.o

$(target) : $(objects)
	$(CC) -o $@ $^

clean:
	rm *.o hanoi
