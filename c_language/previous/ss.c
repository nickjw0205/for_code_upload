#include <stdio.h>

int cache[10001]={0};
void d(int n){
	int result = n;
	while(n>0){
		result += n % 10;
		n /= 10;
	}

	if(result < 10000){
		cache[result] = 1;
		return d(result);
	}
}
int main(){
	for(int i = 1;i<10000;i++) d(i);

	for(int i = 1;i<10000;i++){
		if(cache[i] == 0) printf("%d\n",i);
	}
	return 0;
}