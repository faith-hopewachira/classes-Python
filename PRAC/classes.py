class Student:
    school = "AkiraChix"
    def __init__ (self, first_name, last_name, code, country):
        self.first_name = first_name
        self.last_name = last_name
        self.code = code
        self.country = country

    def enrol_students(self):
        greeting = f"Congratulations {self.first_name}, {self.last_name}, you have been selected to join {self.school}"
        print(greeting)


class ClassesAkiraChix:
    def __init__(self,className,number_of_students):
        self.name = name
        self.number_of_students = number_of_students
    
    def greetClass(self):
        greet = f"Hello {self.className} welcome to AkiraChix"
        print(greet)