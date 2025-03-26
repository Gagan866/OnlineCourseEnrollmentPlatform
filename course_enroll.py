all_students = []
students_Python = []
students_Java = []
def enrolled_student_python():
   print("Students in python are :")
   for student in students_Python:
       print(student)

def enrolled_student_java():
   print("Students in Java are :")
   for student in students_Java:
       print(student)

def enrolled_students():
    print("All students are :")
    for student in all_students:
        print(student)

def enroll_student(student,courses):
    
    course = courses
    if course == "Python":
        user_email = "user@gmail.com"
        user_password = "user@123"
        if check_email_isvalid(user_email):
            if password_strength(user_password):
                print("Successfully enrolled")
                all_students.append(student)
                students_Python.append(student)
                return "Student added to python"
            else:
                print("Password is not strong")
        else:
            print("Email is not valid")    
    elif course == "Java":
        user_email = "user@gmail.com"
        user_password = "user@123"
        if check_email_isvalid(user_email):
            if password_strength(user_password):
                print("Successfully enrolled")
                all_students.append(student)
                students_Java.append(student)
                return "Student added to java"
            else:
                print("Password is not strong")
        else:
            print("Email is not valid")
    else:
        print("Invalid course")

def check_email_isvalid(email):
    if "@" in email:
        return True
    else:
        return False
    
def password_strength(password):
    if len(password) >= 8:
        return True
    else:
        return False    
    
if __name__ == "__main__":
    print("Courses are : /n 1. Python /n 2. Java")
    enroll_student("student1","Python")
    enroll_student("student2","Java")
    enroll_student("student3","Python")
    
    enrolled_students()
    enrolled_student_python()
    enrolled_student_java()
    