class Employee:
    def __init__(self, name, salary, department):
        self.name = name
        self.__salary = salary
        self._department = department

    def get_salary(self):
        return self.__salary

    def increase_salary(self, amount):
        if amount > 0:
            self.__salary += amount

    def calculate_bonus(self):
        return self.__salary * 0.05

    def show_info(self):
        print(
            f"Name: {self.name}, "
            f"Salary: {self.__salary}, "
            f"Department: {self._department}, "
            f"Bonus: {self.calculate_bonus()}"
        )


class Developer(Employee):
    def __init__(self, name, salary, department, programming_language, overtime_hours):
        super().__init__(name, salary, department)
        self.programming_language = programming_language
        self.overtime_hours = overtime_hours

    def calculate_bonus(self):
        return self.get_salary() * 0.10 + self.overtime_hours * 100000


class Manager(Employee):
    def __init__(self, name, salary, department, number_of_employees):
        super().__init__(name, salary, department)
        self.number_of_employees = number_of_employees

    def calculate_bonus(self):
        return self.get_salary() * 0.15 + self.number_of_employees * 200000


employees = [
    Developer("John", 15000000, "IT", "Python", 10),
    Developer("Alice", 18000000, "IT", "Java", 5),
    Manager("Bob", 25000000, "Management", 8),
    Manager("David", 22000000, "Management", 5)
]

for employee in employees:
    employee.show_info()

highest_salary = max(employees, key=lambda employee: employee.get_salary())

total_bonus = sum(employee.calculate_bonus() for employee in employees)

developer_count = sum(isinstance(employee, Developer) for employee in employees)
manager_count = sum(isinstance(employee, Manager) for employee in employees)

print("\nHighest salary:")
print(highest_salary.name, highest_salary.get_salary())

print("Total bonus:", total_bonus)
print("Number of Developers:", developer_count)
print("Number of Managers:", manager_count)