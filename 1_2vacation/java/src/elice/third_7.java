package elice;

public class third_7 {
	public static void main(String args[]) {
		
		boolean isSame = false;//실제로는 0
		boolean isNotSame = false;//실제로는 0
		
		//x와 y가 다른 값을 가지도록 값을 넣어보세요.
		int x = 30;
		int y = 30;
		
		isSame    = x == y;//true;
		isNotSame = x != y;//false
		
		/**
		 * 예상되는 출력은 다음과 같습니다
		 * > 같다
		 * > 같다
		 */
		
		if(isSame){
			System.out.println("같다");
		}else{
			System.out.println("다르다");
		}
		
		if(isNotSame){
			System.out.println("다르다");
		}else{
			System.out.println("같다");
		}
		
	}

}
