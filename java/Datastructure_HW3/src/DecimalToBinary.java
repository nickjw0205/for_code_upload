import java.util.Stack;

public class DecimalToBinary {
	public static void deciTobinRec(int n) {
		int number = n;

		if(number >= 2) {
			deciTobinRec(number/2);
			System.out.print(number%2);
		}
		else if(number == 1) {
			System.out.print(1);
		}
		else if(number == 0) {
			System.out.println(0);
		}
	}
	
	public static void deciTobin(int n) {
		Stack<Integer> stack = new Stack<Integer>();
		int number = n;
		int i = 0;
		while(number >= 1) {
			stack.push(number%2);
			number = number /2;
			i++;			
		}
		for(int j = 0; j < i;j++) {
			System.out.print(stack.pop());
		}
	}
	public static void main(String[] args) {
		deciTobinRec(100);
	}

}
