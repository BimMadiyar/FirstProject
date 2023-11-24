class University:
    def __init__(self, name, students, specialities, employees):
        self.name = name
        self.students = students
        self.specialities = specialities
        self.employees = employees

    def Return(self):
        return [self.name, self.students, self.specialities, self.employees]

class Student:
    def __init__(self, name, surname, id, gpa, courses):
        self.name = name
        self.surname = surname
        self.ID = id
        self.GPA = gpa
        self.courses = courses
    def Return(self):
        return [self.name, self.surname, self.ID, self.GPA, self.courses]

class Speciality:
    def __init__(self, name, courses):
        self.name = name
        self.courses = courses
    def Return(self):
        return [self.name, self.courses]

class Employee:
    def __init__(self, name, surname, id):
        self.name = name
        self.surname = surname
        self.ID = id
    def Return(self):
        return [self.name, self.surname, self.ID]

class Course:
    def __init__(self, name, id, number_weeks, semestrID):
        self.name = name
        self.ID = id
        self.number_weeks = number_weeks
        self.semestrID = semestrID
    def Return(self):
        return [self.name, self.ID, self.number_weeks, self.semestrID]

employees = Employee('abc', 'def', 123)
course = Course('CSS 105', '31-N', 15, 1)
specialities = Speciality('IS', course.Return())
students1 = Student('Madiyar', 'Bimuratov', 230103253, 3.6, course.Return())
student2 = Student()
university = University('SDU', students.Return(), specialities.Return(), employees.Return())
print(university.Return())