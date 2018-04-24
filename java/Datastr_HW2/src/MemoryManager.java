
//import DLinkedList;

/* Block will be used as a type argument */
class Block {
	public int size;
	public int start;
	public int end;

	public Block(int size, int start, int end) {
		this.size = size;
		this.start = start;
		this.end = end;
	}

	@Override
	public String toString() {
		return "(" + size +", " + start + ", " + end + ")";
	}
}	

public class MemoryManager {

	private DLinkedList<Block> heap = new DLinkedList<>();

	public MemoryManager(int capacity) {
		MemoryManager manager = new MemoryManager(capacity);
		Block block = new Block(capacity, 0, capacity -1);
		Node block1 = new Node(capacity, heap.getLast(), heap.getFirst());

	}

	public Block malloc(int size) throws OutOfMemoryException{
		Block block = new Block(size, );
		return null;
	}

	public void free(Block block) {
		/**/
	}

	// for debugging purpose only
	public DLinkedList<Block> getHeap() {
		return heap;
	}

	@Override
	public String toString() {
		return heap.toString();
	}
}


