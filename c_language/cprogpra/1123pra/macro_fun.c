#include <stdio.h>

#define SQUARE(x)			((x) * (x))
#define ADD(x, y, z)		((x) + (y) + (z))
#define MUL(x, y, z)		((x) * (y) * (z))
#define MIN(x, y)			(((x) < (y)) ? (x) : (y))
#define MIN4(x, y, z, w)	MIN(MIN(x, y), MIN(z, w))

#define WRONG_SQUARE(x)		x * x

#define PI					3.14159
#define AREA_CIRCLE(x)		((PI) * (x) * (x))

int main(void){
		int a = 3, b = 4, c = 5, d = 6;
		printf("SQUARE(a) : %d\n",SQUARE(a));
		printf("ADD(a, b, c) : %d\n", ADD(a, b, c));
		printf("MUL(a, b, c) : %d\n", MUL(a, b, c));
		printf("MIN(a, b) : %d\n", MIN(a, b));
		printf("MIN4(a, b, c, d) : %d\n", MIN4(a, b, c, d));

		printf("WROMG_SQUARE(a + b) : %d?\n", WRONG_SQUARE(a + b));
		printf("AREA_CIRCLE(1) : %f\n", AREA_CIRCLE(1));
		printf("AREA_CIRCLE(5) : %f\n", AREA_CIRCLE(5));

		return 0;
}

		
