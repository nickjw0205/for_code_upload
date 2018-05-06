package _1023pra;

public class StudentInfo extends UserInfo {
	private int userId;
	private String userPhone;
	
	public StudentInfo(String uName, int uAge, int uId, String uPhone) {
		super(uName, uAge);
		userId = uId;
		userPhone = uPhone;
	}
	
	void setStudentId(int uId) {
		userId = uId;
	}
	void setStudentPhone(String uPhone) {
		userPhone = uPhone;
	}
	
	int getStudentId() {
		return userId;
	} 
	String getStudentPhone() {
		return userPhone;
	}
}

