
#include <stdio.h>
int main(){
	int i = 1;
	int clone_i;
	while(true){
		clone_i = i;
		while(clone_i != 0){
			printf("!");
			clone_i--;
		}	
		printf("\n");
		i++;
	}
}