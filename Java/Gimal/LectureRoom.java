package Gimal;

public abstract class LectureRoom implements Reservable {
	private String roomNo;
	private int capacity;
	private String location;
	private String department;
	private boolean reserved;
	
	public LectureRoom(String roomNo, int capacity, String location, String department) {
		this.roomNo = roomNo;
		this.capacity = capacity;
		this.location = location;
		this.department = department;
	}

	public String getRoomNo() {
		return roomNo;
	}

	public void setRoomNo(String roomNo) {
		this.roomNo = roomNo;
	}

	public int getCapacity() {
		return capacity;
	}

	public void setCapacity(int capacity) {
		this.capacity = capacity;
	}

	public String getLocation() {
		return location;
	}

	public void setLocation(String location) {
		this.location = location;
	}

	public String getDepartment() {
		return department;
	}

	public void setDepartment(String department) {
		this.department = department;
	}

	public boolean isReserved() {
		return reserved;
	}

	public void setReserved(boolean reserved) {
		this.reserved = reserved;
	}
	
	public abstract void displayInfo();
}
