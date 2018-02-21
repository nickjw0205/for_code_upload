package elice;


import java.util.Scanner;

public class third_5 {
	public static void main(String args[]) {
			
			Scanner scan = new Scanner(System.in);
			 
			System.out.print("당신의 이름을 입력하세요:");
			
			String name = scan.nextLine();//터미널에서 문자열을 받습니다.
			System.out.println(name);
			
			System.out.print("나이를 입력하세요:");
			
			int age = scan.nextInt();//터미널에서 정수를 받습니다.
			System.out.println(age);
			
			System.out.println("제 이름은 "+name+ "이고, 나이는 "+age+"살 입니다.");
		}
	}


