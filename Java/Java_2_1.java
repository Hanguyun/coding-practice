// 입력을 받아 더하기, 빼기, 곱하기, 나누기, 나머지 구하고 출력

import java.util.Scanner;

public class Main {
  public static void main(String[] args) {
    try (Scanner sc = new Scanner(System.in)) {

      int a = sc.nextInt();
      int b = sc.nextInt();

      System.out.println(a+b);
      System.out.println(a-b);
      System.out.println(a*b);
      System.out.println(a/b);
      System.out.println(a%b);

      sc.close();
    }
  }
}
