#include <stdio.h>
int main(){
    int sum = 0;
    int min = 0;
    for(int i;i <7;i++){
        int n;
    
    scanf("%d",&n);
    if(n%2==1) continue;
        if(n<min) n = min;
            sum = sum + n;
        }
        if(sum != 0){
        printf("%d\n%d",sum,min);
        }
    	else printf("-1");
    return 0;
}