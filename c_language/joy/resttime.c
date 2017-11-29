#include <stdio.h>
#include <unistd.h>
#include <string.h>
int main(){

	int a,b,j;
	char str[50];
	char d[] = "second", e[] = "minute", f[] = "hour";
	printf("쉬는시간을 입력해주세요.(ex:10 second)\n");
	scanf("%d %s",&a,str);

	if(strcmp(str,d) == 0){
		b = a;
	}
	else if(strcmp(str,e) == 0){
		b = a*60;
	}
	else if(strcmp(str,f) == 0){
		b = a*3600;
	}
	else{
		printf("단위를 정확히 쳐주세요\n");
		return 0;
	}
	while(b != 0){
		if(b == 10){
			printf("쉬는 시간이 곧 종료 됩니다!!!\n");
		}
		printf("쉬는 시간이 %d초 남았습니다.\n",b);
		b--;
		sleep(1);
	}
}