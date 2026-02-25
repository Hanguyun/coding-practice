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

    List<Object> ai = new ArrayList<>();
    ai.add();

    List<Object> user = new ArrayList<>();


    System.out.println(card);
    }
}
