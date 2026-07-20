package Gimal;

import java.util.*;

public class LectureRoomMain {
	static Scanner sc = new Scanner(System.in);
	static ArrayList<LectureRoom> roomList = new ArrayList<>();
	
	public static void main(String[] args) {
		roomList.add(new TheoryRoom("A101", 40, "1대학관", "IT학과"));
		roomList.add(new TheoryRoom("B201", 30, "2대학관", "기계학과"));
		roomList.add(new PracticeRoom("LAB301", 30, "3대학관", "IT학과", "프로그래밍 실습", "PC 30대"));

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
			
		int menu = Integer.parseInt(sc.nextLine());
		switch (menu) {
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
		System.out.print("예약할 강의실 번호:");
		String roomNo = sc.nextLine();
		
		for(LectureRoom lr : roomList) {
			if(lr.getRoomNo().equalsIgnoreCase(roomNo)) {
				if(lr.isReserved()) {
					System.out.println("이미 예약된 강의실입니다.");
				}
				else {
				lr.setReserved(true); // setReserved(true) 예약 상태를 true로 변경
				System.out.println(roomNo + " 강의실 예약 완료");
				}
				return;
			}
		}
		System.out.println("해당 강의실이 없습니다.");
	}
	
	static void showReservedRooms() {
		System.out.println("===== 예약 현황 =====");
		
		for(LectureRoom lr : roomList) {
			if(lr.isReserved()) { // isReserved(); 현재 예약 상태를 확인
				lr.displayInfo();
			}
		}
	}
	
	static void cancelRoom() {
		System.out.print("취소할 강의실 번호:");
		String roomNo = sc.nextLine();
		
		for(LectureRoom lr : roomList) {
			if(lr.getRoomNo().equalsIgnoreCase(roomNo)) {
				if(lr.isReserved()) {
					lr.setReserved(false);
					System.out.println("강의실이 취소되었습니다.");
				}
				else {
					System.out.println("해당 강의실은 예약되지 않았습니다.");
				}
				return;
			}
		}
		System.out.println("해당 강의실이 없습니다.");
	}
	
	static void addRoom() {
		System.out.println("1. 이론강의실");
		System.out.println("2. 실습강의실");
		System.out.print("종류선택: ");
		int type = Integer.parseInt(sc.nextLine());
		
		System.out.print("강의실 번호: ");
		String roomNo = sc.nextLine();
		
		for(LectureRoom lr : roomList) {
			if (lr.getRoomNo().equalsIgnoreCase(roomNo)) {
				System.out.println("이미 존재하는 강의실 번호입니다.");
				return;
			}
		}
		
		System.out.print("수용인원: ");
		int capacity = Integer.parseInt(sc.nextLine());
		
		System.out.print("위치: ");
		String location = sc.nextLine();
		
		System.out.print("관리부서: ");
		String department = sc.nextLine();
		
		if(type == 1) {
			roomList.add(new TheoryRoom(roomNo, capacity, location, department));
		}
		else if(type == 2) {
			System.out.print("용도: ");
			String purpose = sc.nextLine();
			
			System.out.print("보유장비: ");
			String equipment = sc.nextLine();
			
			roomList.add(new PracticeRoom(roomNo, capacity, location, department, purpose, equipment));
		}
		else {
			System.out.println("잘못된 종류입니다.");
			return;
		}
		
		System.out.println("강의실 추가 완료");
	}
	
	static void deleteRoom() {
		System.out.println("삭제할 강의실 번호:");
		String roomNo = sc.nextLine();
		
		for(int i = 0; i < roomList.size();i++) {
			LectureRoom lr = roomList.get(i);
			
			if(lr.getRoomNo().equalsIgnoreCase(roomNo)) {
				if (lr.isReserved()) {
					System.out.println("현재 예약되어 있어 예약 취소도 함께 진행됩니다.");
				}
				
				roomList.remove(i);
				System.out.println(roomNo+" 강의실 삭제 완료");
				return;
			}
		}
		System.out.println("해당 강의실이 없습니다.");
	}
	
	static void showRoomList() {	
		System.out.println("===== 강의실 목록 =====");
		
		for(LectureRoom tr : roomList) {
			tr.displayInfo();
			}
		}

}
