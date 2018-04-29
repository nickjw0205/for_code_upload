
public class Quiz {
	
	public static int cnt = 0;
	public static int loop = 0;
	
	static boolean Solve(int start, int[] boxes) {
		return move(start, boxes);
	}
	
	private static boolean limit(int loop, int[] list) {
		boolean result = false;
		int limit = list.length * list.length;

		//loop의 회수가 한계보다클때(루프를 돌때)
		if(loop > limit) {
			return result = true;
		}

		return result;
	}

	private static boolean loop_test(int now, int[] list) {

		boolean result = false;
		int temp = list[now];


		if(now + list[now] < list.length && now - list[now] >= 0) {

			//앞과 뒤에 값이 같지않고 같았던 수가 한계보다 작을때.
			if(temp == list[now + list[now]] || temp == list[now - list[now]]) {
				return result = true;
			}

		}
		else if(now + list[now] >= list.length && now - list[now] < 0) {
			return result = true;
		}
		
		else if(now + list[now] >= list.length) {
			if(temp == list[now - list[now]]) {
				return result = true;
			}
		}

		
		else if(now - list[now] < 0) {
			if(temp == list[now + list[now]]) {
				return result = true;
			}
		}


		return result;
	}


	private static boolean move(int current, int[] boxes) {
		boolean result = false; 


		
		//current가 배열안에 있고 0을 만났을 
		if(current >= 0 && current <= boxes.length) {
			if(boxes[current] == 0) {
				return result = true;
			}
		}

		//current가 배열 밖으로 나가버렸을
		else {
			System.out.println("OutOfBoundary");
		}

		//0을 만나지 않았을때
		if(result == false && cnt <= boxes.length*boxes.length && (current + boxes[current] < boxes.length || current - boxes[current] >= 0)){

			//current가 배열안에 있고 오른쪽 왼쪽 둘다 이동이 가능할 때.
			if(current + boxes[current] < boxes.length && current - boxes[current] >= 0) {
				cnt = cnt + 1;
				System.out.println("cnt = " + cnt);
				if(loop_test(current, boxes)) {
					loop++;
					System.out.println("loop_test");
					System.out.println("loop = " + loop);
					if(limit(loop, boxes)) {
						System.out.println();
						System.out.println("loop OutOfCount");
						cnt = boxes.length*boxes.length + 1;
					}
				}
				System.out.println("Left & Right");
				System.out.println("boxes[current] = " + boxes[current]);
				System.out.println();
				return move(current + boxes[current], boxes) || move(current - boxes[current], boxes);
			}

			//오른쪽이나 왼쪽 중 1곳만 이동이 가능할 때.
			else {

				//왼쪽으로 이동이 가능할 때.
				if(current + boxes[current] >= boxes.length) {
					cnt = cnt + 1;
					System.out.println("cnt = " + cnt);
					if(loop_test(current, boxes)) {
						loop++;
						System.out.println("loop_test");
						System.out.println("loop = " + loop);
						if(limit(loop, boxes)) {
							System.out.println();
							System.out.println("loop OutOfCount");
							cnt = boxes.length*boxes.length + 1;
						}
					}
					System.out.println("Left");
					System.out.println("boxes[current] = " + boxes[current]);
					System.out.println();
					return move(current - boxes[current], boxes);
				}

				//오른쪽으로만 이동이 가능할 때. 
				else if(current - boxes[current] < 0) {
					cnt = cnt + 1;
					System.out.println("cnt = " + cnt);
					if(loop_test(current, boxes)) {
						loop++;
						System.out.println("loop_test");
						System.out.println("loop = " + loop);
						if(limit(loop, boxes)) {
							System.out.println("loop OutOfCount");
							cnt = boxes.length*boxes.length + 1;
						}
					}
					System.out.println("Right");
					System.out.println("boxes[current] = " + boxes[current]);
					System.out.println();
					return move(current + boxes[current], boxes);
				}
			}
		}

		//cnt가 length*length를 넘어 갔을때.
		else if(cnt > boxes.length*boxes.length) {
			cnt = boxes.length * boxes.length + 1;
			System.out.println("reach basecase");
			return result = false;
		}

		// result가 true이면 0을 만난것, false이면 0을 못 만난것
		return result;
	}

	//test_case
	public static void main(String[] args) {
//		int[] boxes = {3, 6, 4, 3, 3, 4, 3, 5, 0};
//		int[] boxes = {3, 6, 4, 1, 3, 4, 2, 5, 3, 0};
//		int[] boxes = {2, 1, 2, 0};
//		int[] boxes = {1, 1, 1, 0};
//		int[] boxes = {1, 2, 1, 2, 0};
//		int[] boxes = {1, 2, 3, 4, 5, 6, 7, 8, 9, 0};
		int[] boxes = {3, 1, 2, 3, 0};
		int start = 0;

		//true일때 
		if(Solve(start, boxes)) {
			System.out.println("True");
		}

		//false일때 
		else {
			System.out.println("False");
		}
	}

}
