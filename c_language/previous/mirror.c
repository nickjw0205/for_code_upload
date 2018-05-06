#include <stdio.h>
char arr[101][101];
int n;
void print(){
	for(int i =0;i <n;i++){
		printf("%s\n",arr[i]);
	}
}
void vertical(){
	for(int i = n-1; i >= 0;i--){
		printf("%s\n",arr[i]);
	}
}	
void horzontal(){
	for(int i =0;i < n;i++){
		for(int j = n-1; j >= 0;j--){
			putchar(arr[i][j]);
		}
	printf("\n");
	}
}
int main(){
	scanf("%d",&n);
	for(int i =0;i <n;i++){
		scanf("%s",arr[i]);
	}
	int c;
	scanf("%d",&c);
	if(c == 1){
		print();
	}
	else if(c == 2){
		horzontal();
	}
	else if(c == 3){
		vertical();
	}
}
