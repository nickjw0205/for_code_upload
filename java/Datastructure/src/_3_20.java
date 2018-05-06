import java.util.Arrays;

public class _3_20 {

	public static void main(String[] args) {
		int[] as = {1,2,3,4,5};
		int[] xs = {5,4,3,2,1};
		
		//copyof
		int ys[] = Arrays.copyOf(as,10);
		int zs[] = Arrays.copyOfRange(as, 1, 3);
		
		//배열을 쉽게 출력하는 방법
		System.out.println(Arrays.toString(ys));
		
		//sum
//		int total = 0;
//		for(int i = 0;i<as.length;i++) {
//			total += as[i];
//		}
//		System.out.println(total);
		
		//배열의 원소들의 합을 구하는 방법
		int total = Arrays.stream(as).sum();
		System.out.println(total);
		
		//2차원 배열 생성
		double[][] M = new double[2][3];
		double[][] M1 ={{0,1,2},{1,2,3}};
		//위에거를 row major order이라고 한다.
		//column major order은 011223으로 저장해야하므로 귀찮음.
		
		
		
		
	}
	


}
