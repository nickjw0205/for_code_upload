package practice;

import java.util.Scanner;

public class yunyear {

	public static void main(String[] args) {
		Scanner scanner = new Scanner(System.in);
		System.out.println("년도를 입력해주세요.");
		int y = scanner.nextInt();
		if(y > 0 & y % 4 == 0 & (y % 400 == 0 | y % 100 != 0)) {
			System.out.println("윤년입니다.");
		}
		else {
			System.out.println("윤년이 아닙니다.");
		}
		scanner.close();
		}
}
