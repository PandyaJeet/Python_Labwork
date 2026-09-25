class Person:
    name =""
    course=""
class Student(Person):
    def __init__(self, name, course):
        self.name = name
        self.course = course

    def display(self):
        print("Name:", self.name)
        print("Course:", self.course)
def main():
    s1 = Student("Jeet", "Python")
    s1.display()
main()