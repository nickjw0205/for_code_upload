#include <stdio.h>
int main(){

	long double area, rad;
	printf("원의 반지름을 입력: ");
	scanf("%Lf",&rad);

	area = rad*rad*3.1415;
	printf("원의 넓이: %Lf \n",area);
	return 0;
}