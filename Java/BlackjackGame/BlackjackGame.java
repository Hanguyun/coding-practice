import java.util.*;
import java.util.Scanner;

public class Blackjack2 {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in); // 사용자에게 입력 받을 Scanner 객체 생성
		Random r = new Random(); // 난수를 만들어주는 객체 r 생성
		
		List<String> card = new ArrayList<>(); // 기본 카드를 리스트로 세팅
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
			int game = 1; // game을 지속하기 위한 변수 지정
			
			System.out.println("게임을 시작합니다.");
			System.out.println("--------------------------------------------------");
			
			List<String> ai = new ArrayList<>(); // ai 패를 담을 리스트 생성
			int aiSum = 0; // ai 합계를 담을 변수 생성
			Boolean aiBust = false;
			String aiPick;
			
			List<String> user = new ArrayList<>(); // user 패를 담을 리스트 생성
			String userPick; // user가 뽑은 카드를 담을 변수
			int userSum = 0; // user 합계를 담을 변수 생성
			Boolean userBust = false; 
			
			for(int i =0; i < 2; i++) { // Ai도 두 장 뽑고 시작
				Collections.shuffle(card); // card 리스트 셔플
				
				aiPick = card.get(r.nextInt(card.size()));
				 /*card.size() card에 들어있는 원소 개수. 예를 들어 10개면 size()는 10.
			     r.nextInt(card.size(()) 0 이상 ~ card.size()-1 이하 범위의 랜덤 정수 1개를 생성. 예) size가 10이면 0~9 중 하나.
			     card.get(랜덤인덱스) card에 랜덤 인덱스 위치의 원소를 가져옴.
			     Object aiPick = ... 뽑힌 값을 aiPick에 저장. */
				ai.add(aiPick); // card 랜덤으로 뽑은 카드를 ai덱에 삽입
				
				if (aiPick.equals("A")) { // aiPick이 A라면 실행
					if (aiSum > 10) { // aiSum이 10보다 크면
						aiSum += 1; // +1
					}
					else if (aiSum <= 10) { // aiSum이 10보다 작으면
						aiSum += 11; // +11
					}
				}
				else if (aiPick.equals("J") || aiPick.equals("Q") || aiPick.equals("K")) {
					aiSum += 10; // aiPick에 J,Q,K가 있으면 aiSum에 10 추가
				}
				
				else{ // aiPick이 A,J,Q,K가 아니라 숫자 String이면 Int로 바꾼 다음 userCount 리스트에 삽입
					int intValue = Integer.parseInt(aiPick);
					aiSum += intValue;
				}
			}
			
			System.out.println("AI의 패 중 하나는 ["+(ai.get(0))+"]입니다."); // ai 패 두 개 중 하나만 출력
			
			// ----------------------------사용자 동작 로직------------------------------------
			
			for(int i = 0; i < 2; ++i) { // 사용자는 카드를 2개 뽑고 시작하기 때문에 반복문 사용
				Collections.shuffle(card); // card 리스트 셔플
				userPick = card.get(r.nextInt(card.size()));
				user.add(userPick);
				
				if (userPick.equals("A")) { // 마지막 index에 A가 뽑혔을때 숫자로 변환
					System.out.println("카드 'A'가 뽑혔습니다. 숫자를 선택하세요. 1 OR 11 :");
					int AChoice = sc.nextInt(); // 사용자에게 입력 받기
	
					if (AChoice == 1) { // 사용자에게 입력 받은 값이 1이라면
						user.remove("A");
						user.add("A(1)"); // A(1)을 넣고
						userSum += 1; // user 합계에 + 1
					} else if (AChoice == 11) { // 사용자에게 입력 받은 값이 11이라면
						user.remove("A");
						user.add("A(11)"); // A(11)을 넣고
						userSum += 11; // user 합계에 + 11
					}
				}
				
				else if (userPick.equals("J") || userPick.equals("Q") || userPick.equals("K")) { 
					userSum += 10; // userSum에 10 추가
				}
				
				else { // userPick이 A,J,Q,K가 아니라 숫자 String이면 Int로 바꾼 다음 userCount 리스트에 삽입
					int intValue = Integer.parseInt(userPick);
					userSum += intValue;
				}
			}
			while (true) {
				System.out.println("현재 당신의 패는 " + user + "입니다. 총합: " + userSum);
				System.out.print("카드를 더 뽑으시겠습니까? (Yes=1 No=0):");
	
				int keepGoing = sc.nextInt();
	
				if (keepGoing == 1) {
					Collections.shuffle(card); // card 리스트 셔플
					userPick = card.get(r.nextInt(card.size()));
					user.add(userPick);
					
					if (userPick.equals("A")) { // userPick이 A라면
						System.out.println("카드 'A'가 뽑혔습니다. 숫자를 선택하세요. 1 OR 11 :");
						int AChoice = sc.nextInt(); // 사용자에게 입력 받기
	
						if (AChoice == 1) { // 사용자에게 입력 받은 값이 1이라면
							user.remove("A"); // A를 지우고
							user.add("A(1)"); // A(1)을 넣고
							userSum += 1; // user 합계에 + 1
						} else if (AChoice == 11) { // 사용자에게 입력 받은 값이 11이라면
							user.remove("A"); // A를 지우고
							user.add("A(11)"); // A(11)을 넣고
							userSum += 11; // user 합계에 + 11
						}
						else {
							System.out.println("잘못된 번호를 입력하셨습니다.");
						}
					}
					
					else if (userPick.equals("J") || userPick.equals("Q") || userPick.equals("K")) {
						userSum += 10; // userPick에 J,Q,K가 있으면 userSum에 10 추가
					}
					
					else { // userPick이 A,J,Q,K가 아니라 숫자 String이면 Int로 바꾼 다음 userCount 리스트에 삽입
						int intValue = Integer.parseInt(userPick);
						userSum += intValue;
					}
					if (userSum >= 22) { // userSum을 비교하여 22 이상이라면 패배
						System.out.println("21을 초과하였습니다. 패배!");
						userBust = true;
						break;
					}
				}
				else { break; } // 1이 아니라면 브레이크
			}
// ------------------------------------AI 작동 로직----------------------------------------			
			if(!userBust) {
				while(aiSum < 17) {
					aiPick = card.get(r.nextInt(card.size()));
					ai.add(aiPick);
					
					if (aiPick.equals("A")) { // aiPick이 A라면 실행
						if (aiSum > 10) { // aiSum이 10보다 크면
							aiSum += 1; // +1
						}
						else if (aiSum <= 10) { // aiSum이 10보다 작으면
							aiSum += 11; // +11
						}
					}
					else if (aiPick.equals("J") || aiPick.equals("Q") || aiPick.equals("K")) {
						aiSum += 10; // aiPick에 J,Q,K가 있으면 aiSum에 10 추가
					}
					
					else{ // aiPick이 A,J,Q,K가 아니라 숫자 String이면 Int로 바꾼 다음 userCount 리스트에 삽입
						int intValue = Integer.parseInt(aiPick);
						aiSum += intValue;
					}
					if(aiSum >= 22) {
						System.out.println("컴퓨터가 21을 초과하였습니다. 승리!");
						aiBust = true;
						break;
					}
					else if(aiSum >= 17) {break;}
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
			System.out.println("계임을 계속 하시겠습니까?(yes=1 no=0) :");
			game = sc.nextInt();
			
			if(game == 0) {
				System.out.println("게임을 종료합니다!");
				break;
			}
		}
	sc.close();
	}
}
