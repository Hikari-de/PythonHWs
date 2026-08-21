from abc import ABC, abstractmethod

class Person(ABC):
    def __init__(self, name, yob):
        self.name = name
        self.yob = yob

    @abstractmethod
    def describe(self):
        pass

class Student(Person):
    def __init__(self, name, yob, grade):
        super().__init__(name, yob)
        self.grade = grade

    def describe(self):
        print(f"Student Name: {self.name}, Year of Birth: {self.yob}, Grade: {self.grade}")

class Teacher(Person):
    def __init__(self, name, yob, subject):
        super().__init__(name, yob)
        self.subject = subject

    def describe(self):
        print(f"Teacher Name: {self.name}, Year of Birth: {self.yob}, Subject: {self.subject}")

class Doctor(Person):
    def __init__(self, name, yob, specialization):
        super().__init__(name, yob)
        self.specialization = specialization

    def describe(self):
        print(f"Doctor Name: {self.name}, Year of Birth: {self.yob}, Specialization: {self.specialization}")

class Ward:
    def __init__(self, name):
        self.name = name
        self.people = []

        def add_person(self, person):
            self.people.append:(person)

        def count_doctor(self):
            return sum(isinstance(person, Doctor) for person in self.people)

        def sort_age(self):
            self.people.sort(key=lambda person: person.yob, reverse=True)

        def average_teacher_yob(self):
            teacher_yobs = [person.yob for person in self.people if isinstance(person, Teacher)]
            if teacher_yobs:
                return sum(teacher_yobs) / len(teacher_yobs)
            else:
                return 0
        

                                
