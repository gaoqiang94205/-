package gqSom;

import java.io.BufferedReader;
import java.io.File;
import java.io.FileInputStream;
import java.io.InputStream;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.List;

public class Test_myko {

	public static void main(String[] args) {
		int[] re,re1,re2,ree = new int[8],ree1=new int[8],ree2=new int[8];
		Kohonen_Study koho = new Kohonen_Study(4, 8, 10);
		koho.initi();
		Test_myko te = new Test_myko();

		List<double[]> trainList = te.load_data(); // load数据，将鸢尾花的数据存储到列表当中
		koho.train(trainList); // 用数据对模型开始训练

		System.out.println("this is the firse class:");
		 re = koho.test(new double[] { 5.1, 3.5, 1.4, 0.2 });
		for (int i = 0; i < re.length; i++) {
			System.out.print(re[i] + " ");
			ree[i]=re[i];
		}
		System.out.println();

		System.out.println("this is the second class:");
		  re1 = koho.test(new double[] { 7.0, 3.2, 4.7, 1.4 });
		for (int i = 0; i < re1.length; i++) {
			System.out.print(re1[i] + " ");
			ree1[i]=re1[i];
		}
		System.out.println();

		System.out.println("this is the third class:");
		 re2 = koho.test(new double[] { 7.2, 3.2, 6.0, 1.8 });
		for (int i = 0; i < re2.length; i++) {
			System.out.print(re2[i] + " ");
			ree2[i]=re2[i];
		}
		System.out.println();
		// test for now--------------------------------------
		double[] d1 =  { 6.6, 3.0, 4.4, 1.4 };
		int[] te1 = koho.test(d1);
		int c1 = te.getClass(te1, ree, ree1, ree2);
		te.printClass(d1, c1);
		
		double[] d2 = { 6.9, 3.2, 5.7, 2.3 };
		int[] te2 = koho.test(d2);
		int c2 = te.getClass(te2, ree, ree1, ree2);
		te.printClass(d2, c2);
		
		double[] d3 = { 5.4,3.4,1.5,0.4 };
		int[] te3 = koho.test(d3);
		int c3 = te.getClass(te3, ree, ree1, ree2);
		te.printClass(d3, c3);
	}
	

	public void printClass(double[] test,int c){
			System.out.println("这是鸢尾花的特征：");
			for (int i = 0; i < test.length; i++) {
				System.out.print(test[i] + " ");
			}
			System.out.println("这是第"+c+"种鸢尾花");
	}
	public boolean classequal(int[] cop1,int[] cop2){
		for(int i=0;i<cop1.length;i++){
			if(cop1[i]!=cop2[i])
				return false;
		}
		return true;
	}
	public int getClass(int[] nu,int[] re,int[] re1,int[] re2){
	  if(this.classequal(re, nu))
		  return 1;
	  else if(this.classequal(nu,re1))
		  return 2;
	  else 
		  return 3;
	}

	List<double[]> load_data() {
		File file = new File("D:\\KuGou\\iris.txt");
		InputStream fis;
		List<double[]> list = new ArrayList<double[]>();

		try {
			fis = new FileInputStream(file);
			InputStreamReader isr = new InputStreamReader(fis);
			BufferedReader br = new BufferedReader(isr);
			String str = "";

			while ((str = br.readLine()) != null) {
				String[] data = str.split(";");

				for (int i = 0; i < data.length; i++) {
					String features = data[i];
					String[] fea = features.split(" ");
					double[] detail = new double[4];
					for (int j = 0; j < 4; j++) {
						detail[j] = Double.parseDouble(fea[j]);
					}
					list.add(detail);
				}
			}
			return list;
		} catch (Exception e) {
			e.printStackTrace();
			return null;
		}

	}

}