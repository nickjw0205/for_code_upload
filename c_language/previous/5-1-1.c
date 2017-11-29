#include <stdio.h>
int main(){
	int a,b,c,d;
	printf("좌 상단의 x, y좌표: \n");
	scanf("%d %d",&a,&b);

	printf("우 상단의 x, y좌표: \n");
	scanf("%d %d",&c,&d);

	int result = (c - a)*(d - b);

	printf("두점이 이루는 직사각형의 넓이는 %d 입니다.\n",result);
	
	return 0;

}