import java.util.*;

public class BlackjackGame {

	public static void main(String[] args) {
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
		card.add("J");
		card.add("Q");
		card.add("K");
		
		System.out.println("게임을 시작합니다.");
		System.out.println("--------------------------------------------------");
		
		Scanner sc = new Scanner(System.in); // 사용자에게 입력 받을 Scanner 객체 생성
		List<String> ai = new ArrayList<>(); // AI 덱을 나타낼 List 생성
		List<Integer> aiCount = new ArrayList<>(); // AI 카드 합계를 나타낼 List 생성
		List<String> user = new ArrayList<>(); // USER 덱을 나타낼 List 생성
		List<Integer> userCount = new ArrayList<>(); // USER 카드 합계를 나타낼 List 생성
		List<String> tempAJQK = new ArrayList<>(); // 지운 A,J,Q,K를 담았다가 다시 옮기는 리스트
		
		Collections.shuffle(card); // card 리스트 셔플
		Random r = new Random(); // 난수를 만들어주는 객체 r 생성
		
		String aiPick = card.get(r.nextInt(card.size()));
		// card.size() card에 들어있는 원소 개수. 예를 들어 10개면 size()는 10.
	    // r.nextInt(card.size(()) 0 이상 ~ card.size()-1 이하 범위의 랜덤 정수 1개를 생성. 예) size가 10이면 0~9 중 하나.
	    // card.get(랜덤인덱스) card에 랜덤 인덱스 위치의 원소를 가져옴.
	    // character aiPick = ... 뽑힌 값을 aiPick에 저장.
		
		ai.add(aiPick); // card 랜덤으로 뽑은 카드를 ai덱에 삽입
		System.out.println("AI의 패 중 하나는 "+ai+"입니다.");
		
		for(int i = 0; i < 2; ++i) { // user는 기본 2장 뽑고 시작 그래서 반복문 사용
			Collections.shuffle(card); // card 리스트 셔플
			String userPick = card.get(r.nextInt(card.size())); // card 리스트에서 랜덤 추출 후 userPick에 저장
			user.add(userPick);
			
			if(!userPick.equals("A") && !userPick.equals("J") && !userPick.equals("Q") && !userPick.equals("K")) {
				int intValue = Integer.parseInt(userPick);
				userCount.add(intValue);
			}			
		}
		
		if(user.contains("A")) { // A가 뽑혔을때 숫자로 변환
			System.out.println("카드 'A'가 뽑혔습니다. 숫자를 선택하세요. 1 OR 11 :");
			int AChoice = sc.nextInt(); // 사용자에게 입력 받기
			
			if (AChoice == 1) {
				user.remove("A");
				tempAJQK.add("A(1)");
				userCount.add(1);
			} else if (AChoice == 11) {
				user.remove("A");
				tempAJQK.add("A(11)");
				userCount.add(11);
			}
		}
		
		user.addAll(tempAJQK); // 리스트 합치기
		
		tempAJQK.clear(); // 리스트 초기화
		
		for (int i = 0; i < 2; ++i) { // J,Q,K가 두 개가 나올 수 있으니 for문으로 두 번 실행
	        if (user.contains("J")) { // userCount에 J,Q,K가 있으면 삭제하고 10 추가
	        	user.remove("J");
	        	tempAJQK.add("J");
	            userCount.add(10);
	        } else if (user.contains("Q")) {
	        	user.remove("Q");
	        	tempAJQK.add("Q");
	            userCount.add(10);
	        } else if (user.contains("K")) {
	        	user.remove("K");
	        	tempAJQK.add("K");
	            userCount.add(10);
	        }
	    }
		
		user.addAll(tempAJQK);
		
		int userSum = userCount.stream()
				.mapToInt(Integer::intValue)
				.sum();
		
		System.out.println("현재 당신의 패는 " + user + "입니다. 총합: " + userSum);
	}	
		
}	
