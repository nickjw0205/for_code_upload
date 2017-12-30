#include <stdio.h>

#define MUL(a, b) a * b
#define SQUARE(a) a * a
#define X 5
#define Y 2

int main(void){
	char ch1 = 'A' + MUL(X, X - Y);
	char ch2 = 'A' + SQUARE(X + Y);
	printf("%d, %d\n", ch1, ch2);
	return 0;
}