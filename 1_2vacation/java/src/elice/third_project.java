package elice;

public class third_project {
	public static void main(String args[]) {
		
		int input = 3306;//3306은 박수 3번!(최대 4자리, 9999만 입력하세요);
		int clap = 0;//박수 쳐야하는 수 3306은 3번 박수!!!
		
		/** 1단계 - 각 자리수를 구해보세요! [실습5]참고 **/
		int thousand = input/1000;//천의 자리수,thousand 값을 input/1000%10 로 구해보세요!
		int hundred  = (input/100)%10;//백의 자리수
		int ten      = (input/10)%10;//십의 자리수
		int one      = input%10;//일의 자리수
		
		/** 2단계 3의 배수인지 확인하세요[실습6,7]*/
		if(thousand%3==0){//천의자리수가 3의 배수인지 확인해요
			/** 3단계 : thousand,hundred,ten,one 이 0이 아닌지 확인하세요! [실습6]참고 */
			if(thousand != 0){//0일때는 박수를 치지 않아요!
				clap++;//박수수 증가
			}
		}
		
		/** 2~3단계 반복*/
		if(hundred%3==0){//백의 자리수가 3의 배수인지 확인해요
			if(hundred != 0){//0일때는 박수를 치지 않아요!
				clap++;//박수수 증가
			}
		}
		
		/** 2~3단계 반복*/
		if(ten%3==0){//십의 자리수가 3의 배수인지 확인해요
			if(ten != 0){//0일때는 박수를 치지 않아요!
				clap++;//박수수 증가
			}
		}
		
		/** 2~3단계 반복*/
		if(one%3==0){//일의 자리수가 3의 배수인지 확인해요
			if(one != 0){//0일때는 박수를 치지 않아요!
				clap++;//박수수 증가
			}
		}
		
		// 여기 아래 부터는 수정 하지 마세요. 채점에 반영됩니다!!
		System.out.println("입력 된 숫자 : " + input);//!!지우지 마세요!!
		
		System.out.println(thousand);//천의 자리 숫자
		System.out.println(hundred);//백의 자리 숫자
		System.out.println(ten);//십의 자리 숫자
		System.out.println(one);//일의 자리 숫자
		
		System.out.println("박수 수:" + clap);
	}
}
