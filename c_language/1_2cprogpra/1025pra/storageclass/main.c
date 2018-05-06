#include <stdio.h>

int a =1, b = 2, c = 3;

int extern_function(void);
int static_function(void);

int main(void){
	printf("%3d\n",extern_function());
	printf("%3d%3d%3d\n",a,b,c);
	static_function();
	static_function();
	return 0;
}
