# ---- CLASS APPROACH ----

class Employee:
    def __init__(self, emp_id, name, salary):
        self.emp_id = emp_id
        self.name = name
        self.salary = salary

    def update_salary(self, new_salary):
        self.salary = new_salary
        print(f"Salary updated for {self.name}")

    def get_details(self):
        return {"id": self.emp_id, "name": self.name, "salary": self.salary}


# --- Managing employees collectively ---
class EmployeeManager:
    def __init__(self):
        self.employees = {}

    def add_employee(self, emp_id, name, salary):
        self.employees[emp_id] = Employee(emp_id, name, salary)

    def get_employee(self, emp_id):
        return self.employees.get(emp_id)

# --- Using the classes ---
manager = EmployeeManager()
manager.add_employee(1, "Sagar", 50000)
manager.add_employee(2, "Riya", 60000)

emp = manager.get_employee(1)
emp.update_salary(55000)
print(emp.get_details())
