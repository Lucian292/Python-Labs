class Employee:
    def __init__(self, name, employee_id):
        self.name = name
        self.employee_id = employee_id

    def display_info(self):
        print(f"Employee ID: {self.employee_id}, Name: {self.name}")


class Manager(Employee):
    def __init__(self, name, employee_id, salary, department):
        super().__init__(name, employee_id)
        self.salary = salary
        self.department = department

    def display_info(self):
        super().display_info()
        print(f"Position: Manager, Salary: ${self.salary}, Department: {self.department}")

    def conduct_meeting(self):
        print(f"{self.name} is conducting a meeting.")


class Engineer(Employee):
    def __init__(self, name, employee_id, salary, programming_language):
        super().__init__(name, employee_id)
        self.salary = salary
        self.programming_language = programming_language

    def display_info(self):
        super().display_info()
        print(f"Position: Engineer, Salary: ${self.salary}, Programming Language: {self.programming_language}")

    def write_code(self):
        print(f"{self.name} is writing code in {self.programming_language}.")


class Salesperson(Employee):
    def __init__(self, name, employee_id, salary, sales_target):
        super().__init__(name, employee_id)
        self.salary = salary
        self.sales_target = sales_target

    def display_info(self):
        super().display_info()
        print(f"Position: Salesperson, Salary: ${self.salary}, Sales Target: ${self.sales_target}")

    def make_sale(self):
        print(f"{self.name} made a sale!")


manager = Manager("John Smith", 1, 80000, "Marketing")
manager.display_info()
manager.conduct_meeting()

engineer = Engineer("Alice Johnson", 2, 70000, "Python")
engineer.display_info()
engineer.write_code()

salesperson = Salesperson("Bob Williams", 3, 60000, 100000)
salesperson.display_info()
salesperson.make_sale()
