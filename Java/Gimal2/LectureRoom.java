package Gimal2;

public abstract class LectureRoom implements Reservable {
	protected String roomNo;
	protected int capactiy;
	protected String location;
	protected String department;
	protected boolean reserved;
	
	public LectureRoom(String roomNo, int capactiy, String location, String department) {
		this.roomNo = roomNo;
		this.capactiy = capactiy;
		this.location = location;
		this.department = department;
	}
	@Override
	public void reserve() {
		if(!reserved) {
			reserved = true;
			System.out.println(roomNo + " 강의실 예약 완료");
		}
		else if(reserved) {
			System.out.println(roomNo + " 이미 예약된 강의실입니다.");
		}
		else {
			System.out.println(roomNo + " 해당 강의실은 존재하지 않습니다.");
		}
	}

	@Override
	public void cancelReservation() {
		if(reserved) {
			reserved = false;
			System.out.println(roomNo + " 예약 취소 완료");
		}
		else if(!reserved) {
			System.out.println(roomNo + " 해당 강의실은 예약되어 있지 않습니다.");
		}
		else {
			System.out.println(roomNo + " 해당 강의실은 존재하지 않습니다.");
		}
		
	}

	@Override
	public void showReservation() {
		System.out.println(roomNo + ":" + (reserved ? "예약중" : "예약가능"));
		
	}
	
	public String getRoomNo() {
		return roomNo;
	}
	public void setRoomNo(String roomNo) {
		this.roomNo = roomNo;
	}
	public int getCapactiy() {
		return capactiy;
	}
	public void setCapactiy(int capactiy) {
		this.capactiy = capactiy;
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
	
	
}
