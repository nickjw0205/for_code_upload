class StudentInfo extends UserInfo {
    private String studentId;
    private String studentPhone;

    void setStudentId(String studentId) {
        this.studentId = studentId;
    }
    void setStudentPhone(String studentPhone) {
        this.studentPhone = studentPhone;
    }

    String getStudentId() {
        return this.studentId;
    }
    String getStudentPhone() {
        return studentPhone;
    }
}