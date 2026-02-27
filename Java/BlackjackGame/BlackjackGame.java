package BlackjackGame;

import java.util.*;
import java.util.Scanner;

public static int userSum(List<Object> userCount) {
    return userCount.stream()
            .mapToInt(Object::IntValue)
            .sum();

}

public class BlackjackGame {
    public static void main(String[] args) {
        List<Object> card = new ArrayList<>(); // 기본 덱을 리스트로 세팅
        card.add("A"); // List<Object>는 다양한 데이터 타입을 혼합하여
        card.add(2);   // 저장이 가능하다.
        card.add(3);
        card.add(4);
        card.add(5);
        card.add(6);
        card.add(7);
        card.add(8);
        card.add(9);
        card.add(10);
        card.add("J");
        card.add("Q");
        card.add("K");

    System.out.println("게임을 시작합니다.");
    System.out.println("---------------------------------------------");

    Collections.shuffle(card); // List card를 셔플

    Random r = new Random(); // 난수를 만들어주는 객체 r 생성
    Object PickedAi = card.get(r.nextInt(card.size()));
    // card.size() card에 들어있는 원소 개수. 예를 들어 10개면 size()는 10.
    // r.nextInt(card.size(()) 0 이상 ~ card.size()-1 이하 범위의 랜덤 정수 1개를 생성. 예) size가 10이면 0~9 중 하나.
    // card.get(랜덤인덱스) card에 랜덤 인덱스 위치의 원소를 가져옴.
    // Object PickedAi = ... 뽑힌 값을 PickedAi에 저장.

    List<Object> ai = new ArrayList<>(); // ai 덱에 삽입할 카드를 위해 ai List 생성
    ai.add(PickedAi); // 위에 만들었던 변수 PickedAi에 저장되어 있는 카드를 저장

    System.out.println("AI의 패 중 하나는" + ai + "입니다.");

    List<Object> user = new ArrayList<>(); // user 덱에 삽입할 카드를 위해 user List 생성

    List<Object> userCount = new ArrayList<>(); // user의 덱의 점수를 계산하기 위해 userCount List 생성

    for (int i = 0; i < 2; i++) {
        Object PickedUser = card.get(r.nextInt(card.size())); // card에서 랜덤 인덱스 위치의 원소를 가져와서 변수 PickedUser에 저장
        user.add(PickedUser); // 위에 만들었던 변수 PickedUser에 저장되어 있는 카드를 저장
        userCount.add(PickedUser); // 위에 만들었던 변수 PickedUser에 저잗되어 있는 카드를 저장
    }

    Scanner sc = new Scanner(System.in); // A가 1 or 10으로 변한하기 위해 사용자에게 입력 받을 Scanner 객체 생성

    for (int i = 0; i < 2; ++i) { // A가 두 개가 나올 수 있으니 for문으로 두 번 실행
        if (user.contains("A")) { // user 패에 A가 뽑히면 조건 실행
            System.out.print("A가 뽑혔습니다. 숫자를 선택하세요 1 or 10 :");
            int Achoice = sc.nextInt(); // 사용자에게 입력 받기

            if (Achoice == 1) {
                user.remove("A");
                user.add(1);
                userCount.remove("A");
                userCount.add(1);
            } else {
                user.remove("A");
                user.add(10);
                userCount.remove("A");
                userCount.add(10);
            }
        }
    }

    for (int i = 0; i < 2; ++i) { // J,Q,K가 두 개가 나올 수 있으니 for문으로 두 번 실행
        if (userCount.contains("J")) { // userCount에 J,Q,K가 있으면 삭제하고 10 추가
            userCount.remove("J");
            userCount.add(10);
        } else if (userCount.contains("Q")) {
            userCount.remove("Q");
            userCount.add(10);
        } else if (userCount.contains("K")) {
            userCount.remove("K");
            userCount.add(10);
        }
    }

        System.out.println("당신의 패는" + user +"점수는"+ userCount +"입니다.");
    }
}
