#!/usr/bin/env python3
#Student Number: 100706225(pacharya9)

class Student:

    def __init__(self, name, number):
        self.name = name
        self.number = number
        self.courses = {}

    def displayStudent(self):
        return 'Student Name: ' + self.name + '\n' + 'Student Number: ' + str(self.number)

    def addGrade(self, course, grade):
        self.courses[course] = grade

    def displayGPA(self):
        all_gpa = 0.0
        for gpa in self.courses.values():
            all_gpa += gpa
        if len(self.courses) == 0:
            return 'GPA of student ' + self.name + ' is 0.0'
        grade = all_gpa / len(self.courses)
        return 'GPA of student ' + self.name + ' is ' + str(grade)

    def displayCourses(self):
        courses = []
        for course in self.courses.keys():
            gpa = self.courses[course]
            if gpa > 0.0:
                courses.append(course)
        return ', '.join(courses)


if __name__ == '__main__':
    student1 = Student('John', '013454900')
    student1.addGrade('uli101', 1.0)
    student1.addGrade('ops245', 2.0)
    student1.addGrade('ops445', 3.0)

    student2 = Student('Jessica', '123456')
    student2.addGrade('ipc144', 4.0)
    student2.addGrade('cpp244', 3.5)
    student2.addGrade('cpp344', 0.0)

    print(student1.displayStudent())
    print(student1.displayGPA())
    print(student1.displayCourses())

    print(student2.displayStudent())
    print(student2.displayGPA())
    print(student2.displayCourses())

