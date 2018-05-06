#include <stdio.h>
int main(int argc, char *argv[])
{
	int c;
	while((c = getchar()) != EOF){
		if(c >= 'a' && c <= 'z'){
			putchar(c + 'A' - 'a');
		}
		else{
			putchar(c);
		}
	}
	return 0;
}
