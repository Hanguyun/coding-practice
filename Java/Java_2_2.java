// 정수를 입력받아 누가 더 큰 수 인지 구별하는 프로그램
import java.util.Scanner;

public class Main {
  public static void main(String[] args) {
    try (Scanner sc = new Scanner(System.in)) {

      System.out.println("Enter the first integer");
      int a = sc.nextInt();
    
      System.out.println("Enter the second integer");
      int b = sc.nextInt();

      if (a==b) {
        System.out.println("The numbers are the same.");
        } else if (a>b) {
        System.out.println("A is greater than B.");
        } else {
        System.out.println("B is greater than A.");
      }
    }
  }
}
