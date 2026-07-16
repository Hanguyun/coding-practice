package Gimal;

import java.util.*;

public class LectureRoomMain {
	static Scanner sc = new Scanner(System.in);
	static ArrayList<LectureRoom> roomList = new ArrayList<>();
	
	public static void main(String[] args) {
		roomList.add(new TheoryRoom("A101", 40, "1대학관", "IT학과"));
		roomList.add(new TheoryRoom("B201", 30, "2대학관", "기계학과"));
		roomList.add(new TheoryRoom("LAB301", 30, "3대학관", "IT학과", "프로그래밍 실습", "PC 30대"));

		while(true) {
			System.out.println("\n===== 강의실 관리 프로그램 =====");
			System.out.println("1. 강의실 예약");
			System.out.println("2. 강의실 예약현황");
			System.out.println("3. 강의실 예약 취소");
			System.out.println("4. 강의실 추가");
			System.out.println("5. 강의실 삭제");
			System.out.println("6. 강의실 목록");
			System.out.println("7. 종료");
			System.out.print("메뉴 선택:");
			
		int meun = Integer.parseInt(sc.nextLine());
		switch (meun) {
			case 1: reserveRoom();		break;
			case 2: showReservedRooms();		break;
			case 3: cancelRoom();		break;
			case 4: addRoom();		break;
			case 5: deleteRoom();		break;
			case 6: showRoomList();		break;
			case 7: System.out.println("프로그램 종료");	System.exit(0);
			default: System.out.println("잘못된 입력입니다.");
			}
		}
	}
	
	static void reserveRoom() {
		
	}
	
	static void showReservedRooms() {
		
	}
	
	static void cancelRoom() {
		
	}
	
	static void addRoom() {
		
	}
	
	static void deleteRoom() {
		
	}
	
	static void showRoomList() {
		
	}
}
