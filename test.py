from course_enroll import enroll_student

def test():
    assert enroll_student("Rahul","Python") == "Student added to python"
    assert enroll_student("Rahul","Java") == "Student added to Java"
    assert enroll_student("Rahul","C++") == "Invalid course"