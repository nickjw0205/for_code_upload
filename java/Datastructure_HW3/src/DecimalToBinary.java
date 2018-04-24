import java.util.Stack;

public class DecimalToBinary {
	public static void deciTobinRec(int n) {
		int number = n;
		if(number != 0) {
			deciTobinRec(number/2);
			System.out.print(number%2);			
		}
	}
	public static void deciTobin(int n) {
		Stack<Integer> stack = new Stack<Integer>();
		int number = n;
		int i = 0;
		while(number != 0) {
			stack.push(number%2);
			number = number /2;
			i++;			
		}
		for(int j = 0; j < i;j++) {
			System.out.print(stack.pop());
		}
	}
	public static void main(String[] args) {
		deciTobinRec(1000000);
	}

}
