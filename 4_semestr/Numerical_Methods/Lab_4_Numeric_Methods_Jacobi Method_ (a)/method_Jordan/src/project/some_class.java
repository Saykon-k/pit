package project;

import java.util.ArrayList;

public class some_class {

	public static void main(String[] args) {
		double i[][] ={{5,1,2}, {1, 4, 1}, {2, 1, 3}};
		System.out.println("Исходная матрица");
		printmatrix(i);
		System.out.println("Допустимая погрешность 0.003\n");
		System.out.println("старт программы");
		methodIkobi(i,0.003);
	}
	public static double[][] transpose(double arr[][]){
	    int m = arr.length;
	    int n = arr[0].length;
	    double ret[][] = new double[n][m];

	    for (int i = 0; i < m; i++) {
	        for (int j = 0; j < n; j++) {
	            ret[j][i] = arr[i][j];
	        }
	    }

	    return ret;
	}
    public static double[][] multiplyByMatrix(double[][] m1, double[][] m2) {
        int m1ColLength = m1[0].length; 
        int m2RowLength = m2.length;    
        if(m1ColLength != m2RowLength) return null;
        int mRRowLength = m1.length;    
        int mRColLength = m2[0].length; 
        double[][] mResult = new double[mRRowLength][mRColLength];
        for(int i = 0; i < mRRowLength; i++) {        
            for(int j = 0; j < mRColLength; j++) {    
                for(int k = 0; k < m1ColLength; k++) { 
                    mResult[i][j] += m1[i][k] * m2[k][j];
                }
            }
        }
        return mResult;
    }

	public static void printmatrix(double matr[][]) {
		for(int i = 0; i < matr.length;i++) {
			for(int j = 0; j < matr.length;j++) {
				System.out.print(matr[i][j]+" ");
			}
			System.out.println();
		}
	}
	public static int[] find_i_j(double matr[][]) {
		double first = matr[0][1];
		int i_j []= {0,1};
		for(int i = 0; i < matr.length; i++) 
			for(int j = i+1; j<matr.length;j++ ) {
				if(first < matr[i][j]) { 
					i_j[0]=i;
					i_j[1]=j;
				}
			}

		return i_j;
	}
	public static double approximal(double matr[][]) {
		double res = 0;
		for(int i = 0; i < matr.length; i++) 
			for(int j = i+1; j<matr.length;j++ ) res+=matr[i][j]*matr[i][j];
		return  (double)Math.round(Math.sqrt(res) * 10000d) / 10000d;
	}
	public static double[][] around(double matrix_res[][]) {
		for(int i = 0; i < matrix_res.length; i++)
			for(int j = 0 ; j < matrix_res.length;j++) matrix_res[i][j] = (double)Math.round(matrix_res[i][j] * 1000000d) / 1000000d;
				return matrix_res;
	}
	public static void fill_rotate_matrix(double rotate_matrix[][],int i_j[] ,double fi) {
		for(int i = 0; i < rotate_matrix.length;i++) rotate_matrix[i][i] = 1;
		rotate_matrix[i_j[0]][i_j[0]] =  (double)Math.round(Math.cos(fi) * 1000000d) / 1000000d;
		rotate_matrix[i_j[1]][i_j[1]] = (double)Math.round(Math.cos(fi) * 1000000d) / 1000000d;
		rotate_matrix[i_j[0]][i_j[1]] =  (double)Math.round(-Math.sin(fi) * 1000000d) / 1000000d;
		rotate_matrix[i_j[1]][i_j[0]] =  (double)Math.round(Math.sin(fi) * 1000000d) / 1000000d;

	}
	public static void methodIkobi(double matr[][],double eps) {
		ArrayList<double [][]> matrV = new ArrayList();
		double error=eps+1;
		for(int i = 0; error > eps ; i++) {
		System.out.println(i+" шаг");
		int found_i_j[] = find_i_j(matr);
		System.out.println("максимальный элемент: " + matr[found_i_j[0]][found_i_j[1]]);
		double rotate_matrix[][] = new double [matr.length][matr.length];
		double fi = 0.5*Math.atan(2*matr[found_i_j[0]][found_i_j[1]]/(matr[found_i_j[0]][found_i_j[0]]-matr[found_i_j[1]][found_i_j[1]]));
		fill_rotate_matrix(rotate_matrix,found_i_j,fi);
		matrV.add(rotate_matrix);
		System.out.println("матрица вращения: ");
		printmatrix(rotate_matrix);
		System.out.println();

		
		matr = around(multiplyByMatrix(multiplyByMatrix(transpose(rotate_matrix),matr),rotate_matrix));
		System.out.println("матрица после перемножения: ");
		printmatrix(matr);
		System.out.println("погрешность " + approximal(matr));
		error = approximal(matr);
		System.out.println();
		//}while(error < eps);
		}
		System.out.println("результат вычислений: ");
		printmatrix(matr);
		System.out.println("собственные значения: ");
		System.out.println("");
		for(int i = 0; i < matr.length;i++) System.out.println("собственное число матрицы лямба с индексом "+i+" = "+matr[i][i]);
		System.out.println();

		System.out.println("После того,как были найдены все значения находим собственные вектора путем перемножения всех матриц вращения, которые получились(сохраняются в список matrV)");
		double res_Vector[][] = new double[matr.length][matr.length];
		res_Vector = matrV.get(0);
		for(int i = 1; i < matrV.size();i++) res_Vector = multiplyByMatrix(res_Vector,matrV.get(i));
		printmatrix(res_Vector);
		
		System.out.println("");
}
}