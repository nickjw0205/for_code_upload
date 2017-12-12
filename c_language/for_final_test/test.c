#include <stdio.h>
#include <string.h>

int main(void){
	char a[4][20] = {"Look", "Kingdom Come", "Attaboy", "Perfect 10"};
	char *(p[4]) = {a[0], a[1], a[2], a[3]};
	char **pp = p;
	char result[100] = "Peek A Boo";
	strcat(result, *(pp+2)+4);
	printf("result1 = %s\n",result);
	strcat(result, *(p+1)+3);
	printf("result2 = %s\n",result);
	strcat(result, *(p+3));
	printf("result3 = %s\n",result);
	printf("%lu\n", strlen(result));
	return 0;
}