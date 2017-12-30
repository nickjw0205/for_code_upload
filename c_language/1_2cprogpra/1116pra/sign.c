#include <stdlib.h>
#include <stdio.h>
#include <limits.h>
#include <unistd.h>

void moving_sign(char, char, char, char);
void print_sign(int);

int main(){
		moving_sign('H','E','Y',' ');
		return 0;
}

void print_sign(int a){
		printf(" %c %c %c %c \n",
			a/(256*256*256), a/(256*256), a/256, a);
}

void moving_sign(char _a, char _b, char _c, char _d){
		char a = _a, b = _b, c = _c, d = _d, tmp;
		
		int p;
		p = a;
		p = (p << CHAR_BIT) | b;
		p = (p << CHAR_BIT) | c;
		p = (p << CHAR_BIT) | d;

		while(1){
				system("clear");
				print_sign(p);
				sleep(1);
				int n = 3*CHAR_BIT;
				unsigned mask = 255;
				mask <<= n;
				tmp = ((p & mask) >> n);
				p = (p << CHAR_BIT) | tmp;

		}
}

