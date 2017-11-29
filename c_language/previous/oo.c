#include <stdio.h>
#include <string.h>
int main(){
	int i, lens;
	char str[100] = " ";
	scanf("%s",str);
	lens = strlen(str);
	for(i = 0; i < lens; i++){
		if(str[i] >= 97 && str[i] <= 122){
				str[i] -= 32;
			}
			else if(str[i] >= 65 && str[i] <= 90){	
				str[i] += 32;
			}
		}
	printf("%s\n", str);
}