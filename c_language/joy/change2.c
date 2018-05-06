#include <stdio.h>
#include <unistd.h>
int main()
{
    int number,result,countNum=0;
    char str[100000];
    printf("이진수로 바꿀 숫자를 입력해 주세요.\n");
    scanf("%d",&number);
    int time = number;
    int numtime = 0;
    printf("이진수로 변환중 입니다.....\n");
    while(1) //숫자를 2로 나눈 횟수를 경과 시간으로 지정 그냥 숫자가 클수록 걸리는 시간을 길게잡는 방법중 1가지
    {
        if(time > 1)
        {
            time = time/2;
            numtime++;
        }
        else 
        {
            break;
        }
    }
    float copy_numtime = numtime; //numtime을 건들지 않기 위해 clone생성
    int allot = 0; 
    while(copy_numtime > 1)
    {
        copy_numtime = copy_numtime/10; //밑에 while문 에서 10초동안 도는 과정을 몇번할지를 allot을 통해 지정
        allot++;
    }
    int allotclone = allot; //allot도 건들면 안되니 clone생성
    if(numtime <= 10) //10초 미만일 경우 그냥 지연메세지 없이 돌림 
    {
        sleep(numtime);
    }
    else
    {
        int time1 = 1;
        while(allotclone != 0) //10초가 넘어가면 지연메세지 생성
        {
            sleep(10);
            printf("입력하신 숫자가 커서 연산이 지연되고 있습니다.\n");
            printf("현재 경과 시간: %d초\n",time1*10);//10초 20초를 표현하기위해 time1으로 와일문 돈 횟수 계산 
            copy_numtime++;
            time1++;
            allotclone--;
        }
        sleep(numtime - (allot - 1)*10);//위에서 10단위밖에 못했으니 1의자리도 돌려준다.
    }
    int number_clone = number;//result로 몇번의 나눔셈을 해야하는지 계산
    while(1){
        if(number_clone > 1){
            number_clone = number_clone /2;
            result++;
        }
        else{
            break;
        }
    }
    for(int i=result;i>=0;i--)
    {
        if(number%2==1)
        {
            str[i] = 1;
            countNum++;
            number = number/2;
        }
        else if(number%2==0)
        {
            str[i] = 0;
            countNum++;
            number = number/2;
        }
    }
    for(int j=0;j<countNum;j++)
    {
        printf("%d",str[j]);
    }
    printf("\n");
    printf("경과한 시간: %d초\n",numtime);
}