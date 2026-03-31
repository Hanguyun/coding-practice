package sample1;

import java.util.Scanner;

public class Code0331_5 {
	static Scanner sc = new Scanner(System.in);
	static int[] score = new int[5];
	static int hap;
	
	static void inputing() {
		int temp;
		
		try {
			for(int i=0; i < score.length; i++) {
				System.out.println((i+1) + "번 점수:");
				temp = sc.nextInt();
				if(temp < 0)
					throw new MinusScoreException("점수는 음수가 없습니다.");
				score[i] = temp;
			}
		} catch(MinusScoreException e) {
			System.out.println(e.getMessage());
			System.out.println("입력을 중단합니다....");
		}
	}
	
	static void processing() {
		for(int temp: score) hap+= temp;
	}
	
	static void printing() {
		System.out.println("점수 합계:" + hap);
	}
	
	public static void main(String[] args) {
		inputing();
		processing();
		printing();

	}

}
