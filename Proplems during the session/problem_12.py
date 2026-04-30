"""
Write a Python class called Student that contains the following:
Instance attributes: name, age, courses, and grade (assigned inside __init__).
A class attribute: count_students that starts at 0.
A class method called student_count that increments the student count and returns the updated number.
Inside the constructor __init__, call the class method so the number of students increases every time a new object is created.
Create several student objects and print the total number of students created.
"""

class student:
    count_students = 0
    
    def __init__(self, name, age, courses, grade):
        self.name = name
        self.age = age
        self.courses = courses
        self.grade = grade
        
        student.student_count()

    def __str__(self):
        return f"Name: {self.name}, age: {self.age}, courses: {self.courses}, grade: {self.grade}"
    @classmethod    
    def student_count(cls):
        cls.count_students +=1
        return cls.count_students
    
s1 = student("Youssef", 22, ["Visual based programming", "Computer Graphics"], "CB")
s2 = student("Yusuf", 22, ["Biology"], "C")

print(s1)
print(s2)
print(student.count_students)