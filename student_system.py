class Student:
    def __init__(self,name,roll_num,age,marks):
        self.name = name
        self.roll_num = roll_num
        self.age = age
        self.marks = marks
        
s1 = Student("Amina",1,17,99)
s2 = Student("Atiqa",2,17,98)
s3 = Student("Aira",3,17,97)
s4 = Student("Aniya",4,17,100)

Total_Students = [s1,s2,s3,s4]

n = int(input("Enter Your's Roll Number:-"))

student_info = False

for student in Total_Students:
    if student.roll_num  == n:
        print("Student is found:")
        print(f"Name: {student.name} | Roll Number: {student.roll_num} | Age: {student.age} | Marks: {student.marks}")
        student_info = True
        break

if student_info == False:
    print("Student is not found")
        