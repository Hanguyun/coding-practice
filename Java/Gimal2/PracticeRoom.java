package Gimal2;

public class PracticeRoom extends LectureRoom {
	private String purpose;
	private String equipment;

	public PracticeRoom(String roomNo, int capactiy, String location, String department, String purpose, String equipment) {
		super(roomNo, capactiy, location, department);
		this.purpose = purpose;
		this.equipment = equipment;
	}
	
	public void displayInfo() {
		System.out.println("[이론강의실] " + roomNo + " 수용인원: " + capactiy +
	"위치: " + location + "관리부서: " + department + "용도: " + purpose + "보유장비: " + equipment);
	}

}
