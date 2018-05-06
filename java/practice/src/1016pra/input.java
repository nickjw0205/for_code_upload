package 1016pra

import java.util.Scanner;

public class input {

	public static void main(String[] args) {
		System.out.print("0과 100사이의 정수를 입력해주세요: ");
		Scanner scanner = new Scanner(System.in);
		int max = 0, min = 100;
		int num = 100;
		while(0 <= num && num <= 100) {
			try {
				num = scanner.nextInt();
				if(0 <= num && num <= 100) {
					if(num > max) {
						max = num;
						}
						if(min > num) {
							min = num;
						}
				}
				else {
					break;
				}
			}
			catch(Exception e) {
				scanner.next();
			}
		}
		System.out.print("가장 작은 수는 " + min);
		System.out.print("이고 가장 큰 수는 " + max);
		System.out.print("이다.");
		scanner.close();
		}
	}
		

