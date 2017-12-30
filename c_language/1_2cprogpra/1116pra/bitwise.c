#include <stdio.h>
#include <stdlib.h>
#include <limits.h>

void bit_print(int);
int pack(char, char, char, char);
char unpack(int, int);

int main(int argc, char *argv[]){
		if(argc<3){
				printf("usage: bitwise num1, num2\n");
				exit(1);
		}
		
		int num1 = atoi(argv[1]);
		int num2 = atoi(argv[2]);

		printf("%d, %d: \n",num1,num2);
		bit_print(num1);
		bit_print(num2);

		printf("~%d, ~%d: \n",num1,num2);
		bit_print(~num1);
		bit_print(~num2);

		printf("%d & %d: \n",num1,num2);
		bit_print(num1 & num2);
		
		printf("%d | %d: \n",num1,num2);
		bit_print(num1 | num2);
		
		printf("%d ^ %d: \n",num1,num2);
		bit_print(num1 ^ num2);
		
		printf("%d << 2, %d >> 5 : \n",num1,num2);
		bit_print(num1 << 2);
		bit_print(num2 >> 5);

		char c1 = 'c';
		char c2 = 'h';
		char c3 = 'a';
		char c4 = 'r';

		printf("%c, %c, %c, %c : \n",c1,c2,c3,c4);
		bit_print(c1);
		bit_print(c2);
		bit_print(c3);
		bit_print(c4);
	
		int pdata = pack(c1,c2,c3,c4);
		printf("packed data: \n");
		bit_print(pdata);

		printf("unpack(pdata,0): %c\n",unpack(pdata,0));
		printf("unpack(pdata,2): %c\n",unpack(pdata,2));

		return 0;
}


void bit_print(int a){
		int i;
		int n = sizeof(int) * CHAR_BIT;
		int mask = 1 << (n - 1);

		for(i = 1;i <= n; ++i){
				putchar(((a &mask) == 0) ? '0' : '1');
				a <<= 1;
				if(i % CHAR_BIT == 0 && i < n){
						putchar(' ');
				}
		}
		putchar('\n');
}

int pack(char a, char b, char c, char d){
		int p;

		p = 1;
		p = (p << CHAR_BIT) | b;
		p = (p << CHAR_BIT) | c;
		p = (p << CHAR_BIT) | d;

		return p;
}

char unpack(int p , int k){
		int n = k * CHAR_BIT;
		unsigned mask = 255;

		mask <<= n;
		return ((p & mask) >> n);
}
