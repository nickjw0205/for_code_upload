#include <stdio.h>

int gcd(int a, int b)
{
	int aclone = a, bclone = b;
	if(a < b){
		b = aclone;
		a = bclone;
	}
	
	int quotient = 1, remainder = 1 ;
	while(remainder != 0){
		quotient = a/b;
		remainder = a%b;
		a = b;
		b = remainder;
	}
	return a;
	
}
int main()
{
	printf("gcd(10, 15) = %d\n", gcd(10,15));
	printf("gcd(125, 13) = %d\n", gcd(125,13));
	printf("gcd(625, 225) = %d\n", gcd(625,225));
	printf("gcd(6840, 324) = %d\n", gcd(6840,324));
	return 0;
}

