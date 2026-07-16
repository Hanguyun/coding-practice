package Final;

import java.util.*;

public class TelManager {
	private static ArrayList<Group> groupList = new ArrayList<Group>();
	private static ArrayList<PhoneBook> phoneList = new ArrayList<PhoneBook>();
	private static Scanner sc = new Scanner(System.in);
	private static int nextGroupId = 1;
	private static int nextPhoneId = 1;
	
	private static boolean isDuplicateMPhone(String mPhone) {
		for(PhoneBook p: phoneList) {
			if(p.getmPhone().equals(mPhone))
				return true;
		}
		return false;
	}
	
	private static void addPhone(){
		System.out.println("\n+++[전화번호 등록]+++");
		System.out.print("휴대폰번호(중복불가): ");
		String mPhone = sc.nextLine();
		if(isDuplicateMPhone(mPhone)) {
			System.out.println("등록 실패: 이미 등록 되어 이쓴ㄴ 번호입니다.");
			return;
		}
		System.out.print("이름: "); String name = sc.nextLine();
		System.out.print("직장번호: "); String cPhone = sc.nextLine();
		System.out.print("집번호: "); String hPhone = sc.nextLine();
		
		System.out.print("그룹ID(없으면0): "); 
//		int groupId = Integer.parseInt(sc.nextLine());
		String temp = sc.nextLine();
		int groupId = temp.isBlank()?0: Integer.parseInt(temp);
		
		System.out.print("직장명: "); String comName = sc.nextLine();
		System.out.print("직급/직위: "); String comPos = sc.nextLine();
		System.out.print("email: "); String email = sc.nextLine();
		System.out.print("주소: "); String address = sc.nextLine();
		System.out.print("메모: "); String memo = sc.nextLine();
		
		PhoneBook pb = new PhoneBook(nextPhoneId++, name, mPhone, cPhone, hPhone, groupId, comName, comPos, email, address, memo);
		phoneList.add(pb);
		System.out.println("등록 완료..등록번호: " + pb.getIdNum());
	}
	private static int findByMPhone(String mPhone) {
		int i = 0;
		for( ; i < phoneList.size(); i++) {
			if(phoneList.get(i).getmPhone().equals(mPhone)) return(i);
		}
		return -1;
	}
	private static void updatePhone(){
		System.out.println("\n+++[전화번호 수정]+++");
		System.out.print("수정할 전화번호: ");
		String mPhone = sc.nextLine();
		if(!isDuplicateMPhone(mPhone)) {
			System.out.println("해당 전화번호가 등록되어 있지 않습니다.");
			return;
		}
		System.out.print("새로운 전화번호:");
		String newMPhone = sc.nextLine();
		if(isDuplicateMPhone(newMPhone)) {
			System.out.println("해당 전화번호가 이미 등록되어 있습니다. 수정 실패!");
			return;
		}
		int findNum = findByMPhone(mPhone);
		PhoneBook oldPhone = phoneList.get(findNum);
		oldPhone.setmPhone(newMPhone);
		
		System.out.print("새 이름(기존 이름: " + oldPhone.getName() + ")[엔터 유지]:");
		String name = sc.nextLine();
		if(!name.isEmpty()) oldPhone.setName(name);
		
		System.out.print("새 직장번호(기존 번호: " + oldPhone.getcPhone() + ")[엔터 유지]:");
		String cPhone = sc.nextLine();
		if(!cPhone.isEmpty()) oldPhone.setcPhone(cPhone);
		
		System.out.print("새 집번호(기존 번호: " + oldPhone.gethPhone() + ")[엔터 유지]:");
		String hPhone = sc.nextLine();
		if(!hPhone.isEmpty()) oldPhone.sethPhone(hPhone);
		
		System.out.print("새 그룹번호(기존 번호: " + oldPhone.getGroupId() + ")[엔터 유지]:");
		String groupId = sc.nextLine();
		if(!groupId.isEmpty()) oldPhone.setGroupId(Integer.parseInt(groupId));
		
		System.out.print("새 직장이름(기존 이름: " + oldPhone.getComName() + ")[엔터 유지]:");
		String comName = sc.nextLine();
		if(!comName.isEmpty()) oldPhone.setComName(comName);
		
		System.out.print("새 직급/직위(기존 직위: " + oldPhone.getcPos() + ")[엔터 유지]:");
		String cPos = sc.nextLine();
		if(!cPos.isEmpty()) oldPhone.setcPos(cPos);
		
		System.out.print("새 메일주소(기존 메일: " + oldPhone.getEmail() + ")[엔터 유지]:");
		String email = sc.nextLine();
		if(!email.isEmpty()) oldPhone.setEmail(email);
		
		System.out.print("새 주소(기존 주소: " + oldPhone.getAddress() + ")[엔터 유지]:");
		String address = sc.nextLine();
		if(!address.isEmpty()) oldPhone.setAddress(address);
		
		System.out.print("새 메모(기존 메모: " + oldPhone.getMemo() + ")[엔터 유지]:");
		String memo = sc.nextLine();
		if(!memo.isEmpty()) oldPhone.setMemo(memo);
	}
	private static void deletePhone(){
		System.out.println("\n+++[전화번호 삭제]+++");
		System.out.print("삭제할 전화번호: ");
		String mPhone = sc.nextLine();
		int index = findByMPhone(mPhone);
		if(index == -1) {
			System.out.println("해당 전화번호가 등록되어 있지 않습니다.");
			return;
		}
		phoneList.remove(index);
		System.out.println(mPhone+"번호를 삭제하였습니다...");
		
		/*if(phoneList.contains(mPhone)) { // 입력 받은 전화번호가 목록에 포함되어 있는지 확인하는 기능
			
		}*/
		
	}
	
	private static Group findByGroupId(int id) {
		for(Group g: groupList) {
			if(g.getGroupId() == id) { // 그룹을 찾았다는 의미
				return g;
			}
		}
		return null;
	}
	
	private static void printDetailsOfPhone(PhoneBook p) {
		String groupName = "미분류";
		
		System.out.print("ID: " + p.getIdNum());
		System.out.print(" 이름: " + p.getName());
		Group g = findByGroupId(p.getGroupId());
		if(g != null) {
			groupName =  g.getGroupName();
		}
		System.out.print(" 그룹: " + groupName);
		
		System.out.print(" 휴대폰번호: " + p.getmPhone());
		System.out.print(" 회사번호: " + p.getcPhone());
		System.out.print(" 집번호: " + p.gethPhone());
		System.out.print(" 회사이름: " + p.getComName());
		System.out.print(" 회사 직위: " + p.getcPos());
		System.out.print(" 메일주소: " + p.getEmail());
		System.out.print(" 주소: " + p.getAddress());
		System.out.println(" 메모: " + p.getMemo());
	}
	
	private static void searchPhone(){
		System.out.println("\n+++[전화번호 검색]+++");
		System.out.println("1.전화번호로 검색 2.이름으로 검색");
		System.out.print("선택: ");
		String choice = sc.nextLine();
		
		boolean isFound = false;
		
		if(choice.equals("1")) {
			System.out.print("찾는 전화번호: ");
			String sPhone = sc.nextLine();

			for(PhoneBook p: phoneList) {
				if(p.getmPhone().contains(sPhone)) {
					printDetailsOfPhone(p);
					isFound = true;
				}
			}
		}
		else if(choice.equals("2")) {
			System.out.print("찾는 이름: ");
			String sName = sc.nextLine();

			for(PhoneBook p: phoneList) {
				if(p.getName().contains(sName)) {
					printDetailsOfPhone(p);
					isFound = true;
				}
			}
		}
		else {
			System.out.println("잘못된 입력입니다.");
			return;
		}

		if(!isFound) {
			System.out.println("검색 결과가 없습니다.");
		}
	}
	
	private static void printAllPhone(){
		System.out.println("\n+++[전화번호 목록]+++");
		if(phoneList.isEmpty()) {
			System.out.println("등록된 전화번호가 없습니다...");
			return;
		}
		for(PhoneBook p: phoneList) {
			printDetailsOfPhone(p);
		}
	}
	
	private static void phoneMenu() {
		while(true) {
			System.out.println("\n---[전화번호 관리]---");
			System.out.println("1.등록 2.수정 3.삭제 4.검색 5.전체 출력 0.메인으로");
			System.out.print("선택: ");
			String choice = sc.nextLine();
			
			switch(choice) {
			case "1": addPhone(); break;
			case "2": updatePhone(); break;
			case "3": deletePhone(); break;
			case "4": searchPhone(); break;
			case "5": printAllPhone(); break;
			case "0": return;
			default: System.out.println("잘못된 입력입니다. 다시 입력하세요.");
			}
		}
	}
	
	private static boolean isDuplicateGroup(String name) {
		for(Group g: groupList) {
			if(g.getGroupName().equals(name))
				return true;
		}
		return false;
	}
	
	private static void addGroup() {
		System.out.println("\n+++[그룹 등록]+++");
		System.out.print("그룹 이름: "); String name = sc.nextLine();
		if(isDuplicateGroup(name)) {
			System.out.println("그룹 이름 중복입니다...");
			return;
		}
		System.out.print("그룹 메모: "); String memo = sc.nextLine();
		Group g = new Group(nextGroupId++, name, memo);
		groupList.add(g);
		System.out.println("등록 완료..등록번호: " + g.getGroupId());
	}

	private static int findByGroupName(String name) {
		for(Group g: groupList) {
			if(g.getGroupName().equals(name))
				return groupList.indexOf(g);
		}
		return -1;
	}
	
	private static void updateGroup() {
		System.out.println("\n+++[그룹 수정]+++");
		System.out.print("수정할 그룹이름: ");
		String name = sc.nextLine();
		if(!isDuplicateGroup(name)) {
			System.out.println("해당 그룹이 등록되어 있지 않습니다.");
			return;
		}
		System.out.print("새로운 이름:");
		String newName = sc.nextLine();
		if(isDuplicateGroup(newName)) {
			System.out.println("새로운 그룹 이름이 이미 등록되어 있습니다. 수정 실패!");
			return;
		}
		
		int findNum = findByGroupName(name); // 기존의 그룹 이름을 이용하여 해당 그룹의 객체를 받아옴
		System.out.print("새 메모(기존 메모: " + groupList.get(findNum).getMemo() + ")[엔터 유지]:");
		String memo = sc.nextLine();
		if(!memo.isEmpty()) groupList.get(findNum).setMemo(memo);
		System.out.println("수정이 완료되었습니다.");
		}

	private static void deleteGroup() {
		System.out.println("\n+++[그룹 삭제]+++");
		System.out.print("삭제할 그룹이름: ");
		String name = sc.nextLine();
		if(!isDuplicateGroup(name)) {
			System.out.println("해당 그룹이 등록되어 있지 않습니다.");
			return;
		}
		int findNum = findByGroupName(name);
		int dGroupId = groupList.get(findNum).getGroupId();
		// ver1
		for(PhoneBook p: phoneList) {
			if(p.getGroupId() == dGroupId)
				p.setGroupId(0);
		}
		// ver2
		ArrayList<PhoneBook> dList = new ArrayList<>();
		for(PhoneBook p: phoneList) {
			if(p.getGroupId() == dGroupId) {
				System.out.print("이름: " + p.getName() + ", 휴대폰 번호: " + p.getmPhone() + ", 직장: " + p.getmPhone()+", 직장: " + p.getComName());
				System.out.print("......삭제할까요(y/n): ");
				String yesNo = sc.nextLine();
				if(yesNo.equalsIgnoreCase("y"))
					dList.add(p);
			}
		}
		// for(PhoneBook p:dList)
		//	phoneList.remove(p);
		phoneList.removeAll(dList);
		groupList.remove(groupList.get(findNum)); // groupList.remove(findNum);
		
		System.out.println("그룹 삭제 완료!");
	}

	private static void printAllGroups() {
		System.out.println("\n---[그룹 출력]---");
		for(Group g: groupList)
			System.out.println(g);
	}
	
	private static void groupMenu() {
		while(true) {
			System.out.println("\n---[그룹 관리]---");
			System.out.println("1.등록 2.수정 3.삭제 4.전체 출력 0.메인으로");
			System.out.print("선택: ");
			String choice = sc.nextLine();
			switch(choice) {
			case "1": addGroup(); break;
			case "2": updateGroup(); break;
			case "3": deleteGroup(); break;
			case "4": printAllGroups(); break;
			case "0": return;
			default: System.out.println("잘못된 입력입니다. 다시 입력하세요.");
			}
		}
	}
	
	public static void main(String[] args) {
		groupList.add(new Group (nextGroupId++, "가족", "가족 모임"));
		groupList.add(new Group (nextGroupId++, "초등친구", "초등학교 동창"));
		
		while(true) {
			System.out.println("\n******전화번호부 관리 프로그램 ******");
			System.out.println("1.전화번호 관리 2.그룹 관리 0.종료");
			System.out.print("선택: ");
			String choice = sc.nextLine();
			switch(choice) {
			case "1": phoneMenu(); break;
			case "2": groupMenu(); break;
			case "0": System.out.println("프로그램 종료합니다.");
			          return;
			default: System.out.println("잘못된 입력입니다... 다시 입력하세요.");
			}
		}

	}

}
