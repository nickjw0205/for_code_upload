
import DLinkedList;

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
       /**/
    }

    public Block malloc(int size) {
        /**/
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


