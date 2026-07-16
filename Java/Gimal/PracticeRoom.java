package Gimal;

public class PracticeRoom extends LectureRoom {
	private String purpose;
	private String equipment;
	
	public PracticeRoom(String roomNo, int capacity, String location, String department) {
		super(roomNo, capacity, location, department);
		
		this.purpose = purpose;
		this.equipment = equipment;
	}
	
	public void displayInfo() {
		
	}

}
