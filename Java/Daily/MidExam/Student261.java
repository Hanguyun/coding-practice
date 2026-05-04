package mid_exam;

public class Student261 {
	String name;
	private int num, kor, eng, math, hap;
	private double avg;
	
	Student261(int n, String name, int val1, int val2, int val3) {
	this.name = name;
	num = n; kor = val1; eng = val2; math = val3;
	}
	
	public String name() {
	return name;
	}
	public int getNum() {
	return num;
	}
	public int getKor() {
	return kor;
	}
	public int getEng() {
	return eng;
	}
	public int getMath() {
	return math;
	}
	public int getHap() {
	return hap;
	}
	public double getAvg() {
	return avg;
	}
	
	public void calData() { // 합계, 평균 계산하는 함수
	hap = kor + eng + math;
	avg = (double)hap/3;
	}
		

}
