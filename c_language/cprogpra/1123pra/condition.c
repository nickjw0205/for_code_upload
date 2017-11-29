#include <stdio.h>

#define DEBUG
//#undef DEBUG
#define VERSION 127

int main(){
#ifdef DEBUG
		printf("DEBUG: %s %s %s %d\n",
				__DATE__,__TIME__,__FILE__,__LINE__);

#endif

#if(defined DEBUG || defined TEST) && !defined (VERSION)
	printf("DEBUG\n");

#endif

#if(VERSION == 123)
	printf("Version : 1.2.3\n");

#elif (VERSION == 127)
	printf("Version: 1,2,7\n");

#endif

	return 0;
}
