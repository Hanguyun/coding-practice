package BlackjackGame;

import java.util.*;

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
        user.add(PickedUser); // 위에 만들었던 변수 PickedUser에 저잗되어 있는 카드를 저장
    }

    if (userCount.contains("J")) {
            // 일단 J, Q, K가 있는지 확인하고 삭제 후 추가
    }

        System.out.println("당신의 패는" + user +"점수는"+ userCount +"입니다.");
    }
}
