package Gimal;

public class PracticeRoom extends LectureRoom {
	private String purpose;
	private String equipment;
	
	public PracticeRoom(String roomNo, int capacity, String location, String department, String purpose, String equipment) {
		super(roomNo, capacity, location, department);
		
		this.purpose = purpose;
		this.equipment = equipment;
	}

	public String getPurpose() {
		return purpose;
	}

	public String getEquipment() {
		return equipment;
	}
	
	

}
