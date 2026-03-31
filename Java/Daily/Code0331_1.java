package sample1;
import java.util.Scanner;

public class Code0331_1 {

	static int hap;
	static int[] score;

	static int[] inputData() {
		Scanner sc = new Scanner(System.in);
		System.out.print("학생 수: ");
		
		int su = sc. nextInt();
		score= new int[su];

		for(int i = 0 ; i < su; i++) {
			System.out.print((i+1) + "번 점수: ");
			score[i] = sc.nextInt();
		}
		sc.close();
		return score;

	}
	static void sum() {
		for(int temp: score)
			hap += temp;
		return ;
	}
	
	static double average() {
		return (double)hap/score.length;
	}

	public static void main(String[] args) {
		double avg = 0.0;
		
		score = inputData();
		sum();
		avg = average();
		System.out.println("합계는 " + hap + "점이고, 평균은 " + avg + "점 입니다. ");
	}

}
