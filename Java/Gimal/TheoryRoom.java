package Gimal;

public class TheoryRoom extends LectureRoom {

	public TheoryRoom(String roomNo, int capacity, String location, String department) {
		super(roomNo, capacity, location, department);
	}
	
	public void displayInfo() {
			System.out.println("[이론강의실]"+getRoomNo()+", 수용인원: "+getCapacity()+", 위치: "+getLocation()+", 관리부서: "+getDepartment());
	}
}
