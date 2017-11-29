#include "hanoi.h"

int get_n_from_user(void){
		int n;
		printf("%s",
			"---\n"
			"Tower of hanoi: \n"
			"\n"
			"Input n: ");
		if(scanf("%d",&n) != 1 || n <1){
				printf("\n Error: Positive integer not found - bye!\n\n");
				exit(1);
		}
		printf("\n");
		return n;
}
