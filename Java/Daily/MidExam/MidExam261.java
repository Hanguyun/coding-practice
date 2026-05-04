package mid_exam;
import java.util.*;

public class MidExam261 {
	static Scanner sc = new Scanner(System.in); // 스캐너 객체 생성
	static int su; // 학생수를 입력 받을 변수 지정
	static Student261[] std; // student261 객체 생성
	
	static public void StudentInput() {
		System.out.print("학생수를 입력하세요. :"); 
		su = sc.nextInt(); // 학생수 입력 받기
		 std = new Student261[su]; // 학생수 입력 받고 배열 생성? 확장?
		 
		// https://blog.naver.com/jhj9512z/221935954031 참고
		for (int i = 0; i < std.length; i++) { // i가 배열의 크기 만큼 반복
			System.out.println((i+1) + "번 학생");
			
			System.out.print("번호: ");
			int num = sc.nextInt();
			
			System.out.print("이름: ");
			String name = sc.next();
			
			System.out.print("국어: ");
			int  kor = sc.nextInt();
			
			System.out.print("영어: ");
			int eng = sc.nextInt();
			
			System.out.print("수학: ");
			int math = sc.nextInt();
			
			std[i] = new Student261(num, name, kor, eng, math);
			// std 객체에 [i]에 학생 정보가 들어감
		}
	}

	static public void calculate() { // 합계와 평균을 계산
		for (Student261 temp : std)
			temp.calData();
	}

	static public int rank() { // 1등을 찾는 함수
		int num, index;
		for (num = std[0].getNum(), index = 1; index < std.length; index++) {
			if (std[num].getHap() < std[index].getHap())
				num = std[index].getNum();
		}
		return num;
	}

	static public void sorting() { // 합계 기준으로 내림차순으로 정렬하는 함수
		for (int i = 0; i < std.length - 1; i++) {
			int max = i;
			for (int j = i + 1; j < std.length - 1; j++) {
				if (std[max].getHap() < std[j].getHap())
					max = j;
			}
			Student261 temp = std[i];
			std[i] = std[max];
			std[max] = temp;
		}
	}

	public static void printInfo(int type) { // 출력 담당 함수
		String title, bar;
		if (type == 1) {
			title = "번호\t이름\t국어\t영어\t수학";
			bar = "-----------------------------------";
		} else {
			title = "번호\t이름\t국어\t영어\t수학\t합계\t평균";
			bar = "-------------------------------------------------";
		}

		System.out.println(title);
		System.out.println(bar);

		for (Student261 temp : std) {
			System.out.print(temp.getNum() + "\t");
			System.out.print(temp.name() + "\t");
			System.out.print(temp.getKor() + "\t");
			System.out.print(temp.getEng() + "\t");

			if (type == 1) {
				System.out.print(temp.getMath() + "\n");
			} else {
				System.out.print(temp.getMath() + "\t");
				System.out.print(temp.getHap() + "\t");
				System.out.print(temp.getAvg() + "\n");
			}
		}

		System.out.println(bar);
	}

	public static void main(String[] args) {
		StudentInput();
		calculate();
		System.out.println("********** 원본 데이터 **********");
		printInfo(1);
		rank();
		sorting();
		System.out.println("\n\n\n********** 성적표 **********");
		printInfo(2);
		System.out.println("1등 이름: " + std[0].name + "(번호: " + std[0].getNum() + ")");
	}
}
