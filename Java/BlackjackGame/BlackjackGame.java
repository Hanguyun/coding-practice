import java.util.*;

public class BlackjackGame {
//	public static void Sum(int userSum, List<Integer> userCount) { // userCount에 있는 정수의 합계를 구하는 함수
//		userSum = userCount.stream()
//				.mapToInt(Integer::intValue)
//				.sum();
	
//	 public static void addA(String userPick,List<Integer> userCount) {
//		 if(!userPick.equals("A") && !userPick.equals("J") && !userPick.equals("Q") &&
//				 !userPick.equals("K")) { int intValue = Integer.parseInt(userPick);
//				 userCount.add(intValue); } 
//		 }

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

		Collections.shuffle(card); // card 리스트 셔플
		Random r = new Random(); // 난수를 만들어주는 객체 r 생성

		String aiPick = card.get(r.nextInt(card.size()));
		// card.size() card에 들어있는 원소 개수. 예를 들어 10개면 size()는 10.
		// r.nextInt(card.size(()) 0 이상 ~ card.size()-1 이하 범위의 랜덤 정수 1개를 생성. 예) size가
		// 10이면 0~9 중 하나.
		// card.get(랜덤인덱스) card에 랜덤 인덱스 위치의 원소를 가져옴.
		// character aiPick = ... 뽑힌 값을 aiPick에 저장.

		ai.add(aiPick); // card 랜덤으로 뽑은 카드를 ai덱에 삽입
		System.out.println("AI의 패 중 하나는 " + ai + "입니다.");

		// ---------------------------------user
		// 동작-------------------------------------------------

		for (int i = 0; i < 2; ++i) { // user는 기본 2장 뽑고 시작 그래서 반복문 사용
			Collections.shuffle(card); // card 리스트 셔플
			String userPick = card.get(r.nextInt(card.size())); // card 리스트에서 랜덤 추출 후 userPick에 저장
			user.add(userPick);

			if (user.get(user.size() - 1).equals("A")) { // 마지막 index에 A가 뽑혔을때 숫자로 변환
				System.out.println("카드 'A'가 뽑혔습니다. 숫자를 선택하세요. 1 OR 11 :");
				int AChoice = sc.nextInt(); // 사용자에게 입력 받기

				if (AChoice == 1) {
					user.remove("A");
					user.add("A(1)");
					userCount.add(1);
				} else if (AChoice == 11) {
					user.remove("A");
					user.add("A(11)");
					userCount.add(11);
				}
			}
			if (user.get(user.size() - 1).equals("J")) { // userCount에 J,Q,K가 있으면 Count에 10 추가
				userCount.add(10);
			} else if (user.get(user.size() - 1).equals("Q")) {
				userCount.add(10);
			} else if (user.get(user.size() - 1).equals("K")) {
				userCount.add(10);
			}
			// userPick이 A,J,Q,K가 아니라 숫자 String이면 Int로 바꾼 다음 userCount 리스트에 삽입
			if (!userPick.equals("A") && !userPick.equals("J") && !userPick.equals("Q") && !userPick.equals("K")) {
				int intValue = Integer.parseInt(userPick);
				userCount.add(intValue);
			}
		}

		int userSum = userCount.stream() // userCount에 있는 정수의 합계를 구하는 코드
				.mapToInt(Integer::intValue).sum();

		while (true) {
			if (userSum == 21) {
				System.out.println("현재 당신의 패는 "+ user + "입니다. 총합: "+userSum);
				break;
			}
			else if (userSum >= 22) { // userSum을 비교하여 22 이상이라면 패배
				System.out.println("21을 초과하였습니다. 패배!");
				break;
			}
			
			System.out.println("현재 당신의 패는 " + user + "입니다. 총합: " + userSum);
			System.out.print("카드를 더 뽑으시겠습니까? 1 = Yes 0 = No :");

			int keepGoing = sc.nextInt();

			if (keepGoing == 1) {
				String userPick = card.get(r.nextInt(card.size()));
				user.add(userPick);
				// userPick이 A,J,Q,K가 아니라 숫자 String이면 Int로 바꾼 다음 userCount 리스트에 삽입
				if (!userPick.equals("A") && !userPick.equals("J") && !userPick.equals("Q") && !userPick.equals("K")) {
					int intValue = Integer.parseInt(userPick);
					userCount.add(intValue);
				}
				if (user.get(user.size() - 1).equals("A")) { // 마지막 index에 A가 뽑혔을때 숫자로 변환
					System.out.println("카드 'A'가 뽑혔습니다. 숫자를 선택하세요. 1 OR 11 :");
					int AChoice = sc.nextInt(); // 사용자에게 입력 받기

					if (AChoice == 1) {
						user.remove("A");
						user.add("A(1)");
						userCount.add(1);
					}
					else if (AChoice == 11) {
						user.remove("A");
						user.add("A(11)");
						userCount.add(11);
					}
				}
				if (user.get(user.size() - 1).equals("J")) { // userCount에 J,Q,K가 있으면 Count에 10 추가
					userCount.add(10);
				} else if (user.get(user.size() - 1).equals("Q")) {
					userCount.add(10);
				} else if (user.get(user.size() - 1).equals("K")) {
					userCount.add(10);
				}
				userSum = userCount.stream() // userCount에 있는 정수의 합계를 구하는 코드
						.mapToInt(Integer::intValue)
						.sum();
			}
			else { break; }
			}
		// -------------------------AI 작동---------------------------------
		while(true) {
			aiPick = card.get(r.nextInt(card.size()));
			ai.add(aiPick);
			// userPick이 A,J,Q,K가 아니라 숫자 String이면 Int로 바꾼 다음 userCount 리스트에 삽입
			if (!aiPick.equals("A") && !aiPick.equals("J") && !aiPick.equals("Q") && !aiPick.equals("K")) {
				int intValue = Integer.parseInt(aiPick);
				aiCount.add(intValue);
			}
			if (ai.get(ai.size() - 1).equals("A")) { // 마지막 index에 A가 뽑혔을때 숫자로 변환
				System.out.println("카드 'A'가 뽑혔습니다. 숫자를 선택하세요. 1 OR 11 :");
				int AChoice = sc.nextInt(); // 사용자에게 입력 받기

				if (AChoice == 1) {
					ai.remove("A");
					ai.add("A(1)");
					aiCount.add(1);
				}
				else if (AChoice == 11) {
					ai.remove("A");
					ai.add("A(11)");
					aiCount.add(11);
				}
			}
			if (ai.get(ai.size() - 1).equals("J")) { // userCount에 J,Q,K가 있으면 Count에 10 추가
				aiCount.add(10);
			} else if (ai.get(ai.size() - 1).equals("Q")) {
				userCount.add(10);
			} else if (user.get(user.size() - 1).equals("K")) {
				userCount.add(10);
			}
			userSum = userCount.stream() // userCount에 있는 정수의 합계를 구하는 코드
					.mapToInt(Integer::intValue)
					.sum();
		}
		
		// -------------------------게임 승패 판정-----------------------------
		sc.close();
	}
}
