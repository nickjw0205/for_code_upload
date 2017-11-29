import java.util.ArrayList;
import java.util.Scanner;
import java.io.*;
import java.lang.NumberFormatException;

class StudentManager {
	private ArrayList<StudentInfo> studentInfoList = new ArrayList<StudentInfo>();
	private Scanner scanner = new Scanner(System.in);

	void signUp() {
		StudentInfo studentInfo = new StudentInfo();

		System.out.print("Input Student Name : ");
		studentInfo.setUserName(scanner.next());

		System.out.print("Input Student Age : ");
		try {
			studentInfo.setUserAge(Integer.parseInt(scanner.next()));
		} catch(NumberFormatException e) {
			System.out.println("Please Input Integer Number\nSignUp Aborted");
			return;
		}

		System.out.print("Input Student Id : ");
		studentInfo.setStudentId(scanner.next());
		System.out.print("Input Student Phone : ");
		studentInfo.setStudentPhone(scanner.next());

		studentInfoList.add(studentInfo);
	}

	void displayList() {
		System.out.println("Index\tName\tAge\tId\tPhone");
		for(StudentInfo studentInfo : studentInfoList) {
			System.out.println((studentInfoList.indexOf(studentInfo) + 1) + "\t"
					+ studentInfo.getUserName() + "\t"
					+ studentInfo.getUserAge() + "\t"
					+ studentInfo.getStudentId() + "\t"
					+ studentInfo.getStudentPhone() + "\t");
		}
	}

	void save() {
		FileWriter fw = null;
		try{
			fw = new FileWriter("src/Copy1.txt");
			for(StudentInfo studentInfo : studentInfoList) {
				fw.write(studentInfo.getUserName() + ".");
				fw.write(studentInfo.getUserAge() + ".");
				fw.write(studentInfo.getStudentId() + ".");
				fw.write(studentInfo.getStudentPhone() + ".");
			}
		}catch(Exception e){
			System.out.println("오류발생");
		}finally {
			System.out.println("저장완료");
			try {
				fw.flush();
				fw.close();
			}catch(Exception e) {
				System.out.println("오류발생");
			}
		}


	}



	void load(){
		StudentInfo studentInfo = new StudentInfo();
		FileReader fr = null;
		String ab = new String();
		int i = 0;
		int z = 0;
		char[] reader = new char[10000];
		String[] result = new String[10000];
		int read;
		int c = 0;
		try {
			fr = new FileReader("src/Copy1.txt");
			while((read=fr.read(reader)) != -1) {
				String data = new String(reader,0,read);
				for(i = 0;i < data.length();i++) {
					if(reader[i] != '.') {
						ab += reader[i];
					}
					else {
						result[z] = ab;
						ab = "";
						z += 1;
					}
				}
			}
			
			for(i = 0;i < result.length;i++) {
				if(result[c] != null) {
					StudentInfo studentInfo1 = new StudentInfo();
					studentInfo1.setUserName(result[c]);
					c += 1;
					studentInfo1.setUserAge(Integer.parseInt(result[c]));
					c += 1;
					studentInfo1.setStudentId(result[c]);
					c += 1;
					studentInfo1.setStudentPhone(result[c]);
					c += 1;
					studentInfoList.add(studentInfo1);
				}
				else {
					continue;
				}
			}
		}catch(Exception e) {
			System.out.println("오류발생");
		}finally {
			System.out.println("로딩완료");
			try {
				fr.close();
			}catch(Exception e) {
				System.out.println("오류발생");
			}
		}
	}


	void run() {
		int inputNum;
		while(true) {
			System.out.print("1) Sign Up 2) Display List 3) Save 4) Load 5) exit ==> ");
			try {
				inputNum = Integer.parseInt(scanner.next());
			} catch(NumberFormatException e) {
				System.out.println("Please Input Number: 1~5");
				continue;
			}
			if(inputNum == 1) {
				signUp();
			} else if(inputNum == 2) {
				displayList();
			} else if(inputNum == 3) {
				save();
			} else if(inputNum == 4) {
				load();
			} else if(inputNum == 5) {
				break;
			} else {
				System.out.println("Please Input Number: 1~5");
			}
		}
		scanner.close();
		return;
	}
}
