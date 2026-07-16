package Final;

public class Group {
	private int groupId;
	private String groupName;
	private String memo;
	
	public Group(int gId, String gName, String gMemo) {
		groupId = gId;
		groupName = gName;
		memo = gMemo;
	}

	public int getGroupId() {
		return groupId;
	}


	public String getGroupName() {
		return groupName;
	}

	public void setGroupName(String groupName) {
		this.groupName = groupName;
	}

	public String getMemo() {
		return memo;
	}

	public void setMemo(String memo) {
		this.memo = memo;
	}
	
	@Override
	public String toString() {
		return String.format("[그룹ID: %d] 이름: %s | 메모: %s", groupId, groupName, memo);

	}
}
