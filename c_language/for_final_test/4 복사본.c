#include <stdio.h>

int main(void){

	int a = 300;
	int mask1 = 1;
	int mask2 = 1 << 3; 
	int mask3 = 1 << 5;

	if (a & mask1) a <<= 1; 	
	if (a & mask2) a >>= 2; 
	if (a & mask3) a >>= 3;	

	printf("%d\n", a);

	return 0;
}