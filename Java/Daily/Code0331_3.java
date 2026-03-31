package sample1;

public class Code0331_3 {
	
	static void divide(int a, int b) throws ArithmeticException {
		System.out.println(a / b);
	}

	public static void main(String[] args) {
		try {
		int num1 = Integer.parseInt(args[0]);
		int num2 = Integer.parseInt(args[1]);
			divide(num1, num2);
		} catch(ArithmeticException e) {
			System.out.println("0으로 나눌 수 없습니다.");
			System.out.println(e.getMessage());
			System.out.println(e.toString());
			e.printStackTrace();
		} catch(ArrayIndexOutOfBoundsException e) {
			System.out.println("인자값이 없습니다.");
		}

	}

}
