package testpra;

public class practice {
	int rad;
	
	public practice(int rad) {
		int a;
		this.rad = rad;
	}

	public static double getarea(int rad) {
		return 3.14*rad*rad;
	}
	
	public static void main(String[] args) {
		int m = 10;
		getarea(m);
		System.out.print(m);
	}

}
