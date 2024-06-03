class Student:
    school = "AkiraChix"
    # CONSTRUCTOR
    def __init__(self, first_name, last_name, age, country, code):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.country = country
        self.code = code

    def greet_student(self):
        greeting = f"Hello {self.first_name}, welcome to {self.school}. Your code is {self.code}"
        print(greeting)
    
    def greet_with_year(self):
        greeting_2 = f"Hi {self.first_name}. You're born in {2024 -self.age}"
        print(greeting_2)

    def display_initials(self):
        print(self.first_name[0],self.last_name[0])

    def enrol_student(self):
        enrol = f"Hi {self.first_name}, You have been enrolled at {self.school}"
        print(enrol)