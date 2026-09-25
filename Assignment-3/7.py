class Employee:
    def __init__(self, salary):
        self.salary = salary

    def calculate_salary(self):
        return self.salary


class Manager(Employee):
    def calculate_salary(self):
        return self.salary + 10000


class Developer(Employee):
    def calculate_salary(self):
        return self.salary + 5000


def main():
    base_salary = 50000
    manager = Manager(base_salary)
    developer = Developer(base_salary)
    print("Base Salary =", base_salary)
    print("Manager Salary  =", manager.calculate_salary())
    print("Developer Salary  =", developer.calculate_salary())


main()
