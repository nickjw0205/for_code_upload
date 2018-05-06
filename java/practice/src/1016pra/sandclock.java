package practice;

import java.util.Scanner;

public class sandclock {

	public static void main(String[] args) {
		Scanner scanner = new Scanner(System.in);
		System.out.println("짝수를 입력해주세요?.");
		int countNum = 1;
		while(countNum % 2 != 0) {
			try {
				countNum = scanner.nextInt();
			}
			catch(Exception e) {
				scanner.next();
			}
			
		}
		if(countNum %2 == 0) {
			int time = countNum - 1;
			int bin = countNum/2 - 1;
			int star = 1;
			for(int i = 0;i <2; i++) {
				for(int j = 0; j < countNum/2;j++) {
					if(i == 0) {
						int cj1 = j;
						while(cj1 > 0) {
							System.out.print(" ");
							cj1--;
						}
						int cj2 = time;
						while(cj2 > 0) {
							System.out.print("*");
							cj2--;
						}

						int cj3 = j;
						while(cj3 > 0) {
							System.out.print(" ");
							cj3--;
						}
						System.out.println("");
						time = time - 2;
					}
					if(i == 1) {
						int starclone = star;
						int binclone = bin;
						int binclone1 = bin;
						while(binclone != 0) {
							System.out.print(" ");
							binclone--;
						}
						while(starclone != 0) {
							System.out.print("*");
							starclone--;
						}
						while(binclone1 != 0) {
							System.out.print(" ");
							binclone1--;
						}
						star = star + 2;
						bin--;
						System.out.println("");
					}
				}
				
			}

		}
		scanner.close();
	}
}