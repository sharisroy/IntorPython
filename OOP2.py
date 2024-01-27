class Student:
    def __init__(self):
        self.name = "Haris"
        self.grades = (70, 80, 90, 85)

    def average_grade(self):
        return sum(self.grades) / len(self.grades)


student = Student()
# print(student.name)
# print(student.grades)
# print(Student.average_grade(student))
print(student.average_grade())