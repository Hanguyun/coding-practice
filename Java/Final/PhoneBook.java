package Final;

public class PhoneBook {
	private int idNum;
	private String name;
	private String mPhone;
	private String hPhone;
	private String cPhone;
	private int groupId;
	private String comName;
	private String cPos;
	private String email;
	private String address;
	private String memo;
	
	public PhoneBook(int idNum, String name, String mPhone,	String cPhone, String hPhone,
					 int groupId, String comName, String cPos,	String email, String address, String memo) {
		this.idNum = idNum;
		this.name = name;
		this.mPhone = mPhone;
		this.hPhone = hPhone;
		this.cPhone = cPhone;
		this.groupId = groupId;
		this.comName = comName;
		this.cPos = cPos;
		this.email = email;
		this.address = address;
		this.memo = memo;
	}

	public int getIdNum() {
		return idNum;
	}

	public String getName() {
		return name;
	}

	public void setName(String name) {
		this.name = name;
	}

	public String getmPhone() {
		return mPhone;
	}

	public void setmPhone(String mPhone) {
		this.mPhone = mPhone;
	}

	public String gethPhone() {
		return hPhone;
	}

	public void sethPhone(String hPhone) {
		this.hPhone = hPhone;
	}

	public String getcPhone() {
		return cPhone;
	}

	public void setcPhone(String cPhone) {
		this.cPhone = cPhone;
	}

	public int getGroupId() {
		return groupId;
	}

	public void setGroupId(int groupId) {
		this.groupId = groupId;
	}

	public String getComName() {
		return comName;
	}

	public void setComName(String comName) {
		this.comName = comName;
	}

	public String getcPos() {
		return cPos;
	}

	public void setcPos(String cPos) {
		this.cPos = cPos;
	}

	public String getEmail() {
		return email;
	}

	public void setEmail(String email) {
		this.email = email;
	}

	public String getAddress() {
		return address;
	}

	public void setAddress(String address) {
		this.address = address;
	}

	public String getMemo() {
		return memo;
	}

	public void setMemo(String memo) {
		this.memo = memo;
	}
	
	
}
