#include <stdio.h>
int main(){

	int a;
	printf("원하시는 숫자를 입력해주세요: ");
	scanf("%d",&a);
// 	scanf("%d\n",&a);
//  숫자값, 1자 이상의 공백문자, 숫자값, 1자 이상의 공백문자, 공백문자가 아
//  닌 문자가 입력버퍼에 있기를 기대한다.
	printf("입력하신 문자는 %c 입니다.\n",a);

	return 0;
}