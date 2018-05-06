#include <stdio.h>
int main(){
	int arr[101][101] = {0};
	int n = 4;
	while(n--){
		int a, b, c, d;	
		scanf("%d %d %d %d",&a,&b,&c,&d);
		for(int i = a; i < c; i++){
			for(int j = b;j < d;j++){
				arr[i][j] = 1;
			}
		}
	}
	int result = 0;
	for(int i = 0; i < 101;i++){
		for(int j = 0; j < 101; j++){
			result += arr[i][j];
		}
	}
	printf("%d\n",result);
}