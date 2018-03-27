import java.util.Arrays;

public class _3_21 {
	
	public static void print(int[] A) {
//		System.out.println(
//				Arrays.stream(A).mapToObj(i -> i).collect(toList())
//				);
		 for (int i = 0; i < A.length - 1; i++)
				       System.out.print(A[i] + ", ");
				     System.out.println(A[A.length-1]);
	}

	public static void isort(int[] A) {
		for (int i = 1; i < A.length; i++) {
			int j = i;
			while (j > 0 && A[j-1] > A[j]) {
				swap(A, j-1, j);
				j = j - 1;
			}
		}
	}

	public static void swap(int[] A, int i, int j){
		int temp = A[i];
		A[i] = A[j];
		A[j] = temp;
	}

	
	//----------------------------------------//
	public static void main(String[] args) {
		
		int A[] = {1, 10, 5, 3, 7, 8, 2, 4};
		int B[] = Arrays.copyOf(A, A.length);
		// B = new int[A.length];
		//		     for (int i = 0; i < A.length; i ++)
		//		       B[i]= A[i];

		print(A);
		Arrays.sort(A);
		print(A);

		System.out.println("Before sorting");
		print(B);
		isort(B);
		print(B);
	}
}
