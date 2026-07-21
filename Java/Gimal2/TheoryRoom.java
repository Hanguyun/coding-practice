package Gimal2;

public class TheoryRoom extends LectureRoom {

	public TheoryRoom(String roomNo, int capactiy, String location, String department) {
		super(roomNo, capactiy, location, department);
		
	}
	
	public void displayInfo() {
		System.out.println("[이론강의실] " + roomNo + " 수용인원: " + capactiy +
	"위치: " + location + "관리부서: " + department);
	}
	
}
