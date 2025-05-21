class Employee:
    def __init__(self, name, id, salary):
        self.name = name
        self.id = id
        self.salary = salary    
    
    def display_info(self):
        return (f"ID: {self.id}, Name: {self.name}")
    
    def calculate_salary(self):
        pass
    
class FullTimeEmployee(Employee):
    def calculate_salary(self):
        return self.salary 
    
class PartTimeEmployee(Employee):
    def __init__(self, name, id, salary, hour):
        super().__init__(name, id, salary)
        self.hour = hour
        
    def calculate_salary(self):
        return self.salary * self.hour
        

print("\nEmployee Salary Report:\n")

emp1 = FullTimeEmployee("Alice", 1001, 5000)
print(emp1.display_info())
print(f"Calculated Salary: ${emp1.calculate_salary():.2f}")
print("-" * 30)

emp2 = PartTimeEmployee("Bob", 1002, 120, 20)
print(emp2.display_info())
print(f"Calculated Salary: ${emp2.calculate_salary():.2f}")
print("-" * 30)

emp3 = FullTimeEmployee("Charlie", 1003, 6000)
print(emp3.display_info())
print(f"Calculated Salary: ${emp3.calculate_salary():.2f}")
print("-" * 30)

emp4 = PartTimeEmployee("Diana", 1004, 90, 25)
print(emp4.display_info())
print(f"Calculated Salary: ${emp4.calculate_salary():.2f}")
print("-" * 30)
print ()