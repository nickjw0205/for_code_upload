#include <stdio.h>

int extra(int a);

int main(){
	int a, i;
	scanf("%x",&a);
	for(i = 0;i < 32;++i){
		printf("%d",extra(a));
		a = a<<1;
	}
	printf("\n");
}

int extra(int a){
	return !!(a & 0x80000000);
}