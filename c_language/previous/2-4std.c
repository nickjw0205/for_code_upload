#include <stdio.h>
int main(){
	// 변수는 숫자로 시작할수없고 특수문자및 공백이 사용되면 안된다.
	int num1;
	num1 = 0;
	int num2;
	num2 = 1;
	double num3;
	num3 = 3.14;
	printf("%d %d %f\n",num1,num2,num3);
	

	return 0;
	// 위의 변수선언은 1999년도 이전에는 컴파일에러가 떴음.
}