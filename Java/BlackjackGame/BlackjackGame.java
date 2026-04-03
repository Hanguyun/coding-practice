import java.util.*;
import java.util.Scanner;

public class Blackjack3 {
	static Scanner sc = new Scanner(System.in); // 사용자에게 입력 받을 Scanner 객체 생성
	
	static List<String> card = new ArrayList<>(); // 기본 카드를 리스트로 세팅
	
	static List<String> ai = new ArrayList<>(); // ai 패를 담을 리스트 생성
	static int aiSum = 0; // ai 합계를 담을 변수 생성
	static int userSum = 0; // user 합계를 담을 변수 생성
	static boolean userBust = false; // user bust 체킹용 불리언
	static boolean aiBust = false; // ai bust 체킹용 불리언
	static String aiPick; // ai가 뽑은 카드를 저장하는 변수
	
	static String userPick;
	static int AChoice;
	static List<String> user = new ArrayList<>(); // user 패를 담을 리스트 생성
	
	public static void applyAiCard() {
		switch(aiPick) {
		case "A":
			if (aiSum >= 10) { // aiSum이 10 이상이면
				aiSum += 1; // +1
				ai.add("A(1)"); // ai List에 삽입
				break;
			}
			else { // aiSum이 10보다 작으면
				aiSum += 11; // +11
				ai.add("A(11)"); // ai List에 삽입
				break;
			}
		case "J","Q","K":
			aiSum += 10; // aiPick에 J,Q,K가 있으면 aiSum에 10 추가
			ai.add(aiPick); // ai List에 삽입
			break;
			
		default:
			int intValue = Integer.parseInt(aiPick);
			aiSum += intValue;
			ai.add(aiPick);
		}
	}
	
	public static void applyUserCard() {
		switch(userPick) {
		case "A":
			while(true) { // 잘못된 입력을 받았을 때 예외 처리
				System.out.println("현재 패: " + user + " 카드 'A'가 뽑혔습니다. 숫자를 선택하세요. 1 OR 11 :");
				AChoice = sc.nextInt(); // 사용자에게 입력 받기
				if (AChoice == 1) { // 사용자에게 입력 받은 값이 1이라면
					userSum += 1; // user 합계에 + 1
					user.add("A(1)"); // A(1)를 삽입
					break;
				}
				else if (AChoice == 11) { // 사용자에게 입력 받은 값이 11이라면
					userSum += 11; // user 합계에 + 11
					user.add("A(11)"); // A(11)를 삽입
					break;
				}
				else {System.out.println("잘못된 번호입니다. 다시 입력하세요.");}
			}
			break;
		
		case "J","Q","K":
			userSum += 10; // userSum에 10 추가
			user.add(userPick);
			break;
		
		default:
			user.add(userPick);
			int intValue = Integer.parseInt(userPick);
			userSum += intValue;
			break;
		}
	}
	
	public static void gameReset() { // 변수 초기화 함수
		ai.clear();
		aiSum = 0;
		aiBust = false;
		
		user.clear();
		userSum = 0;
		userBust = false;
	}
	
	public static void main(String[] args) {
		card.add("A");
		card.add("2");
		card.add("3");
		card.add("4");
		card.add("5");
		card.add("6");
		card.add("7");
		card.add("8");
		card.add("9");
		card.add("10");
		card.add("J");
		card.add("Q");
		card.add("K");
		
		while(true) {
			System.out.println("게임을 시작합니다.");
			System.out.println("--------------------------------------------------");
			
			for(int i =0; i < 2; i++) { // ai 두 장 뽑고 시작
				Collections.shuffle(card); // card 리스트 셔플
				aiPick = card.get(card.size()-1);
				
				applyAiCard();
				}
			
			System.out.println("AI의 패 중 하나는 ["+(ai.get(0))+"]입니다.");
			
			// ----------------------------사용자 동작 로직------------------------------------
			
			for(int i = 0; i < 2; ++i) { // 사용자는 카드를 2개 뽑고 시작하기 때문에 반복문 사용
				Collections.shuffle(card); // card 리스트 셔플
				userPick = card.get(card.size()-1);
				
				applyUserCard();
				
				if (userSum > 21) {
					userBust = true;
					System.out.println("21을 초과하였습니다. 패배!");
					break;
				}
			}
			
			game1 :
			while (!userBust) {
				while(true) {
					System.out.println("현재 당신의 패는 " + user + "입니다. 총합: " + userSum);
					System.out.print("카드를 더 뽑으시겠습니까? (Yes=1 No=0):");
		
					int keepGoing = sc.nextInt();
		
					if (keepGoing == 1) {
						Collections.shuffle(card); // card 리스트 셔플
						userPick = card.get(card.size()-1);
						
						applyUserCard();
						
						if (userSum >= 22) { // userSum을 비교하여 22 이상이라면 패배
							System.out.println("21을 초과하였습니다. 패배!");
							userBust = true;
							break game1;
						}
					}
					else if(keepGoing == 0) { break game1; } // 1이 아니라면 브레이크
					else {System.out.println("잘못된 번호입니다. 다시 입력하세요.");}
				}
			}
// ------------------------------------AI 작동 로직----------------------------------------			
			if(!userBust) {
				for(;aiSum <= 17;) {
					Collections.shuffle(card); // card 리스트 셔플
					aiPick = card.get(card.size()-1);

					applyAiCard();
					
					if(aiSum >= 22) {
						System.out.println("컴퓨터가 21을 초과하였습니다. 승리!");
						aiBust = true;
						break;
					}
				}
			}
// -----------------------------------승부 판정-----------------------------------------
			if(!aiBust && !userBust) {
				if(userSum == aiSum) {
					System.out.println("현재 당신의 패는 "+ user + "입니다. 총합: "+userSum);
					System.out.println("현재 AI의 패는 "+ ai + "입니다. 총합: "+aiSum);
					System.out.println("비겼습니다!");
				}
				else if(userSum > aiSum) {
					System.out.println("현재 당신의 패는 "+ user + "입니다. 총합: "+userSum);
					System.out.println("현재 AI의 패는 "+ ai + "입니다. 총합: "+aiSum);
					System.out.println("이겼습니다!");
				}
				else {
					System.out.println("현재 당신의 패는 "+ user + "입니다. 총합: "+userSum);
					System.out.println("현재 AI의 패는 "+ ai + "입니다. 총합: "+aiSum);
					System.out.println("졌습니다!");
				}		
			}
			
			System.out.println("게임을 계속 하시겠습니까?(yes=1 no=0) :");
			int game = sc.nextInt();
			
			if(game == 0) {
				System.out.println("게임을 종료합니다!");
				break;
			}
		gameReset();
		}
	}
}
