package _1023pra;

public class UserInfo {
	private String userName;
	private int userAge;
	
	public UserInfo(String uName, int uAge) {
		userName = uName;
		userAge = uAge;
	}
	void setUserName(String uName) {
		userName = uName;
	}
	void setUserAge(int uAge) {
		userAge = uAge;
	}
	
	String getUserName() {
		return userName;
	}
	int getUserAge() {
		return userAge;
	}
}

