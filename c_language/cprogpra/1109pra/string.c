#include <stdio.h>

int main(void){

		char null1 = NULL;
		char null2 = 0;
		char null3 = '\0';

		char zero = '0';
		printf("%d, %d, %d, %d\n\n",null1,null2,null3,zero);

		char *str1 = "HYU";
		char ary_str1[4] = {'H','Y','U'};
		char ary_str2[] = {"HYU"};
		printf("%s, %s, %s\n\n",str1,ary_str1,ary_str2);

		ary_str1[0] = 'A';
		ary_str2[0] = 'A';
		printf("%s, %s\n",ary_str1,ary_str2);
		
		return 0;
}

