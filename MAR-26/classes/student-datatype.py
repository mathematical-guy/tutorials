class Student:
    #__init__ is a constructor
    def __init__(self, name, marks, roll_no):
        self.name = name
        self.marks = marks
        self.roll_no = roll_no

    def dance(self):
        print(self.name, "is dancing")

    def program_a_code(self):
        print(self.name, " knows Python Programming Lanaguage")

    def __str__(self):
        return f"{self.name} - {self.marks}"


def calculate_gst(number):
    print(number)


student1 = Student(name="Abhinav", marks=100, roll_no=40)
student2 = Student(name="Mohit", marks=6, roll_no=0)


print(student1)
print(student2)