#include <stdio.h>

int main(){
    int sum = 0;
    int min = 99;
    for(int i = 0; i < 7; i++){
        int n;
        scanf("%d",&n);

        if(n%2 == 0) continue;

        if(n < min) min = n;
        sum = sum + n; 
    }
    if(sum != 0){
        printf("%d\n%d\n", sum, min);
    }
    else printf("-1");

    return 0;
}