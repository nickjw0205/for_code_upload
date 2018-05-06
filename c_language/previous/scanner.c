#include <stdio.h>
int main(){
	char arr[51][51];
	int R, C, ZR, ZC;
	scanf("%d %d %d %d",&R, &C, &ZR, &ZC);
	for(int i = 0;i < R;i++){
		scanf("%s",arr[i]);
	}
	for(int i = 0;i < R;i++){
		int x = ZR;
		while(x--){
			for(int j = 0;j < C;j++){
				int y = ZC;
				while(y--){
					putchar(arr[i][j]);
				}
			}
			putchar('\n');
		}
	}
	return 0;
}