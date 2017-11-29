#include <stdio.h>
#include <math.h>
double my_sqrt(double number)
{
	double sqrt;
	int a = 200;
	while(1){
		if(sqrt*sqrt < number){
			sqrt++;	
		}else{
			break;	
		}
	}
	while(a != 0){
	sqrt = 0.5*(sqrt + number/sqrt);
	a--;
	}
	return sqrt;
	
}
int main(int argx, char *argv[])
{
	double x;
	printf("Insert Non-negative number x: ");
	scanf("%lf",&x);
	printf("\nsqrt(x) = %10.15lf,sqrt(x)^2 = %.0lf\n",
	my_sqrt(x), my_sqrt(x)*my_sqrt(x));
	return 0;
}
