#include <stdio.h>
#include <string.h>

int main(){
		char str[50] ="hi";
		char *p1 = "abc", *p2 = "pacific sea";
		strcat(str,"abc");
		strcat(str,"pacific");
		printf("%s\t%s\t%s\n",p1,p2,str);
		return 0;
}

