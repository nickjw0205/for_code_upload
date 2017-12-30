#include <stdio.h>

int main(void){

	int a = 300;
	int mask1 = 1;
	int mask2 = 1 << 3;
	printf("mask2 => %d\n", mask2);
	int mask3 = 1 << 5;
	printf("mask3 => %d\n", mask3);

	if (a & mask1) a <<= 1;
	printf("1 => %d\n", a);
	if (a & mask2) a >>= 2;
	printf("2 => %d\n", a);
	if (a & mask3) a >>= 3;
	printf("3 => %d\n", a);

	printf("%d\n", a);

	return 0;
}