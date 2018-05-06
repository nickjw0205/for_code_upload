
public class _4_3 {

	private static final int False = 0;
	private static final Exception Exception = null;

	public static void main(String[] args) throws java.lang.Exception {
		System.out.println(f(100));
	}
	
	public static int f(int n) throws Exception{
		if(n < 0) {
			throw new Exception();
		}
		else if(n == 0) {
			return 1;
		}
		else {
			System.out.println(n + " * factorial(" + (n-1) + ")");
			return n * f(n-1);
			
		}
	}

	
	/*	Recursion Trace
	 *	f(5) = 5*f(4) = 5*4*f(3) ......
	 *
	 * ----------------------------------
	 * 
	 *	주의사항 -> stackoverflow발생가능 팩토리알 100 정도 
	 * ----------------------------------
	 * 
	 * 
	 */
	
}
