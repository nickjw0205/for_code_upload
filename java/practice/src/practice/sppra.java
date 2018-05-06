package practice;

import java.util.Scanner;

public class sppra {

	public static void main(String[] args) {
		Scanner scanner = new Scanner(System.in);
		System.out.println("국어점수를 입력해주세요.");
		int kor = scanner.nextInt();
		System.out.println("영어 점수를 입력해주세요.");
		int eng = scanner.nextInt();
		System.out.println("수학점수를 입력해주세요");
		int math = scanner.nextInt();
		int total = (kor + eng + math);
		double average = (double)(total)/3.0;
		double per = Double.parseDouble(String.format("%.2f",average));
		System.out.println("총점: " + total);
		System.out.println("평균: " + per);
		scanner.close();
	}

}
