package _1023pra;

import java.util.ArrayList;
import java.util.Scanner;


class StudentManager { 
	public void start() {
		Scanner scanner =  new Scanner(System.in);
		ArrayList<StudentInfo> studentInfoList = new ArrayList<StudentInfo>();
	
		String name;
		int age;
		int id;
		String phone;
		String b;
		int n = 0;
		String s_name;
		int s_id;
		int a;
	
		while (true) {
		
			System.out.println("------------------------------------------------------------------------------");
			System.out.print("1) sign up 2) modify 3) delete 4) list 5) name search 6) ID search 7) Quit ==> ");
			n = Integer.parseInt(scanner.next());
			System.out.println("------------------------------------------------------------------------------");
			
			if (n == 1) {
			
				System.out.print("Input name : ");
					name = scanner.next();
				System.out.print("Input age : ");
					age = scanner.nextInt();
				System.out.print("Input student ID : ");
					id = scanner.nextInt();
				System.out.print("Input phone number : ");
					phone = scanner.next();
				
				studentInfoList.add(new StudentInfo(name,age,id,phone));
			}	
			
			else if (n == 2) {
				System.out.println("No.\tName\tAge\tStudent ID\tPhone Number ");
				for(StudentInfo user : studentInfoList) 
					System.out.println((studentInfoList.indexOf(user)+1) + "\t" 
					+ user.getUserName() + "\t"
					+ user.getUserAge() + "\t" 
					+ user.getStudentId() + "\t"
					+ user.getStudentPhone());
				System.out.print("==> Input modify No. : ");
				
				a = Integer.parseInt(scanner.next());
				
				System.out.print("Input name : ");
					name = scanner.next();
				System.out.print("Input age : ");
					age = scanner.nextInt();
				System.out.print("Input student ID : ");
					id = scanner.nextInt();
				System.out.print("Input phone number : ");
					phone = scanner.next();
			
				studentInfoList.add(a-1, new StudentInfo(name,age,id,phone));
				studentInfoList.remove(a);
			}
		
			else if (n == 3) {
				System.out.println("No.\tName\tAge\tStudent ID\tPhone Number ");
				for(StudentInfo user : studentInfoList) {
					System.out.println((studentInfoList.indexOf(user)+1) + "\t" 
					+ user.getUserName() + "\t"
					+ user.getUserAge() + "\t" 
					+ user.getStudentId() + "\t"
					+ user.getStudentPhone());
				}
				System.out.print("==> Input delete No. : ");
				
				a = Integer.parseInt(scanner.next());
				
				System.out.print("Really Delete?(Y/N) ");
				b = scanner.next();
				if (b.equals("Y")) {
					System.out.println("Delete Finished");
					studentInfoList.remove(a-1);
				}
				else {
					if(b.equals("N"))
						continue;
					else {
						System.out.print("Wrong!");
						continue;
					}
				}
			}
			
			if (n == 4) {
				System.out.println("Name\tAge\tStudent ID\tPhone Number ");
				for(StudentInfo user : studentInfoList) {
					System.out.println(user.getUserName() + "\t" 
						+ user.getUserAge() + "\t" 
						+ user.getStudentId() + "\t" 
						+ user.getStudentPhone());
				}
			}
			
			if (n == 5) {
				System.out.print("Input Search Name : ");
				s_name = scanner.next();
				System.out.println("No.\tName\tAge\tStudent ID\tPhone Number ");
				for(StudentInfo user : studentInfoList) {
					if (user.getUserName().equals(s_name)) {
						System.out.println((studentInfoList.indexOf(user)+1) + "\t" 
							+ user.getUserName() + "\t"
							+ user.getUserAge() + "\t" 
							+ user.getStudentId() + "\t"
							+ user.getStudentPhone());
					}
				}
			}
		
			if (n == 6) {
				System.out.println("Input Search ID : ");
				s_id = Integer.parseInt(scanner.next());
				System.out.println("No.\tName\tAge\tStudent ID\tPhone Number ");
				for(StudentInfo user : studentInfoList) {
					if (user.getStudentId() == s_id) {
						System.out.println((studentInfoList.indexOf(user)+1) + "\t" 
							+ user.getUserName() + "\t"
							+ user.getUserAge() + "\t" 
							+ user.getStudentId() + "\t"
							+ user.getStudentPhone());
					}
				}
			}
				
			if (n == 7) {
				System.out.println("Program Finished");
				System.exit(0);
				scanner.close();
			}
		}
	}
	public StudentManager() {
		start();
	}
}