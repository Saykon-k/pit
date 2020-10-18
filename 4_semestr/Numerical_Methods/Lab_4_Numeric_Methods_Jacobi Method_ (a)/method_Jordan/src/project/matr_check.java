package project;

public class matr_check {

	public static void main(String[] args) {
		int i[][] ={{4, 2, 1}, {2, 5, 3}, {1, 3, 6}};
		int i1 [][] = new int[i.length][i.length];
		printmatr(i1);
	}
	public static void printmatr(int matr[][]) {
		for(int i = 0; i < matr.length;i++) {
			for(int j = 0; j < matr.length;j++) {
				System.out.print(matr[i][j]+" ");
			}
			System.out.println();
		}
	}
}
