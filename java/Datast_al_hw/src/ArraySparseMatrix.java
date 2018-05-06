import java.util.Arrays;

public class ArraySparseMatrix implements SparseMatrix {

	public static final int DEFAULT_CAPACITY = 1024;

	private int rowCount;
	private int columnCount;
	private int elemCount;
	private Entry[] elements = new Entry[0];

	public ArraySparseMatrix(int rowCount, int columnCount, int capacity) {
		elements = new Entry[capacity];
		this.rowCount = rowCount;
		this.columnCount = columnCount;
		this.elemCount = 0;
	}

	public ArraySparseMatrix(int rowCount, int columnCount) {
		this(rowCount, columnCount, DEFAULT_CAPACITY);
	}
	/*
	 * This routine simulates reading from files using two-dimensional matrix.
	 */
	public static SparseMatrix create(double[][] aMatrix, int rowCount, int columnCount, int elemCount) {
		ArraySparseMatrix matrix = new ArraySparseMatrix(rowCount, columnCount, elemCount);

		int nonZeroCount = 0;
		for (int i = 0; i < aMatrix.length; i++)
			for (int j = 0; j < aMatrix[i].length; j++) {
				if (Double.compare(aMatrix[i][j], 0.0) != 0) {
					matrix.put(new Entry(i, j, aMatrix[i][j]));
					nonZeroCount++;
				}
			}

		if (nonZeroCount != elemCount)
			throw new IllegalStateException("Non zero count doesn't match");

		return matrix;
	}

	@Override
	public SparseMatrix transpose() {
		int row = 0;
		int col = 0;
		int elem = this.elemCount;
		for(int i = 0; i < elem;i++) {
			col = this.elements[i].col;
			row = this.elements[i].row;
			this.elements[i].col = row;
			this.elements[i].row = col;
		}

		int b = 0;
		int c = 0;
		b = this.rowCount;
		c = this.columnCount;
		this.rowCount = c;
		this.columnCount = b;

		int length = elements.length;
		int cnt = 0;
		for(int i = length;i > 0;i--) {
			for(int j = 0;j < i - 1;j++) {
				if(elements[j].row > elements[j+1].row) {
					Entry copy1 = new Entry(9,9,9);
					Entry copy2 = new Entry(9,9,9);
					copy1 = elements[j].copy();
					copy2 = elements[j+1].copy();
					elements[j] = copy2;
					elements[j+1] = copy1;
				}
			}
		}
		return this;
	}

	@Override
	public SparseMatrix add(SparseMatrix other) {
		if (this.rowCount != other.getRowCount() || this.columnCount != other.getColumnCount())
			throw new IllegalArgumentException("Matrix size doesn't match");
		ArraySparseMatrix other1 = (ArraySparseMatrix) other;
		double[][] sm1 = new double[1024][1024]; 

		for(int i = 0;i < 1024;i++) {
			for(int j = 0;j < 1024; j++) {
				sm1[i][j] = 0;
			}
		}

		int a = 0;
		for(int i = 0;i < 1024;i++) {
			for(int j = 0;j < 1024;j++) {
				if(i == elements[a].row && j == elements[a].col) {
					sm1[i][j] = elements[a].value;
					a++;
				}
				if(a == elements.length) {
					break;
				}
			}
			if(a == elements.length) {
				break;
			}
		}



		int b = 0;

		for(int i = 0;i < 1024;i++) {
			for(int j = 0;j < 1024;j++) {
				if(i == other1.elements[b].row && j == other1.elements[b].col) {
					sm1[i][j] += other1.elements[b].value;
					b++;	
				}
				if(b == other1.getElemCount()) {
					break;
				}
			}
			if(b == other1.getElemCount()) {
				break;
			}
		}

		int elem = 0;
		for(int i = 0;i < 1024;i++) {
			for(int j = 0;j < 1024;j++) {
				if(sm1[i][j] != 0) {
					elem += 1;
				}
			}
		}

		ArraySparseMatrix matrix = new ArraySparseMatrix(other.getRowCount(), other.getColumnCount(), elem);

		return matrix.create(sm1,other.getRowCount(),other.getColumnCount(),elem);


	}


	public void put(Entry entry) {
		elements[elemCount++] = entry;
	}

	@Override
	public SparseMatrix multiply(SparseMatrix other) {
		throw new IllegalStateException("Not implemented");
	}

	@Override
	public int getRowCount() {
		return rowCount;
	}

	@Override
	public int getColumnCount() {
		return columnCount;
	}

	@Override
	public int getElemCount() {
		return elemCount;
	}

	@Override
	public boolean equals(Object obj) {
		if (this == obj) return true;
		if (!(obj instanceof ArraySparseMatrix)) return false;
		ArraySparseMatrix other = (ArraySparseMatrix) obj;

		if (rowCount != other.rowCount || columnCount != other.columnCount || elemCount != other.elemCount)
			return false;

		for (int i = 0; i < elements.length; i++) {
			if (!elements[i].equals(other.elements[i])) return false;
		}
		return true;
	}

	@Override
	public String toString() {
		StringBuilder builder = new StringBuilder();
		builder.append(rowCount + "\t" + columnCount + "\t" + elemCount + "\n");
		for (int i = 0; i < elemCount; i ++)
			builder.append(elements[i] + "\n");

		return builder.toString();
	}
}


