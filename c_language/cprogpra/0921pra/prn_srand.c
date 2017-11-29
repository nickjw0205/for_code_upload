#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int main(void)
{
	int i, n, seed; //let i,n and seed be int

	seed = time(NULL); //let seed and time(NULL) be a same thing
	srand(seed);
	//to choose different integers give srand seed.this means everytime try to act this
	//code srand get different seed and choose different integers.

	printf("\n%s\n%s",
			"Some randomly distributed integers will be printed.",
			"How many do you want to See? ");
	//print two string with enter.

	scanf("%d",&n);// get a integer let n get that.

	for(i = 0;i<n;++i){ 
		//i is zero and while i is smaller than n, act this code and if you act one time then add 1 to i.

		if(i % 10 == 0){ //if i is a multiple of 10, add enter 
			putchar('\n');
		}
		printf("%12d",rand()); //print random integer
	}
	printf("\n\n");// print enter and enter
	return 0; //end the code
}
