#include <stdio.h>

void swap(int *p, int *q);

int main(void){
		int I = 3, j = 5;
		swap(&I,&j);
		printf("%d %d \n",I, j);
		return 0;
}

void swap(int *p, int *q){
		int tmp;
		tmp = *p;
		*p = *q;
		*q = tmp;
}
