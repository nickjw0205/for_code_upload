
import java.util.Scanner;

public class matrices {
	public static void main(String[] args) {
		int[][] matrix1 = new int[3][3];
		int[][] matrix2 = new int[3][3];
		int[][] matrix3 = new int[3][3];
		Scanner scanner = new Scanner(System.in);
		System.out.println("1번째 행렬 입력");
		for(int i = 0; i < 3; i++) {
			for(int j = 0;j < 3;j++) {
				matrix1[i][j] += scanner.nextInt();
				
			}
		}
		System.out.println("2번째 행렬 입력");
		for(int i = 0; i < 3; i++) {
			for(int j = 0;j < 3;j++) {
				matrix2[i][j] += scanner.nextInt();
			}
		}
		for(int i = 0; i < 3; i++) {
			for(int j = 0;j < 3;j++) {
				matrix3[i][j] = matrix1[i][0]*matrix2[0][j] 
								+ matrix1[i][1]*matrix2[1][j] 
								+ matrix1[i][2]*matrix2[2][j];
			}
		}
		System.out.println("1번째 행렬 출력");
		for(int i = 0;i < 3; i++) {
			for(int j = 0;j < 3; j++) {
				System.out.print(+matrix1[i][j]+"  ");
			}
			System.out.println("");
			System.out.println("");
		}
		System.out.println("2번째 행렬 출력");
		for(int i = 0;i < 3; i++) {
			for(int j = 0;j < 3; j++) {
				System.out.print(+matrix2[i][j]+"  ");
			}
			System.out.println("");
			System.out.println("");
		}
		System.out.println("두 행렬의 곱");
		for(int i = 0;i < 3; i++) {
			for(int j = 0;j < 3; j++) {
				System.out.print(+matrix3[i][j]+"  ");
			}
			System.out.println("");
			System.out.println("");
		}
		scanner.close();
	}

}
